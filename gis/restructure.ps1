$file = "d:\Final Year\Theory\gis\theory\chapter6.html"
$lines = [System.IO.File]::ReadAllLines($file)
Write-Host "Total lines: $($lines.Count)"

# Find Section 3 tool figure endpoints (where to insert examples)
# And Exam Examples section boundaries (where to extract from)
$toolFigEnds = @{}  # letter -> line index of </figure> for that tool in Section 3
$exCommentStart = -1
$exH2Start = -1
$theoryStart = -1
$calloutStart = -1

# Map of figcaption identifiers to tool letters
$figMap = @{
    'Fig 6.3' = 'A'
    'Fig 6.4' = 'B' 
    'Fig 6.5' = 'C'
    'Fig 6.6' = 'D'
    'Fig 6.8' = 'E'  # Buffer has Fig 6.7 + Fig 6.8, we want end of 6.8
    'Fig 6.9' = 'F'
    'Fig 6.10' = 'G'
    'Fig 6.11' = 'H'
    'Fig 6.12' = 'I'
    'Fig 6.13' = 'J'
}

for ($i = 0; $i -lt $lines.Count; $i++) {
    # Find figcaptions and their closing </figure> tags
    foreach ($fig in $figMap.Keys) {
        if ($lines[$i].Contains($fig) -and $lines[$i].Contains('figcaption')) {
            # Find the </figure> tag after this figcaption
            for ($j = $i; $j -lt [Math]::Min($i + 5, $lines.Count); $j++) {
                if ($lines[$j].Contains('</figure>')) {
                    $letter = $figMap[$fig]
                    $toolFigEnds[$letter] = $j
                    Write-Host "Tool $letter figure ends at idx $j"
                    break
                }
            }
        }
    }
    
    if ($lines[$i].Contains('<!-- Exam Examples for Each Geoprocessing Function -->')) {
        $exCommentStart = $i
        Write-Host "Exam Examples comment at idx $i"
    }
    if ($lines[$i].Contains('<h2>Exam Examples for Each Geoprocessing Function</h2>')) {
        $exH2Start = $i
        Write-Host "Exam Examples H2 at idx $i"
    }
    if ($lines[$i].Contains('<!-- The Theory Question')) {
        $theoryStart = $i
        Write-Host "Theory Question at idx $i"
    }
}

# Find the callout-box that comes right before the Exam Examples section
# It starts a few lines before the comment
if ($exCommentStart -gt 0) {
    for ($i = $exCommentStart - 1; $i -ge $exCommentStart - 5; $i--) {
        if ($lines[$i].Trim() -eq '') {
            continue
        }
        if ($lines[$i].Contains('</figure>')) {
            $calloutStart = $i + 1
            break
        }
    }
    Write-Host "Callout/section starts at idx $calloutStart"
}

# Find each example block within the Exam Examples section
$exampleBlocks = @{}  # letter -> array of lines
$exH3Positions = @()

for ($i = $exH2Start + 1; $i -lt $theoryStart; $i++) {
    if ($lines[$i] -match '^\s*<h3>([A-J])\.') {
        $exH3Positions += [PSCustomObject]@{Letter=$matches[1]; Index=$i}
    }
}

Write-Host "`nExample blocks found: $($exH3Positions.Count)"

for ($t = 0; $t -lt $exH3Positions.Count; $t++) {
    $letter = $exH3Positions[$t].Letter
    $start = $exH3Positions[$t].Index
    $end = if ($t -lt $exH3Positions.Count - 1) { $exH3Positions[$t+1].Index - 1 } else { $theoryStart - 1 }
    
    # Skip trailing empty lines
    while ($end -ge $start -and $lines[$end].Trim() -eq '') { $end-- }
    
    $exampleBlocks[$letter] = $lines[$start..$end]
    Write-Host "  $letter : idx $start to $end ($($end - $start + 1) lines)"
}

# Now rebuild the file
# Strategy: Process the file from top to bottom
# 1. For each tool in Section 3, after its </figure>, insert the example block
# 2. Skip the entire Exam Examples standalone section

$output = [System.Collections.Generic.List[string]]::new()
$skipStart = $calloutStart  # Start of the section to skip (callout + exam examples)
$skipEnd = $theoryStart - 1   # End of section to skip (before Theory Question)

# Skip trailing blank lines
while ($skipEnd -ge $skipStart -and $lines[$skipEnd].Trim() -eq '') { $skipEnd-- }
# Include the trailing blank line for clean spacing
$skipEnd++

Write-Host "`nSkipping lines $skipStart to $skipEnd (Exam Examples section)"

$i = 0
while ($i -lt $lines.Count) {
    # Skip the standalone Exam Examples section
    if ($i -eq $skipStart) {
        Write-Host "Skipping standalone section at idx $i"
        $i = $skipEnd
        continue
    }
    
    $output.Add($lines[$i])
    
    # Check if this is the end of a tool's figure in Section 3
    foreach ($letter in $toolFigEnds.Keys) {
        if ($i -eq $toolFigEnds[$letter]) {
            # Insert the example block after this figure
            $output.Add("")
            # Change the h3 to h4 to make it a subsection
            foreach ($exLine in $exampleBlocks[$letter]) {
                $modified = $exLine -replace '<h3>([A-J])\. .+</h3>', '<h4>Exam Example</h4>'
                $output.Add($modified)
            }
            Write-Host "Inserted example $letter after idx $i"
        }
    }
    
    $i++
}

# Write output
[System.IO.File]::WriteAllLines($file, $output.ToArray())
Write-Host "`nDone! Original: $($lines.Count) lines, New: $($output.Count) lines"

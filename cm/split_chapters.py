import re, os

INPUT = r"D:\Final Year\Theory\cm\ocr_output\full_ocr_text.txt"
OUTDIR = r"D:\Final Year\Theory\cm\ocr_output"

with open(INPUT, "r", encoding="utf-8") as f:
    text = f.read()
    lines = text.split("\n")

# Find all PAGE markers
page_map = {}  # page_num -> line_index (0-based)
for i, line in enumerate(lines):
    m = re.match(r"^PAGE (\d+)$", line.strip())
    if m:
        page_map[int(m.group(1))] = i

print(f"Total lines: {len(lines)}, Pages found: {len(page_map)}")

# Print first content line of each page to find chapters
print("\n=== First content lines of each page ===")
for pnum in sorted(page_map.keys()):
    idx = page_map[pnum]
    content_lines = []
    for j in range(idx + 1, min(idx + 15, len(lines))):
        s = lines[j].strip()
        if s and s != "=" * 60:
            content_lines.append(s)
        if len(content_lines) >= 2:
            break
    first = " | ".join(content_lines[:2])
    print(f"  Page {pnum:3d} (L{idx+1:5d}): {first[:120]}")

# Based on the textbook structure from TOC, define chapter boundaries by page numbers
# We'll detect them by looking for chapter heading patterns on each page's first few lines
chapter_starts = {}  # chapter_num -> (page_num, line_index)

for pnum in sorted(page_map.keys()):
    idx = page_map[pnum]
    # Get content within first 10 lines of this page
    block = "\n".join(lines[idx:idx+12])
    
    # Pattern 1: Standalone chapter title pages (like "CONSTRUCTION MANAGEMENT\nFRAMEWORK")
    # Pattern 2: Lines like "2. PROJECT PLANNING" 
    # Pattern 3: Lines starting with chapter topic keywords
    
    patterns = [
        (1, r"CONSTRUCTION MANAGEMENT\s*\n\s*FRAMEWORK"),
        (2, r"PROJECT PLANNING"),
        (3, r"SCHEDULING"),
        (4, r"MATERIAL MANAGEMENT|MATERIALS MANAGEMENT"),
        (5, r"CONTRACT MANAGEMENT"),
        (6, r"EQUIPMENT MANAGEMENT"),
        (7, r"WORK EXECUTION|CONSTRUCTION EXECUTION"),
        (8, r"SITE MANAGEMENT"),
        (9, r"LABOR MANAGEMENT|LABOUR MANAGEMENT"),
        (10, r"QUALITY MANAGEMENT|QUALITY CONTROL"),
        (11, r"SAFETY|OCCUPATIONAL HEALTH"),
        (12, r"VALUATION"),
    ]
    
    for chap, pat in patterns:
        if chap not in chapter_starts and re.search(pat, block, re.IGNORECASE):
            # Verify it's a chapter start page (not just a mention)
            # Chapter starts typically have the title near the top
            first_5 = "\n".join(lines[idx:idx+8])
            if re.search(pat, first_5, re.IGNORECASE):
                chapter_starts[chap] = (pnum, idx)

print("\n=== Detected Chapter Starts ===")
for ch in sorted(chapter_starts.keys()):
    pnum, lidx = chapter_starts[ch]
    print(f"  Chapter {ch:2d} -> Page {pnum:3d} (line {lidx+1})")

# Now split the text by page-based chapter boundaries
chapters_sorted = sorted(chapter_starts.items())
print(f"\n=== Writing {len(chapters_sorted)} chapter files ===")

for i, (chap, (pnum, lidx)) in enumerate(chapters_sorted):
    # End = start of next chapter or end of file
    if i + 1 < len(chapters_sorted):
        _, (_, next_lidx) = chapters_sorted[i + 1]
        # Go back to include the PAGE separator
        end_lidx = next_lidx - 2  # before the separator of next chapter's page
    else:
        end_lidx = len(lines)
    
    # Start from 2 lines before (to include PAGE separator)
    start_lidx = max(0, lidx - 2)
    
    chapter_text = "\n".join(lines[start_lidx:end_lidx])
    fname = f"chapter{chap:02d}.txt"
    fpath = os.path.join(OUTDIR, fname)
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(chapter_text)
    
    num_lines = end_lidx - start_lidx
    print(f"  {fname}: pages {pnum}-{chapters_sorted[i+1][1][0]-1 if i+1 < len(chapters_sorted) else 386}, {num_lines} lines, {len(chapter_text)} chars")

# Also write frontmatter (before chapter 1)
if chapters_sorted:
    first_ch_lidx = chapters_sorted[0][1][1]
    front = "\n".join(lines[:first_ch_lidx - 2])
    fpath = os.path.join(OUTDIR, "00_frontmatter.txt")
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(front)
    print(f"  00_frontmatter.txt: {first_ch_lidx} lines, {len(front)} chars")

print("\nDone!")

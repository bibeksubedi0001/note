"""Fix equation rendering in SVG text elements across all GW_THE chapters.
Replaces plain-text subscript/superscript notation with proper SVG tspan elements."""
import re
import os

BASE = r"d:\Final Year\Theory\gw\GW_THE"
FILES = [f"chapter{i}.html" for i in range(5, 10)]

# Map of plain text patterns → proper SVG with tspan
# Only applies INSIDE <text> or <tspan> SVG elements
SUBSCRIPT_PATTERNS = [
    # Common subscript patterns (X_y format in displayed text)
    # Power & efficiency  
    (r'P_w\b', 'P<tspan baseline-shift="sub" font-size="75%">w</tspan>'),
    (r'P_s\b', 'P<tspan baseline-shift="sub" font-size="75%">s</tspan>'),
    (r'P_m\b', 'P<tspan baseline-shift="sub" font-size="75%">m</tspan>'),
    (r'P_N\b', 'P<tspan baseline-shift="sub" font-size="75%">N</tspan>'),
    (r'η_p\b', 'η<tspan baseline-shift="sub" font-size="75%">p</tspan>'),
    (r'η_m\b', 'η<tspan baseline-shift="sub" font-size="75%">m</tspan>'),
    # Head components
    (r'h_s\b', 'h<tspan baseline-shift="sub" font-size="75%">s</tspan>'),
    (r'h_d\b', 'h<tspan baseline-shift="sub" font-size="75%">d</tspan>'),
    (r'h_f\b', 'h<tspan baseline-shift="sub" font-size="75%">f</tspan>'),
    (r'h_v\b', 'h<tspan baseline-shift="sub" font-size="75%">v</tspan>'),
    (r'H_s\b', 'H<tspan baseline-shift="sub" font-size="75%">s</tspan>'),
    # Drawdown
    (r's_w\b', 's<tspan baseline-shift="sub" font-size="75%">w</tspan>'),
    (r's_1\b', 's<tspan baseline-shift="sub" font-size="75%">1</tspan>'),
    (r's_2\b', 's<tspan baseline-shift="sub" font-size="75%">2</tspan>'),
    # Hydraulic parameters
    (r'S_s\b', 'S<tspan baseline-shift="sub" font-size="75%">s</tspan>'),
    (r'S_y\b', 'S<tspan baseline-shift="sub" font-size="75%">y</tspan>'),
    (r'K_h\b', 'K<tspan baseline-shift="sub" font-size="75%">h</tspan>'),
    (r'K_v\b', 'K<tspan baseline-shift="sub" font-size="75%">v</tspan>'),
    (r'C_u\b', 'C<tspan baseline-shift="sub" font-size="75%">u</tspan>'),
    (r'v_e\b', 'v<tspan baseline-shift="sub" font-size="75%">e</tspan>'),
    (r'O_a\b', 'O<tspan baseline-shift="sub" font-size="75%">a</tspan>'),
    # Specific speed
    (r'N_s\b', 'N<tspan baseline-shift="sub" font-size="75%">s</tspan>'),
    # Resistivity
    (r'ρ_a\b', 'ρ<tspan baseline-shift="sub" font-size="75%">a</tspan>'),
    (r'x_c\b', 'x<tspan baseline-shift="sub" font-size="75%">c</tspan>'),
    # D-values (sieve analysis)
    (r'D_10\b', 'D<tspan baseline-shift="sub" font-size="75%">10</tspan>'),
    (r'D_50\b', 'D<tspan baseline-shift="sub" font-size="75%">50</tspan>'),
    (r'D_60\b', 'D<tspan baseline-shift="sub" font-size="75%">60</tspan>'),
    # General subscript-like: H_available, H_required
    (r'H_available\b', 'H<tspan baseline-shift="sub" font-size="75%">avail</tspan>'),
    (r'H_required\b', 'H<tspan baseline-shift="sub" font-size="75%">req</tspan>'),
]

SUPERSCRIPT_PATTERNS = [
    # Superscripts (e.g., H^(3/4))
    (r'H\^\(3/4\)', 'H<tspan baseline-shift="super" font-size="75%">3/4</tspan>'),
    (r'Q²', 'Q<tspan baseline-shift="super" font-size="75%">2</tspan>'),
]

def fix_svg_equations(html):
    """Fix equation text only inside SVG text/tspan elements."""
    count = 0
    
    def fix_text_content(match):
        nonlocal count
        tag_open = match.group(1)  # Everything before the text content
        content = match.group(2)   # The text content
        tag_close = match.group(3) # Closing tag
        
        original_content = content
        
        # Apply subscript fixes
        for pattern, replacement in SUBSCRIPT_PATTERNS:
            content = re.sub(pattern, replacement, content)
        
        # Apply superscript fixes
        for pattern, replacement in SUPERSCRIPT_PATTERNS:
            content = re.sub(pattern, replacement, content)
        
        if content != original_content:
            count += 1
        
        return tag_open + content + tag_close
    
    # Match SVG <text> elements (including those with attributes)
    # This matches: <text ...>content</text> where content doesn't contain nested text tags
    # We need to be more careful - process text between > and < within SVG blocks
    
    # Strategy: Find all SVG blocks, then within each, fix text content
    svg_pattern = re.compile(r'(<svg\b[^>]*>)(.*?)(</svg>)', re.DOTALL)
    
    def fix_svg_block(svg_match):
        nonlocal count
        svg_open = svg_match.group(1)
        svg_content = svg_match.group(2)
        svg_close = svg_match.group(3)
        
        # Within SVG content, fix text between > and < 
        def fix_text_segment(seg_match):
            nonlocal count
            prefix = seg_match.group(1)  # >
            text = seg_match.group(2)     # text content
            suffix = seg_match.group(3)   # <
            
            if not text.strip():
                return prefix + text + suffix
            
            original = text
            for pattern, replacement in SUBSCRIPT_PATTERNS:
                text = re.sub(pattern, replacement, text)
            for pattern, replacement in SUPERSCRIPT_PATTERNS:
                text = re.sub(pattern, replacement, text)
            
            if text != original:
                count += 1
            
            return prefix + text + suffix
        
        # Fix text between > and < (text nodes)
        svg_content = re.sub(r'(>)([^<]+)(<)', fix_text_segment, svg_content)
        
        return svg_open + svg_content + svg_close
    
    html = svg_pattern.sub(fix_svg_block, html)
    
    return html, count

# Also fix figcaption text that has plain subscript notation
def fix_figcaption_subscripts(html):
    """Fix subscript notation in figcaption divs."""
    count = 0
    
    def fix_caption(match):
        nonlocal count
        prefix = match.group(1)
        content = match.group(2)
        suffix = match.group(3)
        
        original = content
        # In HTML figcaptions, use <sub> tags
        for pattern, _ in SUBSCRIPT_PATTERNS:
            # Extract the base and subscript from the pattern
            plain = re.search(r'(\w+)_(\w+)', pattern.replace(r'\b', ''))
            if plain:
                base = plain.group(1)
                sub = plain.group(2)
                content = re.sub(re.escape(base) + r'_' + re.escape(sub) + r'\b', 
                               f'{base}<sub>{sub}</sub>', content)
        
        if content != original:
            count += 1
        
        return prefix + content + suffix
    
    html = re.sub(r'(<div class="figcaption">)(.*?)(</div>)', fix_caption, html, flags=re.DOTALL)
    return html, count


for fname in FILES:
    fpath = os.path.join(BASE, fname)
    if not os.path.exists(fpath):
        print(f"  ✗ {fname} not found")
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html, svg_fixes = fix_svg_equations(html)
    html, cap_fixes = fix_figcaption_subscripts(html)
    
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"  ✓ {fname}: {svg_fixes} SVG text fixes, {cap_fixes} figcaption fixes")

print("\nDone!")

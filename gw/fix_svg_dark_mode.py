"""
Fix SVGs for dark mode and apply Times New Roman font to all GW_THE chapters.

Strategy for SVG dark mode:
- Replace hardcoded fill="black" with fill="var(--ink, black)"  → uses CSS var
- Replace hardcoded stroke="black" with stroke="var(--ink, black)"
- Replace fill="white" background rects with fill="var(--paper, white)"
- Replace fill="#eee" with fill="var(--soft, #eee)"
- Replace fill="url(#hatch)" pattern fills - keep but fix pattern colors
- Add a <style> inside each SVG for dark mode color variables
- Update SVG inline font-family references
"""
import re
import os
import glob

GW_THE_DIR = os.path.join(os.path.dirname(__file__), 'GW_THE')

# CSS block to add to the <style> section of each file
DARK_MODE_SVG_CSS = """
    /* — Dark mode SVG support — */
    :root {
      --svg-fg: #111111;
      --svg-bg-fill: #ffffff;
      --svg-bg-soft: #eeeeee;
      --svg-bg-light: #f5f5f5;
      --svg-mid: #888888;
      --svg-dim: #777777;
      --svg-faint: #999999;
      --svg-wave: #4a90d9;
      --svg-accent: #2563eb;
      --svg-accent-2: #dc2626;
      --svg-accent-3: #16a34a;
      --svg-label-bg: rgba(255,255,255,0.92);
    }
    [data-theme="dark"] {
      --svg-fg: #e0ddd5;
      --svg-bg-fill: #1e222a;
      --svg-bg-soft: #252a36;
      --svg-bg-light: #2a2d33;
      --svg-mid: #8a8a8a;
      --svg-dim: #9a9a9a;
      --svg-faint: #7a7a7a;
      --svg-wave: #5ea3e0;
      --svg-accent: #60a5fa;
      --svg-accent-2: #f87171;
      --svg-accent-3: #4ade80;
      --svg-label-bg: rgba(30,34,42,0.92);
    }
    /* Force SVG text to follow theme */
    .figure-container svg text { fill: var(--svg-fg); }
    .figure-container svg line,
    .figure-container svg path,
    .figure-container svg rect,
    .figure-container svg circle,
    .figure-container svg polygon,
    .figure-container svg polyline,
    .figure-container svg ellipse { stroke: var(--svg-fg); }
    /* Font for all content */
    body, h1, h2, h3, h4, h5, p, span, div, li, table, td, th, a, small {
      font-family: 'Times New Roman', Times, serif;
    }
"""

# Updated SVG defs block with dark-mode aware patterns
NEW_SVG_DEFS = '''<svg style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true">
  <defs>
    <pattern id="hatch" width="10" height="10" patternTransform="rotate(45)" patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="0" y2="10" stroke="var(--svg-fg, black)" stroke-width="1.2"/></pattern>
    <pattern id="hatch-light" width="12" height="12" patternTransform="rotate(45)" patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="0" y2="12" stroke="var(--svg-mid, #888)" stroke-width="0.8"/></pattern>
    <pattern id="dots" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="2" fill="var(--svg-dim, #777)"/><circle cx="9" cy="9" r="2" fill="var(--svg-dim, #777)"/></pattern>
    <pattern id="dots-fine" width="8" height="8" patternUnits="userSpaceOnUse"><circle cx="4" cy="4" r="1.2" fill="var(--svg-faint, #999)"/></pattern>
    <pattern id="ground" width="14" height="10" patternUnits="userSpaceOnUse"><line x1="0" y1="10" x2="7" y2="0" stroke="var(--svg-fg, black)" stroke-width="0.8"/><line x1="7" y1="10" x2="14" y2="0" stroke="var(--svg-fg, black)" stroke-width="0.8"/></pattern>
    <marker id="arr" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto" markerUnits="strokeWidth"><polygon points="0 0, 10 3.5, 0 7" fill="var(--svg-fg, black)"/></marker>
    <marker id="arr-r" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto" markerUnits="strokeWidth"><polygon points="10 0, 0 3.5, 10 7" fill="var(--svg-fg, black)"/></marker>
  </defs>
</svg>'''


def fix_svg_colors(html):
    """Replace hardcoded SVG colors with CSS variable-aware alternatives."""
    
    # Find all content SVGs (not the defs SVG)
    # We need to process SVG elements within figure-container divs
    
    def fix_svg_element(svg_match):
        svg = svg_match.group(0)
        
        # Skip the hidden defs SVG
        if 'position:absolute' in svg and 'overflow:hidden' in svg:
            return svg
        
        # --- Fix strokes ---
        # stroke="black" → stroke="var(--svg-fg, #111)"
        svg = re.sub(r'stroke="black"', 'stroke="var(--svg-fg, #111)"', svg)
        svg = re.sub(r"stroke='black'", "stroke='var(--svg-fg, #111)'", svg)
        
        # --- Fix fills ---
        # fill="black" on polygons/arrows/markers → var(--svg-fg)
        svg = re.sub(r'fill="black"', 'fill="var(--svg-fg, #111)"', svg)
        svg = re.sub(r"fill='black'", "fill='var(--svg-fg, #111)'", svg)
        
        # fill="white" on background rects → var(--svg-bg-fill)
        svg = re.sub(r'fill="white"', 'fill="var(--svg-bg-fill, #fff)"', svg)
        svg = re.sub(r"fill='white'", "fill='var(--svg-bg-fill, #fff)'", svg)
        
        # fill="#eee" → var(--svg-bg-soft)
        svg = re.sub(r'fill="#eee"', 'fill="var(--svg-bg-soft, #eee)"', svg)
        svg = re.sub(r'fill="#EEE"', 'fill="var(--svg-bg-soft, #eee)"', svg)
        
        # fill="#f5f5f5" or similar light grays → var(--svg-bg-light)
        svg = re.sub(r'fill="#f5f5f5"', 'fill="var(--svg-bg-light, #f5f5f5)"', svg)
        svg = re.sub(r'fill="#F5F5F5"', 'fill="var(--svg-bg-light, #f5f5f5)"', svg)
        
        # background-color:white in inline styles
        svg = re.sub(r'background-color:\s*white', 'background-color:var(--svg-bg-fill, white)', svg)
        svg = re.sub(r'background:\s*white', 'background:var(--svg-bg-fill, white)', svg)
        
        # stroke="#888" → stroke="var(--svg-mid)"
        svg = re.sub(r'stroke="#888"', 'stroke="var(--svg-mid, #888)"', svg)
        
        # fill="#777" → fill="var(--svg-dim)"
        svg = re.sub(r'fill="#777"', 'fill="var(--svg-dim, #777)"', svg)
        
        # fill="#999" → fill="var(--svg-faint)"  
        svg = re.sub(r'fill="#999"', 'fill="var(--svg-faint, #999)"', svg)
        
        # Color references in text
        svg = re.sub(r'fill="#333"', 'fill="var(--svg-fg, #333)"', svg)
        svg = re.sub(r'fill="#222"', 'fill="var(--svg-fg, #222)"', svg)
        svg = re.sub(r'fill="#111"', 'fill="var(--svg-fg, #111)"', svg)
        svg = re.sub(r'fill="#000"', 'fill="var(--svg-fg, #000)"', svg)
        
        # Fix any remaining color:black in SVG inline styles
        svg = re.sub(r'color:\s*black', 'color:var(--svg-fg, black)', svg)
        
        return svg
    
    # Process all SVG elements
    html = re.sub(r'<svg\b[^>]*>.*?</svg>', fix_svg_element, html, flags=re.DOTALL)
    
    return html


def fix_defs_svg(html):
    """Replace the old defs SVG block with the new dark-mode aware one."""
    # Find and replace the hidden defs SVG
    old_defs_pattern = r'<svg\s+style="position:absolute[^"]*"[^>]*aria-hidden="true"[^>]*>\s*<defs>.*?</defs>\s*</svg>'
    html = re.sub(old_defs_pattern, NEW_SVG_DEFS, html, flags=re.DOTALL)
    return html


def add_dark_mode_css(html):
    """Add dark mode SVG CSS variables and font to the style block."""
    # Find the closing </style> in the head and add our CSS before it
    # But check if already added
    if '--svg-fg' in html:
        return html
    
    # Find the last @media rule in our style block and add after it
    html = html.replace(
        '    @media (max-width: 760px) { .grid-two { grid-template-columns: 1fr; } }\n  </style>',
        '    @media (max-width: 760px) { .grid-two { grid-template-columns: 1fr; } }\n' + DARK_MODE_SVG_CSS + '  </style>'
    )
    
    return html


def process_file(filepath):
    """Process a single chapter file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html
    
    # 1. Add dark mode CSS variables and font
    html = add_dark_mode_css(html)
    
    # 2. Fix the defs SVG
    html = fix_defs_svg(html)
    
    # 3. Fix all content SVG colors
    html = fix_svg_colors(html)
    
    if html != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated: {os.path.basename(filepath)}")
    else:
        print(f"No changes: {os.path.basename(filepath)}")


def main():
    files = sorted(glob.glob(os.path.join(GW_THE_DIR, 'chapter*.html')))
    for f in files:
        process_file(f)
    print(f"\nProcessed {len(files)} files.")


if __name__ == '__main__':
    main()

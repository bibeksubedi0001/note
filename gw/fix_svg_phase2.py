"""
Fix remaining hardcoded SVG colors for dark mode - Phase 2.
Handles semantic colors like water blue, concrete gray, etc.
"""
import re
import os
import glob

GW_THE_DIR = os.path.join(os.path.dirname(__file__), 'GW_THE')

# Map of hardcoded colors to CSS variable replacements
# These are semantic colors used in diagrams
COLOR_MAP = {
    # Light grays (backgrounds/structures)
    '#ddd': ('var(--svg-struct, #ddd)', '--svg-struct'),
    '#ccc': ('var(--svg-struct-2, #ccc)', '--svg-struct-2'),
    '#e0e0e0': ('var(--svg-struct-3, #e0e0e0)', '--svg-struct-3'),
    
    # Water blue
    '#d4e8ff': ('var(--svg-water, #d4e8ff)', '--svg-water'),
    '#4fc3f7': ('var(--svg-water-2, #4fc3f7)', '--svg-water-2'),
    '#3498db': ('var(--svg-water-3, #3498db)', '--svg-water-3'),
    '#2980b9': ('var(--svg-water-4, #2980b9)', '--svg-water-4'),
    '#5dade2': ('var(--svg-water-5, #5dade2)', '--svg-water-5'),
    '#1a5276': ('var(--svg-water-dk, #1a5276)', '--svg-water-dk'),
    
    # Warm tones
    '#c9a84c': ('var(--svg-gold, #c9a84c)', '--svg-gold'),
    '#8B7355': ('var(--svg-earth, #8B7355)', '--svg-earth'),
    '#ffb74d': ('var(--svg-orange, #ffb74d)', '--svg-orange'),
    '#fff3cd': ('var(--svg-sand, #fff3cd)', '--svg-sand'),
    
    # Reds
    '#c0392b': ('var(--svg-red, #c0392b)', '--svg-red'),
    
    # Misc text
    '#555': ('var(--svg-muted, #555)', '--svg-muted'),
}

# Additional CSS variables for dark mode
EXTRA_DARK_CSS = """
    /* — Additional dark mode SVG semantic colors — */
    :root {
      --svg-struct: #dddddd;
      --svg-struct-2: #cccccc;
      --svg-struct-3: #e0e0e0;
      --svg-water: #d4e8ff;
      --svg-water-2: #4fc3f7;
      --svg-water-3: #3498db;
      --svg-water-4: #2980b9;
      --svg-water-5: #5dade2;
      --svg-water-dk: #1a5276;
      --svg-gold: #c9a84c;
      --svg-earth: #8B7355;
      --svg-orange: #ffb74d;
      --svg-sand: #fff3cd;
      --svg-red: #c0392b;
      --svg-muted: #555555;
    }
    [data-theme="dark"] {
      --svg-struct: #3a3d44;
      --svg-struct-2: #33363d;
      --svg-struct-3: #2e3138;
      --svg-water: #1a3050;
      --svg-water-2: #2a6090;
      --svg-water-3: #2980b9;
      --svg-water-4: #2471a3;
      --svg-water-5: #4a90c8;
      --svg-water-dk: #5ea3e0;
      --svg-gold: #d4a017;
      --svg-earth: #9a8060;
      --svg-orange: #e69530;
      --svg-sand: #2a2518;
      --svg-red: #e74c3c;
      --svg-muted: #999999;
    }
"""


def fix_remaining_colors(html):
    """Replace remaining hardcoded hex colors in SVG elements."""
    
    def fix_svg(svg_match):
        svg = svg_match.group(0)
        
        # Skip hidden defs SVG
        if 'position:absolute' in svg and 'overflow:hidden' in svg:
            return svg
        
        for hex_color, (var_replacement, _) in COLOR_MAP.items():
            # fill="..." replacements
            svg = re.sub(
                rf'fill="{re.escape(hex_color)}"',
                f'fill="{var_replacement}"',
                svg, flags=re.IGNORECASE
            )
            # stroke="..." replacements
            svg = re.sub(
                rf'stroke="{re.escape(hex_color)}"',
                f'stroke="{var_replacement}"',
                svg, flags=re.IGNORECASE
            )
        
        return svg
    
    html = re.sub(r'<svg\b[^>]*>.*?</svg>', fix_svg, html, flags=re.DOTALL)
    return html


def add_extra_css(html):
    """Add extra dark mode CSS variables for semantic colors."""
    if '--svg-struct' in html:
        return html  # Already added
    
    # Insert before the closing </style>
    # Find the last </style> that's in the head
    insert_point = html.find('  </style>\n</head>')
    if insert_point == -1:
        insert_point = html.find('</style>')
    
    if insert_point != -1:
        html = html[:insert_point] + EXTRA_DARK_CSS + html[insert_point:]
    
    return html


def process_file(filepath):
    """Process a single chapter file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    original = html
    
    html = add_extra_css(html)
    html = fix_remaining_colors(html)
    
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

"""
Fix remaining SVG colors - Phase 3.
Handles all semantic accent colors from chapter8 pump diagrams and others.
"""
import re
import os
import glob

GW_THE_DIR = os.path.join(os.path.dirname(__file__), 'GW_THE')

# All remaining hex colors found in SVGs and their CSS variable mappings
COLOR_MAP = {
    # Blues (water/pump related)
    '#d6eaf8': ('var(--svg-blue-lt, #d6eaf8)', '--svg-blue-lt'),
    '#aed6f1': ('var(--svg-blue-md, #aed6f1)', '--svg-blue-md'),
    '#2471a3': ('var(--svg-blue-accent, #2471a3)', '--svg-blue-accent'),
    '#1f618d': ('var(--svg-blue-dk2, #1f618d)', '--svg-blue-dk2'),
    '#2e86c1': ('var(--svg-blue-mid, #2e86c1)', '--svg-blue-mid'),
    
    # Greens
    '#d5f5e3': ('var(--svg-green-lt, #d5f5e3)', '--svg-green-lt'),
    '#a9dfbf': ('var(--svg-green-md, #a9dfbf)', '--svg-green-md'),
    '#27ae60': ('var(--svg-green-accent, #27ae60)', '--svg-green-accent'),
    
    # Yellows/Oranges
    '#fef9e7': ('var(--svg-yellow-lt, #fef9e7)', '--svg-yellow-lt'),
    '#fad7a0': ('var(--svg-yellow-md, #fad7a0)', '--svg-yellow-md'),
    '#e67e22': ('var(--svg-orange-accent, #e67e22)', '--svg-orange-accent'),
    
    # Reds/Pinks
    '#fadbd8': ('var(--svg-red-lt, #fadbd8)', '--svg-red-lt'),
    '#f5b7b1': ('var(--svg-red-md, #f5b7b1)', '--svg-red-md'),
    '#e74c3c': ('var(--svg-red-accent, #e74c3c)', '--svg-red-accent'),
    
    # Purple
    '#f5eef8': ('var(--svg-purple-lt, #f5eef8)', '--svg-purple-lt'),
    '#8e44ad': ('var(--svg-purple-accent, #8e44ad)', '--svg-purple-accent'),
}

EXTRA_CSS = """
    /* — Phase 3: Semantic accent colors for dark mode — */
    :root {
      --svg-blue-lt: #d6eaf8;
      --svg-blue-md: #aed6f1;
      --svg-blue-accent: #2471a3;
      --svg-blue-dk2: #1f618d;
      --svg-blue-mid: #2e86c1;
      --svg-green-lt: #d5f5e3;
      --svg-green-md: #a9dfbf;
      --svg-green-accent: #27ae60;
      --svg-yellow-lt: #fef9e7;
      --svg-yellow-md: #fad7a0;
      --svg-orange-accent: #e67e22;
      --svg-red-lt: #fadbd8;
      --svg-red-md: #f5b7b1;
      --svg-red-accent: #e74c3c;
      --svg-purple-lt: #f5eef8;
      --svg-purple-accent: #8e44ad;
    }
    [data-theme="dark"] {
      --svg-blue-lt: #1a3050;
      --svg-blue-md: #1e4a70;
      --svg-blue-accent: #5ea3e0;
      --svg-blue-dk2: #4a90d0;
      --svg-blue-mid: #4a9ad8;
      --svg-green-lt: #1a2a1e;
      --svg-green-md: #1e3a25;
      --svg-green-accent: #4ade80;
      --svg-yellow-lt: #2a2518;
      --svg-yellow-md: #5a4a20;
      --svg-orange-accent: #f59e0b;
      --svg-red-lt: #2a1a1e;
      --svg-red-md: #3a2025;
      --svg-red-accent: #f87171;
      --svg-purple-lt: #251a30;
      --svg-purple-accent: #c084fc;
    }
"""


def fix_remaining_colors(html):
    """Replace remaining hardcoded colors in SVG elements."""
    
    def fix_svg(svg_match):
        svg = svg_match.group(0)
        if 'position:absolute' in svg and 'overflow:hidden' in svg:
            return svg
        
        for hex_color, (var_replacement, _) in COLOR_MAP.items():
            svg = re.sub(
                rf'fill="{re.escape(hex_color)}"',
                f'fill="{var_replacement}"',
                svg, flags=re.IGNORECASE
            )
            svg = re.sub(
                rf'stroke="{re.escape(hex_color)}"',
                f'stroke="{var_replacement}"',
                svg, flags=re.IGNORECASE
            )
        
        return svg
    
    html = re.sub(r'<svg\b[^>]*>.*?</svg>', fix_svg, html, flags=re.DOTALL)
    return html


def add_css(html):
    """Add CSS variables for semantic colors."""
    if '--svg-blue-lt' in html:
        return html
    
    # Find the Phase 2 extra CSS block end and add after it
    marker = '      --svg-muted: #555555;\n    }'
    if marker in html:
        html = html.replace(marker, marker + EXTRA_CSS)
    else:
        # Fallback: find the style closing tag
        idx = html.find('  </style>\n</head>')
        if idx != -1:
            html = html[:idx] + EXTRA_CSS + html[idx:]
    return html


def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    original = html
    html = add_css(html)
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

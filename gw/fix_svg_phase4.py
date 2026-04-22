"""
Fix ALL remaining hardcoded SVG colors - Final comprehensive sweep.
"""
import re
import os
import glob

GW_THE_DIR = os.path.join(os.path.dirname(__file__), 'GW_THE')

# Complete map of remaining colors
COLOR_MAP = {
    # Dark slate/charcoal (structural lines in ch8)
    '#2c3e50': ('var(--svg-slate, #2c3e50)', '--svg-slate'),
    
    # Grays
    '#bbb': ('var(--svg-gray-md, #bbb)', '--svg-gray-md'),
    '#aab7b8': ('var(--svg-gray-cool, #aab7b8)', '--svg-gray-cool'),
    '#d5dbdb': ('var(--svg-gray-lt, #d5dbdb)', '--svg-gray-lt'),
    
    # Blues (more shades from ch8)
    '#85c1e9': ('var(--svg-sky, #85c1e9)', '--svg-sky'),
    
    # Purple
    '#e8daef': ('var(--svg-purple-lt2, #e8daef)', '--svg-purple-lt2'),
}

EXTRA_CSS = """
    /* — Phase 4: Final remaining accent colors — */
    :root {
      --svg-slate: #2c3e50;
      --svg-gray-md: #bbbbbb;
      --svg-gray-cool: #aab7b8;
      --svg-gray-lt: #d5dbdb;
      --svg-sky: #85c1e9;
      --svg-purple-lt2: #e8daef;
    }
    [data-theme="dark"] {
      --svg-slate: #a0b0c0;
      --svg-gray-md: #4a4d55;
      --svg-gray-cool: #4a5055;
      --svg-gray-lt: #353840;
      --svg-sky: #4a90c8;
      --svg-purple-lt2: #2a1e38;
    }
"""


def fix_colors(html):
    def fix_svg(m):
        svg = m.group(0)
        if 'position:absolute' in svg and 'overflow:hidden' in svg:
            return svg
        for hex_c, (var_r, _) in COLOR_MAP.items():
            svg = re.sub(rf'fill="{re.escape(hex_c)}"', f'fill="{var_r}"', svg, flags=re.IGNORECASE)
            svg = re.sub(rf'stroke="{re.escape(hex_c)}"', f'stroke="{var_r}"', svg, flags=re.IGNORECASE)
        return svg
    return re.sub(r'<svg\b[^>]*>.*?</svg>', fix_svg, html, flags=re.DOTALL)


def add_css(html):
    if '--svg-slate' in html:
        return html
    marker = '      --svg-purple-accent: #c084fc;\n    }'
    if marker in html:
        html = html.replace(marker, marker + EXTRA_CSS)
    return html


def process_file(fp):
    with open(fp, 'r', encoding='utf-8') as f:
        html = f.read()
    orig = html
    html = add_css(html)
    html = fix_colors(html)
    if html != orig:
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Updated: {os.path.basename(fp)}")
    else:
        print(f"No changes: {os.path.basename(fp)}")


def main():
    files = sorted(glob.glob(os.path.join(GW_THE_DIR, 'chapter*.html')))
    for f in files:
        process_file(f)
    print(f"\nDone. Processed {len(files)} files.")


if __name__ == '__main__':
    main()

"""Add prev/next chapter navigation to all GW_THE chapter files."""
import os

GW_THE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'GW_THE')

CHAPTERS = [
    {'file': 'chapter1.html', 'num': 1, 'short': 'Occurrence of GW'},
    {'file': 'chapter2.html', 'num': 2, 'short': 'GW Motion'},
    {'file': 'chapter3.html', 'num': 3, 'short': 'Flow Theory'},
    {'file': 'chapter4.html', 'num': 4, 'short': 'Well Hydraulics'},
    {'file': 'chapter5.html', 'num': 5, 'short': 'Pumping Tests'},
    {'file': 'chapter6.html', 'num': 6, 'short': 'GW Exploration'},
    {'file': 'chapter7.html', 'num': 7, 'short': 'Well Design'},
    {'file': 'chapter8.html', 'num': 8, 'short': 'Pumps'},
    {'file': 'chapter9.html', 'num': 9, 'short': 'GW in Nepal'},
]

def make_nav(i):
    """Build chapter-nav HTML for chapter at index i."""
    lines = ['\n    <nav class="chapter-nav">']
    if i > 0:
        prev = CHAPTERS[i - 1]
        lines.append(f'      <a href="{prev["file"]}">')
        lines.append(f'        <span class="nav-label">&larr; Previous</span>')
        lines.append(f'        <span class="nav-title">Ch {prev["num"]}: {prev["short"]}</span>')
        lines.append(f'      </a>')
    if i < len(CHAPTERS) - 1:
        nxt = CHAPTERS[i + 1]
        lines.append(f'      <a href="{nxt["file"]}" class="nav-next">')
        lines.append(f'        <span class="nav-label">Next &rarr;</span>')
        lines.append(f'        <span class="nav-title">Ch {nxt["num"]}: {nxt["short"]}</span>')
        lines.append(f'      </a>')
    lines.append('    </nav>')
    return '\n'.join(lines)

for i, ch in enumerate(CHAPTERS):
    path = os.path.join(GW_THE, ch['file'])
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    nav_html = make_nav(i)

    # Remove existing chapter-nav if present (idempotent)
    import re
    html = re.sub(r'\n\s*<nav class="chapter-nav">.*?</nav>', '', html, flags=re.DOTALL)

    # Insert before </main>
    # Try pattern with blank line first, then without
    if '\n  </main>\n</div>' in html:
        html = html.replace(
            '\n  </main>\n</div>',
            nav_html + '\n  </main>\n</div>',
            1
        )
    elif '</main>\n</div>' in html:
        html = html.replace(
            '</main>\n</div>',
            nav_html + '\n  </main>\n</div>',
            1
        )
    else:
        print(f"WARNING: Could not find </main> pattern in {ch['file']}")
        continue

    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Added nav to {ch['file']} (prev={'Ch'+str(CHAPTERS[i-1]['num']) if i>0 else 'none'}, next={'Ch'+str(CHAPTERS[i+1]['num']) if i<len(CHAPTERS)-1 else 'none'})")

print("\nDone! Chapter navigation added to all 9 files.")

"""
Transform gw/Theory chapter HTML files to match cm/Theory design (using TES/style.css).
Creates new files in gw/GW_THE/ folder.
"""
import re
import os

CHAPTERS = {
    'chapter3_flow_theory.html': {
        'out': 'chapter3.html',
        'num': '3',
        'title': 'Potential Groundwater Flow Theory and Flow Net Analysis',
        'hours': '8',
        'badge_topic': 'Flow Theory & Flow Nets',
        'badge_exam': '~15+ Past Questions',
    },
    'chapter4_well_hydraulics_old.html': {
        'out': 'chapter4.html',
        'num': '4',
        'title': 'Well Hydraulics',
        'hours': '10',
        'badge_topic': 'Well Hydraulics',
        'badge_exam': '~20+ Past Questions',
    },
    'chapter5_pumping_test.html': {
        'out': 'chapter5.html',
        'num': '5',
        'title': 'Pumping Test and Analysis',
        'hours': '8',
        'badge_topic': 'Pumping Tests',
        'badge_exam': '~15+ Past Questions',
    },
    'chapter6_groundwater_exploration.html': {
        'out': 'chapter6.html',
        'num': '6',
        'title': 'Groundwater Exploration',
        'hours': '6',
        'badge_topic': 'GW Exploration',
        'badge_exam': '~12+ Past Questions',
    },
    'chapter7_water_well_design.html': {
        'out': 'chapter7.html',
        'num': '7',
        'title': 'Water Well Design and Construction',
        'hours': '6',
        'badge_topic': 'Well Design',
        'badge_exam': '~15+ Past Questions',
    },
    'chapter8_pumps.html': {
        'out': 'chapter8.html',
        'num': '8',
        'title': 'Pumps for Water Wells',
        'hours': '4',
        'badge_topic': 'Pumps',
        'badge_exam': '~10+ Past Questions',
    },
    'chapter9_groundwater_nepal.html': {
        'out': 'chapter9.html',
        'num': '9',
        'title': 'Groundwater Development in Nepal',
        'hours': '3',
        'badge_topic': 'GW in Nepal',
        'badge_exam': '~8+ Past Questions',
    },
}

TEMPLATE_HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Chapter {num} &ndash; {title}</title>
  <link rel="stylesheet" href="../../TES/style.css">
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    /* GW-specific additions for content compatibility */
    .equation {{ display: flex; justify-content: center; align-items: center; margin: 1.5rem 0; overflow-x: auto; }}
    .figure-container {{ text-align: center; margin: 2rem 0; padding: 1rem; border: 1px solid var(--line); border-radius: var(--radius); overflow-x: auto; background: var(--soft); }}
    .figcaption {{ font-style: italic; margin-top: 0.5rem; text-align: center; color: var(--muted); }}
    .info-table, .question-table, .formula-table {{ width: 100%; border-collapse: collapse; margin: 1rem 0; }}
    .info-table th, .info-table td, .question-table th, .question-table td,
    .formula-table th, .formula-table td {{ border: 1px solid var(--line); padding: 8px 12px; text-align: left; vertical-align: top; }}
    .info-table th, .question-table th, .formula-table th {{ font-weight: bold; background: var(--soft); }}
    .toc {{ border: 1px solid var(--line); padding: 1.2rem; margin-bottom: 1.5rem; border-radius: var(--radius); background: var(--soft); }}
    .toc ol {{ margin-bottom: 0; }} .toc a {{ text-decoration: none; color: var(--accent); }}
    .toc a:hover {{ text-decoration: underline; }}
    .grid-two {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem; }}
    .mini-note {{ border: 1px solid var(--line); padding: 0.85rem; margin: 1rem 0; border-radius: var(--radius); background: var(--soft); }}
    .solution-box {{ border: 2px solid var(--accent); padding: 1.2rem; margin-bottom: 1.5rem; border-radius: var(--radius); background: var(--accent-light); }}
    .solution-box h4 {{ font-weight: bold; margin-top: 0; border-bottom: 1px dashed var(--line); padding-bottom: 0.25rem; }}
    .study-note {{ border: 1px solid var(--green); padding: 1rem; margin-bottom: 1.5rem; border-radius: var(--radius); background: var(--green-lt); }}
    .study-note h4 {{ margin-top: 0; border-bottom: 1px dashed var(--line); padding-bottom: 0.25rem; }}
    .question-card {{ border: 1px solid var(--line); padding: 1rem; margin-bottom: 1.5rem; border-radius: var(--radius); background: var(--soft); }}
    .question-card h4 {{ margin-top: 0; border-bottom: 1px dashed var(--line); padding-bottom: 0.25rem; }}
    .question-meta {{ display: flex; flex-wrap: wrap; gap: 0.5rem; margin-bottom: 0.75rem; }}
    .pill {{ display: inline-block; border: 1px solid var(--line); padding: 2px 8px; font-size: 0.85em; border-radius: 4px; background: var(--soft); }}
    .data-block {{ margin-top: 0.75rem; padding: 0.75rem; border: 1px solid var(--line); border-radius: var(--radius); background: var(--soft); }}
    .data-block pre {{ margin: 0; white-space: pre-wrap; word-break: break-word; font-family: 'Courier New', Courier, monospace; font-size: 0.92rem; line-height: 1.45; }}
    .example-box {{ border: 1px solid var(--accent); padding: 1.2rem; margin: 1.5rem 0; border-radius: var(--radius); background: var(--accent-light); }}
    @media (max-width: 760px) {{ .grid-two {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
<svg style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true">
  <defs>
    <pattern id="hatch" width="10" height="10" patternTransform="rotate(45)" patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="0" y2="10" stroke="currentColor" stroke-width="1.2"/></pattern>
    <pattern id="hatch-light" width="12" height="12" patternTransform="rotate(45)" patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="0" y2="12" stroke="#888" stroke-width="0.8"/></pattern>
    <pattern id="dots" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="2" fill="#777"/><circle cx="9" cy="9" r="2" fill="#777"/></pattern>
    <pattern id="dots-fine" width="8" height="8" patternUnits="userSpaceOnUse"><circle cx="4" cy="4" r="1.2" fill="#999"/></pattern>
    <pattern id="ground" width="14" height="10" patternUnits="userSpaceOnUse"><line x1="0" y1="10" x2="7" y2="0" stroke="currentColor" stroke-width="0.8"/><line x1="7" y1="10" x2="14" y2="0" stroke="currentColor" stroke-width="0.8"/></pattern>
    <marker id="arr" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto" markerUnits="strokeWidth"><polygon points="0 0, 10 3.5, 0 7" fill="currentColor"/></marker>
    <marker id="arr-r" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto" markerUnits="strokeWidth"><polygon points="10 0, 0 3.5, 10 7" fill="currentColor"/></marker>
  </defs>
</svg>
<div class="scroll-progress" id="scrollProgress"></div>
<button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode">&#9790;</button>
<button class="scroll-top" id="scrollTop" aria-label="Scroll to top">&#8593;</button>

<div class="page">
  <header>
    <a href="../index.html" class="back-link">&larr; GW Home</a>
    <div class="eyebrow">Chapter {num}</div>
    <h1>{title} <span style="font-weight:400;font-size:.55em">[{hours} Hours]</span></h1>
    <div class="chapter-meta">
      <span class="meta-badge topic">{badge_topic}</span>
      <span class="meta-badge exam">{badge_exam}</span>
    </div>
  </header>
  <main>
'''

TEMPLATE_FOOT = '''  </main>
</div>
<script src="../../common.js"></script>
</body>
</html>
'''

def extract_content(html_text):
    """Extract the body content from the original HTML, removing old head/styles/dark-mode."""
    # Find the <main> tag content
    main_match = re.search(r'<main[^>]*>(.*?)</main>', html_text, re.DOTALL)
    if not main_match:
        # Try to find content after the body tag
        body_match = re.search(r'<body[^>]*>(.*?)</body>', html_text, re.DOTALL)
        if body_match:
            content = body_match.group(1)
        else:
            return html_text
    else:
        content = main_match.group(1)
    
    # Remove the old header section (we'll add our own)
    content = re.sub(r'<header>.*?</header>', '', content, flags=re.DOTALL)
    
    # Remove the old print button
    content = re.sub(r'<button[^>]*class="print-btn"[^>]*>.*?</button>', '', content, flags=re.DOTALL)
    
    # Remove old SVG defs block (we add our own)
    content = re.sub(r'<svg[^>]*style="position:absolute[^"]*"[^>]*>.*?</svg>', '', content, flags=re.DOTALL)
    
    # Remove old dark mode toggle button
    content = re.sub(r'<button[^>]*class="dm-toggle"[^>]*>.*?</button>', '', content, flags=re.DOTALL)
    
    # Remove dark mode script
    content = re.sub(r'<script>\s*//\s*Dark\s*mode.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'<script>\s*\(function\s*\(\)\s*\{[^}]*dark[^}]*theme[^}]*\}.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Clean up excessive whitespace
    content = re.sub(r'\n{4,}', '\n\n', content)
    
    # Indent content properly
    lines = content.split('\n')
    cleaned_lines = []
    for line in lines:
        # Remove excessive leading whitespace but keep structure
        stripped = line.rstrip()
        if stripped:
            # Normalize indentation: remove first 8 spaces if present, add 4
            if stripped.startswith('        '):
                stripped = '    ' + stripped[8:]
            elif stripped.startswith('    '):
                stripped = '    ' + stripped[4:]
            cleaned_lines.append(stripped)
        else:
            cleaned_lines.append('')
    
    return '\n'.join(cleaned_lines)


def transform_chapter(src_path, info, out_dir):
    """Read source chapter, extract content, wrap in new template, write to output."""
    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    content = extract_content(html)
    
    head = TEMPLATE_HEAD.format(**info)
    
    output = head + content + TEMPLATE_FOOT
    
    out_path = os.path.join(out_dir, info['out'])
    os.makedirs(out_dir, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"Created: {out_path}")


def main():
    src_dir = os.path.join(os.path.dirname(__file__), 'Theory')
    out_dir = os.path.join(os.path.dirname(__file__), 'GW_THE')
    
    for src_file, info in CHAPTERS.items():
        src_path = os.path.join(src_dir, src_file)
        if os.path.exists(src_path):
            transform_chapter(src_path, info, out_dir)
        else:
            print(f"WARNING: {src_path} not found, skipping")
    
    # Create index.html
    create_index(out_dir)
    print("Done! All chapters transformed.")


def create_index(out_dir):
    """Create index page for GW_THE folder."""
    index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Groundwater Engineering &ndash; Theory</title>
  <link rel="stylesheet" href="../../TES/style.css">
</head>
<body>
<div class="scroll-progress" id="scrollProgress"></div>
<button class="theme-toggle" id="themeToggle" aria-label="Toggle dark mode">&#9790;</button>
<button class="scroll-top" id="scrollTop" aria-label="Scroll to top">&#8593;</button>

<div class="page">
  <header>
    <a href="../index.html" class="back-link">&larr; GW Home</a>
    <div class="eyebrow">CE 76509</div>
    <h1>Groundwater Engineering <span style="font-weight:400;font-size:.55em">Theory Chapters</span></h1>
    <div class="chapter-meta">
      <span class="meta-badge topic">Chapters 3&ndash;9</span>
      <span class="meta-badge exam">Complete Theory</span>
    </div>
  </header>
  <main>
    <div class="chapter-grid">
      <a href="chapter3.html" class="chapter-card">
        <span class="card-number">3</span>
        <span class="card-title">Potential Groundwater Flow Theory &amp; Flow Nets</span>
        <span class="card-hours">8 Hours</span>
      </a>
      <a href="chapter4.html" class="chapter-card">
        <span class="card-number">4</span>
        <span class="card-title">Well Hydraulics</span>
        <span class="card-hours">10 Hours</span>
      </a>
      <a href="chapter5.html" class="chapter-card">
        <span class="card-number">5</span>
        <span class="card-title">Pumping Test and Analysis</span>
        <span class="card-hours">8 Hours</span>
      </a>
      <a href="chapter6.html" class="chapter-card">
        <span class="card-number">6</span>
        <span class="card-title">Groundwater Exploration</span>
        <span class="card-hours">6 Hours</span>
      </a>
      <a href="chapter7.html" class="chapter-card">
        <span class="card-number">7</span>
        <span class="card-title">Water Well Design &amp; Construction</span>
        <span class="card-hours">6 Hours</span>
      </a>
      <a href="chapter8.html" class="chapter-card">
        <span class="card-number">8</span>
        <span class="card-title">Pumps for Water Wells</span>
        <span class="card-hours">4 Hours</span>
      </a>
      <a href="chapter9.html" class="chapter-card">
        <span class="card-number">9</span>
        <span class="card-title">Groundwater Development in Nepal</span>
        <span class="card-hours">3 Hours</span>
      </a>
    </div>
  </main>
</div>
<script src="../../common.js"></script>
</body>
</html>
'''
    out_path = os.path.join(out_dir, 'index.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    print(f"Created: {out_path}")


if __name__ == '__main__':
    main()

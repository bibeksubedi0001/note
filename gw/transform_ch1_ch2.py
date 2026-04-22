"""Transform gw/Theory chapter1 and chapter2 (_old versions) into GW_THE template format."""
import re, os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(SCRIPT_DIR, 'Theory')
DST_DIR = os.path.join(SCRIPT_DIR, 'GW_THE')

# Chapter metadata — using _old source files
CHAPTERS = {
    'chapter1_groundwater_old.html': {
        'out': 'chapter1.html',
        'num': '1',
        'title': 'Occurrence of Groundwater and Its Importance',
        'hours': '5',
        'topic': 'GW Occurrence & Importance',
        'exam': '~8 Past Questions',
    },
    'chapter2_groundwater_motion_old.html': {
        'out': 'chapter2.html',
        'num': '2',
        'title': 'Fundamentals of Groundwater Motion',
        'hours': '8',
        'topic': 'GW Motion & Darcy\'s Law',
        'exam': '~12+ Past Questions',
        'inject_solutions': True,  # old file lacks sec-2-8 worked solutions
    },
}

# Template head (matches existing GW_THE chapters exactly)
TEMPLATE_HEAD = r'''<!DOCTYPE html>
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

    /* — Dark mode SVG support — */
    :root {{
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
    }}
    [data-theme="dark"] {{
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
    }}
    /* Force SVG text to follow theme */
    .figure-container svg text {{ fill: var(--svg-fg); }}
    .figure-container svg line,
    .figure-container svg path,
    .figure-container svg rect,
    .figure-container svg circle,
    .figure-container svg polygon,
    .figure-container svg polyline,
    .figure-container svg ellipse {{ stroke: var(--svg-fg); }}
    /* Font for all content */
    body, h1, h2, h3, h4, h5, p, span, div, li, table, td, th, a, small {{
      font-family: 'Times New Roman', Times, serif;
    }}

    /* — Additional dark mode SVG semantic colors — */
    :root {{
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
    }}
    :root {{
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
    }}
    [data-theme="dark"] {{
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
    }}
    :root {{
      --svg-slate: #2c3e50;
      --svg-gray-md: #bbbbbb;
      --svg-gray-cool: #aab7b8;
      --svg-gray-lt: #d5dbdb;
      --svg-sky: #85c1e9;
      --svg-purple-lt2: #e8daef;
    }}
    [data-theme="dark"] {{
      --svg-slate: #a0b0c0;
      --svg-gray-md: #4a4d55;
      --svg-gray-cool: #4a5055;
      --svg-gray-lt: #353840;
      --svg-sky: #4a90c8;
      --svg-purple-lt2: #2a1e38;
    }}

    [data-theme="dark"] {{
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
    }}
  </style>
</head>
<body>
<svg style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true">
  <defs>
    <pattern id="hatch" width="10" height="10" patternTransform="rotate(45)" patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="0" y2="10" stroke="var(--svg-fg, black)" stroke-width="1.2"/></pattern>
    <pattern id="hatch-light" width="12" height="12" patternTransform="rotate(45)" patternUnits="userSpaceOnUse"><line x1="0" y1="0" x2="0" y2="12" stroke="var(--svg-mid, #888)" stroke-width="0.8"/></pattern>
    <pattern id="dots" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="2" fill="var(--svg-dim, #777)"/><circle cx="9" cy="9" r="2" fill="var(--svg-dim, #777)"/></pattern>
    <pattern id="dots-coarse" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="3" cy="3" r="2" fill="var(--svg-dim, #777)"/><circle cx="9" cy="9" r="2" fill="var(--svg-dim, #777)"/></pattern>
    <pattern id="dots-fine" width="8" height="8" patternUnits="userSpaceOnUse"><circle cx="4" cy="4" r="1.2" fill="var(--svg-faint, #999)"/></pattern>
    <pattern id="ground" width="14" height="10" patternUnits="userSpaceOnUse"><line x1="0" y1="10" x2="7" y2="0" stroke="var(--svg-fg, black)" stroke-width="0.8"/><line x1="7" y1="10" x2="14" y2="0" stroke="var(--svg-fg, black)" stroke-width="0.8"/></pattern>
    <marker id="arr" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto" markerUnits="strokeWidth"><polygon points="0 0, 10 3.5, 0 7" fill="var(--svg-fg, black)"/></marker>
    <marker id="arr-r" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto" markerUnits="strokeWidth"><polygon points="10 0, 0 3.5, 10 7" fill="var(--svg-fg, black)"/></marker>
    <marker id="arrow" markerWidth="10" markerHeight="7" refX="10" refY="3.5" orient="auto" markerUnits="strokeWidth"><polygon points="0 0, 10 3.5, 0 7" fill="var(--svg-fg, black)"/></marker>
    <marker id="arrow-rev" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto" markerUnits="strokeWidth"><polygon points="10 0, 0 3.5, 10 7" fill="var(--svg-fg, black)"/></marker>
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
      <span class="meta-badge topic">{topic}</span>
      <span class="meta-badge exam">{exam}</span>
    </div>
  </header>
  <main>

'''

TEMPLATE_TAIL = '''
  </main>
</div>

<script src="../../common.js"></script>
</body>
</html>
'''

def extract_body_content(html):
    """Extract content between <main>...</main>, stripping old header."""
    # Find content after the old header block inside <main>
    # The old files have: <main> <header>...</header> <section>...
    m = re.search(r'<main>\s*<header>.*?</header>\s*(.*?)\s*</main>', html, re.DOTALL)
    if m:
        return m.group(1).strip()
    # Fallback: try to get everything between first <section and </main>
    m = re.search(r'(<section.*?)\s*</main>', html, re.DOTALL)
    if m:
        return m.group(1).strip()
    raise ValueError("Could not extract body content")

def fix_svg_colors(content):
    """Replace hardcoded SVG colors with CSS variables for dark mode."""
    # Core colors
    replacements = [
        # Stroke/fill black → var(--svg-fg)
        (r'(stroke|fill)="black"', r'\1="var(--svg-fg, black)"'),
        # Stroke/fill white → var(--svg-bg-fill)
        (r'(stroke|fill)="white"', r'\1="var(--svg-bg-fill, #fff)"'),
        # Fill #ddd, #ccc, #eee → var(--svg-struct)
        (r'fill="#[dD]{3}"', 'fill="var(--svg-struct, #ddd)"'),
        (r'fill="#[cC]{3}"', 'fill="var(--svg-struct-2, #ccc)"'),
        (r'fill="#[eE]{3}"', 'fill="var(--svg-bg-soft, #eee)"'),
        (r'fill="#f5f5f5"', 'fill="var(--svg-bg-light, #f5f5f5)"'),
        # Fill various grays
        (r'fill="#888"', 'fill="var(--svg-mid, #888)"'),
        (r'fill="#777"', 'fill="var(--svg-dim, #777)"'),
        (r'fill="#999"', 'fill="var(--svg-faint, #999)"'),
        (r'fill="#666"', 'fill="var(--svg-muted, #666)"'),
        # Stroke grays
        (r'stroke="#888"', 'stroke="var(--svg-mid, #888)"'),
        (r'stroke="#777"', 'stroke="var(--svg-dim, #777)"'),
        (r'stroke="#999"', 'stroke="var(--svg-faint, #999)"'),
        (r'stroke="#666"', 'stroke="var(--svg-muted, #666)"'),
        (r'stroke="#aaa"', 'stroke="var(--svg-faint, #aaa)"'),
        (r'stroke="#bbb"', 'stroke="var(--svg-gray-md, #bbb)"'),
        # Named colors
        (r'stroke="blue"', 'stroke="var(--svg-water-3, #3498db)"'),
        (r'fill="blue"', 'fill="var(--svg-water-3, #3498db)"'),
        (r'stroke="red"', 'stroke="var(--svg-red-accent, #e74c3c)"'),
        (r'fill="red"', 'fill="var(--svg-red-accent, #e74c3c)"'),
        (r'stroke="green"', 'stroke="var(--svg-green-accent, #27ae60)"'),
        (r'fill="green"', 'fill="var(--svg-green-accent, #27ae60)"'),
        # Named colors - brown/gray/etc
        (r'stroke="gray"', 'stroke="var(--svg-mid, #888)"'),
        (r'fill="gray"', 'fill="var(--svg-mid, #888)"'),
        (r'stroke="grey"', 'stroke="var(--svg-mid, #888)"'),
        (r'fill="grey"', 'fill="var(--svg-mid, #888)"'),
        # Hex blues
        (r'(stroke|fill)="#3498db"', r'\1="var(--svg-water-3, #3498db)"'),
        (r'(stroke|fill)="#2980b9"', r'\1="var(--svg-water-4, #2980b9)"'),
        (r'(stroke|fill)="#4fc3f7"', r'\1="var(--svg-water-2, #4fc3f7)"'),
        (r'(stroke|fill)="#5dade2"', r'\1="var(--svg-water-5, #5dade2)"'),
        # Hex reds
        (r'(stroke|fill)="#c0392b"', r'\1="var(--svg-red, #c0392b)"'),
        (r'(stroke|fill)="#e74c3c"', r'\1="var(--svg-red-accent, #e74c3c)"'),
        # Hex greens
        (r'(stroke|fill)="#27ae60"', r'\1="var(--svg-green-accent, #27ae60)"'),
        (r'(stroke|fill)="#16a34a"', r'\1="var(--svg-accent-3, #16a34a)"'),
        # Light fills
        (r'fill="#d4e8ff"', 'fill="var(--svg-water, #d4e8ff)"'),
        (r'fill="#fff3cd"', 'fill="var(--svg-sand, #fff3cd)"'),
    ]
    for pattern, repl in replacements:
        content = re.sub(pattern, repl, content)
    return content

CH2_SOLUTIONS = r'''
        <!-- ======== 2.8 WORKED SOLUTIONS ======== -->
        <section id="sec-2-8">
            <h2>2.8 WORKED NUMERICAL SOLUTIONS</h2>

            <div class="solution-box">
                <h4>SOLUTION 1: 2078 Chaitra Q2(b) — Darcy Validity Domain</h4>
                <p><strong>Given:</strong> \(Q = 0.3\) m&sup3;/s, \(b = 18\) m, \(d_m = 1\) mm = \(0.001\) m, \(Re_{cr} = 8\), \(\nu = 1\) centistoke = \(1 \times 10^{-6}\) m&sup2;/s.</p>
                <p><strong>Required:</strong> Minimum radius \(r_{min}\) from the well beyond which Darcy's law is valid.</p>
                <p><strong>Step 1:</strong> For a fully penetrating well in a confined aquifer, the Darcy flux at radial distance \(r\) is:</p>
                <div class="equation">$$ q_r = \frac{Q}{2\pi r b} $$</div>
                <p><strong>Step 2:</strong> Reynolds number defined using Darcy flux:</p>
                <div class="equation">$$ Re = \frac{q_r \cdot d_m}{\nu} = \frac{Q \cdot d_m}{2\pi \cdot r \cdot b \cdot \nu} $$</div>
                <p><strong>Step 3:</strong> At the boundary of Darcy validity, \(Re = Re_{cr}\). Solve for \(r_{min}\):</p>
                <div class="equation">$$ r_{min} = \frac{Q \cdot d_m}{2\pi \cdot b \cdot \nu \cdot Re_{cr}} $$</div>
                <p><strong>Step 4:</strong> Substitute values:</p>
                <div class="equation">$$ r_{min} = \frac{0.3 \times 0.001}{2\pi \times 18 \times 1 \times 10^{-6} \times 8} $$</div>
                <div class="equation">$$ r_{min} = \frac{3 \times 10^{-4}}{2\pi \times 144 \times 10^{-6}} = \frac{3 \times 10^{-4}}{9.0478 \times 10^{-4}} $$</div>
                <div class="equation">$$ \boxed{r_{min} = 0.332 \text{ m} \approx 0.33 \text{ m}} $$</div>
                <p><strong>Conclusion:</strong> Darcy's law is valid for \(r \geq 0.33\) m from the well centre. Within 0.33 m, flow velocities are too high and non-Darcian effects dominate.</p>
            </div>

            <div class="solution-box">
                <h4>SOLUTION 2: 2073 Bhadra Q2(b) — Darcy Validity Domain</h4>
                <p><strong>Given:</strong> \(Q = 1000\) m&sup3;/hr, \(b = 28\) m, \(d_m = 1\) mm = \(0.001\) m, \(Re_{cr} = 6\), \(\nu = 1\) centistoke = \(1 \times 10^{-6}\) m&sup2;/s.</p>
                <p><strong>Step 1:</strong> Convert units: \(Q = \frac{1000}{3600} = 0.2778\) m&sup3;/s.</p>
                <p><strong>Step 2:</strong> Apply the formula:</p>
                <div class="equation">$$ r_{min} = \frac{Q \cdot d_m}{2\pi \cdot b \cdot \nu \cdot Re_{cr}} = \frac{0.2778 \times 0.001}{2\pi \times 28 \times 10^{-6} \times 6} $$</div>
                <div class="equation">$$ r_{min} = \frac{2.778 \times 10^{-4}}{2\pi \times 168 \times 10^{-6}} = \frac{2.778 \times 10^{-4}}{1.0556 \times 10^{-3}} $$</div>
                <div class="equation">$$ \boxed{r_{min} = 0.263 \text{ m} \approx 0.26 \text{ m}} $$</div>
                <p><strong>Conclusion:</strong> Darcy's law is applicable for \(r \geq 0.26\) m from the pumping well.</p>
            </div>

            <div class="solution-box">
                <h4>SOLUTION 3: 2071 Bhadra Q6 — Darcy Applicability and Pore Velocity</h4>
                <p><strong>Given:</strong> \(b = 25\) m, \(n_e = 0.20\), \(K = 15\) m/day, \(L = 1100\) m, \(h_1 = 5.5\) m, \(h_2 = 3.0\) m, \(d_m = 1\) mm = \(0.001\) m, \(\nu = 0.01\) cm&sup2;/s = \(1 \times 10^{-6}\) m&sup2;/s.</p>
                <p><strong>Step 1: Hydraulic gradient</strong></p>
                <div class="equation">$$ i = \frac{h_1 - h_2}{L} = \frac{5.5 - 3.0}{1100} = \frac{2.5}{1100} = 2.273 \times 10^{-3} $$</div>
                <p><strong>Step 2: Darcy flux (specific discharge)</strong></p>
                <div class="equation">$$ q = K \cdot i = 15 \times 2.273 \times 10^{-3} = 0.0341 \text{ m/day} $$</div>
                <p>Convert to m/s: \(q = \frac{0.0341}{86400} = 3.945 \times 10^{-7}\) m/s.</p>
                <p><strong>Step 3: Check Darcy validity (Reynolds number)</strong></p>
                <div class="equation">$$ Re = \frac{q \cdot d_m}{\nu} = \frac{3.945 \times 10^{-7} \times 0.001}{1 \times 10^{-6}} = \frac{3.945 \times 10^{-10}}{10^{-6}} $$</div>
                <div class="equation">$$ \boxed{Re = 3.95 \times 10^{-4} \ll 1} $$</div>
                <p><strong>Conclusion:</strong> Since \(Re \approx 0.0004\), which is far below any commonly accepted limit (1–10), <strong>Darcy's law is fully applicable</strong>.</p>
                <p><strong>Step 4: Average pore velocity (seepage velocity)</strong></p>
                <div class="equation">$$ v_s = \frac{q}{n_e} = \frac{0.0341}{0.20} $$</div>
                <div class="equation">$$ \boxed{v_s = 0.170 \text{ m/day} = 1.973 \times 10^{-6} \text{ m/s}} $$</div>
                <p>The actual groundwater velocity in the pores is about 5 times the Darcy flux, and the flow is deeply in the laminar regime.</p>
            </div>
        </section>
'''

def process_chapter(src_file, meta):
    src_path = os.path.join(SRC_DIR, src_file)
    dst_path = os.path.join(DST_DIR, meta['out'])

    with open(src_path, 'r', encoding='utf-8') as f:
        html = f.read()

    body = extract_body_content(html)

    # Also extract any TOC section if it exists before first <section id=
    toc_match = re.search(r'(<section class="toc">.*?</section>)\s*', html, re.DOTALL)
    toc_block = ''
    if toc_match:
        toc_block = toc_match.group(1).strip() + '\n\n'
        # If the toc is already in the body, don't duplicate
        if '<section class="toc">' in body:
            toc_block = ''

    # Fix SVG colors
    body = fix_svg_colors(body)
    if toc_block:
        toc_block = fix_svg_colors(toc_block)

    # For ch2: inject worked solutions section before sec-summary
    if meta.get('inject_solutions'):
        # Insert sec-2-8 before the summary section using simple string replace
        summary_marker = '<section id="sec-summary">'
        if summary_marker in body:
            body = body.replace(
                summary_marker,
                CH2_SOLUTIONS + '\n        ' + summary_marker,
                1
            )
        # Add TOC entry for worked solutions if TOC exists
        toc_summary_marker = '<li><a href="#sec-summary">'
        if toc_block and toc_summary_marker in toc_block and 'sec-2-8' not in toc_block:
            toc_block = toc_block.replace(
                toc_summary_marker,
                '<li><a href="#sec-2-8">Worked numerical solutions</a></li>\n                ' + toc_summary_marker,
                1
            )
        elif toc_summary_marker in body and 'sec-2-8' not in body.split('sec-summary')[0]:
            body = body.replace(
                toc_summary_marker,
                '<li><a href="#sec-2-8">Worked numerical solutions</a></li>\n                ' + toc_summary_marker,
                1
            )
        print(f"  Injected sec-2-8 worked solutions for {src_file}")

    # Build the file
    head = TEMPLATE_HEAD.format(**meta)
    output = head + toc_block + body + TEMPLATE_TAIL

    with open(dst_path, 'w', encoding='utf-8') as f:
        f.write(output)

    print(f"Created {dst_path}")
    print(f"  Size: {len(output)} chars, {output.count(chr(10))} lines")

# Process
for src_file, meta in CHAPTERS.items():
    process_chapter(src_file, meta)

print("\nDone! Both chapters created in GW_THE/")

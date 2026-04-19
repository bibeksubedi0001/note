"""
Add SVG diagrams to all Theory chapter files.
At least 10 SVGs per chapter, with Chapter 4 getting extra equipment sketches.
Uses CSS custom properties matching existing style (--svg-hub, --svg-blue, etc.)
"""
import re, os

FOLDER = r'd:\Final Year\Theory\cm\Theory'

def insert_after_line(lines, line_idx, new_content):
    """Insert new_content (string) after line_idx."""
    new_lines = new_content.split('\n')
    return lines[:line_idx+1] + [l + '\n' for l in new_lines] + lines[line_idx+1:]

def find_line(lines, text, start=0):
    """Find first line containing text (case-insensitive) starting from start."""
    for i in range(start, len(lines)):
        if text.lower() in lines[i].lower():
            return i
    return -1

def find_closing_tag_after(lines, tag, start):
    """Find closing tag like </ul>, </ol>, </table>, </p>, </div> after start."""
    for i in range(start, len(lines)):
        if f'</{tag}>' in lines[i]:
            return i
    return start + 2

# ═══════════════════════════════════════════════════════════
# SVG TEMPLATES - Reusable diagram builders
# ═══════════════════════════════════════════════════════════

def svg_wrap(svg_content, fig_num, caption, width=650, height=380, vw=None, vh=None):
    vw = vw or width
    vh = vh or height
    return f'''
    <!-- SVG: {caption} -->
    <div class="figure">
      <figure>
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vw} {vh}" width="{width}" height="{height}">
{svg_content}
        </svg>
        <figcaption><strong>{fig_num}</strong> &mdash; {caption}</figcaption>
      </figure>
    </div>'''

def hub_spoke_svg(prefix, hub_text, items, hub_sub=None, width=650, height=480):
    """Generate a hub-and-spoke SVG diagram. items = [(title, subtitle, color), ...]"""
    colors = ['blue','green','yellow','pink','purple','red','orange','teal','blue','green','yellow','pink','purple','red','orange','teal']
    n = len(items)
    import math
    cx, cy, r_hub = width//2, height//2, 50
    r_orbit = min(width, height) * 0.38
    
    defs = f'''          <defs><style>
              .{prefix}-hub{{fill:var(--svg-hub);stroke:var(--svg-hub);stroke-width:2}}
              .{prefix}-ht{{fill:#fff;font:bold 13px 'Source Sans 3',sans-serif;text-anchor:middle}}
              .{prefix}-card{{rx:8;ry:8;stroke-width:1.5;opacity:.92}}
              .{prefix}-t{{font:600 10.5px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-text)}}
              .{prefix}-s{{font:italic 9px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
              .{prefix}-conn{{stroke:var(--svg-hub);stroke-width:1.2;stroke-dasharray:4 3;opacity:.4}}
              .{prefix}-n{{font:bold 10px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle}}
            </style></defs>'''
    
    # Hub
    hub = f'          <circle class="{prefix}-hub" cx="{cx}" cy="{cy}" r="{r_hub}"/>\n'
    hub += f'          <text class="{prefix}-ht" x="{cx}" y="{cy-5}">{hub_text}</text>\n'
    if hub_sub:
        hub += f'          <text class="{prefix}-ht" x="{cx}" y="{cy+13}" style="font-size:11px;font-weight:400">{hub_sub}</text>\n'
    
    cards = ''
    conns = ''
    cw, ch_h = 150, 48
    for i, item in enumerate(items):
        title = item[0]
        sub = item[1] if len(item) > 1 else ''
        c = colors[i % len(colors)]
        angle = (2 * math.pi * i / n) - math.pi/2
        px = cx + r_orbit * math.cos(angle)
        py = cy + r_orbit * math.sin(angle)
        conns += f'          <line class="{prefix}-conn" x1="{cx}" y1="{cy}" x2="{int(px)}" y2="{int(py)}"/>\n'
        rx = int(px - cw/2)
        ry = int(py - ch_h/2)
        cards += f'          <rect class="{prefix}-card" x="{rx}" y="{ry}" width="{cw}" height="{ch_h}" style="fill:var(--svg-{c});stroke:var(--svg-{c}-s)"/>\n'
        cards += f'          <text class="{prefix}-n" x="{int(px)}" y="{int(py-8)}">{i+1}</text>\n'
        cards += f'          <text class="{prefix}-t" x="{int(px)}" y="{int(py+4)}" style="fill:var(--svg-text-{c})">{title}</text>\n'
        if sub:
            cards += f'          <text class="{prefix}-s" x="{int(px)}" y="{int(py+16)}">{sub}</text>\n'
    
    return defs + '\n' + conns + hub + cards

def flow_svg(prefix, steps, direction='horizontal'):
    """Generate a flow diagram. steps = [(label, sublabel), ...]"""
    n = len(steps)
    colors = ['blue','green','yellow','orange','red','purple','teal','pink','blue','green','yellow','orange']
    
    if direction == 'horizontal':
        bw, bh = 100, 55
        gap = 15
        total_w = n * bw + (n-1) * gap
        w = max(total_w + 40, 650)
        h = 100
        start_x = (w - total_w) // 2
        
        defs = f'''          <defs><style>
              .{prefix}-box{{rx:8;ry:8;stroke-width:1.5;opacity:.92}}
              .{prefix}-t{{font:600 10px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-text)}}
              .{prefix}-s{{font:italic 8.5px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
              .{prefix}-arr{{stroke:var(--svg-hub);stroke-width:2;fill:none;marker-end:url(#{prefix}-ah)}}
            </style>
            <marker id="{prefix}-ah" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
              <path d="M0,0 L8,3 L0,6" fill="var(--svg-hub)"/>
            </marker>
          </defs>'''
        
        boxes = ''
        y = (h - bh) // 2
        for i, step in enumerate(steps):
            c = colors[i % len(colors)]
            x = start_x + i * (bw + gap)
            boxes += f'          <rect class="{prefix}-box" x="{x}" y="{y}" width="{bw}" height="{bh}" style="fill:var(--svg-{c});stroke:var(--svg-{c}-s)"/>\n'
            boxes += f'          <text class="{prefix}-t" x="{x+bw//2}" y="{y+22}" style="fill:var(--svg-text-{c})">{step[0]}</text>\n'
            if len(step) > 1 and step[1]:
                boxes += f'          <text class="{prefix}-s" x="{x+bw//2}" y="{y+38}">{step[1]}</text>\n'
            if i < n - 1:
                boxes += f'          <line class="{prefix}-arr" x1="{x+bw}" y1="{y+bh//2}" x2="{x+bw+gap}" y2="{y+bh//2}"/>\n'
        
        return defs + '\n' + boxes, w, h
    else:  # vertical
        bw, bh = 200, 45
        gap = 20
        total_h = n * bh + (n-1) * gap
        w = 350
        h = total_h + 40
        start_y = 20
        
        defs = f'''          <defs><style>
              .{prefix}-box{{rx:8;ry:8;stroke-width:1.5;opacity:.92}}
              .{prefix}-t{{font:600 11px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-text)}}
              .{prefix}-s{{font:italic 9px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
              .{prefix}-arr{{stroke:var(--svg-hub);stroke-width:2;fill:none;marker-end:url(#{prefix}-ah)}}
            </style>
            <marker id="{prefix}-ah" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
              <path d="M0,0 L8,3 L0,6" fill="var(--svg-hub)"/>
            </marker>
          </defs>'''
        
        boxes = ''
        x = (w - bw) // 2
        for i, step in enumerate(steps):
            c = colors[i % len(colors)]
            y = start_y + i * (bh + gap)
            boxes += f'          <rect class="{prefix}-box" x="{x}" y="{y}" width="{bw}" height="{bh}" style="fill:var(--svg-{c});stroke:var(--svg-{c}-s)"/>\n'
            boxes += f'          <text class="{prefix}-t" x="{x+bw//2}" y="{y+20}" style="fill:var(--svg-text-{c})">{step[0]}</text>\n'
            if len(step) > 1 and step[1]:
                boxes += f'          <text class="{prefix}-s" x="{x+bw//2}" y="{y+34}">{step[1]}</text>\n'
            if i < n - 1:
                boxes += f'          <line class="{prefix}-arr" x1="{x+bw//2}" y1="{y+bh}" x2="{x+bw//2}" y2="{y+bh+gap}"/>\n'
        
        return defs + '\n' + boxes, w, h

def comparison_table_svg(prefix, title, col1, col2, rows, w=600, fig_num='Fig'):
    """Create a comparison table SVG. rows = [(left, right), ...]"""
    rh = 30
    hdr_h = 35
    h = hdr_h + len(rows) * rh + 20
    half = (w - 40) // 2
    
    content = f'''          <defs><style>
              .{prefix}-hdr{{font:bold 12px 'Source Sans 3',sans-serif;fill:#fff;text-anchor:middle}}
              .{prefix}-cell{{font:10.5px 'Source Sans 3',sans-serif;fill:var(--svg-text);text-anchor:start}}
              .{prefix}-line{{stroke:var(--svg-sub);stroke-width:0.5;opacity:.3}}
            </style></defs>
          <text style="font:bold 14px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="{w//2}" y="18">{title}</text>
          <rect x="20" y="25" width="{half}" height="{hdr_h}" rx="6" style="fill:var(--svg-blue);opacity:.9"/>
          <rect x="{20+half}" y="25" width="{half}" height="{hdr_h}" rx="6" style="fill:var(--svg-green);opacity:.9"/>
          <text class="{prefix}-hdr" x="{20+half//2}" y="{25+22}">{col1}</text>
          <text class="{prefix}-hdr" x="{20+half+half//2}" y="{25+22}">{col2}</text>\n'''
    
    for i, (left, right) in enumerate(rows):
        y = 25 + hdr_h + i * rh
        if i % 2 == 0:
            content += f'          <rect x="20" y="{y}" width="{2*half}" height="{rh}" style="fill:var(--svg-sub);opacity:.08"/>\n'
        content += f'          <text class="{prefix}-cell" x="30" y="{y+20}">{left}</text>\n'
        content += f'          <text class="{prefix}-cell" x="{30+half}" y="{y+20}">{right}</text>\n'
    
    return content, w, h

def equipment_sketch(prefix, name, parts, w=500, h=300):
    """Create a simple equipment sketch with labeled parts.
    parts = [(x, y, w, h, label, shape), ...] where shape is 'rect'/'circle'/'trapezoid'/'triangle'
    """
    content = f'''          <defs><style>
              .{prefix}-body{{fill:var(--svg-yellow);stroke:var(--svg-hub);stroke-width:1.5;opacity:.85}}
              .{prefix}-part{{fill:var(--svg-blue);stroke:var(--svg-blue-s);stroke-width:1;opacity:.8}}
              .{prefix}-track{{fill:var(--svg-sub);stroke:var(--svg-hub);stroke-width:1.5;opacity:.6}}
              .{prefix}-cab{{fill:var(--svg-green);stroke:var(--svg-green-s);stroke-width:1.5;opacity:.85;rx:4;ry:4}}
              .{prefix}-boom{{stroke:var(--svg-hub);stroke-width:3;fill:none}}
              .{prefix}-cable{{stroke:var(--svg-hub);stroke-width:1.5;stroke-dasharray:5 3;fill:none}}
              .{prefix}-lbl{{font:600 9px 'Source Sans 3',sans-serif;fill:var(--svg-text);text-anchor:middle}}
              .{prefix}-lead{{stroke:var(--svg-red);stroke-width:1;stroke-dasharray:3 2;opacity:.7}}
              .{prefix}-dot{{fill:var(--svg-red);r:3}}
              .{prefix}-title{{font:bold 13px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle}}
              .{prefix}-wheel{{fill:var(--svg-sub);stroke:var(--svg-hub);stroke-width:2}}
              .{prefix}-bucket{{fill:var(--svg-orange);stroke:var(--svg-orange-s);stroke-width:1.5}}
              .{prefix}-drum{{fill:var(--svg-teal);stroke:var(--svg-hub);stroke-width:1.5;opacity:.85}}
              .{prefix}-foot{{fill:var(--svg-purple);stroke:var(--svg-purple-s);stroke-width:1}}
              .{prefix}-arrow{{stroke:var(--svg-red);stroke-width:1.5;fill:none;marker-end:url(#{prefix}-arh)}}
            </style>
            <marker id="{prefix}-arh" markerWidth="6" markerHeight="5" refX="6" refY="2.5" orient="auto">
              <path d="M0,0 L6,2.5 L0,5" fill="var(--svg-red)"/>
            </marker>
          </defs>\n'''
    return content

# ═══════════════════════════════════════════════════════════
# CHAPTER-SPECIFIC SVG DEFINITIONS
# ═══════════════════════════════════════════════════════════

def get_ch1_svgs():
    """Chapter 1 already has 6 SVGs. Add 4 more to reach 10."""
    svgs = {}
    
    # 1. Project Environment diagram (after 1.3.5)
    env_content = hub_spoke_svg('env', 'PROJECT', [
        ('Political', 'Govt policy, stability'),
        ('Economic', 'GDP, inflation, forex'),
        ('Social', 'Culture, labor, community'),
        ('Technological', 'Materials, methods'),
        ('Legal', 'Acts, regulations, codes'),
        ('Environmental', 'EIA, climate, terrain'),
    ], hub_sub='Environment', width=600, height=420)
    svgs['Construction Project Environment'] = svg_wrap(env_content, 'Fig 1.4', 'Construction Project Environment Factors', 600, 420)
    
    # 2. CM Functions diagram (after 1.5.1b)
    func_content = hub_spoke_svg('cmf', 'CM', [
        ('Planning', 'What, when, how'),
        ('Organizing', 'Structure &amp; resources'),
        ('Staffing', 'Right people, right jobs'),
        ('Directing', 'Leadership &amp; motivation'),
        ('Controlling', 'Monitor &amp; correct'),
        ('Coordinating', 'Integrate activities'),
        ('Communicating', 'Info flow &amp; feedback'),
    ], hub_sub='Functions', width=650, height=480)
    svgs['Functions of Construction Project Management'] = svg_wrap(func_content, 'Fig 1.5', 'Seven Functions of Construction Project Management')
    
    # 3. Three-Party System diagram (after 1.6.1)
    three_party = f'''          <defs><style>
              .tp-box{{rx:12;ry:12;stroke-width:2;opacity:.92}}
              .tp-t{{font:bold 14px 'Source Sans 3',sans-serif;text-anchor:middle;fill:#fff}}
              .tp-s{{font:11px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
              .tp-arr{{stroke:var(--svg-hub);stroke-width:2;fill:none;marker-end:url(#tp-ah)}}
              .tp-lbl{{font:600 9.5px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle}}
            </style>
            <marker id="tp-ah" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
              <path d="M0,0 L8,3 L0,6" fill="var(--svg-hub)"/>
            </marker>
          </defs>
          <!-- Client at top -->
          <rect class="tp-box" x="225" y="20" width="180" height="60" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text class="tp-t" x="315" y="45" style="fill:var(--svg-text-blue)">CLIENT / OWNER</text>
          <text class="tp-s" x="315" y="65">Conceives &amp; Finances</text>
          <!-- Consultant bottom-left -->
          <rect class="tp-box" x="50" y="200" width="180" height="60" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <text class="tp-t" x="140" y="225" style="fill:var(--svg-text-green)">CONSULTANT</text>
          <text class="tp-s" x="140" y="245">Designs &amp; Supervises</text>
          <!-- Contractor bottom-right -->
          <rect class="tp-box" x="400" y="200" width="180" height="60" style="fill:var(--svg-orange);stroke:var(--svg-orange-s)"/>
          <text class="tp-t" x="490" y="225" style="fill:var(--svg-text-orange)">CONTRACTOR</text>
          <text class="tp-s" x="490" y="245">Builds on Site</text>
          <!-- Arrows -->
          <line class="tp-arr" x1="270" y1="80" x2="185" y2="200"/>
          <text class="tp-lbl" x="205" y="140" transform="rotate(-35,205,140)">Agreement</text>
          <line class="tp-arr" x1="360" y1="80" x2="445" y2="200"/>
          <text class="tp-lbl" x="425" y="140" transform="rotate(35,425,140)">Contract</text>
          <line class="tp-arr" x1="230" y1="230" x2="400" y2="230"/>
          <text class="tp-lbl" x="315" y="218">Supervision &amp; Certification</text>
          <!-- FIDIC label -->
          <text style="font:bold 11px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="315" y="290">Three-Party System (FIDIC)</text>'''
    svgs['Three-Party System'] = svg_wrap(three_party, 'Fig 1.6', 'Three-Party System (FIDIC) &mdash; Client, Consultant, Contractor', 630, 300)
    
    # 4. Two-Party System diagram (after 1.6.2)
    two_party = f'''          <defs><style>
              .twp-box{{rx:12;ry:12;stroke-width:2;opacity:.92}}
              .twp-t{{font:bold 14px 'Source Sans 3',sans-serif;text-anchor:middle;fill:#fff}}
              .twp-s{{font:11px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
              .twp-arr{{stroke:var(--svg-hub);stroke-width:2.5;fill:none;marker-end:url(#twp-ah)}}
              .twp-lbl{{font:600 10px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle}}
            </style>
            <marker id="twp-ah" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
              <path d="M0,0 L8,3 L0,6" fill="var(--svg-hub)"/>
            </marker>
          </defs>
          <!-- Client left -->
          <rect class="twp-box" x="50" y="60" width="200" height="70" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text class="twp-t" x="150" y="90" style="fill:var(--svg-text-blue)">CLIENT / OWNER</text>
          <text class="twp-s" x="150" y="115">Finances &amp; Supervises</text>
          <!-- Contractor right -->
          <rect class="twp-box" x="380" y="60" width="200" height="70" style="fill:var(--svg-orange);stroke:var(--svg-orange-s)"/>
          <text class="twp-t" x="480" y="90" style="fill:var(--svg-text-orange)">CONTRACTOR</text>
          <text class="twp-s" x="480" y="115">Designs &amp; Builds</text>
          <!-- Arrows -->
          <line class="twp-arr" x1="250" y1="85" x2="380" y2="85"/>
          <line class="twp-arr" x1="380" y1="105" x2="250" y2="105"/>
          <text class="twp-lbl" x="315" y="78">Contract &amp; Payment</text>
          <text class="twp-lbl" x="315" y="125">Work &amp; Reports</text>
          <!-- NCB label -->
          <text style="font:bold 11px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="315" y="170">Two-Party System (NCB / Japanese)</text>
          <text style="font:italic 10px 'Source Sans 3',sans-serif;fill:var(--svg-sub);text-anchor:middle" x="315" y="185">No independent consultant &mdash; client directly supervises</text>'''
    svgs['Two-Party System'] = svg_wrap(two_party, 'Fig 1.7', 'Two-Party System (NCB / Japanese) &mdash; Direct Client-Contractor', 630, 200)
    
    return svgs

def get_ch2_svgs():
    """Chapter 2 has 3 SVGs. Add 7+ more."""
    svgs = {}
    
    # 1. Planning Process flow
    steps_content, w, h = flow_svg('pl', [
        ('Define\nObjective', ''),
        ('Identify\nActivities', ''),
        ('Sequence\nActivities', ''),
        ('Estimate\nDuration', ''),
        ('Allocate\nResources', ''),
        ('Schedule', ''),
    ])
    svgs['Steps Involved in Planning'] = svg_wrap(steps_content, 'Fig 2.1', 'Steps in Construction Planning Process', w, h, w, h)
    
    # 2. Planning Stages
    stages_content, w, h = flow_svg('stg', [
        ('Strategic\nPlanning', 'Long-term'),
        ('Operational\nPlanning', 'Medium-term'),
        ('Scheduling', 'Short-term'),
        ('Action\nPlan', 'Daily/Weekly'),
    ])
    svgs['Stages of Planning'] = svg_wrap(stages_content, 'Fig 2.2', 'Stages of Construction Planning', w, h, w, h)
    
    # 3. Client vs Contractor Planning
    comp_content, w, h = comparison_table_svg('ccpl', 'Client vs Contractor Planning', 
        'Client Planning', 'Contractor Planning',
        [
            ('Project feasibility study', 'Site survey &amp; mobilization plan'),
            ('Budget estimation', 'Detailed cost estimation'),
            ('Consultant selection', 'Resource allocation'),
            ('Land acquisition', 'Equipment procurement'),
            ('Environmental clearance (EIA)', 'Work schedule (bar chart/CPM)'),
            ('Design approval', 'Quality control plan'),
            ('Tender preparation', 'Safety management plan'),
            ('Contract award', 'Cash flow projection'),
        ])
    svgs['Planning by the Client'] = svg_wrap(comp_content, 'Fig 2.3', 'Planning Responsibilities: Client vs Contractor', w, h, w, h)
    
    # 4. Scheduling Methods comparison
    sched_hub = hub_spoke_svg('sch', 'SCHEDULING', [
        ('Bar Chart', 'Simple, visual, Gantt'),
        ('Milestone', 'Key events only'),
        ('CPM', 'Critical path, float'),
        ('PERT', 'Probabilistic, 3 estimates'),
        ('LOB', 'Repetitive work, slopes'),
        ('S-Curve', 'Cumulative progress'),
    ], hub_sub='Methods', width=600, height=420)
    svgs['Methods of Scheduling'] = svg_wrap(sched_hub, 'Fig 2.4', 'Methods of Scheduling in Construction', 600, 420)
    
    # 5. Bar Chart Example
    bar_chart = f'''          <defs><style>
              .bc-hdr{{font:bold 11px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:start}}
              .bc-act{{font:10px 'Source Sans 3',sans-serif;fill:var(--svg-text);text-anchor:start}}
              .bc-bar{{rx:3;ry:3;opacity:.85;height:14}}
              .bc-wk{{font:9px 'Source Sans 3',sans-serif;fill:var(--svg-sub);text-anchor:middle}}
              .bc-grid{{stroke:var(--svg-sub);stroke-width:0.3;opacity:.3}}
            </style></defs>
          <text class="bc-hdr" x="10" y="20">Activity</text>
          <text class="bc-hdr" x="140" y="20">Dur</text>
          <text class="bc-wk" x="200" y="20">W1</text><text class="bc-wk" x="240" y="20">W2</text>
          <text class="bc-wk" x="280" y="20">W3</text><text class="bc-wk" x="320" y="20">W4</text>
          <text class="bc-wk" x="360" y="20">W5</text><text class="bc-wk" x="400" y="20">W6</text>
          <text class="bc-wk" x="440" y="20">W7</text><text class="bc-wk" x="480" y="20">W8</text>
          <line class="bc-grid" x1="180" y1="25" x2="180" y2="200"/>
          <line class="bc-grid" x1="220" y1="25" x2="220" y2="200"/>
          <line class="bc-grid" x1="260" y1="25" x2="260" y2="200"/>
          <line class="bc-grid" x1="300" y1="25" x2="300" y2="200"/>
          <line class="bc-grid" x1="340" y1="25" x2="340" y2="200"/>
          <line class="bc-grid" x1="380" y1="25" x2="380" y2="200"/>
          <line class="bc-grid" x1="420" y1="25" x2="420" y2="200"/>
          <line class="bc-grid" x1="460" y1="25" x2="460" y2="200"/>
          <line class="bc-grid" x1="500" y1="25" x2="500" y2="200"/>
          <text class="bc-act" x="10" y="48">Excavation</text><text class="bc-act" x="145" y="48">3w</text>
          <rect class="bc-bar" x="180" y="36" width="120" style="fill:var(--svg-blue)"/>
          <text class="bc-act" x="10" y="73">Foundation</text><text class="bc-act" x="145" y="73">2w</text>
          <rect class="bc-bar" x="300" y="61" width="80" style="fill:var(--svg-green)"/>
          <text class="bc-act" x="10" y="98">Superstructure</text><text class="bc-act" x="145" y="98">4w</text>
          <rect class="bc-bar" x="300" y="86" width="160" style="fill:var(--svg-orange)"/>
          <text class="bc-act" x="10" y="123">Plastering</text><text class="bc-act" x="145" y="123">2w</text>
          <rect class="bc-bar" x="420" y="111" width="80" style="fill:var(--svg-pink)"/>
          <text class="bc-act" x="10" y="148">Painting</text><text class="bc-act" x="145" y="148">1w</text>
          <rect class="bc-bar" x="460" y="136" width="40" style="fill:var(--svg-purple)"/>
          <text class="bc-act" x="10" y="173">Finishing</text><text class="bc-act" x="145" y="173">1w</text>
          <rect class="bc-bar" x="460" y="161" width="40" style="fill:var(--svg-teal)"/>
          <text style="font:italic 9px 'Source Sans 3',sans-serif;fill:var(--svg-sub);text-anchor:start" x="10" y="198">Critical Path: Excavation &rarr; Foundation &rarr; Superstructure &rarr; Painting</text>'''
    svgs['Bar Charts'] = svg_wrap(bar_chart, 'Fig 2.5', 'Sample Bar Chart (Gantt Chart) for Building Construction', 520, 210, 520, 210)
    
    # 6. CPM vs PERT comparison
    cpm_pert, w, h = comparison_table_svg('cpv', 'CPM vs PERT', 'CPM', 'PERT',
        [
            ('Deterministic', 'Probabilistic'),
            ('Single time estimate', 'Three estimates (a, m, b)'),
            ('Activity-oriented', 'Event-oriented'),
            ('Cost optimization', 'Time optimization'),
            ('Repetitive projects', 'R&amp;D / new projects'),
            ('Construction &amp; maintenance', 'Space &amp; defence programs'),
            ('Arrow diagram', 'Node diagram common'),
            ('te = single duration', 'te = (a + 4m + b) / 6'),
        ])
    svgs['Differences between CPM and PERT'] = svg_wrap(cpm_pert, 'Fig 2.6', 'CPM vs PERT &mdash; Key Differences', w, h, w, h)
    
    # 7. Float types diagram
    float_svg = f'''          <defs><style>
              .fl-box{{rx:6;ry:6;stroke-width:1.5;opacity:.88}}
              .fl-t{{font:bold 11px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-text)}}
              .fl-s{{font:10px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
              .fl-f{{font:italic 10px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-hub)}}
            </style></defs>
          <text style="font:bold 14px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="300" y="22">Types of Float</text>
          <!-- Total Float -->
          <rect class="fl-box" x="150" y="40" width="300" height="55" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text class="fl-t" x="300" y="60" style="fill:var(--svg-text-blue)">Total Float (TF)</text>
          <text class="fl-s" x="300" y="76">TF = LS &minus; ES = LF &minus; EF</text>
          <text class="fl-f" x="300" y="90">Max delay without delaying PROJECT</text>
          <!-- Free Float -->
          <rect class="fl-box" x="150" y="110" width="300" height="55" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <text class="fl-t" x="300" y="130" style="fill:var(--svg-text-green)">Free Float (FF)</text>
          <text class="fl-s" x="300" y="146">FF = ES(successor) &minus; EF(activity)</text>
          <text class="fl-f" x="300" y="160">Max delay without delaying NEXT activity</text>
          <!-- Independent Float -->
          <rect class="fl-box" x="150" y="180" width="300" height="55" style="fill:var(--svg-orange);stroke:var(--svg-orange-s)"/>
          <text class="fl-t" x="300" y="200" style="fill:var(--svg-text-orange)">Independent Float (IF)</text>
          <text class="fl-s" x="300" y="216">IF = ES(succ) &minus; LF(pred) &minus; Duration</text>
          <text class="fl-f" x="300" y="230">Float when all predecessors are LATE</text>
          <!-- Relationship -->
          <text style="font:bold 10px 'Source Sans 3',sans-serif;fill:var(--svg-red);text-anchor:middle" x="300" y="258">TF &ge; FF &ge; IF &ge; 0 &ensp;|&ensp; Critical Path: TF = 0</text>'''
    svgs['Floats'] = svg_wrap(float_svg, 'Fig 2.7', 'Types of Float in Network Analysis', 600, 270, 600, 270)
    
    # 8. TCTO Concept diagram
    tcto_svg = f'''          <defs><style>
              .tc-ax{{stroke:var(--svg-hub);stroke-width:2}}
              .tc-lbl{{font:bold 11px 'Source Sans 3',sans-serif;fill:var(--svg-hub)}}
              .tc-line{{stroke-width:2.5;fill:none}}
              .tc-dot{{r:5;stroke:#fff;stroke-width:1.5}}
              .tc-note{{font:10px 'Source Sans 3',sans-serif;fill:var(--svg-sub)}}
              .tc-opt{{font:bold 12px 'Source Sans 3',sans-serif;fill:var(--svg-red)}}
            </style></defs>
          <!-- Axes -->
          <line class="tc-ax" x1="80" y1="20" x2="80" y2="280"/>
          <line class="tc-ax" x1="80" y1="280" x2="550" y2="280"/>
          <text class="tc-lbl" x="40" y="150" transform="rotate(-90,40,150)">COST (Rs)</text>
          <text class="tc-lbl" x="315" y="310">TIME (Duration)</text>
          <!-- Direct Cost curve (decreasing) -->
          <path class="tc-line" d="M120,240 Q200,230 280,180 Q360,120 450,60" style="stroke:var(--svg-blue)"/>
          <text style="font:600 10px 'Source Sans 3',sans-serif;fill:var(--svg-blue);text-anchor:start" x="455" y="55">Direct Cost</text>
          <!-- Indirect Cost curve (increasing) -->
          <path class="tc-line" d="M120,60 Q200,80 280,120 Q360,180 450,260" style="stroke:var(--svg-orange)"/>
          <text style="font:600 10px 'Source Sans 3',sans-serif;fill:var(--svg-orange);text-anchor:start" x="455" y="265">Indirect Cost</text>
          <!-- Total Cost curve (U-shape) -->
          <path class="tc-line" d="M120,200 Q200,170 280,155 Q310,152 340,155 Q400,170 450,210" style="stroke:var(--svg-red);stroke-width:3"/>
          <text style="font:bold 11px 'Source Sans 3',sans-serif;fill:var(--svg-red);text-anchor:start" x="455" y="215">Total Cost</text>
          <!-- Optimum point -->
          <circle class="tc-dot" cx="310" cy="152" style="fill:var(--svg-red)"/>
          <text class="tc-opt" x="310" y="140">Optimum</text>
          <text class="tc-note" x="310" y="128" style="text-anchor:middle">Min total cost</text>
          <!-- Arrow labels -->
          <text class="tc-note" x="160" y="268" style="text-anchor:middle">Crash</text>
          <text class="tc-note" x="430" y="268" style="text-anchor:middle">Normal</text>'''
    svgs['Time-Cost Trade-off'] = svg_wrap(tcto_svg, 'Fig 2.8', 'Time-Cost Trade-off (TCTO) Concept Curve', 580, 320, 580, 320)
    
    # 9. Cost Slope formula
    slope_svg = f'''          <defs><style>
              .cs-box{{rx:10;ry:10;stroke-width:2;opacity:.92}}
              .cs-t{{font:bold 14px 'Source Sans 3',sans-serif;text-anchor:middle;fill:#fff}}
              .cs-f{{font:bold 16px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-hub)}}
              .cs-s{{font:11px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
            </style></defs>
          <rect class="cs-box" x="100" y="15" width="400" height="70" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text class="cs-t" x="300" y="40" style="fill:var(--svg-text-blue)">Cost Slope Formula</text>
          <text class="cs-f" x="300" y="70">Cost Slope = (Crash Cost &minus; Normal Cost) / (Normal Time &minus; Crash Time)</text>
          <rect class="cs-box" x="50" y="100" width="220" height="50" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <text class="cs-s" x="160" y="120" style="fill:var(--svg-text-green)">Crash the activity with</text>
          <text style="font:bold 11px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-text-green)" x="160" y="138">LEAST cost slope first</text>
          <rect class="cs-box" x="330" y="100" width="220" height="50" style="fill:var(--svg-red);stroke:var(--svg-red-s)"/>
          <text class="cs-s" x="440" y="120" style="fill:var(--svg-text-red)">Only crash activities on</text>
          <text style="font:bold 11px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-text-red)" x="440" y="138">CRITICAL PATH</text>'''
    svgs['Steps in Time-Cost Trade-off'] = svg_wrap(slope_svg, 'Fig 2.9', 'TCTO: Cost Slope &amp; Crashing Rules', 600, 165, 600, 165)
    
    # 10. Network Diagram Example
    net_svg = f'''          <defs><style>
              .nd-node{{fill:var(--svg-blue);stroke:var(--svg-blue-s);stroke-width:2}}
              .nd-crit{{fill:var(--svg-red);stroke:var(--svg-red-s);stroke-width:2.5}}
              .nd-nt{{font:bold 12px 'Source Sans 3',sans-serif;fill:#fff;text-anchor:middle}}
              .nd-arr{{stroke:var(--svg-hub);stroke-width:2;fill:none;marker-end:url(#nd-ah)}}
              .nd-carr{{stroke:var(--svg-red);stroke-width:3;fill:none;marker-end:url(#nd-cah)}}
              .nd-lbl{{font:600 10px 'Source Sans 3',sans-serif;fill:var(--svg-text);text-anchor:middle}}
              .nd-dur{{font:bold 9px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle}}
            </style>
            <marker id="nd-ah" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
              <path d="M0,0 L8,3 L0,6" fill="var(--svg-hub)"/>
            </marker>
            <marker id="nd-cah" markerWidth="8" markerHeight="6" refX="8" refY="3" orient="auto">
              <path d="M0,0 L8,3 L0,6" fill="var(--svg-red)"/>
            </marker>
          </defs>
          <!-- Nodes -->
          <circle class="nd-crit" cx="80" cy="120" r="22"/><text class="nd-nt" x="80" y="125">1</text>
          <circle class="nd-crit" cx="230" cy="60" r="22"/><text class="nd-nt" x="230" y="65">2</text>
          <circle class="nd-node" cx="230" cy="180" r="22"/><text class="nd-nt" x="230" y="185">3</text>
          <circle class="nd-crit" cx="380" cy="60" r="22"/><text class="nd-nt" x="380" y="65">4</text>
          <circle class="nd-node" cx="380" cy="180" r="22"/><text class="nd-nt" x="380" y="185">5</text>
          <circle class="nd-crit" cx="520" cy="120" r="22"/><text class="nd-nt" x="520" y="125">6</text>
          <!-- Critical path arrows (red) -->
          <line class="nd-carr" x1="102" y1="108" x2="208" y2="68"/>
          <text class="nd-lbl" x="155" y="78">A</text><text class="nd-dur" x="155" y="92">3d</text>
          <line class="nd-carr" x1="252" y1="60" x2="358" y2="60"/>
          <text class="nd-lbl" x="305" y="52">C</text><text class="nd-dur" x="305" y="75">5d</text>
          <line class="nd-carr" x1="402" y1="68" x2="498" y2="108"/>
          <text class="nd-lbl" x="455" y="80">F</text><text class="nd-dur" x="455" y="98">4d</text>
          <!-- Non-critical arrows -->
          <line class="nd-arr" x1="102" y1="132" x2="208" y2="172"/>
          <text class="nd-lbl" x="155" y="165">B</text><text class="nd-dur" x="155" y="148">2d</text>
          <line class="nd-arr" x1="252" y1="180" x2="358" y2="180"/>
          <text class="nd-lbl" x="305" y="172">D</text><text class="nd-dur" x="305" y="196">3d</text>
          <line class="nd-arr" x1="402" y1="172" x2="498" y2="132"/>
          <text class="nd-lbl" x="455" y="162">E</text><text class="nd-dur" x="455" y="148">2d</text>
          <!-- Legend -->
          <line style="stroke:var(--svg-red);stroke-width:3" x1="80" y1="230" x2="120" y2="230"/>
          <text style="font:10px 'Source Sans 3',sans-serif;fill:var(--svg-text)" x="130" y="234">Critical Path (TF=0): 1&rarr;2&rarr;4&rarr;6 = 12 days</text>'''
    svgs['Network Diagrams'] = svg_wrap(net_svg, 'Fig 2.10', 'Sample CPM Network Diagram with Critical Path', 560, 250, 560, 250)
    
    return svgs

def get_ch3_svgs():
    svgs = {}
    
    # 1. ABC Classification diagram
    abc_hub = hub_spoke_svg('abc', 'ABC', [
        ('A Items', '70-80% value, 10-20% qty'),
        ('B Items', '15-25% value, 20-30% qty'),
        ('C Items', '5-10% value, 50-70% qty'),
    ], hub_sub='Analysis', width=500, height=350)
    svgs['ABC Analysis'] = svg_wrap(abc_hub, 'Fig 3.1', 'ABC Classification of Construction Materials', 500, 350, 500, 350)
    
    # 2. Material Wastage causes
    waste_hub = hub_spoke_svg('wst', 'MATERIAL', [
        ('Transport', 'Handling damage'),
        ('Storage', 'Exposure, theft'),
        ('Design Change', 'Rework'),
        ('Over-ordering', 'Excess quantity'),
        ('Poor Workmanship', 'Unskilled labor'),
        ('Conversion', 'Cutting waste'),
    ], hub_sub='Wastage Causes', width=600, height=420)
    svgs['Controllable Wastage'] = svg_wrap(waste_hub, 'Fig 3.2', 'Causes of Controllable Material Wastage', 600, 420)
    
    # 3. Provisioning Process flow
    prov_content, w, h = flow_svg('prv', [
        ('Material\nPlanning', ''),
        ('Source\nIdentify', ''),
        ('Inquiry &amp;\nQuotation', ''),
        ('Purchase\nOrder', ''),
        ('Inspection\n&amp; Receipt', ''),
        ('Storage', ''),
    ], 'horizontal')
    svgs['Steps in Material Provisioning'] = svg_wrap(prov_content, 'Fig 3.3', 'Material Provisioning Process Flow', w, h, w, h)
    
    # 4. Inventory Cost diagram
    inv_cost = f'''          <defs><style>
              .ic-ax{{stroke:var(--svg-hub);stroke-width:2}}
              .ic-lbl{{font:bold 11px 'Source Sans 3',sans-serif;fill:var(--svg-hub)}}
              .ic-line{{stroke-width:2.5;fill:none}}
              .ic-dot{{r:5;stroke:#fff;stroke-width:1.5}}
              .ic-note{{font:10px 'Source Sans 3',sans-serif;fill:var(--svg-sub)}}
            </style></defs>
          <line class="ic-ax" x1="80" y1="20" x2="80" y2="250"/>
          <line class="ic-ax" x1="80" y1="250" x2="500" y2="250"/>
          <text class="ic-lbl" x="40" y="135" transform="rotate(-90,40,135)">COST</text>
          <text class="ic-lbl" x="290" y="280">ORDER QUANTITY (Q)</text>
          <path class="ic-line" d="M100,230 Q200,180 300,100 Q380,50 460,30" style="stroke:var(--svg-orange)"/>
          <text style="font:600 10px 'Source Sans 3',sans-serif;fill:var(--svg-orange)" x="465" y="30">Carrying Cost</text>
          <path class="ic-line" d="M100,40 Q200,100 300,160 Q380,200 460,225" style="stroke:var(--svg-blue)"/>
          <text style="font:600 10px 'Source Sans 3',sans-serif;fill:var(--svg-blue)" x="465" y="225">Ordering Cost</text>
          <path class="ic-line" d="M100,180 Q200,135 280,125 Q340,125 400,140 Q460,160 480,170" style="stroke:var(--svg-red);stroke-width:3"/>
          <text style="font:bold 11px 'Source Sans 3',sans-serif;fill:var(--svg-red)" x="465" y="170">Total Cost</text>
          <circle class="ic-dot" cx="280" cy="125" style="fill:var(--svg-red)"/>
          <text style="font:bold 11px 'Source Sans 3',sans-serif;fill:var(--svg-red);text-anchor:middle" x="280" y="115">EOQ</text>
          <line style="stroke:var(--svg-sub);stroke-dasharray:4 3;stroke-width:1" x1="280" y1="125" x2="280" y2="250"/>'''
    svgs['Economic Order Quantity'] = svg_wrap(inv_cost, 'Fig 3.4', 'EOQ: Economic Order Quantity Graph', 520, 290, 520, 290)
    
    # 5. Stock Levels diagram
    stock_svg = f'''          <defs><style>
              .sl-ax{{stroke:var(--svg-hub);stroke-width:2}}
              .sl-lbl{{font:bold 10px 'Source Sans 3',sans-serif;fill:var(--svg-hub)}}
              .sl-line{{stroke-width:2;fill:none}}
              .sl-dash{{stroke-dasharray:6 4;stroke-width:1.5}}
              .sl-note{{font:9px 'Source Sans 3',sans-serif;fill:var(--svg-sub)}}
            </style></defs>
          <line class="sl-ax" x1="60" y1="20" x2="60" y2="220"/>
          <line class="sl-ax" x1="60" y1="220" x2="550" y2="220"/>
          <text class="sl-lbl" x="30" y="120" transform="rotate(-90,30,120)">Stock Level</text>
          <text class="sl-lbl" x="305" y="240">Time</text>
          <!-- Max stock line -->
          <line class="sl-dash" x1="60" y1="40" x2="550" y2="40" style="stroke:var(--svg-red)"/>
          <text class="sl-lbl" x="555" y="44" style="fill:var(--svg-red);font-size:9px">Max Level</text>
          <!-- ROL line -->
          <line class="sl-dash" x1="60" y1="110" x2="550" y2="110" style="stroke:var(--svg-orange)"/>
          <text class="sl-lbl" x="555" y="114" style="fill:var(--svg-orange);font-size:9px">Re-order Level</text>
          <!-- Min stock line -->
          <line class="sl-dash" x1="60" y1="160" x2="550" y2="160" style="stroke:var(--svg-blue)"/>
          <text class="sl-lbl" x="555" y="164" style="fill:var(--svg-blue);font-size:9px">Min / Safety Stock</text>
          <!-- Sawtooth pattern -->
          <path class="sl-line" d="M60,40 L180,160 L180,40 L300,160 L300,40 L420,160 L420,40 L540,160" style="stroke:var(--svg-green)"/>
          <!-- Lead time bracket -->
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="130" y1="112" x2="130" y2="200"/>
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="180" y1="160" x2="180" y2="200"/>
          <text class="sl-note" x="155" y="198" style="text-anchor:middle">Lead Time</text>'''
    svgs['Stock Levels'] = svg_wrap(stock_svg, 'Fig 3.5', 'Inventory Stock Levels &amp; Re-order Point', 650, 250, 680, 250)
    
    # 6. EOQ Formula
    eoq_svg = f'''          <defs><style>
              .eq-box{{rx:10;ry:10;stroke-width:2;opacity:.92}}
              .eq-t{{font:bold 18px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-hub)}}
              .eq-s{{font:11px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
            </style></defs>
          <rect class="eq-box" x="80" y="10" width="420" height="60" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text class="eq-t" x="290" y="40" style="fill:var(--svg-text-blue)">EOQ = &radic;(2 &times; D &times; Co / Cc)</text>
          <text class="eq-s" x="290" y="58" style="fill:var(--svg-text-blue)">D = Annual Demand, Co = Order Cost, Cc = Carrying Cost/unit/year</text>
          <rect class="eq-box" x="30" y="85" width="250" height="45" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <text style="font:600 11px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-text-green)" x="155" y="107">ROL = Daily Usage &times; Lead Time</text>
          <text class="eq-s" x="155" y="122" style="fill:var(--svg-text-green)">+ Safety Stock (if any)</text>
          <rect class="eq-box" x="300" y="85" width="260" height="45" style="fill:var(--svg-orange);stroke:var(--svg-orange-s)"/>
          <text style="font:600 11px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-text-orange)" x="430" y="107">Total Cost = D/Q&times;Co + Q/2&times;Cc</text>
          <text class="eq-s" x="430" y="122" style="fill:var(--svg-text-orange)">Minimum at Q = EOQ</text>'''
    svgs['Inventory Cost Formulas'] = svg_wrap(eoq_svg, 'Fig 3.6', 'Key Inventory Formulas: EOQ, ROL, Total Cost', 580, 140, 580, 140)
    
    # 7. Value Engineering phases
    ve_content, w, h = flow_svg('ve', [
        ('Information', 'Gather data'),
        ('Function\nAnalysis', 'What does it do?'),
        ('Creative', 'Brainstorm'),
        ('Evaluation', 'Best ideas'),
        ('Development', 'Detail solution'),
        ('Presentation', 'Recommend'),
    ], 'horizontal')
    svgs['VE Job Plan Phases'] = svg_wrap(ve_content, 'Fig 3.7', 'Value Engineering Job Plan Phases', w, h, w, h)
    
    # 8. Material Classification
    mat_class = hub_spoke_svg('mc', 'MATERIALS', [
        ('Cement', 'Binding agent'),
        ('Aggregates', 'Sand, gravel, stone'),
        ('Steel', 'Reinforcement bars'),
        ('Timber', 'Formwork, scaffolding'),
        ('Bricks/Blocks', 'Masonry units'),
        ('Bitumen', 'Road surfacing'),
        ('Pipes/Fittings', 'Plumbing, drainage'),
        ('Electrical', 'Wires, fixtures'),
    ], hub_sub='Classification', width=620, height=440)
    svgs['Classification of Construction Materials'] = svg_wrap(mat_class, 'Fig 3.8', 'Classification of Construction Materials', 620, 440)
    
    # 9. Wastage Standards table
    ws_content, w, h = comparison_table_svg('ws', 'Standard Wastage Percentages', 'Material', 'Wastage %',
        [
            ('Cement', '2-5%'),
            ('Steel Reinforcement', '3-5%'),
            ('Bricks', '5-10%'),
            ('Timber (formwork)', '10-15%'),
            ('Sand / Aggregate', '5-8%'),
            ('Tiles', '5-8%'),
            ('Paint', '3-5%'),
            ('Plumbing Fittings', '2-3%'),
        ])
    svgs['Typical Standard Wastage'] = svg_wrap(ws_content, 'Fig 3.9', 'Standard Material Wastage Percentages', w, h, w, h)
    
    # 10. Value formula
    vf_svg = f'''          <defs><style>
              .vf-box{{rx:12;ry:12;stroke-width:2;opacity:.92}}
              .vf-t{{font:bold 20px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-hub)}}
              .vf-s{{font:12px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
            </style></defs>
          <rect class="vf-box" x="100" y="15" width="400" height="70" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <text class="vf-t" x="300" y="45" style="fill:var(--svg-text-green)">Value = Function / Cost</text>
          <text class="vf-s" x="300" y="68" style="fill:var(--svg-text-green)">Increase value by: &uarr; Function or &darr; Cost or Both</text>
          <rect class="vf-box" x="40" y="100" width="160" height="40" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text style="font:600 10px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-text-blue)" x="120" y="124">Primary Function</text>
          <rect class="vf-box" x="240" y="100" width="160" height="40" style="fill:var(--svg-orange);stroke:var(--svg-orange-s)"/>
          <text style="font:600 10px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-text-orange)" x="320" y="124">Secondary Function</text>
          <rect class="vf-box" x="440" y="100" width="120" height="40" style="fill:var(--svg-red);stroke:var(--svg-red-s)"/>
          <text style="font:600 10px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-text-red)" x="500" y="124">Unnecessary</text>'''
    svgs['Definition'] = svg_wrap(vf_svg, 'Fig 3.10', 'Value Engineering: Value = Function / Cost', 600, 150, 600, 150)
    
    return svgs

def get_ch4_svgs():
    """Chapter 4 - LOTS of equipment sketches for exam questions."""
    svgs = {}
    
    # 1. Equipment Categories Overview
    eq_hub = hub_spoke_svg('eqo', 'CONSTRUCTION', [
        ('Excavation', 'Excavator, Dozer, Dragline'),
        ('Transportation', 'Trucks, Dumpers, Conveyor'),
        ('Compaction', 'Roller, Vibrator, Rammer'),
        ('Crushing', 'Jaw, Cone, Impact'),
        ('Concrete', 'Mixer, Pump, Vibrator'),
        ('Lifting', 'Crane, Hoist, Winch'),
        ('Tunneling', 'TBM, Drill &amp; Blast'),
        ('Highway', 'Paver, Distributor, Roller'),
    ], hub_sub='Equipment', width=650, height=480)
    svgs['Advantages of Using Equipment'] = svg_wrap(eq_hub, 'Fig 4.1', 'Categories of Construction Equipment', 650, 480)
    
    # 2. Excavator Sketch
    excavator = equipment_sketch('exc', 'Excavator', [])
    excavator += f'''
          <!-- Ground -->
          <line style="stroke:var(--svg-sub);stroke-width:2" x1="20" y1="250" x2="480" y2="250"/>
          <rect style="fill:var(--svg-sub);opacity:.15" x="20" y="250" width="460" height="30"/>
          <!-- Tracks -->
          <rect class="exc-track" x="80" y="220" width="180" height="30" rx="15"/>
          <circle class="exc-wheel" cx="95" cy="235" r="12" style="fill:var(--svg-sub);stroke:var(--svg-hub);stroke-width:1.5"/>
          <circle class="exc-wheel" cx="245" cy="235" r="12" style="fill:var(--svg-sub);stroke:var(--svg-hub);stroke-width:1.5"/>
          <!-- Track rollers -->
          <circle cx="130" cy="238" r="5" style="fill:var(--svg-sub);stroke:var(--svg-hub);stroke-width:1"/>
          <circle cx="160" cy="238" r="5" style="fill:var(--svg-sub);stroke:var(--svg-hub);stroke-width:1"/>
          <circle cx="190" cy="238" r="5" style="fill:var(--svg-sub);stroke:var(--svg-hub);stroke-width:1"/>
          <circle cx="220" cy="238" r="5" style="fill:var(--svg-sub);stroke:var(--svg-hub);stroke-width:1"/>
          <!-- Body/Platform -->
          <rect class="exc-body" x="100" y="170" width="140" height="50" rx="5" style="fill:var(--svg-yellow);stroke:var(--svg-hub);stroke-width:2"/>
          <!-- Cab -->
          <rect class="exc-cab" x="110" y="135" width="55" height="40"/>
          <rect style="fill:var(--svg-blue);opacity:.3;rx:2" x="118" y="140" width="40" height="25"/>
          <!-- Engine Housing -->
          <rect style="fill:var(--svg-yellow);stroke:var(--svg-hub);stroke-width:1.5;rx:3" x="175" y="148" width="55" height="25"/>
          <!-- Counterweight -->
          <rect style="fill:var(--svg-orange);stroke:var(--svg-orange-s);stroke-width:2;rx:4" x="220" y="170" width="25" height="40"/>
          <!-- Boom -->
          <line class="exc-boom" x1="165" y1="165" x2="310" y2="90"/>
          <line class="exc-boom" x1="165" y1="175" x2="310" y2="100"/>
          <!-- Arm (Stick) -->
          <line class="exc-boom" x1="310" y1="95" x2="400" y2="180" style="stroke-width:2.5"/>
          <!-- Bucket -->
          <path class="exc-bucket" d="M390,175 L410,175 L420,210 L380,210 Z"/>
          <line style="stroke:var(--svg-hub);stroke-width:1.5" x1="395" y1="210" x2="385" y2="220"/>
          <line style="stroke:var(--svg-hub);stroke-width:1.5" x1="405" y1="210" x2="395" y2="220"/>
          <line style="stroke:var(--svg-hub);stroke-width:1.5" x1="415" y1="210" x2="405" y2="220"/>
          <!-- Hydraulic cylinder -->
          <line style="stroke:var(--svg-red);stroke-width:2" x1="135" y1="170" x2="260" y2="95"/>
          <!-- Labels -->
          <line class="exc-lead" x1="137" y1="150" x2="80" y2="115"/><circle class="exc-dot" cx="80" cy="115"/>
          <text class="exc-lbl" x="80" y="108">Cab</text>
          <line class="exc-lead" x1="240" y1="90" x2="270" y2="55"/><circle class="exc-dot" cx="270" cy="55"/>
          <text class="exc-lbl" x="270" y="48">Boom</text>
          <line class="exc-lead" x1="360" y1="140" x2="410" y2="100"/><circle class="exc-dot" cx="410" cy="100"/>
          <text class="exc-lbl" x="410" y="93">Arm (Stick)</text>
          <line class="exc-lead" x1="400" y1="195" x2="445" y2="170"/><circle class="exc-dot" cx="445" cy="170"/>
          <text class="exc-lbl" x="445" y="163">Bucket (with teeth)</text>
          <line class="exc-lead" x1="170" y1="230" x2="65" y2="265"/><circle class="exc-dot" cx="65" cy="265"/>
          <text class="exc-lbl" x="65" y="272">Crawler Tracks</text>
          <line class="exc-lead" x1="232" y1="185" x2="280" y2="195"/><circle class="exc-dot" cx="280" cy="195"/>
          <text class="exc-lbl" x="310" y="198">Counterweight</text>
          <line class="exc-lead" x1="197" y1="108" x2="210" y2="80"/><circle class="exc-dot" cx="210" cy="80"/>
          <text class="exc-lbl" x="218" y="73">Hydraulic Cylinder</text>'''
    svgs['a. Excavator'] = svg_wrap(excavator, 'Fig 4.2', 'Hydraulic Excavator &mdash; Components &amp; Parts', 500, 290, 500, 290)
    
    # 3. Bulldozer Sketch
    dozer = equipment_sketch('doz', 'Bulldozer', [])
    dozer += f'''
          <line style="stroke:var(--svg-sub);stroke-width:2" x1="20" y1="230" x2="480" y2="230"/>
          <!-- Tracks -->
          <rect class="doz-track" x="100" y="195" width="200" height="35" rx="17"/>
          <circle cx="117" cy="213" r="14" style="fill:var(--svg-sub);stroke:var(--svg-hub);stroke-width:2"/>
          <circle cx="283" cy="213" r="14" style="fill:var(--svg-sub);stroke:var(--svg-hub);stroke-width:2"/>
          <circle cx="160" cy="218" r="5" style="fill:var(--svg-sub);stroke:var(--svg-hub);stroke-width:1"/>
          <circle cx="200" cy="218" r="5" style="fill:var(--svg-sub);stroke:var(--svg-hub);stroke-width:1"/>
          <circle cx="240" cy="218" r="5" style="fill:var(--svg-sub);stroke:var(--svg-hub);stroke-width:1"/>
          <!-- Body -->
          <rect style="fill:var(--svg-yellow);stroke:var(--svg-hub);stroke-width:2;rx:5" x="130" y="140" width="160" height="55"/>
          <!-- Engine housing -->
          <rect style="fill:var(--svg-yellow);stroke:var(--svg-hub);stroke-width:1.5;rx:3" x="210" y="110" width="70" height="35"/>
          <!-- Cab -->
          <rect class="doz-cab" x="145" y="95" width="55" height="48"/>
          <rect style="fill:var(--svg-blue);opacity:.3;rx:2" x="152" y="100" width="40" height="28"/>
          <!-- Exhaust -->
          <rect style="fill:var(--svg-sub);stroke:var(--svg-hub);stroke-width:1;rx:2" x="260" y="90" width="8" height="25"/>
          <!-- Blade -->
          <rect style="fill:var(--svg-orange);stroke:var(--svg-orange-s);stroke-width:2;rx:3" x="70" y="140" width="15" height="80"/>
          <!-- Push frame -->
          <line style="stroke:var(--svg-hub);stroke-width:2.5" x1="85" y1="165" x2="130" y2="165"/>
          <line style="stroke:var(--svg-hub);stroke-width:2.5" x1="85" y1="195" x2="130" y2="195"/>
          <!-- Ripper (back) -->
          <path style="fill:none;stroke:var(--svg-red);stroke-width:2" d="M300,195 L330,175 L340,195 L350,230"/>
          <!-- Labels -->
          <line class="doz-lead" x1="77" y1="175" x2="40" y2="135"/><circle class="doz-dot" cx="40" cy="135"/>
          <text class="doz-lbl" x="40" y="128">Blade</text>
          <line class="doz-lead" x1="170" y1="115" x2="120" y2="70"/><circle class="doz-dot" cx="120" cy="70"/>
          <text class="doz-lbl" x="120" y="63">Cab</text>
          <line class="doz-lead" x1="200" y1="212" x2="200" y2="260"/><circle class="doz-dot" cx="200" cy="260"/>
          <text class="doz-lbl" x="200" y="273">Crawler Tracks</text>
          <line class="doz-lead" x1="340" y1="210" x2="390" y2="200"/><circle class="doz-dot" cx="390" cy="200"/>
          <text class="doz-lbl" x="410" y="203">Ripper</text>
          <line class="doz-lead" x1="108" y1="180" x2="108" y2="260"/><circle class="doz-dot" cx="108" cy="260"/>
          <text class="doz-lbl" x="108" y="273">Push Frame</text>'''
    svgs['b. Dozers'] = svg_wrap(dozer, 'Fig 4.3', 'Bulldozer &mdash; Components: Blade, Cab, Tracks, Ripper', 500, 285, 500, 285)
    
    # 4. Dragline Sketch
    dragline = equipment_sketch('drg', 'Dragline', [])
    dragline += f'''
          <line style="stroke:var(--svg-sub);stroke-width:2" x1="20" y1="280" x2="500" y2="280"/>
          <!-- Base/Tracks -->
          <rect class="drg-track" x="120" y="250" width="160" height="30" rx="15"/>
          <!-- Body -->
          <rect style="fill:var(--svg-yellow);stroke:var(--svg-hub);stroke-width:2;rx:5" x="140" y="190" width="120" height="60"/>
          <!-- Cab -->
          <rect class="drg-cab" x="150" y="155" width="50" height="40"/>
          <rect style="fill:var(--svg-blue);opacity:.3;rx:2" x="156" y="160" width="38" height="25"/>
          <!-- A-Frame mast -->
          <line style="stroke:var(--svg-hub);stroke-width:3" x1="200" y1="190" x2="200" y2="80"/>
          <line style="stroke:var(--svg-hub);stroke-width:2" x1="170" y1="190" x2="200" y2="80"/>
          <line style="stroke:var(--svg-hub);stroke-width:2" x1="230" y1="190" x2="200" y2="80"/>
          <!-- Boom -->
          <line class="drg-boom" x1="200" y1="160" x2="400" y2="80"/>
          <line class="drg-boom" x1="200" y1="170" x2="400" y2="90"/>
          <!-- Hoist cable (from boom tip through fairlead) -->
          <line class="drg-cable" x1="200" y1="80" x2="400" y2="85"/>
          <line class="drg-cable" x1="400" y1="85" x2="380" y2="240"/>
          <!-- Drag cable -->
          <line class="drg-cable" x1="200" y1="210" x2="380" y2="245" style="stroke:var(--svg-red);stroke-width:2"/>
          <!-- Bucket -->
          <path class="drg-bucket" d="M365,235 L395,235 L405,260 L355,260 Z"/>
          <!-- Labels -->
          <line class="drg-lead" x1="200" y1="80" x2="160" y2="50"/><circle class="drg-dot" cx="160" cy="50"/>
          <text class="drg-lbl" x="160" y="43">Mast (A-Frame)</text>
          <line class="drg-lead" x1="350" y1="90" x2="420" y2="55"/><circle class="drg-dot" cx="420" cy="55"/>
          <text class="drg-lbl" x="420" y="48">Boom</text>
          <line class="drg-lead" x1="390" y1="160" x2="440" y2="140"/><circle class="drg-dot" cx="440" cy="140"/>
          <text class="drg-lbl" x="440" y="133">Hoist Cable</text>
          <line class="drg-lead" x1="300" y1="228" x2="310" y2="195"/><circle class="drg-dot" cx="310" cy="195"/>
          <text class="drg-lbl" x="340" y="195">Drag Cable</text>
          <line class="drg-lead" x1="380" y1="250" x2="440" y2="250"/><circle class="drg-dot" cx="440" cy="250"/>
          <text class="drg-lbl" x="450" y="253">Bucket</text>
          <line class="drg-lead" x1="200" y1="265" x2="80" y2="265"/><circle class="drg-dot" cx="80" cy="265"/>
          <text class="drg-lbl" x="80" y="258">Crawler Base</text>'''
    svgs['e. Dragline'] = svg_wrap(dragline, 'Fig 4.4', 'Dragline Excavator &mdash; Boom, Cables, Bucket', 500, 295, 500, 295)
    
    # 5. Sheepfoot Roller Sketch
    sheep = equipment_sketch('sfr', 'Sheepfoot Roller', [])
    sheep += f'''
          <line style="stroke:var(--svg-sub);stroke-width:2" x1="20" y1="220" x2="480" y2="220"/>
          <!-- Frame -->
          <rect style="fill:var(--svg-yellow);stroke:var(--svg-hub);stroke-width:1.5;rx:3" x="100" y="120" width="280" height="30"/>
          <!-- Tow bar -->
          <line style="stroke:var(--svg-hub);stroke-width:3" x1="100" y1="135" x2="50" y2="135"/>
          <circle style="fill:var(--svg-hub)" cx="50" cy="135" r="5"/>
          <!-- Drum -->
          <ellipse class="sfr-drum" cx="240" cy="185" rx="100" ry="35"/>
          <!-- Feet projections -->
          <rect class="sfr-foot" x="155" y="152" width="6" height="14" rx="1"/>
          <rect class="sfr-foot" x="175" y="148" width="6" height="12" rx="1"/>
          <rect class="sfr-foot" x="195" y="147" width="6" height="10" rx="1"/>
          <rect class="sfr-foot" x="220" y="147" width="6" height="8" rx="1"/>
          <rect class="sfr-foot" x="255" y="147" width="6" height="8" rx="1"/>
          <rect class="sfr-foot" x="280" y="147" width="6" height="10" rx="1"/>
          <rect class="sfr-foot" x="300" y="148" width="6" height="12" rx="1"/>
          <rect class="sfr-foot" x="315" y="152" width="6" height="14" rx="1"/>
          <!-- Bottom feet (touching ground) -->
          <rect class="sfr-foot" x="165" y="218" width="6" height="14" rx="1"/>
          <rect class="sfr-foot" x="190" y="218" width="6" height="16" rx="1"/>
          <rect class="sfr-foot" x="215" y="218" width="6" height="16" rx="1"/>
          <rect class="sfr-foot" x="240" y="218" width="6" height="16" rx="1"/>
          <rect class="sfr-foot" x="265" y="218" width="6" height="16" rx="1"/>
          <rect class="sfr-foot" x="290" y="218" width="6" height="16" rx="1"/>
          <rect class="sfr-foot" x="310" y="218" width="6" height="14" rx="1"/>
          <!-- Ballast box -->
          <rect style="fill:var(--svg-orange);stroke:var(--svg-orange-s);stroke-width:1.5;rx:3" x="185" y="100" width="110" height="22"/>
          <text style="font:9px 'Source Sans 3',sans-serif;fill:var(--svg-text-orange);text-anchor:middle" x="240" y="115">Ballast Box</text>
          <!-- Labels -->
          <line class="sfr-lead" x1="240" y1="180" x2="400" y2="165"/><circle class="sfr-dot" cx="400" cy="165"/>
          <text class="sfr-lbl" x="400" y="158">Steel Drum</text>
          <line class="sfr-lead" x1="215" y1="230" x2="400" y2="250"/><circle class="sfr-dot" cx="400" cy="250"/>
          <text class="sfr-lbl" x="400" y="257">Protruding Feet</text>
          <line class="sfr-lead" x1="50" y1="135" x2="35" y2="100"/><circle class="sfr-dot" cx="35" cy="100"/>
          <text class="sfr-lbl" x="35" y="93">Tow Hitch</text>
          <text style="font:italic 9px 'Source Sans 3',sans-serif;fill:var(--svg-sub);text-anchor:middle" x="240" y="260">Best for: Cohesive (Clay) Soils &bull; Compaction: Bottom to Top</text>'''
    svgs['b. Sheep Foot Roller'] = svg_wrap(sheep, 'Fig 4.5', 'Sheepfoot Roller &mdash; Drum with Projecting Feet', 500, 270, 500, 270)
    
    # 6. Compaction Equipment Suitability Chart
    comp_chart, w, h = comparison_table_svg('cmp', 'Compaction Equipment vs Soil Type', 'Soil Type', 'Best Equipment',
        [
            ('Gravel / Sand (Granular)', 'Vibrating Roller'),
            ('Clay (Cohesive)', 'Sheepfoot Roller'),
            ('Silt-Clay Mix', 'Pneumatic Tired Roller'),
            ('Rock Fill / Weathered Rock', 'Grid Roller'),
            ('All Types (Universal)', 'Pneumatic Tired Roller'),
            ('Asphalt / Road Surface', 'Smooth Wheel Roller'),
            ('Confined Spaces', 'Frog Rammer / Plate Compactor'),
            ('Dam / Embankment', 'Sheepfoot + Vibrating Roller'),
        ])
    svgs['Compaction Equipment Suitability'] = svg_wrap(comp_chart, 'Fig 4.6', 'Compaction Equipment Selection by Soil Type', w, h, w, h)
    
    # 7. Tower Crane Sketch
    tower_crane = equipment_sketch('tcr', 'Tower Crane', [])
    tower_crane += f'''
          <line style="stroke:var(--svg-sub);stroke-width:2" x1="20" y1="380" x2="580" y2="380"/>
          <!-- Foundation -->
          <rect style="fill:var(--svg-sub);stroke:var(--svg-hub);stroke-width:2;opacity:.4" x="145" y="360" width="60" height="20"/>
          <!-- Tower / Mast -->
          <rect style="fill:var(--svg-yellow);stroke:var(--svg-hub);stroke-width:2" x="165" y="60" width="20" height="300"/>
          <!-- Cross bracing on tower -->
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="165" y1="80" x2="185" y2="120"/>
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="185" y1="80" x2="165" y2="120"/>
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="165" y1="140" x2="185" y2="180"/>
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="185" y1="140" x2="165" y2="180"/>
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="165" y1="200" x2="185" y2="240"/>
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="185" y1="200" x2="165" y2="240"/>
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="165" y1="260" x2="185" y2="300"/>
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="185" y1="260" x2="165" y2="300"/>
          <!-- Slewing Unit -->
          <circle style="fill:var(--svg-blue);stroke:var(--svg-blue-s);stroke-width:2" cx="175" cy="60" r="12"/>
          <!-- Operator Cab -->
          <rect class="tcr-cab" x="185" y="50" width="25" height="20"/>
          <rect style="fill:var(--svg-blue);opacity:.3;rx:1" x="189" y="53" width="17" height="12"/>
          <!-- Jib (working arm) - horizontal -->
          <line style="stroke:var(--svg-hub);stroke-width:3" x1="175" y1="48" x2="470" y2="48"/>
          <line style="stroke:var(--svg-hub);stroke-width:3" x1="175" y1="55" x2="470" y2="55"/>
          <!-- Jib cross members -->
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="220" y1="48" x2="230" y2="55"/>
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="260" y1="48" x2="270" y2="55"/>
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="300" y1="48" x2="310" y2="55"/>
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="340" y1="48" x2="350" y2="55"/>
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="380" y1="48" x2="390" y2="55"/>
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="420" y1="48" x2="430" y2="55"/>
          <!-- Counter-jib -->
          <line style="stroke:var(--svg-hub);stroke-width:3" x1="175" y1="48" x2="80" y2="48"/>
          <line style="stroke:var(--svg-hub);stroke-width:3" x1="175" y1="55" x2="80" y2="55"/>
          <!-- Counterweight -->
          <rect style="fill:var(--svg-red);stroke:var(--svg-red-s);stroke-width:2;rx:3" x="60" y="55" width="40" height="25"/>
          <!-- Trolley on jib -->
          <rect style="fill:var(--svg-purple);stroke:var(--svg-purple-s);stroke-width:1.5;rx:2" x="360" y="38" width="20" height="12"/>
          <!-- Hoist cable from trolley -->
          <line style="stroke:var(--svg-hub);stroke-width:1.5" x1="370" y1="50" x2="370" y2="130"/>
          <!-- Hook -->
          <path style="fill:none;stroke:var(--svg-hub);stroke-width:2" d="M370,130 Q380,145 370,150 Q360,145 370,130"/>
          <!-- Cat head / peak -->
          <line style="stroke:var(--svg-hub);stroke-width:2" x1="175" y1="48" x2="175" y2="25"/>
          <!-- Pendant cables -->
          <line class="tcr-cable" x1="175" y1="25" x2="470" y2="48"/>
          <line class="tcr-cable" x1="175" y1="25" x2="80" y2="48"/>
          <!-- Labels -->
          <line class="tcr-lead" x1="175" y1="200" x2="45" y2="200"/><circle class="tcr-dot" cx="45" cy="200"/>
          <text class="tcr-lbl" x="45" y="193">Tower (Mast)</text>
          <line class="tcr-lead" x1="380" y1="50" x2="430" y2="25"/><circle class="tcr-dot" cx="430" cy="25"/>
          <text class="tcr-lbl" x="438" y="22">Jib (Working Arm)</text>
          <line class="tcr-lead" x1="80" y1="67" x2="45" y2="100"/><circle class="tcr-dot" cx="45" cy="100"/>
          <text class="tcr-lbl" x="45" y="113">Counterweight</text>
          <line class="tcr-lead" x1="370" y1="44" x2="420" y2="80"/><circle class="tcr-dot" cx="420" cy="80"/>
          <text class="tcr-lbl" x="420" y="93">Trolley</text>
          <line class="tcr-lead" x1="370" y1="150" x2="420" y2="155"/><circle class="tcr-dot" cx="420" cy="155"/>
          <text class="tcr-lbl" x="430" y="158">Hook Block</text>
          <line class="tcr-lead" x1="175" y1="25" x2="130" y2="15"/><circle class="tcr-dot" cx="130" cy="15"/>
          <text class="tcr-lbl" x="110" y="12">Cat Head</text>
          <line class="tcr-lead" x1="197" y1="60" x2="250" y2="80"/><circle class="tcr-dot" cx="250" cy="80"/>
          <text class="tcr-lbl" x="250" y="93">Operator Cab</text>
          <line class="tcr-lead" x1="175" y1="60" x2="130" y2="75"/><circle class="tcr-dot" cx="130" cy="75"/>
          <text class="tcr-lbl" x="115" y="82">Slewing Unit</text>
          <line class="tcr-lead" x1="175" y1="370" x2="280" y2="370"/><circle class="tcr-dot" cx="280" cy="370"/>
          <text class="tcr-lbl" x="300" y="373">Foundation Base</text>'''
    svgs['d) Tower Crane'] = svg_wrap(tower_crane, 'Fig 4.7', 'Tower Crane &mdash; Components: Mast, Jib, Trolley, Counterweight', 580, 395, 580, 395)
    
    # 8. TBM Sketch
    tbm = equipment_sketch('tbm', 'TBM', [])
    tbm += f'''
          <!-- Tunnel outline -->
          <ellipse style="fill:var(--svg-sub);opacity:.15;stroke:var(--svg-hub);stroke-width:1.5" cx="130" cy="150" rx="110" ry="110"/>
          <!-- Shield -->
          <rect style="fill:var(--svg-teal);stroke:var(--svg-hub);stroke-width:2;opacity:.8" x="130" y="55" width="320" height="190" rx="5"/>
          <!-- Cutter head (disc) -->
          <circle style="fill:var(--svg-orange);stroke:var(--svg-hub);stroke-width:3" cx="130" cy="150" r="95"/>
          <circle style="fill:var(--svg-yellow);stroke:var(--svg-hub);stroke-width:2" cx="130" cy="150" r="40"/>
          <!-- Cutter disc blades -->
          <line style="stroke:var(--svg-hub);stroke-width:2" x1="130" y1="55" x2="130" y2="245"/>
          <line style="stroke:var(--svg-hub);stroke-width:2" x1="35" y1="150" x2="225" y2="150"/>
          <line style="stroke:var(--svg-hub);stroke-width:2" x1="63" y1="83" x2="197" y2="217"/>
          <line style="stroke:var(--svg-hub);stroke-width:2" x1="197" y1="83" x2="63" y2="217"/>
          <!-- Conveyor belt -->
          <rect style="fill:var(--svg-green);stroke:var(--svg-green-s);stroke-width:1;rx:2" x="230" y="195" width="220" height="15"/>
          <!-- Thrust jacks -->
          <rect style="fill:var(--svg-red);stroke:var(--svg-red-s);stroke-width:1.5;rx:2" x="230" y="85" width="30" height="20"/>
          <rect style="fill:var(--svg-red);stroke:var(--svg-red-s);stroke-width:1.5;rx:2" x="230" y="115" width="30" height="20"/>
          <!-- Segment erector area -->
          <rect style="fill:var(--svg-purple);stroke:var(--svg-purple-s);stroke-width:1;rx:3;opacity:.5" x="360" y="65" width="80" height="125"/>
          <!-- Installed segments -->
          <path style="fill:none;stroke:var(--svg-blue);stroke-width:3" d="M460,55 Q470,150 460,245"/>
          <!-- Labels -->
          <line class="tbm-lead" x1="130" y1="55" x2="130" y2="25"/><circle class="tbm-dot" cx="130" cy="25"/>
          <text class="tbm-lbl" x="130" y="18">Cutter Head</text>
          <line class="tbm-lead" x1="245" y1="95" x2="290" y2="60"/><circle class="tbm-dot" cx="290" cy="60"/>
          <text class="tbm-lbl" x="310" y="57">Thrust Jacks</text>
          <line class="tbm-lead" x1="340" y1="200" x2="370" y2="230"/><circle class="tbm-dot" cx="370" cy="230"/>
          <text class="tbm-lbl" x="390" y="233">Muck Conveyor</text>
          <line class="tbm-lead" x1="400" y1="130" x2="440" y2="40"/><circle class="tbm-dot" cx="440" cy="40"/>
          <text class="tbm-lbl" x="458" y="37">Segment Erector</text>
          <line class="tbm-lead" x1="460" y1="150" x2="510" y2="150"/><circle class="tbm-dot" cx="510" cy="150"/>
          <text class="tbm-lbl" x="520" y="153">Lining Segments</text>
          <line class="tbm-lead" x1="300" y1="150" x2="340" y2="160"/><circle class="tbm-dot" cx="340" cy="160"/>
          <text class="tbm-lbl" x="340" y="175">Shield</text>'''
    svgs['B. Tunneling by Tunnel Boring Machine'] = svg_wrap(tbm, 'Fig 4.8', 'Tunnel Boring Machine (TBM) &mdash; Cross-section View', 560, 260, 560, 260)
    
    # 9. Concrete Construction Equipment Flow
    conc_flow = hub_spoke_svg('ccn', 'CONCRETE', [
        ('Batching', 'Weigh/measure materials'),
        ('Mixing', 'Tilting/Pan/Transit mixer'),
        ('Transport', 'Pump, chute, bucket'),
        ('Placing', 'Formwork &amp; pouring'),
        ('Compaction', 'Needle/plate vibrator'),
        ('Finishing', 'Power trowel, float'),
        ('Curing', 'Moist/membrane/steam'),
    ], hub_sub='Process', width=600, height=420)
    svgs['Equipment for Concrete Construction'] = svg_wrap(conc_flow, 'Fig 4.9', 'Concrete Construction Process &amp; Equipment', 600, 420)
    
    # 10. Needle Vibrator Sketch
    needle = equipment_sketch('nv', 'Needle Vibrator', [])
    needle += f'''
          <!-- Power Unit / Motor -->
          <rect style="fill:var(--svg-blue);stroke:var(--svg-blue-s);stroke-width:2;rx:5" x="50" y="100" width="100" height="70"/>
          <text style="font:600 10px 'Source Sans 3',sans-serif;fill:var(--svg-text-blue);text-anchor:middle" x="100" y="130">Motor</text>
          <text style="font:8px 'Source Sans 3',sans-serif;fill:var(--svg-text-blue);text-anchor:middle" x="100" y="148">Power Unit</text>
          <!-- Flexible shaft -->
          <path style="fill:none;stroke:var(--svg-hub);stroke-width:4" d="M150,135 Q200,125 250,135 Q300,145 350,135"/>
          <!-- Vibrating head (needle) -->
          <rect style="fill:var(--svg-orange);stroke:var(--svg-orange-s);stroke-width:2;rx:10" x="350" y="125" width="120" height="20"/>
          <ellipse style="fill:var(--svg-orange);stroke:var(--svg-orange-s);stroke-width:2" cx="470" cy="135" rx="8" ry="10"/>
          <!-- Vibration waves -->
          <path style="fill:none;stroke:var(--svg-red);stroke-width:1;opacity:.6" d="M380,115 Q390,110 400,115"/>
          <path style="fill:none;stroke:var(--svg-red);stroke-width:1;opacity:.6" d="M410,115 Q420,108 430,115"/>
          <path style="fill:none;stroke:var(--svg-red);stroke-width:1;opacity:.6" d="M440,115 Q450,108 460,115"/>
          <path style="fill:none;stroke:var(--svg-red);stroke-width:1;opacity:.5" d="M380,155 Q390,160 400,155"/>
          <path style="fill:none;stroke:var(--svg-red);stroke-width:1;opacity:.5" d="M410,155 Q420,162 430,155"/>
          <path style="fill:none;stroke:var(--svg-red);stroke-width:1;opacity:.5" d="M440,155 Q450,162 460,155"/>
          <!-- Concrete surface -->
          <rect style="fill:var(--svg-sub);opacity:.15" x="300" y="150" width="200" height="60"/>
          <line style="stroke:var(--svg-sub);stroke-width:1.5" x1="300" y1="150" x2="500" y2="150"/>
          <text style="font:italic 9px 'Source Sans 3',sans-serif;fill:var(--svg-sub);text-anchor:middle" x="400" y="190">Fresh Concrete</text>
          <!-- Labels -->
          <line class="nv-lead" x1="100" y1="100" x2="100" y2="70"/><circle class="nv-dot" cx="100" cy="70"/>
          <text class="nv-lbl" x="100" y="63">Power Unit</text>
          <line class="nv-lead" x1="250" y1="135" x2="250" y2="80"/><circle class="nv-dot" cx="250" cy="80"/>
          <text class="nv-lbl" x="250" y="73">Flexible Shaft</text>
          <line class="nv-lead" x1="410" y1="125" x2="410" y2="80"/><circle class="nv-dot" cx="410" cy="80"/>
          <text class="nv-lbl" x="410" y="73">Vibrating Head</text>
          <text style="font:italic 9px 'Source Sans 3',sans-serif;fill:var(--svg-sub);text-anchor:middle" x="260" y="220">3 Parts: Power Unit + Flexible Shaft + Vibrating Head (Needle)</text>'''
    svgs['e. Concrete Compaction Equipment'] = svg_wrap(needle, 'Fig 4.10', 'Needle Vibrator &mdash; 3 Parts: Motor, Flexible Shaft, Vibrating Head', 530, 230, 530, 230)
    
    # 11. Highway Pavement layers
    highway = f'''          <defs><style>
              .hw-lyr{{stroke:var(--svg-hub);stroke-width:1.5}}
              .hw-t{{font:bold 10px 'Source Sans 3',sans-serif;fill:#fff;text-anchor:middle}}
              .hw-eq{{font:italic 9px 'Source Sans 3',sans-serif;fill:var(--svg-text);text-anchor:start}}
            </style></defs>
          <text style="font:bold 13px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="280" y="20">Highway Pavement Layers &amp; Equipment</text>
          <!-- Surface/Wearing course -->
          <rect class="hw-lyr" x="120" y="35" width="320" height="35" rx="3" style="fill:var(--svg-hub);opacity:.85"/>
          <text class="hw-t" x="280" y="57">Surface / Wearing Course</text>
          <text class="hw-eq" x="460" y="50">Asphalt Paver</text>
          <text class="hw-eq" x="460" y="63">Smooth Wheel Roller</text>
          <!-- Binder course -->
          <rect class="hw-lyr" x="110" y="70" width="340" height="30" rx="2" style="fill:var(--svg-orange);opacity:.85"/>
          <text class="hw-t" x="280" y="90">Binder Course (Bituminous)</text>
          <text class="hw-eq" x="460" y="87">Bitumen Distributor</text>
          <!-- Base course -->
          <rect class="hw-lyr" x="100" y="100" width="360" height="35" rx="2" style="fill:var(--svg-blue);opacity:.8"/>
          <text class="hw-t" x="280" y="122">Base Course (WBM/WMM)</text>
          <text class="hw-eq" x="460" y="115">Grader, Vibrating Roller</text>
          <!-- Sub-base -->
          <rect class="hw-lyr" x="90" y="135" width="380" height="30" rx="2" style="fill:var(--svg-green);opacity:.8"/>
          <text class="hw-t" x="280" y="155">Sub-Base Course</text>
          <text class="hw-eq" x="460" y="152">Loader, Pneu. Roller</text>
          <!-- Sub-grade -->
          <rect class="hw-lyr" x="80" y="165" width="400" height="35" rx="2" style="fill:var(--svg-teal);opacity:.7"/>
          <text class="hw-t" x="280" y="187">Sub-Grade (Natural Soil)</text>
          <text class="hw-eq" x="460" y="182">Motor Grader</text>
          <text class="hw-eq" x="460" y="195">Sheepfoot Roller</text>
          <!-- Natural ground -->
          <rect style="fill:var(--svg-sub);opacity:.2" x="70" y="200" width="420" height="20"/>
          <text style="font:italic 9px 'Source Sans 3',sans-serif;fill:var(--svg-sub);text-anchor:middle" x="280" y="215">Natural Ground</text>'''
    svgs['Equipment for Highway Construction'] = svg_wrap(highway, 'Fig 4.11', 'Highway Pavement Layers with Equipment for Each Layer', 580, 230, 580, 230)
    
    # 12. Equipment Selection Factors
    sel_hub = hub_spoke_svg('sel', 'EQUIPMENT', [
        ('Site Conditions', 'Terrain, access, soil'),
        ('Nature of Work', 'Excavation, lifting'),
        ('Output Required', 'Capacity, speed'),
        ('Availability', 'Buy, hire, lease'),
        ('Cost', 'Capital + operating'),
        ('Safety', 'Operator protection'),
        ('Maintenance', 'Spares, workshop'),
        ('Climate', 'Rain, temp, altitude'),
    ], hub_sub='Selection Factors', width=650, height=480)
    svgs['Detailed Selection Factors'] = svg_wrap(sel_hub, 'Fig 4.12', 'Factors for Selection of Construction Equipment', 650, 480)
    
    # 13. Crusher Types
    crush_flow = hub_spoke_svg('crs', 'CRUSHING', [
        ('Jaw Crusher', 'Primary, compression'),
        ('Gyratory', 'Primary, large capacity'),
        ('Cone Crusher', 'Secondary, fine output'),
        ('Roll Crusher', 'Soft-medium material'),
        ('Impact/Hammer', 'Cubical aggregates'),
    ], hub_sub='Plants', width=520, height=380)
    svgs['Crushing Plants'] = svg_wrap(crush_flow, 'Fig 4.13', 'Types of Crushing Equipment', 520, 380, 520, 380)
    
    # 14. Wheel vs Crawler
    wc_content, w, h = comparison_table_svg('wc', 'Wheel vs Crawler Mounted Equipment', 'Wheel Mounted', 'Crawler Mounted',
        [
            ('Fast on roads (30-50 km/h)', 'Slow (3-6 km/h)'),
            ('Good for paved surfaces', 'Good for rough/soft terrain'),
            ('Lower traction', 'Higher traction'),
            ('Easier to transport', 'Needs trailer for transport'),
            ('Lower ground pressure', 'Distributes weight well'),
            ('Rubber tires wear on rocky ground', 'Steel tracks handle rocks'),
            ('Example: Mobile crane', 'Example: Excavator, dozer'),
        ])
    svgs['Comparison: Wheel vs Crawler'] = svg_wrap(wc_content, 'Fig 4.14', 'Wheel Mounted vs Crawler Mounted Equipment', w, h, w, h)
    
    # 15. Drill & Blast Steps
    db_content, w, h = flow_svg('db', [
        ('Setting\nOut', ''),
        ('Drilling', ''),
        ('Charging', ''),
        ('Blasting', ''),
        ('Ventilate', ''),
        ('Scaling', ''),
        ('Mucking', ''),
        ('Support\n&amp; Lining', ''),
    ], 'horizontal')
    svgs['Steps in Conventional Tunnel'] = svg_wrap(db_content, 'Fig 4.15', 'Drill &amp; Blast Tunnel Construction Steps', w, h, w, h)
    
    return svgs

def get_ch5_svgs():
    svgs = {}
    
    # 1. Contract Types
    ct_hub = hub_spoke_svg('ct', 'CONTRACT', [
        ('Lump Sum', 'Fixed total price'),
        ('Unit Price', 'Rate per item/BOQ'),
        ('Cost Plus', 'Cost + fee/percentage'),
        ('Percentage', '% of actual cost'),
        ('Turnkey', 'Single responsibility'),
        ('D&amp;B', 'Design + Build'),
        ('BOOT/BOT', 'Concessionaire builds'),
        ('CM Contract', 'Professional management'),
    ], hub_sub='Types', width=650, height=480)
    svgs['Types of Contract'] = svg_wrap(ct_hub, 'Fig 5.1', 'Types of Construction Contracts', 650, 480)
    
    # 2. Tendering Process flow
    tend_content, w, h = flow_svg('tnd', [
        ('Tender\nNotice', 'Publish'),
        ('Document\nSale', ''),
        ('Pre-bid\nConf.', ''),
        ('Bid\nSubmission', ''),
        ('Bid\nOpening', ''),
        ('Evaluation', ''),
        ('LOA', 'Award'),
        ('Contract\nSigning', ''),
    ], 'horizontal')
    svgs['Bidding Stages'] = svg_wrap(tend_content, 'Fig 5.2', 'Tendering Process Flow: Notice to Contract Signing', w, h, w, h)
    
    # 3. Procurement Methods
    proc_comp, w, h = comparison_table_svg('prm', 'Procurement Methods (as per PPA)', 'Method', 'Threshold / Details',
        [
            ('ICB (International Competitive)', '&gt; threshold, 45 days notice, English'),
            ('NCB (National Competitive)', '&gt; 20 Lakh, 30 days notice'),
            ('Sealed Quotation', '&le; 20 Lakh, 15 days'),
            ('Direct Procurement', 'Emergency / single source'),
            ('Force Account (Amanat)', 'Govt departments, sensitive work'),
            ('Users Committee', 'Community projects'),
        ])
    svgs['Methods of Procurement'] = svg_wrap(proc_comp, 'Fig 5.3', 'Procurement Methods as per PPA Nepal', w, h, w, h)
    
    # 4. BOOT Project flow
    boot_content, w, h = flow_svg('bot', [
        ('BUILD', 'Construct\nfacility'),
        ('OWN', 'Private\nownership'),
        ('OPERATE', 'Run &amp; earn\nrevenue'),
        ('TRANSFER', 'Return to\nGovt'),
    ])
    svgs['BOOT Contract'] = svg_wrap(boot_content, 'Fig 5.4', 'BOOT Contract: Build-Own-Operate-Transfer', w, h, w, h)
    
    # 5. Three-party contract relationship
    preq = hub_spoke_svg('pq', 'PRE-', [
        ('Experience', 'Similar projects'),
        ('Financial', 'Bank statements'),
        ('Equipment', 'Owned/available'),
        ('Personnel', 'Key staff CV'),
        ('Litigation', 'Legal history'),
        ('Current Work', 'Committed capacity'),
    ], hub_sub='Qualification', width=550, height=400)
    svgs['Matters in Pre-qualification'] = svg_wrap(preq, 'Fig 5.5', 'Pre-qualification Criteria for Contractors', 550, 400, 550, 400)
    
    # 6. Consultant Selection Methods
    cons_hub = hub_spoke_svg('cns', 'CONSULTANT', [
        ('QCBS', 'Quality + Cost Based'),
        ('QBS', 'Quality Only'),
        ('FBS', 'Fixed Budget'),
        ('LCS', 'Least Cost'),
        ('CQS', 'Consultant Qualification'),
        ('SSS', 'Single Source'),
    ], hub_sub='Selection', width=550, height=400)
    svgs['Quality and Cost Based Selection'] = svg_wrap(cons_hub, 'Fig 5.6', 'Consultant Selection Methods', 550, 400, 550, 400)
    
    # 7. Contract Documents priority
    doc_content, w, h = flow_svg('doc', [
        ('Agreement', '1st'),
        ('LOA', '2nd'),
        ('Bid', '3rd'),
        ('SCC', '4th'),
        ('GCC', '5th'),
        ('Specs', '6th'),
        ('Drawings', '7th'),
        ('BOQ', '8th'),
    ], 'horizontal')
    svgs['Priority of Document'] = svg_wrap(doc_content, 'Fig 5.7', 'Priority of Contract Documents (Highest to Lowest)', w, h, w, h)
    
    # 8. Performance Security formula
    ps_svg = f'''          <defs><style>
              .ps-box{{rx:10;ry:10;stroke-width:2;opacity:.92}}
              .ps-t{{font:bold 14px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-hub)}}
              .ps-s{{font:11px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
            </style></defs>
          <rect class="ps-box" x="50" y="10" width="500" height="55" style="fill:var(--svg-red);stroke:var(--svg-red-s)"/>
          <text class="ps-t" x="300" y="32" style="fill:var(--svg-text-red)">If Bid Price &lt; 0.85 &times; Estimated Price:</text>
          <text style="font:bold 13px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-text-red)" x="300" y="52">PS = 5% of BP + 0.5 &times; (0.85&times;EP &minus; BP)</text>
          <rect class="ps-box" x="50" y="75" width="240" height="40" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text class="ps-s" x="170" y="95" style="fill:var(--svg-text-blue)">Normal PS: 5-13% of Contract</text>
          <rect class="ps-box" x="310" y="75" width="240" height="40" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <text class="ps-s" x="430" y="95" style="fill:var(--svg-text-green)">Bid Security: 2-3% of Estimated</text>'''
    svgs['Performance Security'] = svg_wrap(ps_svg, 'Fig 5.8', 'Performance Security &amp; Bid Security Formulae', 600, 125, 600, 125)
    
    # 9. Liquidated Damages
    ld_svg = f'''          <defs><style>
              .ld-box{{rx:10;ry:10;stroke-width:2;opacity:.92}}
              .ld-t{{font:bold 13px 'Source Sans 3',sans-serif;text-anchor:middle}}
              .ld-s{{font:11px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
            </style></defs>
          <rect class="ld-box" x="50" y="10" width="500" height="50" style="fill:var(--svg-orange);stroke:var(--svg-orange-s)"/>
          <text class="ld-t" x="300" y="30" style="fill:var(--svg-text-orange)">Liquidated Damages (LD)</text>
          <text class="ld-s" x="300" y="50" style="fill:var(--svg-text-orange)">0.05% of contract price per day of delay &bull; Max: 10% of contract price</text>
          <rect class="ld-box" x="50" y="70" width="240" height="40" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <text class="ld-s" x="170" y="92" style="fill:var(--svg-text-green)">&cross; NOT for employer-caused delays</text>
          <rect class="ld-box" x="310" y="70" width="240" height="40" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text class="ld-s" x="430" y="92" style="fill:var(--svg-text-blue)">&check; Pre-agreed, no proof needed</text>'''
    svgs['Liquidated Damages'] = svg_wrap(ld_svg, 'Fig 5.9', 'Liquidated Damages: Rate, Cap &amp; Rules', 600, 120, 600, 120)
    
    # 10. FIDIC Rainbow
    fidic_svg = f'''          <defs><style>
              .fd-box{{rx:8;ry:8;stroke-width:1.5;opacity:.92}}
              .fd-t{{font:bold 11px 'Source Sans 3',sans-serif;text-anchor:middle;fill:#fff}}
              .fd-s{{font:9px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
            </style></defs>
          <text style="font:bold 14px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="300" y="20">FIDIC Rainbow Suite of Contracts</text>
          <rect class="fd-box" x="20" y="35" width="120" height="50" style="fill:var(--svg-red)"/>
          <text class="fd-t" x="80" y="55">Red Book</text>
          <text class="fd-s" x="80" y="80">Construction</text>
          <rect class="fd-box" x="155" y="35" width="120" height="50" style="fill:var(--svg-yellow)"/>
          <text class="fd-t" x="215" y="55" style="fill:#333">Yellow Book</text>
          <text class="fd-s" x="215" y="80">Plant &amp; D&amp;B</text>
          <rect class="fd-box" x="290" y="35" width="120" height="50" style="fill:#c0c0c0"/>
          <text class="fd-t" x="350" y="55" style="fill:#333">Silver Book</text>
          <text class="fd-s" x="350" y="80">EPC / Turnkey</text>
          <rect class="fd-box" x="425" y="35" width="120" height="50" style="fill:var(--svg-green)"/>
          <text class="fd-t" x="485" y="55">Green Book</text>
          <text class="fd-s" x="485" y="80">Short Form</text>
          <rect class="fd-box" x="20" y="100" width="120" height="50" style="fill:var(--svg-blue)"/>
          <text class="fd-t" x="80" y="120">Blue Book</text>
          <text class="fd-s" x="80" y="145">Dredging</text>
          <rect class="fd-box" x="155" y="100" width="120" height="50" style="fill:#f5f5f5;stroke:#999"/>
          <text class="fd-t" x="215" y="120" style="fill:#333">White Book</text>
          <text class="fd-s" x="215" y="145">Consultant Svc</text>
          <rect class="fd-box" x="290" y="100" width="120" height="50" style="fill:#c9a636"/>
          <text class="fd-t" x="350" y="120">Gold Book</text>
          <text class="fd-s" x="350" y="145">DBO</text>
          <rect class="fd-box" x="425" y="100" width="120" height="50" style="fill:var(--svg-pink)"/>
          <text class="fd-t" x="485" y="120">Pink Book</text>
          <text class="fd-s" x="485" y="145">MDB Harmonised</text>'''
    svgs['FIDIC'] = svg_wrap(fidic_svg, 'Fig 5.10', 'FIDIC Rainbow Suite of Contract Forms', 570, 160, 570, 160)
    
    return svgs

def get_ch6_svgs():
    svgs = {}
    
    # 1. Job Layout factors
    jl_hub = hub_spoke_svg('jl', 'JOB', [
        ('Access Roads', 'Entry/exit routes'),
        ('Storage Areas', 'Material yards'),
        ('Office/Lab', 'Site office, testing'),
        ('Worker Camp', 'Labor accommodation'),
        ('Equipment Yard', 'Parking, maintenance'),
        ('Utilities', 'Water, power, drainage'),
    ], hub_sub='Layout', width=550, height=400)
    svgs['Objectives of Layout Decision'] = svg_wrap(jl_hub, 'Fig 6.1', 'Key Components of Construction Site Layout', 550, 400, 550, 400)
    
    # 2. Material Handling principles
    mh_content, w, h = flow_svg('mh', [
        ('Plan', 'Route &amp;\nmethod'),
        ('Receive', 'Inspect &amp;\nrecord'),
        ('Store', 'Protect &amp;\naccess'),
        ('Handle', 'Minimize\nmovement'),
        ('Deliver', 'To work\npoint'),
    ])
    svgs['Key Points of Material Handling'] = svg_wrap(mh_content, 'Fig 6.2', 'Material Handling System Flow', w, h, w, h)
    
    # 3. S-Curve diagram
    scurve = f'''          <defs><style>
              .sc-ax{{stroke:var(--svg-hub);stroke-width:2}}
              .sc-lbl{{font:bold 11px 'Source Sans 3',sans-serif;fill:var(--svg-hub)}}
              .sc-line{{stroke-width:3;fill:none}}
            </style></defs>
          <line class="sc-ax" x1="60" y1="20" x2="60" y2="220"/>
          <line class="sc-ax" x1="60" y1="220" x2="500" y2="220"/>
          <text class="sc-lbl" x="25" y="120" transform="rotate(-90,25,120)">Cumulative %</text>
          <text class="sc-lbl" x="280" y="248">Time</text>
          <!-- Planned S-curve -->
          <path class="sc-line" d="M60,210 Q120,205 180,180 Q260,110 340,60 Q400,35 460,30" style="stroke:var(--svg-blue)"/>
          <text style="font:600 10px 'Source Sans 3',sans-serif;fill:var(--svg-blue)" x="465" y="35">Planned</text>
          <!-- Actual S-curve (delayed) -->
          <path class="sc-line" d="M60,210 Q140,208 200,195 Q280,140 360,80 Q420,50 460,40" style="stroke:var(--svg-red);stroke-dasharray:8 4"/>
          <text style="font:600 10px 'Source Sans 3',sans-serif;fill:var(--svg-red)" x="465" y="50">Actual</text>
          <!-- Labels for phases -->
          <text style="font:italic 9px 'Source Sans 3',sans-serif;fill:var(--svg-sub);text-anchor:middle" x="120" y="238">Slow Start</text>
          <text style="font:italic 9px 'Source Sans 3',sans-serif;fill:var(--svg-sub);text-anchor:middle" x="260" y="238">Peak Progress</text>
          <text style="font:italic 9px 'Source Sans 3',sans-serif;fill:var(--svg-sub);text-anchor:middle" x="400" y="238">Finishing</text>
          <text style="font:9px 'Source Sans 3',sans-serif;fill:var(--svg-sub)" x="65" y="35">100%</text>
          <text style="font:9px 'Source Sans 3',sans-serif;fill:var(--svg-sub)" x="65" y="215">0%</text>'''
    svgs['S-Curve'] = svg_wrap(scurve, 'Fig 6.3', 'S-Curve: Planned vs Actual Progress', 520, 260, 520, 260)
    
    # 4. Cash Flow diagram
    cashflow = f'''          <defs><style>
              .cf-ax{{stroke:var(--svg-hub);stroke-width:2}}
              .cf-bar{{stroke-width:1.5;opacity:.85}}
              .cf-lbl{{font:bold 10px 'Source Sans 3',sans-serif;fill:var(--svg-hub)}}
              .cf-mo{{font:9px 'Source Sans 3',sans-serif;fill:var(--svg-sub);text-anchor:middle}}
            </style></defs>
          <text style="font:bold 13px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="300" y="18">Contractor's Cash Flow Diagram</text>
          <line class="cf-ax" x1="60" y1="130" x2="560" y2="130"/>
          <text class="cf-lbl" x="25" y="70" transform="rotate(-90,25,70)">Inflow (+)</text>
          <text class="cf-lbl" x="25" y="180" transform="rotate(-90,25,180)">Outflow (&minus;)</text>
          <!-- Months -->
          <text class="cf-mo" x="100" y="145">M1</text><text class="cf-mo" x="160" y="145">M2</text>
          <text class="cf-mo" x="220" y="145">M3</text><text class="cf-mo" x="280" y="145">M4</text>
          <text class="cf-mo" x="340" y="145">M5</text><text class="cf-mo" x="400" y="145">M6</text>
          <text class="cf-mo" x="460" y="145">M7</text><text class="cf-mo" x="520" y="145">M8</text>
          <!-- Income bars (above line) -->
          <rect class="cf-bar" x="88" y="100" width="24" height="30" rx="2" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <rect class="cf-bar" x="148" y="80" width="24" height="50" rx="2" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <rect class="cf-bar" x="208" y="60" width="24" height="70" rx="2" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <rect class="cf-bar" x="268" y="45" width="24" height="85" rx="2" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <rect class="cf-bar" x="328" y="50" width="24" height="80" rx="2" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <rect class="cf-bar" x="388" y="65" width="24" height="65" rx="2" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <rect class="cf-bar" x="448" y="85" width="24" height="45" rx="2" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <rect class="cf-bar" x="508" y="105" width="24" height="25" rx="2" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <!-- Expense bars (below line) -->
          <rect class="cf-bar" x="88" y="130" width="24" height="50" rx="2" style="fill:var(--svg-red);stroke:var(--svg-red-s)"/>
          <rect class="cf-bar" x="148" y="130" width="24" height="60" rx="2" style="fill:var(--svg-red);stroke:var(--svg-red-s)"/>
          <rect class="cf-bar" x="208" y="130" width="24" height="65" rx="2" style="fill:var(--svg-red);stroke:var(--svg-red-s)"/>
          <rect class="cf-bar" x="268" y="130" width="24" height="70" rx="2" style="fill:var(--svg-red);stroke:var(--svg-red-s)"/>
          <rect class="cf-bar" x="328" y="130" width="24" height="60" rx="2" style="fill:var(--svg-red);stroke:var(--svg-red-s)"/>
          <rect class="cf-bar" x="388" y="130" width="24" height="45" rx="2" style="fill:var(--svg-red);stroke:var(--svg-red-s)"/>
          <rect class="cf-bar" x="448" y="130" width="24" height="30" rx="2" style="fill:var(--svg-red);stroke:var(--svg-red-s)"/>
          <rect class="cf-bar" x="508" y="130" width="24" height="15" rx="2" style="fill:var(--svg-red);stroke:var(--svg-red-s)"/>
          <!-- Legend -->
          <rect x="200" y="215" width="12" height="12" rx="2" style="fill:var(--svg-green)"/>
          <text style="font:10px 'Source Sans 3',sans-serif;fill:var(--svg-text)" x="218" y="226">Income (IPC Payments)</text>
          <rect x="370" y="215" width="12" height="12" rx="2" style="fill:var(--svg-red)"/>
          <text style="font:10px 'Source Sans 3',sans-serif;fill:var(--svg-text)" x="388" y="226">Expenditure (Materials, Labor)</text>'''
    svgs['Cash Flow Diagram'] = svg_wrap(cashflow, 'Fig 6.4', 'Contractor&rsquo;s Monthly Cash Flow: Income vs Expenditure', 580, 240, 580, 240)
    
    # 5. Site Survey checklist
    survey = hub_spoke_svg('sv', 'SITE', [
        ('Topography', 'Contours, levels'),
        ('Soil/Geology', 'Bearing capacity'),
        ('Access', 'Roads, bridges'),
        ('Utilities', 'Water, power supply'),
        ('Drainage', 'Flood level, rivers'),
        ('Climate', 'Rain, temperature'),
        ('Labor', 'Local availability'),
        ('Legal', 'Land ownership, EIA'),
    ], hub_sub='Survey', width=600, height=440)
    svgs['Site Surveying'] = svg_wrap(survey, 'Fig 6.5', 'Site Survey Checklist for Construction Projects', 600, 440)
    
    # 6. Balance Sheet structure
    bs_svg = f'''          <defs><style>
              .bs-box{{rx:8;ry:8;stroke-width:1.5;opacity:.92}}
              .bs-t{{font:bold 12px 'Source Sans 3',sans-serif;text-anchor:middle;fill:#fff}}
              .bs-item{{font:10px 'Source Sans 3',sans-serif;fill:var(--svg-text);text-anchor:start}}
            </style></defs>
          <text style="font:bold 14px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="280" y="20">Balance Sheet Structure</text>
          <!-- Assets side -->
          <rect class="bs-box" x="30" y="35" width="220" height="30" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text class="bs-t" x="140" y="55">ASSETS</text>
          <text class="bs-item" x="40" y="82">Fixed Assets (Land, Building)</text>
          <text class="bs-item" x="40" y="100">Current Assets (Cash, Stock)</text>
          <text class="bs-item" x="40" y="118">Receivables (Debtors)</text>
          <text class="bs-item" x="40" y="136">Bank Balance</text>
          <!-- Liabilities side -->
          <rect class="bs-box" x="310" y="35" width="220" height="30" style="fill:var(--svg-red);stroke:var(--svg-red-s)"/>
          <text class="bs-t" x="420" y="55">LIABILITIES</text>
          <text class="bs-item" x="320" y="82">Owner's Equity (Capital)</text>
          <text class="bs-item" x="320" y="100">Long-term Loans</text>
          <text class="bs-item" x="320" y="118">Current Liabilities (Creditors)</text>
          <text class="bs-item" x="320" y="136">Reserves &amp; Surplus</text>
          <!-- Equation -->
          <rect style="fill:var(--svg-green);stroke:var(--svg-green-s);stroke-width:2;rx:8;opacity:.9" x="100" y="150" width="360" height="30"/>
          <text style="font:bold 12px 'Source Sans 3',sans-serif;fill:var(--svg-text-green);text-anchor:middle" x="280" y="170">Assets = Liabilities + Owner&rsquo;s Equity</text>'''
    svgs['Balance Sheet'] = svg_wrap(bs_svg, 'Fig 6.6', 'Balance Sheet: Assets = Liabilities + Equity', 560, 190, 560, 190)
    
    # 7-10 more for ch6
    # 7. Financial Management functions
    fm_hub = hub_spoke_svg('fm', 'FINANCIAL', [
        ('Budgeting', 'Cost estimation'),
        ('Accounting', 'Record keeping'),
        ('Cash Flow', 'In/out monitoring'),
        ('Reporting', 'IPC, Final Bill'),
        ('Auditing', 'Verification'),
    ], hub_sub='Management', width=500, height=380)
    svgs['Financial Management'] = svg_wrap(fm_hub, 'Fig 6.7', 'Functions of Financial Management', 500, 380, 500, 380)
    
    # 8. Mobilization Advance effect
    mob_svg = f'''          <defs><style>
              .mb-box{{rx:10;ry:10;stroke-width:2;opacity:.92}}
              .mb-t{{font:bold 12px 'Source Sans 3',sans-serif;text-anchor:middle}}
              .mb-s{{font:10px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
            </style></defs>
          <rect class="mb-box" x="50" y="10" width="500" height="50" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text class="mb-t" x="300" y="30" style="fill:var(--svg-text-blue)">Mobilization Advance: 10-20% of Contract Amount</text>
          <text class="mb-s" x="300" y="48" style="fill:var(--svg-text-blue)">Given upfront &bull; Recovered by deducting from IPCs (usually 10-20% per bill)</text>
          <rect class="mb-box" x="50" y="70" width="240" height="40" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <text class="mb-s" x="170" y="92" style="fill:var(--svg-text-green)">&check; Helps contractor's cash flow</text>
          <rect class="mb-box" x="310" y="70" width="240" height="40" style="fill:var(--svg-orange);stroke:var(--svg-orange-s)"/>
          <text class="mb-s" x="430" y="92" style="fill:var(--svg-text-orange)">&check; Bank guarantee required</text>'''
    svgs['Effect of Mobilization Advance'] = svg_wrap(mob_svg, 'Fig 6.8', 'Mobilization Advance: Amount, Recovery &amp; Impact on Cash Flow', 600, 120, 600, 120)
    
    # 9. Cash flow components
    cfc = hub_spoke_svg('cfc', 'CASH FLOW', [
        ('Material Cost', '40-60% of total'),
        ('Labor Cost', '20-30%'),
        ('Equipment', '10-15%'),
        ('Overheads', '8-12%'),
        ('Profit Margin', '5-10%'),
    ], hub_sub='Components', width=500, height=380)
    svgs['Cash Flow Components'] = svg_wrap(cfc, 'Fig 6.9', 'Components of Contractor&rsquo;s Cash Flow', 500, 380, 500, 380)
    
    # 10. Site preparation steps
    sp_content, w, h = flow_svg('sp', [
        ('Clearing', 'Vegetation'),
        ('Grubbing', 'Roots/stumps'),
        ('Leveling', 'Cut &amp; fill'),
        ('Drainage', 'Temp system'),
        ('Fencing', 'Boundary'),
        ('Temp Roads', 'Access'),
    ], 'horizontal')
    svgs['Construction Site Preparation'] = svg_wrap(sp_content, 'Fig 6.10', 'Site Preparation Steps', w, h, w, h)
    
    return svgs

def get_ch7_svgs():
    svgs = {}
    
    # 1. Scope Control Process
    sc_content, w, h = flow_svg('wsc', [
        ('Define\nScope', ''),
        ('WBS', 'Breakdown'),
        ('Verify\nScope', ''),
        ('Control\nChanges', ''),
    ])
    svgs['Scope Control Processes'] = svg_wrap(sc_content, 'Fig 7.1', 'Project Scope Control Process', w, h, w, h)
    
    # 2. Labor Productivity Factors
    lp_hub = hub_spoke_svg('lp', 'LABOR', [
        ('Weather', 'Rain, heat, cold'),
        ('Supervision', 'Quality of foreman'),
        ('Material Supply', 'Timely availability'),
        ('Equipment', 'Proper tools'),
        ('Motivation', 'Wages, bonus'),
        ('Site Conditions', 'Access, congestion'),
        ('Worker Skill', 'Training level'),
        ('Work Hours', 'Overtime fatigue'),
    ], hub_sub='Productivity Factors', width=650, height=480)
    svgs['Factors Affecting Labor Productivity'] = svg_wrap(lp_hub, 'Fig 7.2', 'Factors Affecting Labor Productivity in Construction', 650, 480)
    
    # 3. Equipment Productivity formula
    ep_svg = f'''          <defs><style>
              .ep-box{{rx:10;ry:10;stroke-width:2;opacity:.92}}
              .ep-t{{font:bold 13px 'Source Sans 3',sans-serif;text-anchor:middle}}
              .ep-s{{font:11px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
            </style></defs>
          <rect class="ep-box" x="50" y="10" width="500" height="50" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text class="ep-t" x="300" y="30" style="fill:var(--svg-text-blue)">Equipment Productivity = Output / Time</text>
          <text class="ep-s" x="300" y="50" style="fill:var(--svg-text-blue)">Utilization Rate = Actual Working Hours / Available Hours &times; 100%</text>
          <rect class="ep-box" x="50" y="70" width="240" height="45" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <text class="ep-t" x="170" y="88" style="fill:var(--svg-text-green);font-size:11px">Idle Time Causes</text>
          <text class="ep-s" x="170" y="105" style="fill:var(--svg-text-green)">Breakdown, no fuel, rain, holidays</text>
          <rect class="ep-box" x="310" y="70" width="240" height="45" style="fill:var(--svg-orange);stroke:var(--svg-orange-s)"/>
          <text class="ep-t" x="430" y="88" style="fill:var(--svg-text-orange);font-size:11px">Target: &ge; 85% Utilization</text>
          <text class="ep-s" x="430" y="105" style="fill:var(--svg-text-orange)">Scheduled maintenance reduces breakdown</text>'''
    svgs['Equipment Productivity Accounting'] = svg_wrap(ep_svg, 'Fig 7.3', 'Equipment Productivity &amp; Utilization Rate', 600, 125, 600, 125)
    
    # 4. EVA Parameters
    eva_hub = hub_spoke_svg('eva', 'EVA', [
        ('PV / BCWS', 'Planned Value'),
        ('EV / BCWP', 'Earned Value'),
        ('AC / ACWP', 'Actual Cost'),
        ('SV', 'EV &minus; PV'),
        ('CV', 'EV &minus; AC'),
        ('SPI', 'EV / PV'),
        ('CPI', 'EV / AC'),
        ('EAC', 'BAC / CPI'),
    ], hub_sub='Parameters', width=650, height=480)
    svgs['What is EVA?'] = svg_wrap(eva_hub, 'Fig 7.4', 'Earned Value Analysis (EVA) &mdash; Key Parameters', 650, 480)
    
    # 5. EVA Status interpretation
    eva_status, w, h = comparison_table_svg('evs', 'EVA Status Interpretation', 'Condition', 'Meaning',
        [
            ('SV &gt; 0 (SPI &gt; 1)', 'Ahead of Schedule'),
            ('SV &lt; 0 (SPI &lt; 1)', 'Behind Schedule'),
            ('SV = 0 (SPI = 1)', 'On Schedule'),
            ('CV &gt; 0 (CPI &gt; 1)', 'Under Budget'),
            ('CV &lt; 0 (CPI &lt; 1)', 'Over Budget'),
            ('CV = 0 (CPI = 1)', 'On Budget'),
        ])
    svgs['Variance Formulae'] = svg_wrap(eva_status, 'Fig 7.5', 'EVA Variance &amp; Performance Index Interpretation', w, h, w, h)
    
    # 6. EVA Formulas
    evf_svg = f'''          <defs><style>
              .evf-box{{rx:8;ry:8;stroke-width:1.5;opacity:.92}}
              .evf-t{{font:bold 11px 'Source Sans 3',sans-serif;text-anchor:middle}}
              .evf-f{{font:bold 13px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-hub)}}
            </style></defs>
          <text style="font:bold 14px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="300" y="18">EVA Key Formulas</text>
          <rect class="evf-box" x="20" y="30" width="175" height="40" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text class="evf-t" x="107" y="45" style="fill:var(--svg-text-blue)">% Schedule</text>
          <text class="evf-f" x="107" y="62">EV / PV &times; 100</text>
          <rect class="evf-box" x="215" y="30" width="175" height="40" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <text class="evf-t" x="302" y="45" style="fill:var(--svg-text-green)">% Cost</text>
          <text class="evf-f" x="302" y="62">EV / AC &times; 100</text>
          <rect class="evf-box" x="410" y="30" width="175" height="40" style="fill:var(--svg-orange);stroke:var(--svg-orange-s)"/>
          <text class="evf-t" x="497" y="45" style="fill:var(--svg-text-orange)">EAC (Forecast)</text>
          <text class="evf-f" x="497" y="62">BAC / CPI</text>
          <rect class="evf-box" x="20" y="80" width="270" height="40" style="fill:var(--svg-red);stroke:var(--svg-red-s)"/>
          <text class="evf-t" x="155" y="95" style="fill:var(--svg-text-red)">ETC (Estimate to Complete)</text>
          <text class="evf-f" x="155" y="112">EAC &minus; AC</text>
          <rect class="evf-box" x="310" y="80" width="275" height="40" style="fill:var(--svg-purple);stroke:var(--svg-purple-s)"/>
          <text class="evf-t" x="447" y="95" style="fill:var(--svg-text-purple)">TCPI (To-Complete PI)</text>
          <text class="evf-f" x="447" y="112">(BAC &minus; EV) / (BAC &minus; AC)</text>'''
    svgs['Status in Percentage'] = svg_wrap(evf_svg, 'Fig 7.6', 'EVA: Schedule %, Cost %, EAC, ETC &amp; TCPI Formulas', 600, 130, 600, 130)
    
    # 7. Material Wastage causes diagram
    mw_content, w, h = comparison_table_svg('mwc', 'Material Wastage: Causes &amp; Remedies', 'Cause', 'Remedy',
        [
            ('Improper storage', 'Covered sheds, proper stacking'),
            ('Poor handling', 'Trained workers, equipment'),
            ('Over-ordering', 'Accurate BOQ, just-in-time'),
            ('Theft &amp; pilferage', 'Security, fencing, records'),
            ('Design changes', 'Freeze design early'),
            ('Wrong cutting', 'Templates, bar-bending schedule'),
        ])
    svgs['Causes and Remedies to Minimize Wastage'] = svg_wrap(mw_content, 'Fig 7.7', 'Material Wastage: Causes and Remedies', w, h, w, h)
    
    # 8. Quality Control Measures
    qc_hub = hub_spoke_svg('qc', 'QUALITY', [
        ('Inspection', 'Visual &amp; dimensional'),
        ('Testing', 'Lab &amp; field tests'),
        ('Standards', 'IS, BS, ASTM codes'),
        ('Documentation', 'Test reports, NCR'),
        ('Certification', 'Material certificates'),
    ], hub_sub='Control', width=500, height=380)
    svgs['Quality Control Measures'] = svg_wrap(qc_hub, 'Fig 7.8', 'Quality Control Measures in Construction', 500, 380, 500, 380)
    
    # 9. Bin Card format
    bin_svg = f'''          <defs><style>
              .bn-hdr{{font:bold 11px 'Source Sans 3',sans-serif;fill:#fff;text-anchor:middle}}
              .bn-cell{{font:10px 'Source Sans 3',sans-serif;fill:var(--svg-text);text-anchor:middle}}
              .bn-line{{stroke:var(--svg-sub);stroke-width:0.5}}
            </style></defs>
          <text style="font:bold 13px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="280" y="18">Bin Card Format (Material Stock Record)</text>
          <rect x="30" y="25" width="500" height="30" rx="4" style="fill:var(--svg-blue);opacity:.9"/>
          <text class="bn-hdr" x="80" y="45">Date</text>
          <text class="bn-hdr" x="170" y="45">Received</text>
          <text class="bn-hdr" x="280" y="45">Issued</text>
          <text class="bn-hdr" x="380" y="45">Balance</text>
          <text class="bn-hdr" x="480" y="45">Remarks</text>
          <rect x="30" y="55" width="500" height="25" style="fill:var(--svg-sub);opacity:.08"/>
          <text class="bn-cell" x="80" y="72">Day 1</text><text class="bn-cell" x="170" y="72">100 bags</text>
          <text class="bn-cell" x="280" y="72">&mdash;</text><text class="bn-cell" x="380" y="72">100</text>
          <text class="bn-cell" x="480" y="72">Opening</text>
          <text class="bn-cell" x="80" y="97">Day 3</text><text class="bn-cell" x="170" y="97">&mdash;</text>
          <text class="bn-cell" x="280" y="97">30 bags</text><text class="bn-cell" x="380" y="97">70</text>
          <text class="bn-cell" x="480" y="97">Foundation</text>
          <rect x="30" y="105" width="500" height="25" style="fill:var(--svg-sub);opacity:.08"/>
          <text class="bn-cell" x="80" y="122">Day 5</text><text class="bn-cell" x="170" y="122">50 bags</text>
          <text class="bn-cell" x="280" y="122">&mdash;</text><text class="bn-cell" x="380" y="122">120</text>
          <text class="bn-cell" x="480" y="122">Replenished</text>'''
    svgs['Materials Stock Accounting'] = svg_wrap(bin_svg, 'Fig 7.9', 'Bin Card: Material Stock Record Format', 560, 140, 560, 140)
    
    # 10. Scope Control System
    scs = hub_spoke_svg('scs', 'SCOPE', [
        ('WBS', 'Work Breakdown Structure'),
        ('Baseline', 'Approved scope statement'),
        ('Change Control', 'Formal process'),
        ('Verification', 'Deliverable acceptance'),
    ], hub_sub='Control System', width=500, height=360)
    svgs['Project Scope Control System'] = svg_wrap(scs, 'Fig 7.10', 'Project Scope Control System Components', 500, 360, 500, 360)
    
    return svgs

def get_ch8_svgs():
    svgs = {}
    
    # 1. Site Engineer Responsibilities
    se_hub = hub_spoke_svg('se', 'SITE', [
        ('Quality Control', 'Testing, inspection'),
        ('Progress Monitor', 'Daily reports'),
        ('Measurement', 'MB entries, bills'),
        ('Coordination', 'Subcontractors, labor'),
        ('Safety', 'PPE, training'),
        ('Records', 'Logs, site order book'),
    ], hub_sub='Engineer', width=550, height=400)
    svgs['Roles and Responsibilities'] = svg_wrap(se_hub, 'Fig 8.1', 'Site Engineer: Key Roles &amp; Responsibilities', 550, 400, 550, 400)
    
    # 2. Record Keeping flow
    rk_content, w, h = flow_svg('rk', [
        ('Site Diary', 'Daily'),
        ('Weather\nLog', 'Daily'),
        ('Material\nRegister', 'On receipt'),
        ('MB Entry', 'On work done'),
        ('Running\nBill', 'Monthly'),
        ('Final\nBill', 'Completion'),
    ], 'horizontal')
    svgs['Types of Documentation'] = svg_wrap(rk_content, 'Fig 8.2', 'Site Documentation Types &amp; Frequency', w, h, w, h)
    
    # 3. Site Order Book
    sob = f'''          <defs><style>
              .so-hdr{{font:bold 11px 'Source Sans 3',sans-serif;fill:#fff;text-anchor:middle}}
              .so-cell{{font:10px 'Source Sans 3',sans-serif;fill:var(--svg-text);text-anchor:start}}
            </style></defs>
          <text style="font:bold 13px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="280" y="18">Site Order Book Format</text>
          <rect x="30" y="25" width="500" height="28" rx="4" style="fill:var(--svg-blue);opacity:.9"/>
          <text class="so-hdr" x="70" y="44">S.N.</text>
          <text class="so-hdr" x="140" y="44">Date</text>
          <text class="so-hdr" x="280" y="44">Description of Order / Instruction</text>
          <text class="so-hdr" x="475" y="44">Signature</text>
          <text class="so-cell" x="60" y="72">1</text><text class="so-cell" x="120" y="72">2082/01/15</text>
          <text class="so-cell" x="190" y="72">Stop concreting until cube test results arrive</text>
          <text class="so-cell" x="460" y="72">Eng.</text>
          <rect x="30" y="80" width="500" height="25" style="fill:var(--svg-sub);opacity:.08"/>
          <text class="so-cell" x="60" y="97">2</text><text class="so-cell" x="120" y="97">2082/01/18</text>
          <text class="so-cell" x="190" y="97">Increase formwork support spacing to 900mm c/c</text>
          <text class="so-cell" x="460" y="97">Eng.</text>'''
    svgs['Site Order Book'] = svg_wrap(sob, 'Fig 8.3', 'Site Order Book: Format &amp; Sample Entries', 560, 115, 560, 115)
    
    # 4. Measurement Book format
    mb = f'''          <defs><style>
              .mb-hdr{{font:bold 10px 'Source Sans 3',sans-serif;fill:#fff;text-anchor:middle}}
              .mb-cell{{font:9.5px 'Source Sans 3',sans-serif;fill:var(--svg-text);text-anchor:middle}}
            </style></defs>
          <text style="font:bold 13px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="290" y="18">Measurement Book (MB) Format</text>
          <rect x="20" y="25" width="540" height="28" rx="4" style="fill:var(--svg-green);opacity:.9"/>
          <text class="mb-hdr" x="50" y="43">S.N.</text>
          <text class="mb-hdr" x="140" y="43">Description</text>
          <text class="mb-hdr" x="260" y="43">No.</text>
          <text class="mb-hdr" x="310" y="43">L (m)</text>
          <text class="mb-hdr" x="360" y="43">B (m)</text>
          <text class="mb-hdr" x="410" y="43">H/D (m)</text>
          <text class="mb-hdr" x="470" y="43">Quantity</text>
          <text class="mb-hdr" x="535" y="43">Unit</text>
          <text class="mb-cell" x="50" y="70">1</text><text class="mb-cell" x="140" y="70">Earthwork</text>
          <text class="mb-cell" x="260" y="70">1</text><text class="mb-cell" x="310" y="70">10</text>
          <text class="mb-cell" x="360" y="70">5</text><text class="mb-cell" x="410" y="70">1.5</text>
          <text class="mb-cell" x="470" y="70">75</text><text class="mb-cell" x="535" y="70">m&sup3;</text>
          <rect x="20" y="78" width="540" height="22" style="fill:var(--svg-sub);opacity:.08"/>
          <text class="mb-cell" x="50" y="93">2</text><text class="mb-cell" x="140" y="93">RCC M20</text>
          <text class="mb-cell" x="260" y="93">1</text><text class="mb-cell" x="310" y="93">8</text>
          <text class="mb-cell" x="360" y="93">4</text><text class="mb-cell" x="410" y="93">0.3</text>
          <text class="mb-cell" x="470" y="93">9.6</text><text class="mb-cell" x="535" y="93">m&sup3;</text>'''
    svgs['MB Sample Format'] = svg_wrap(mb, 'Fig 8.4', 'Measurement Book: Sample Format', 580, 110, 580, 110)
    
    # 5. Muster Roll format
    muster = f'''          <defs><style>
              .mr-hdr{{font:bold 10px 'Source Sans 3',sans-serif;fill:#fff;text-anchor:middle}}
              .mr-cell{{font:9.5px 'Source Sans 3',sans-serif;fill:var(--svg-text);text-anchor:middle}}
            </style></defs>
          <text style="font:bold 13px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="290" y="18">Muster Roll Format</text>
          <rect x="20" y="25" width="540" height="28" rx="4" style="fill:var(--svg-orange);opacity:.9"/>
          <text class="mr-hdr" x="50" y="43">S.N.</text>
          <text class="mr-hdr" x="130" y="43">Name</text>
          <text class="mr-hdr" x="220" y="43">Trade</text>
          <text class="mr-hdr" x="290" y="43">Daily Rate</text>
          <text class="mr-hdr" x="360" y="43">Days</text>
          <text class="mr-hdr" x="430" y="43">OT Hrs</text>
          <text class="mr-hdr" x="510" y="43">Total Pay</text>
          <text class="mr-cell" x="50" y="68">1</text><text class="mr-cell" x="130" y="68">Ram B.</text>
          <text class="mr-cell" x="220" y="68">Mason</text><text class="mr-cell" x="290" y="68">Rs 800</text>
          <text class="mr-cell" x="360" y="68">26</text><text class="mr-cell" x="430" y="68">12</text>
          <text class="mr-cell" x="510" y="68">Rs 22,000</text>
          <rect x="20" y="76" width="540" height="22" style="fill:var(--svg-sub);opacity:.08"/>
          <text class="mr-cell" x="50" y="91">2</text><text class="mr-cell" x="130" y="91">Hari K.</text>
          <text class="mr-cell" x="220" y="91">Helper</text><text class="mr-cell" x="290" y="91">Rs 500</text>
          <text class="mr-cell" x="360" y="91">26</text><text class="mr-cell" x="430" y="91">0</text>
          <text class="mr-cell" x="510" y="91">Rs 13,000</text>'''
    svgs['Muster Roll Contents'] = svg_wrap(muster, 'Fig 8.5', 'Muster Roll: Daily Labor Payment Record', 580, 108, 580, 108)
    
    # 6. Bill preparation steps
    bill_content, w, h = flow_svg('bil', [
        ('Measure\nWork', 'MB entry'),
        ('Abstract\nof Cost', ''),
        ('Check &amp;\nVerify', 'Engineer'),
        ('Bill\nPrep', 'Format'),
        ('Submit\nto Client', ''),
        ('IPC\nIssued', 'Payment'),
    ], 'horizontal')
    svgs['Steps for Preparing Bills'] = svg_wrap(bill_content, 'Fig 8.6', 'Steps for Preparing Running Bills / IPC', w, h, w, h)
    
    # 7-10: Supervision and monitoring
    sup_hub = hub_spoke_svg('sup', 'SUPERVISION', [
        ('Quality Check', 'Tests, inspections'),
        ('Progress Track', 'Bar chart update'),
        ('Resource Monitor', 'Labor, material'),
        ('Safety Watch', 'Hazard prevention'),
        ('Cost Control', 'Budget vs actual'),
    ], hub_sub='Functions', width=500, height=380)
    svgs['Monitoring and Progress Controls'] = svg_wrap(sup_hub, 'Fig 8.7', 'Supervision: Monitoring &amp; Progress Control Functions', 500, 380, 500, 380)
    
    admin = hub_spoke_svg('adm', 'ADMIN', [
        ('Correspondence', 'Letters, notices'),
        ('Meeting Minutes', 'Progress meetings'),
        ('Variation Orders', 'Scope changes'),
        ('Claims', 'EOT, cost claims'),
        ('Reports', 'Monthly/weekly'),
    ], hub_sub='Functions', width=500, height=380)
    svgs['Administrative Functions'] = svg_wrap(admin, 'Fig 8.8', 'Administrative Functions of Site Engineer', 500, 380, 500, 380)
    
    contr_sup = hub_spoke_svg('csup', "CONTRACTOR'S", [
        ('Project Manager', 'Overall coordination'),
        ('Site Engineer', 'Technical supervision'),
        ('Quantity Surveyor', 'Bills, measurement'),
        ('Foreman', 'Labor supervision'),
        ('Safety Officer', 'HSE management'),
        ('Store Keeper', 'Material management'),
    ], hub_sub='Team', width=550, height=400)
    svgs['Supervision Team'] = svg_wrap(contr_sup, 'Fig 8.9', "Contractor's Site Supervision Team", 550, 400, 550, 400)
    
    delay_hub = hub_spoke_svg('dly', 'DELAY', [
        ('Rain/Weather', 'Force majeure'),
        ('Material Shortage', 'Supply chain'),
        ('Design Change', 'Client variation'),
        ('Labor Strike', 'Industrial action'),
        ('Payment Delay', 'Cash flow impact'),
    ], hub_sub='Causes', width=500, height=380)
    svgs['During Construction Period'] = svg_wrap(delay_hub, 'Fig 8.10', 'Common Causes of Construction Delays', 500, 380, 500, 380)
    
    return svgs

def get_ch9_svgs():
    svgs = {}
    
    maint_types = hub_spoke_svg('mt', 'MAINTENANCE', [
        ('Preventive', 'Scheduled, planned'),
        ('Corrective', 'After failure/damage'),
        ('Predictive', 'Condition monitoring'),
        ('Emergency', 'Urgent, unplanned'),
        ('Routine', 'Daily cleaning, oiling'),
    ], hub_sub='Types', width=500, height=380)
    svgs['Types of Maintenance'] = svg_wrap(maint_types, 'Fig 9.1', 'Types of Maintenance in Construction', 500, 380, 500, 380)
    
    maint_plan, w, h = flow_svg('mp', [
        ('Identify\nNeeds', ''),
        ('Set\nPriority', ''),
        ('Schedule\nWork', ''),
        ('Allocate\nResources', ''),
        ('Execute', ''),
        ('Record &amp;\nReview', ''),
    ], 'horizontal')
    svgs['Maintenance Planning'] = svg_wrap(maint_plan, 'Fig 9.2', 'Maintenance Planning Process Flow', w, h, w, h)
    
    prev_corr, w, h = comparison_table_svg('pvc', 'Preventive vs Corrective Maintenance', 'Preventive', 'Corrective',
        [
            ('Before failure occurs', 'After failure occurs'),
            ('Scheduled &amp; planned', 'Unscheduled, reactive'),
            ('Lower long-term cost', 'Higher repair cost'),
            ('Reduces downtime', 'Causes downtime'),
            ('Extends equipment life', 'May shorten life'),
            ('Needs regular inspection', 'Needs emergency response'),
        ])
    svgs['Preventive vs Corrective'] = svg_wrap(prev_corr, 'Fig 9.3', 'Preventive vs Corrective Maintenance Comparison', w, h, w, h)
    
    maint_obj = hub_spoke_svg('mo', 'MAINTENANCE', [
        ('Safety', 'Protect users'),
        ('Functionality', 'Keep working'),
        ('Economy', 'Minimize cost'),
        ('Appearance', 'Aesthetics'),
        ('Value', 'Preserve asset value'),
        ('Life Extension', 'Durability'),
    ], hub_sub='Objectives', width=500, height=380)
    svgs['Objectives of Maintenance'] = svg_wrap(maint_obj, 'Fig 9.4', 'Objectives of Construction Maintenance', 500, 380, 500, 380)
    
    sched_tech = hub_spoke_svg('st', 'SCHEDULING', [
        ('Calendar', 'Fixed intervals'),
        ('Condition-Based', 'Monitor &amp; trigger'),
        ('Priority', 'Rank by importance'),
        ('Backlog', 'Pending work queue'),
    ], hub_sub='Techniques', width=450, height=340)
    svgs['Scheduling Techniques'] = svg_wrap(sched_tech, 'Fig 9.5', 'Maintenance Scheduling Techniques', 450, 340, 450, 340)
    
    plan_levels, w, h = flow_svg('plv', [
        ('Long-term', '5-10 years'),
        ('Annual', 'Yearly budget'),
        ('Monthly', 'Work orders'),
        ('Weekly', 'Crew tasks'),
        ('Daily', 'Execution'),
    ], 'horizontal')
    svgs['Levels of Planning Process'] = svg_wrap(plan_levels, 'Fig 9.6', 'Levels of Maintenance Planning', w, h, w, h)
    
    maint_basics = hub_spoke_svg('mb2', 'WHY', [
        ('Deterioration', 'Wear &amp; tear over time'),
        ('Weather Damage', 'Rain, sun, frost'),
        ('Usage Damage', 'Traffic, loads'),
        ('Defective Work', 'Original construction'),
        ('Accidents', 'Fire, earthquake'),
    ], hub_sub='Maintenance?', width=500, height=380)
    svgs['Why Maintenance is Needed'] = svg_wrap(maint_basics, 'Fig 9.7', 'Why Maintenance is Needed', 500, 380, 500, 380)
    
    planned_types = f'''          <defs><style>
              .pt-box{{rx:8;ry:8;stroke-width:1.5;opacity:.92}}
              .pt-t{{font:bold 11px 'Source Sans 3',sans-serif;text-anchor:middle}}
              .pt-s{{font:10px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
            </style></defs>
          <text style="font:bold 14px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="300" y="20">Planned Maintenance Breakdown</text>
          <rect class="pt-box" x="175" y="30" width="250" height="35" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text class="pt-t" x="300" y="52" style="fill:var(--svg-text-blue)">Planned Maintenance</text>
          <line style="stroke:var(--svg-hub);stroke-width:1.5" x1="200" y1="65" x2="200" y2="85"/>
          <line style="stroke:var(--svg-hub);stroke-width:1.5" x1="400" y1="65" x2="400" y2="85"/>
          <rect class="pt-box" x="100" y="85" width="200" height="35" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <text class="pt-t" x="200" y="107" style="fill:var(--svg-text-green)">Preventive</text>
          <rect class="pt-box" x="320" y="85" width="200" height="35" style="fill:var(--svg-orange);stroke:var(--svg-orange-s)"/>
          <text class="pt-t" x="420" y="107" style="fill:var(--svg-text-orange)">Corrective</text>
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="140" y1="120" x2="140" y2="135"/>
          <line style="stroke:var(--svg-hub);stroke-width:1" x1="260" y1="120" x2="260" y2="135"/>
          <rect class="pt-box" x="60" y="135" width="160" height="30" style="fill:var(--svg-teal);stroke:var(--svg-teal-s)"/>
          <text class="pt-s" x="140" y="155" style="fill:var(--svg-text-teal)">Time-Based (Scheduled)</text>
          <rect class="pt-box" x="240" y="135" width="160" height="30" style="fill:var(--svg-pink);stroke:var(--svg-pink-s)"/>
          <text class="pt-s" x="320" y="155" style="fill:var(--svg-text-pink)">Condition-Based</text>'''
    svgs['1. Planned Maintenance'] = svg_wrap(planned_types, 'Fig 9.8', 'Planned Maintenance Classification Tree', 600, 175, 600, 175)
    
    planning_proc, w, h = flow_svg('pp', [
        ('Survey\nCondition', ''),
        ('Identify\nDefects', ''),
        ('Prioritize', 'Urgency'),
        ('Estimate\nCost', ''),
        ('Schedule', 'Timeline'),
        ('Execute &amp;\nMonitor', ''),
    ], 'horizontal')
    svgs['Planning Procedures'] = svg_wrap(planning_proc, 'Fig 9.9', 'Maintenance Planning Procedure Steps', w, h, w, h)
    
    maint_needs = f'''          <defs><style>
              .mn-box{{rx:10;ry:10;stroke-width:2;opacity:.92}}
              .mn-t{{font:bold 12px 'Source Sans 3',sans-serif;text-anchor:middle}}
              .mn-s{{font:10px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
            </style></defs>
          <rect class="mn-box" x="50" y="10" width="500" height="50" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <text class="mn-t" x="300" y="32" style="fill:var(--svg-text-green)">Maintenance = Preservation + Restoration</text>
          <text class="mn-s" x="300" y="50" style="fill:var(--svg-text-green)">Keeping structure serviceable &bull; Restoring to acceptable standard</text>'''
    svgs['Maintenance Basics'] = svg_wrap(maint_needs, 'Fig 9.10', 'Maintenance: Preservation &amp; Restoration', 600, 70, 600, 70)
    
    return svgs

def get_ch10_svgs():
    svgs = {}
    
    fayol = hub_spoke_svg('fy', "FAYOL'S", [
        ('Division of Work', 'Specialization'),
        ('Authority', 'Right to command'),
        ('Discipline', 'Obedience, respect'),
        ('Unity of Command', 'One boss'),
        ('Unity of Direction', 'One plan'),
        ('Subordination', 'Org &gt; individual'),
        ('Remuneration', 'Fair pay'),
        ('Centralization', 'Balance of power'),
        ('Scalar Chain', 'Hierarchy'),
        ('Order', 'Right place'),
        ('Equity', 'Fairness'),
        ('Stability', 'Low turnover'),
        ('Initiative', 'Encourage ideas'),
        ('Esprit de Corps', 'Team spirit'),
    ], hub_sub='14 Principles', width=700, height=550)
    svgs["Fayol's 14 Principles"] = svg_wrap(fayol, 'Fig 10.1', "Fayol's 14 Principles of Administrative Management", 700, 550)
    
    cent_dec, w, h = comparison_table_svg('cd', 'Centralization vs Decentralization', 'Centralization', 'Decentralization',
        [
            ('Decision at top level', 'Decision at lower levels'),
            ('Uniformity in action', 'Flexibility in action'),
            ('Small organizations', 'Large organizations'),
            ('Less autonomy', 'More autonomy'),
            ('Faster in crisis', 'Faster routine decisions'),
            ('Tight control', 'Motivation &amp; development'),
        ])
    svgs['Centralization'] = svg_wrap(cent_dec, 'Fig 10.2', 'Centralization vs Decentralization', w, h, w, h)
    
    lead_types = hub_spoke_svg('ld', 'LEADERSHIP', [
        ('Autocratic', 'Dictates, controls'),
        ('Democratic', 'Participative, team'),
        ('Laissez-faire', 'Hands-off, delegates'),
        ('Bureaucratic', 'By rules &amp; procedures'),
        ('Transformational', 'Inspires change'),
    ], hub_sub='Styles', width=550, height=400)
    svgs['Types of Leadership Styles'] = svg_wrap(lead_types, 'Fig 10.3', 'Types of Leadership Styles in Management', 550, 400, 550, 400)
    
    maslow = f'''          <defs><style>
              .msl-t{{font:bold 11px 'Source Sans 3',sans-serif;fill:#fff;text-anchor:middle}}
              .msl-s{{font:9px 'Source Sans 3',sans-serif;fill:var(--svg-sub);text-anchor:middle}}
            </style></defs>
          <text style="font:bold 14px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="300" y="18">Maslow's Hierarchy of Needs</text>
          <polygon points="300,30 500,260 100,260" style="fill:none;stroke:var(--svg-hub);stroke-width:1;opacity:.2"/>
          <rect rx="4" x="250" y="35" width="100" height="30" style="fill:var(--svg-purple);stroke:var(--svg-purple-s);opacity:.9"/>
          <text class="msl-t" x="300" y="55">Self-Actual.</text>
          <rect rx="4" x="220" y="75" width="160" height="30" style="fill:var(--svg-blue);stroke:var(--svg-blue-s);opacity:.9"/>
          <text class="msl-t" x="300" y="95">Esteem Needs</text>
          <rect rx="4" x="190" y="115" width="220" height="30" style="fill:var(--svg-green);stroke:var(--svg-green-s);opacity:.9"/>
          <text class="msl-t" x="300" y="135">Social / Belonging</text>
          <rect rx="4" x="160" y="155" width="280" height="30" style="fill:var(--svg-orange);stroke:var(--svg-orange-s);opacity:.9"/>
          <text class="msl-t" x="300" y="175">Safety &amp; Security</text>
          <rect rx="4" x="130" y="195" width="340" height="30" style="fill:var(--svg-red);stroke:var(--svg-red-s);opacity:.9"/>
          <text class="msl-t" x="300" y="215">Physiological (Food, Shelter, Water)</text>
          <text class="msl-s" x="300" y="250">Lower needs must be satisfied before higher needs motivate</text>'''
    svgs['Content Theories of Motivation'] = svg_wrap(maslow, 'Fig 10.4', "Maslow's Hierarchy of Needs (Motivation Theory)", 600, 260, 600, 260)
    
    herzberg, w, h = comparison_table_svg('hz', "Herzberg's Two-Factor Theory", 'Hygiene Factors (Dissatisfiers)', 'Motivators (Satisfiers)',
        [
            ('Salary / Wages', 'Achievement'),
            ('Working conditions', 'Recognition'),
            ('Company policy', 'Work itself'),
            ('Supervision quality', 'Responsibility'),
            ('Job security', 'Advancement'),
            ('Interpersonal relations', 'Growth'),
        ])
    svgs['B. Process Theories of Motivation'] = svg_wrap(herzberg, 'Fig 10.5', "Herzberg's Two-Factor Theory of Motivation", w, h, w, h)
    
    decision, w, h = flow_svg('dec', [
        ('Identify\nProblem', ''),
        ('Gather\nInfo', ''),
        ('Generate\nOptions', ''),
        ('Evaluate\nOptions', ''),
        ('Select\nBest', ''),
        ('Implement', ''),
        ('Review', ''),
    ], 'horizontal')
    svgs['Decision Making'] = svg_wrap(decision, 'Fig 10.6', 'Decision Making Process Steps', w, h, w, h)
    
    comm_process, w, h = flow_svg('com', [
        ('Sender', 'Encodes'),
        ('Message', 'Info content'),
        ('Channel', 'Medium'),
        ('Receiver', 'Decodes'),
        ('Feedback', 'Response'),
    ])
    svgs['Communication Process'] = svg_wrap(comm_process, 'Fig 10.7', 'Communication Process: Sender to Feedback', w, h, w, h)
    
    comm_barriers = hub_spoke_svg('cb', 'COMMUNICATION', [
        ('Language', 'Technical jargon'),
        ('Noise', 'Physical disturbance'),
        ('Distance', 'Remote sites'),
        ('Emotions', 'Anger, fear, bias'),
        ('Cultural', 'Different backgrounds'),
        ('Overload', 'Too much information'),
    ], hub_sub='Barriers', width=550, height=400)
    svgs['Barriers to Communication'] = svg_wrap(comm_barriers, 'Fig 10.8', 'Barriers to Effective Communication', 550, 400, 550, 400)
    
    admin_mgmt, w, h = comparison_table_svg('am', 'Administration vs Management', 'Administration', 'Management',
        [
            ('Policy making', 'Policy implementing'),
            ('Top-level function', 'Middle/lower-level'),
            ('What should be done', 'How it should be done'),
            ('Legislative function', 'Executive function'),
            ('Determines objectives', 'Achieves objectives'),
        ])
    svgs['Difference between Administration'] = svg_wrap(admin_mgmt, 'Fig 10.9', 'Difference between Administration and Management', w, h, w, h)
    
    recruit, w, h = flow_svg('rec', [
        ('Job\nAnalysis', ''),
        ('Advertise', 'Notice'),
        ('Screen\nApplications', ''),
        ('Tests &amp;\nInterview', ''),
        ('Select', 'Offer'),
        ('Train &amp;\nInduct', ''),
    ], 'horizontal')
    svgs['Recruitment'] = svg_wrap(recruit, 'Fig 10.10', 'Recruitment &amp; Selection Process Flow', w, h, w, h)
    
    return svgs

def get_ch11_svgs():
    svgs = {}
    
    accident_causes = hub_spoke_svg('ac', 'ACCIDENT', [
        ('Unsafe Acts', 'Carelessness, shortcuts'),
        ('Unsafe Conditions', 'Faulty equipment'),
        ('Lack of Training', 'Unskilled workers'),
        ('No PPE', 'Missing helmets, boots'),
        ('Poor Housekeeping', 'Cluttered workspace'),
        ('Fatigue', 'Long hours, stress'),
    ], hub_sub='Causes', width=550, height=400)
    svgs['Causes of Accidents'] = svg_wrap(accident_causes, 'Fig 11.1', 'Causes of Construction Accidents', 550, 400, 550, 400)
    
    safety_measures = hub_spoke_svg('sm', 'SAFETY', [
        ('PPE', 'Helmet, boots, gloves'),
        ('Training', 'Toolbox talks'),
        ('Signage', 'Warning boards'),
        ('Fencing', 'Barricades, nets'),
        ('First Aid', 'Emergency kits'),
        ('Inspection', 'Regular audits'),
        ('Reporting', 'Incident records'),
    ], hub_sub='Measures', width=600, height=440)
    svgs['Safety Measures in Construction'] = svg_wrap(safety_measures, 'Fig 11.2', 'Safety Measures in Construction Sites', 600, 440)
    
    fire_types, w, h = comparison_table_svg('ft', 'Fire Classifications &amp; Extinguishers', 'Fire Class', 'Type &amp; Extinguisher',
        [
            ('Class A', 'Solid materials (wood, paper) &mdash; Water'),
            ('Class B', 'Flammable liquids &mdash; Foam / CO2'),
            ('Class C', 'Flammable gases &mdash; Dry powder'),
            ('Class D', 'Metals (Mg, Na) &mdash; Special powder'),
            ('Class E/F', 'Electrical / Cooking oil &mdash; CO2 / Wet chemical'),
        ])
    svgs['Fire Safety'] = svg_wrap(fire_types, 'Fig 11.3', 'Fire Classifications &amp; Appropriate Extinguishers', w, h, w, h)
    
    insurance = hub_spoke_svg('ins', 'INSURANCE', [
        ("Contractor's All Risk", 'CAR - covers works'),
        ('Third Party', 'Public liability'),
        ("Workmen's Comp", 'Injury/death'),
        ('Equipment', 'Plant &amp; machinery'),
        ('Professional', 'Consultant liability'),
        ('Performance Bond', 'Guarantee of completion'),
    ], hub_sub='Types', width=550, height=400)
    svgs['Insurance'] = svg_wrap(insurance, 'Fig 11.4', 'Types of Insurance in Construction', 550, 400, 550, 400)
    
    eia_content, w, h = flow_svg('eia', [
        ('Screening', 'Need EIA?'),
        ('Scoping', 'Key issues'),
        ('Impact\nStudy', 'Assess'),
        ('Mitigation', 'Reduce'),
        ('Public\nReview', 'Comment'),
        ('Decision', 'Approve/\nReject'),
        ('Monitor', 'Compliance'),
    ], 'horizontal')
    svgs['Environmental Law'] = svg_wrap(eia_content, 'Fig 11.5', 'EIA Process: Screening to Monitoring', w, h, w, h)
    
    nbc = hub_spoke_svg('nbc', 'NBC', [
        ('Mandatory', 'Minimum standards'),
        ('Deemed-to-Satisfy', 'Prescriptive rules'),
        ('Guidelines', 'Recommendations'),
        ('Commentary', 'Explanations'),
    ], hub_sub='4 Levels', width=450, height=340)
    svgs['Four Levels of NBC'] = svg_wrap(nbc, 'Fig 11.6', 'Four Levels of National Building Code', 450, 340, 450, 340)
    
    acc_class = hub_spoke_svg('acl', 'ACCIDENT', [
        ('Fatal', 'Causes death'),
        ('Major Injury', 'Fracture, amputation'),
        ('Minor Injury', 'Cut, bruise, sprain'),
        ('Near Miss', 'Could have caused injury'),
        ('Property Damage', 'Equipment, structure'),
    ], hub_sub='Classification', width=500, height=380)
    svgs['Classification of Accidents'] = svg_wrap(acc_class, 'Fig 11.7', 'Classification of Construction Accidents by Severity', 500, 380, 500, 380)
    
    safety_approach, w, h = flow_svg('sa', [
        ('Identify\nHazards', ''),
        ('Assess\nRisk', ''),
        ('Control\nMeasures', ''),
        ('Implement', ''),
        ('Monitor\n&amp; Review', ''),
    ])
    svgs['Approach to Improve Safety'] = svg_wrap(safety_approach, 'Fig 11.8', 'Approach to Improve Construction Safety', w, h, w, h)
    
    ppe_hub = hub_spoke_svg('ppe', 'PPE', [
        ('Hard Hat', 'Head protection'),
        ('Safety Boots', 'Foot protection'),
        ('Gloves', 'Hand protection'),
        ('Hi-Vis Vest', 'Visibility'),
        ('Eye Protection', 'Goggles/glasses'),
        ('Ear Plugs', 'Noise protection'),
        ('Harness', 'Fall protection'),
        ('Mask', 'Dust/fume protection'),
    ], hub_sub='Equipment', width=600, height=440)
    svgs['Safety Requirement'] = svg_wrap(ppe_hub, 'Fig 11.9', 'Personal Protective Equipment (PPE) Types', 600, 440)
    
    factors = hub_spoke_svg('sfact', 'FACTORS', [
        ('Management', 'Policy, commitment'),
        ('Workers', 'Attitude, training'),
        ('Environment', 'Site conditions'),
        ('Equipment', 'Maintenance, guards'),
        ('Method', 'Safe procedures'),
    ], hub_sub='Influencing Safety', width=500, height=380)
    svgs['Factors Influencing Safety'] = svg_wrap(factors, 'Fig 11.10', 'Factors Influencing Construction Safety', 500, 380, 500, 380)
    
    return svgs

def get_ch12_svgs():
    svgs = {}
    
    spec_types = hub_spoke_svg('spt', 'SPECIFICATION', [
        ('Contract Spec', 'Project-specific'),
        ('Standard Spec', 'IS, BS, ASTM'),
        ('Performance Spec', 'End result oriented'),
        ("Manufacturer's", 'Product datasheet'),
    ], hub_sub='Types', width=500, height=360)
    svgs['Types of Specifications'] = svg_wrap(spec_types, 'Fig 12.1', 'Types of Specifications in Construction', 500, 360, 500, 360)
    
    spec_purpose = hub_spoke_svg('spp', 'PURPOSE', [
        ('Quality Control', 'Define standards'),
        ('Fair Bidding', 'Equal comparison'),
        ('Dispute Prevention', 'Clear expectations'),
        ('Cost Estimation', 'Material &amp; workmanship'),
        ('Contract Compliance', 'Legal basis'),
    ], hub_sub='of Specifications', width=500, height=380)
    svgs['Purpose of Specification'] = svg_wrap(spec_purpose, 'Fig 12.2', 'Purpose of Specifications in Construction', 500, 380, 500, 380)
    
    spec_importance = hub_spoke_svg('spi', 'IMPORTANCE', [
        ('Basis of Contract', 'Legal document'),
        ('Quality Assurance', 'Material + workmanship'),
        ('Avoid Ambiguity', 'Clear instructions'),
        ('Cost Control', 'Prevent extras'),
        ('Standard Reference', 'IS/BS codes'),
    ], hub_sub='of Specification', width=500, height=380)
    svgs['Importance of Specifications'] = svg_wrap(spec_importance, 'Fig 12.3', 'Importance of Specifications', 500, 380, 500, 380)
    
    writing, w, h = flow_svg('sw', [
        ('Study\nDrawings', ''),
        ('Define\nMaterials', ''),
        ('Set\nStandards', 'IS/BS'),
        ('Describe\nMethod', ''),
        ('Specify\nTesting', ''),
        ('Review &amp;\nFinalize', ''),
    ], 'horizontal')
    svgs['Principles/Techniques of Specification Writing'] = svg_wrap(writing, 'Fig 12.4', 'Specification Writing Process Steps', w, h, w, h)
    
    brick_spec = f'''          <defs><style>
              .bk-box{{rx:8;ry:8;stroke-width:1.5;opacity:.92}}
              .bk-t{{font:bold 11px 'Source Sans 3',sans-serif;text-anchor:middle}}
              .bk-item{{font:10px 'Source Sans 3',sans-serif;fill:var(--svg-text);text-anchor:start}}
            </style></defs>
          <text style="font:bold 13px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="280" y="18">Key Points: Brick Work Specification</text>
          <rect class="bk-box" x="30" y="30" width="240" height="120" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text class="bk-t" x="150" y="50" style="fill:var(--svg-text-blue)">Material Requirements</text>
          <text class="bk-item" x="45" y="70" style="fill:var(--svg-text-blue)">&bull; First class bricks (IS 1077)</text>
          <text class="bk-item" x="45" y="88" style="fill:var(--svg-text-blue)">&bull; Compressive strength &ge; 75 kg/cm&sup2;</text>
          <text class="bk-item" x="45" y="106" style="fill:var(--svg-text-blue)">&bull; Water absorption &lt; 20%</text>
          <text class="bk-item" x="45" y="124" style="fill:var(--svg-text-blue)">&bull; Cement: OPC 43 grade</text>
          <rect class="bk-box" x="290" y="30" width="240" height="120" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <text class="bk-t" x="410" y="50" style="fill:var(--svg-text-green)">Workmanship</text>
          <text class="bk-item" x="305" y="70" style="fill:var(--svg-text-green)">&bull; Bricks soaked in water 2 hrs</text>
          <text class="bk-item" x="305" y="88" style="fill:var(--svg-text-green)">&bull; English bond / Flemish bond</text>
          <text class="bk-item" x="305" y="106" style="fill:var(--svg-text-green)">&bull; Mortar: 1:4 or 1:6 (C:S)</text>
          <text class="bk-item" x="305" y="124" style="fill:var(--svg-text-green)">&bull; Curing: min 7 days</text>'''
    svgs['Specification for Brick Work'] = svg_wrap(brick_spec, 'Fig 12.5', 'Brick Work Specification: Key Points', 560, 160, 560, 160)
    
    rcc_spec = f'''          <defs><style>
              .rc-box{{rx:8;ry:8;stroke-width:1.5;opacity:.92}}
              .rc-t{{font:bold 11px 'Source Sans 3',sans-serif;text-anchor:middle}}
              .rc-item{{font:10px 'Source Sans 3',sans-serif;fill:var(--svg-text);text-anchor:start}}
            </style></defs>
          <text style="font:bold 13px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="280" y="18">Key Points: RCC Works Specification</text>
          <rect class="rc-box" x="30" y="30" width="240" height="135" style="fill:var(--svg-orange);stroke:var(--svg-orange-s)"/>
          <text class="rc-t" x="150" y="50" style="fill:var(--svg-text-orange)">Materials</text>
          <text class="rc-item" x="45" y="70" style="fill:var(--svg-text-orange)">&bull; OPC 43/53 grade cement</text>
          <text class="rc-item" x="45" y="88" style="fill:var(--svg-text-orange)">&bull; Clean, graded aggregates</text>
          <text class="rc-item" x="45" y="106" style="fill:var(--svg-text-orange)">&bull; TMT bars (Fe 500/500D)</text>
          <text class="rc-item" x="45" y="124" style="fill:var(--svg-text-orange)">&bull; W/C ratio: 0.40-0.50</text>
          <text class="rc-item" x="45" y="142" style="fill:var(--svg-text-orange)">&bull; Slump: 50-100mm (general)</text>
          <rect class="rc-box" x="290" y="30" width="240" height="135" style="fill:var(--svg-teal);stroke:var(--svg-teal-s)"/>
          <text class="rc-t" x="410" y="50" style="fill:var(--svg-text-teal)">Execution</text>
          <text class="rc-item" x="305" y="70" style="fill:var(--svg-text-teal)">&bull; Mix design as per IS 10262</text>
          <text class="rc-item" x="305" y="88" style="fill:var(--svg-text-teal)">&bull; Cover: 25-50mm (beams)</text>
          <text class="rc-item" x="305" y="106" style="fill:var(--svg-text-teal)">&bull; Vibration: needle vibrator</text>
          <text class="rc-item" x="305" y="124" style="fill:var(--svg-text-teal)">&bull; Cube test: 3 cubes / 50 m&sup3;</text>
          <text class="rc-item" x="305" y="142" style="fill:var(--svg-text-teal)">&bull; Curing: min 14-28 days</text>'''
    svgs['Specification for RCC Works'] = svg_wrap(rcc_spec, 'Fig 12.6', 'RCC Works Specification: Key Points', 560, 175, 560, 175)
    
    spec_doc, w, h = flow_svg('sd', [
        ('Scope', 'What to do'),
        ('Materials', 'Standards'),
        ('Workmanship', 'Method'),
        ('Testing', 'QC tests'),
        ('Measurement', 'Units'),
        ('Payment', 'Rate basis'),
    ], 'horizontal')
    svgs['Contract Specification'] = svg_wrap(spec_doc, 'Fig 12.7', 'Structure of a Contract Specification', w, h, w, h)
    
    plaster_spec = f'''          <defs><style>
              .pl-box{{rx:8;ry:8;stroke-width:1.5;opacity:.92}}
              .pl-t{{font:bold 11px 'Source Sans 3',sans-serif;text-anchor:middle}}
              .pl-item{{font:10px 'Source Sans 3',sans-serif;fill:var(--svg-text);text-anchor:start}}
            </style></defs>
          <text style="font:bold 13px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="280" y="18">Plaster Work Specification: Key Points</text>
          <rect class="pl-box" x="50" y="30" width="460" height="90" style="fill:var(--svg-pink);stroke:var(--svg-pink-s)"/>
          <text class="pl-item" x="65" y="50" style="fill:var(--svg-text-pink)">&bull; Surface cleaned, joints raked 12mm deep, wetted before plastering</text>
          <text class="pl-item" x="65" y="68" style="fill:var(--svg-text-pink)">&bull; Two coats: Base coat (12mm, 1:4) + Finishing coat (6mm, 1:3)</text>
          <text class="pl-item" x="65" y="86" style="fill:var(--svg-text-pink)">&bull; Thickness: Internal 12mm, External 20mm, Ceiling 6mm</text>
          <text class="pl-item" x="65" y="104" style="fill:var(--svg-text-pink)">&bull; Curing: minimum 7 days continuous moist curing</text>'''
    svgs['Specification for Plaster Work'] = svg_wrap(plaster_spec, 'Fig 12.8', 'Plaster Work Specification Highlights', 560, 130, 560, 130)
    
    gabion_spec = f'''          <defs><style>
              .gb-box{{rx:8;ry:8;stroke-width:1.5;opacity:.92}}
              .gb-item{{font:10px 'Source Sans 3',sans-serif;fill:var(--svg-text);text-anchor:start}}
            </style></defs>
          <text style="font:bold 13px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="280" y="18">Gabion &amp; Stone Masonry Spec: Key Points</text>
          <rect class="gb-box" x="30" y="30" width="240" height="80" style="fill:var(--svg-purple);stroke:var(--svg-purple-s)"/>
          <text style="font:bold 11px 'Source Sans 3',sans-serif;fill:var(--svg-text-purple);text-anchor:middle" x="150" y="48">Gabion Works</text>
          <text class="gb-item" x="42" y="66" style="fill:var(--svg-text-purple)">&bull; GI wire mesh boxes (2&times;1&times;1m)</text>
          <text class="gb-item" x="42" y="82" style="fill:var(--svg-text-purple)">&bull; Stones: 150-300mm, hard</text>
          <text class="gb-item" x="42" y="98" style="fill:var(--svg-text-purple)">&bull; Bracing wires at 300mm c/c</text>
          <rect class="gb-box" x="290" y="30" width="240" height="80" style="fill:var(--svg-yellow);stroke:var(--svg-yellow-s)"/>
          <text style="font:bold 11px 'Source Sans 3',sans-serif;fill:var(--svg-text-yellow);text-anchor:middle" x="410" y="48">Stone Masonry</text>
          <text class="gb-item" x="302" y="66" style="fill:var(--svg-text-yellow)">&bull; Coursed rubble/ashlar</text>
          <text class="gb-item" x="302" y="82" style="fill:var(--svg-text-yellow)">&bull; Mortar 1:4 or 1:6 (C:S)</text>
          <text class="gb-item" x="302" y="98" style="fill:var(--svg-text-yellow)">&bull; Header stones every 1m</text>'''
    svgs['Specification for Gabion Works'] = svg_wrap(gabion_spec, 'Fig 12.9', 'Gabion &amp; Stone Masonry Specification', 560, 120, 560, 120)
    
    painting_spec = f'''          <defs><style>
              .pt2-box{{rx:8;ry:8;stroke-width:1.5;opacity:.92}}
              .pt2-item{{font:10px 'Source Sans 3',sans-serif;fill:var(--svg-text);text-anchor:start}}
            </style></defs>
          <text style="font:bold 13px 'Source Sans 3',sans-serif;fill:var(--svg-hub);text-anchor:middle" x="280" y="18">Painting Work Specification</text>
          <rect class="pt2-box" x="50" y="30" width="460" height="80" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text class="pt2-item" x="65" y="50" style="fill:var(--svg-text-blue)">&bull; Surface: Clean, dry, smooth, free from dust and oil</text>
          <text class="pt2-item" x="65" y="68" style="fill:var(--svg-text-blue)">&bull; Apply: 1 primer + 2 coats of approved paint (min 24hr gap)</text>
          <text class="pt2-item" x="65" y="86" style="fill:var(--svg-text-blue)">&bull; Coverage: as per manufacturer recommendation</text>
          <text class="pt2-item" x="65" y="104" style="fill:var(--svg-text-blue)">&bull; Types: Distemper (internal), Enamel (wood/metal), Emulsion (walls)</text>'''
    svgs['Specification for Painting Work'] = svg_wrap(painting_spec, 'Fig 12.10', 'Painting Work Specification Highlights', 560, 120, 560, 120)
    
    return svgs

def get_ch13_svgs():
    svgs = {}
    
    val_methods = hub_spoke_svg('vm', 'VALUATION', [
        ('Cost-Based', 'Construction cost'),
        ('Plinth Area', 'Rate &times; area'),
        ('Depreciated', 'Cost &minus; depreciation'),
        ('Rental', 'Net income / YP'),
        ('Profit-Based', 'Business income'),
        ('Comparison', 'Market data'),
        ('Development', 'Future potential'),
    ], hub_sub='Methods', width=600, height=440)
    svgs['Methods of Valuation'] = svg_wrap(val_methods, 'Fig 13.1', 'Methods of Property Valuation', 600, 440)
    
    cost_value, w, h = comparison_table_svg('cv', 'Cost vs Value', 'Cost', 'Value',
        [
            ('Amount spent to build', 'Amount buyer will pay'),
            ('Based on materials &amp; labor', 'Based on demand &amp; utility'),
            ('Objective (can calculate)', 'Subjective (can vary)'),
            ('Past-oriented', 'Present/future-oriented'),
            ('Fixed at time of construction', 'Changes with market'),
        ])
    svgs['Cost and Value'] = svg_wrap(cost_value, 'Fig 13.2', 'Difference between Cost and Value', w, h, w, h)
    
    val_factors = hub_spoke_svg('vf', 'FACTORS', [
        ('Location', 'Prime vs remote area'),
        ('Size &amp; Shape', 'Regular preferred'),
        ('Age', 'Depreciation with time'),
        ('Condition', 'Maintenance status'),
        ('Infrastructure', 'Roads, water, power'),
        ('Legal', 'Title, zoning, encumbrance'),
        ('Market Demand', 'Supply vs demand'),
        ('Future Development', 'Growth potential'),
    ], hub_sub='Affecting Value', width=650, height=480)
    svgs['Factors Affecting Value'] = svg_wrap(val_factors, 'Fig 13.3', 'Factors Affecting Property Value', 650, 480)
    
    depr_methods, w, h = comparison_table_svg('dm', 'Methods of Depreciation', 'Method', 'Formula / Approach',
        [
            ('Straight Line', 'D = (C &minus; S) / N'),
            ('Diminishing Balance', 'D = C(1 &minus; r)&#x207F; where r = 1&minus;(S/C)^(1/n)'),
            ('Sinking Fund', 'Annual deposit to replace at end'),
            ('Quantity Survey', 'Item-wise condition assessment'),
            ('Sum of Years Digits', 'Accelerated early depreciation'),
        ])
    svgs['Methods of Calculating Depreciation'] = svg_wrap(depr_methods, 'Fig 13.4', 'Methods of Calculating Depreciation', w, h, w, h)
    
    yp_formula = f'''          <defs><style>
              .yp-box{{rx:10;ry:10;stroke-width:2;opacity:.92}}
              .yp-t{{font:bold 16px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-hub)}}
              .yp-s{{font:12px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
            </style></defs>
          <rect class="yp-box" x="50" y="10" width="500" height="60" style="fill:var(--svg-blue);stroke:var(--svg-blue-s)"/>
          <text class="yp-t" x="300" y="35" style="fill:var(--svg-text-blue)">Years Purchase (YP) = 100 / Rate of Return (%)</text>
          <text class="yp-s" x="300" y="55" style="fill:var(--svg-text-blue)">Capitalized Value = Net Annual Income &times; YP</text>
          <rect class="yp-box" x="50" y="80" width="240" height="40" style="fill:var(--svg-green);stroke:var(--svg-green-s)"/>
          <text class="yp-s" x="170" y="105" style="fill:var(--svg-text-green)">If rate = 5%, YP = 100/5 = 20</text>
          <rect class="yp-box" x="310" y="80" width="240" height="40" style="fill:var(--svg-orange);stroke:var(--svg-orange-s)"/>
          <text class="yp-s" x="430" y="105" style="fill:var(--svg-text-orange)">If rate = 8%, YP = 100/8 = 12.5</text>'''
    svgs['Years Purchase'] = svg_wrap(yp_formula, 'Fig 13.5', 'Years Purchase (YP) &amp; Capitalized Value Formula', 600, 130, 600, 130)
    
    sf_formula = f'''          <defs><style>
              .sf-box{{rx:10;ry:10;stroke-width:2;opacity:.92}}
              .sf-t{{font:bold 14px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-hub)}}
              .sf-s{{font:11px 'Source Sans 3',sans-serif;text-anchor:middle;fill:var(--svg-sub)}}
            </style></defs>
          <rect class="sf-box" x="50" y="10" width="500" height="55" style="fill:var(--svg-teal);stroke:var(--svg-teal-s)"/>
          <text class="sf-t" x="300" y="32" style="fill:var(--svg-text-teal)">Sinking Fund = A &times; [(1+i)&#x207F; &minus; 1] / i</text>
          <text class="sf-s" x="300" y="52" style="fill:var(--svg-text-teal)">A = annual installment, i = interest rate, n = years</text>
          <rect class="sf-box" x="130" y="75" width="340" height="35" style="fill:var(--svg-purple);stroke:var(--svg-purple-s)"/>
          <text class="sf-s" x="300" y="97" style="fill:var(--svg-text-purple)">Purpose: Accumulate fund to replace asset after useful life</text>'''
    svgs['Sinking Fund'] = svg_wrap(sf_formula, 'Fig 13.6', 'Sinking Fund Formula &amp; Purpose', 600, 120, 600, 120)
    
    obsolescence = hub_spoke_svg('obs', 'OBSOLESCENCE', [
        ('Physical', 'Wear, deterioration'),
        ('Functional', 'Outdated design'),
        ('Economic', 'Better alternatives'),
        ('Social', 'Changed needs'),
        ('Legal', 'New regulations'),
    ], hub_sub='Types', width=500, height=380)
    svgs['Obsolescence'] = svg_wrap(obsolescence, 'Fig 13.7', 'Types of Obsolescence in Property Valuation', 500, 380, 500, 380)
    
    outgoings = hub_spoke_svg('out', 'OUTGOINGS', [
        ('Repairs', '10-15% of gross'),
        ('Taxes', 'Property tax'),
        ('Insurance', '1-2% of value'),
        ('Management', '5-10% of gross'),
        ('Vacancy', 'Assumed 10%'),
        ('Sinking Fund', 'Replacement reserve'),
    ], hub_sub='Types', width=550, height=400)
    svgs['Outgoings'] = svg_wrap(outgoings, 'Fig 13.8', 'Types of Outgoings in Property Valuation', 550, 400, 550, 400)
    
    val_process, w, h = flow_svg('vp', [
        ('Inspect\nProperty', ''),
        ('Collect\nData', ''),
        ('Select\nMethod', ''),
        ('Calculate\nValue', ''),
        ('Prepare\nReport', ''),
    ])
    svgs['Introduction to Valuation'] = svg_wrap(val_process, 'Fig 13.9', 'Property Valuation Process Steps', w, h, w, h)
    
    valuer_qual = hub_spoke_svg('vq', 'VALUER', [
        ('Engineering Degree', 'Civil/Architecture'),
        ('Experience', 'Min 5-7 years'),
        ('Registration', 'Govt registered'),
        ('Knowledge', 'Market, law, methods'),
        ('Ethics', 'Impartial, honest'),
    ], hub_sub='Qualifications', width=500, height=380)
    svgs['Qualification of Valuers'] = svg_wrap(valuer_qual, 'Fig 13.10', 'Qualifications Required for Property Valuers', 500, 380, 500, 380)
    
    return svgs

# ═══════════════════════════════════════════════════════════
# MAIN INJECTION LOGIC
# ═══════════════════════════════════════════════════════════

def inject_svgs(chapter_num, lines, svgs_dict):
    """Inject SVGs after the matching heading in the file."""
    injected = 0
    # Process in reverse order of line number to avoid offset issues
    insertions = []
    
    for heading_text, svg_content in svgs_dict.items():
        idx = find_line(lines, heading_text)
        if idx == -1:
            print(f'  WARNING: heading "{heading_text}" not found in chapter{chapter_num}.html')
            continue
        
        # Find a good insertion point: after the next closing tag (</p>, </ul>, </ol>, </table>, </div>)
        # or after 2-5 lines if no clear closing tag
        insert_at = idx
        # Look for first major content block end after heading
        for j in range(idx + 1, min(idx + 15, len(lines))):
            stripped = lines[j].strip()
            if stripped.startswith('<div') or stripped.startswith('<ul') or stripped.startswith('<ol') or stripped.startswith('<table') or stripped.startswith('<p>'):
                # Find end of this element
                if stripped.startswith('<p>') and '</p>' in stripped:
                    insert_at = j
                    break
                elif stripped.startswith('<p'):
                    for k in range(j, min(j+10, len(lines))):
                        if '</p>' in lines[k]:
                            insert_at = k
                            break
                    break
                elif stripped.startswith('<ul') or stripped.startswith('<ol'):
                    tag = 'ul' if 'ul' in stripped else 'ol'
                    for k in range(j, min(j+50, len(lines))):
                        if f'</{tag}>' in lines[k]:
                            insert_at = k
                            break
                    break
                elif stripped.startswith('<table'):
                    for k in range(j, min(j+80, len(lines))):
                        if '</table>' in lines[k]:
                            insert_at = k
                            break
                    break
                elif stripped.startswith('<div'):
                    # Look for closing div but be careful with nesting
                    depth = 0
                    for k in range(j, min(j+100, len(lines))):
                        depth += lines[k].count('<div') - lines[k].count('</div')
                        if depth <= 0:
                            insert_at = k
                            break
                    break
            elif stripped and not stripped.startswith('<'):
                insert_at = j
                break
        
        if insert_at == idx:
            insert_at = min(idx + 3, len(lines) - 1)
        
        insertions.append((insert_at, svg_content))
        injected += 1
    
    # Sort by line number descending to avoid offset issues
    insertions.sort(key=lambda x: x[0], reverse=True)
    
    for insert_at, svg_content in insertions:
        svg_lines = svg_content.split('\n')
        lines = lines[:insert_at+1] + [l + '\n' for l in svg_lines] + lines[insert_at+1:]
    
    return lines, injected

def main():
    import sys
    dry_run = '--dry-run' in sys.argv
    if dry_run:
        print("=== DRY RUN MODE ===\n")
    
    chapter_svg_funcs = {
        1: get_ch1_svgs,
        2: get_ch2_svgs,
        3: get_ch3_svgs,
        4: get_ch4_svgs,
        5: get_ch5_svgs,
        6: get_ch6_svgs,
        7: get_ch7_svgs,
        8: get_ch8_svgs,
        9: get_ch9_svgs,
        10: get_ch10_svgs,
        11: get_ch11_svgs,
        12: get_ch12_svgs,
        13: get_ch13_svgs,
    }
    
    total = 0
    for ch_num in range(1, 14):
        fpath = os.path.join(FOLDER, f'chapter{ch_num}.html')
        if not os.path.exists(fpath):
            print(f'chapter{ch_num}.html: NOT FOUND')
            continue
        
        with open(fpath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        original = len(lines)
        svg_func = chapter_svg_funcs.get(ch_num)
        if not svg_func:
            print(f'chapter{ch_num}.html: no SVG function')
            continue
        
        svgs = svg_func()
        lines, injected = inject_svgs(ch_num, lines, svgs)
        
        new_count = len(lines)
        if injected > 0 and not dry_run:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.writelines(lines)
        
        print(f'chapter{ch_num}.html: {injected} SVGs added ({original} -> {new_count} lines)')
        total += injected
    
    print(f'\nTotal: {total} SVG diagrams added across all chapters')

if __name__ == '__main__':
    main()

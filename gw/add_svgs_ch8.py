"""Add 10 new educational SVG diagrams to Chapter 8 (GW Pumps)."""
import re

FILE = r"d:\Final Year\Theory\gw\GW_THE\chapter8.html"

def svg_wrap(svg_content, caption):
    return f'''
            <div class="figure-container">
{svg_content}
                <div class="figcaption">{caption}</div>
            </div>
'''

SVGS = {}

# 1. Main Components
SVGS['8.3.2 Main Components'] = svg_wrap('''
                <svg width="600" height="230" viewBox="0 0 600 230" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Centrifugal Pump — Main Components</text>
                    <ellipse cx="200" cy="130" rx="90" ry="85" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="200" y="110" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-fg)">Impeller</text>
                    <text x="200" y="125" text-anchor="middle" font-size="8" fill="var(--svg-fg)">(rotating vanes)</text>
                    <text x="200" y="160" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Converts mechanical</text>
                    <text x="200" y="174" text-anchor="middle" font-size="8" fill="var(--svg-muted)">energy → velocity head</text>
                    <line x1="70" y1="130" x2="108" y2="130" stroke="var(--svg-accent)" stroke-width="3" marker-end="url(#arr)"/>
                    <text x="60" y="125" text-anchor="end" font-size="9" fill="var(--svg-accent)">Suction</text>
                    <text x="60" y="138" text-anchor="end" font-size="8" fill="var(--svg-accent)">(eye)</text>
                    <line x1="290" y1="80" x2="340" y2="60" stroke="var(--svg-green-accent)" stroke-width="3" marker-end="url(#arr)"/>
                    <text x="360" y="58" font-size="9" fill="var(--svg-green-accent)">Delivery</text>
                    <text x="260" y="52" font-size="8" fill="var(--svg-fg)">Volute casing</text>
                    <text x="260" y="65" font-size="8" fill="var(--svg-fg)">(spiral → expands)</text>
                    <rect x="370" y="80" width="210" height="130" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="475" y="100" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-fg)">Key Components</text>
                    <text x="475" y="120" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Impeller (open/closed)</text>
                    <text x="475" y="137" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Volute/diffuser casing</text>
                    <text x="475" y="154" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Shaft + bearings</text>
                    <text x="475" y="171" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Mechanical seal</text>
                    <text x="475" y="188" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Suction &amp; delivery pipes</text>
                    <text x="475" y="205" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Foot valve + strainer</text>
                    <text x="300" y="225" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Volute converts velocity head to pressure head (velocity decreases, pressure increases)</text>
                </svg>''',
    'Figure 8.3b: Centrifugal pump components — the impeller accelerates water outward, and the volute casing converts velocity to pressure head.')

# 2. Types of Centrifugal Pumps
SVGS['8.3.4 Types of Centrifugal Pu'] = svg_wrap('''
                <svg width="650" height="220" viewBox="0 0 650 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="325" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Types of Centrifugal Pumps</text>
                    <rect x="20" y="45" width="190" height="140" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="115" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-accent)">Radial Flow</text>
                    <text x="115" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Flow ⊥ to shaft axis</text>
                    <text x="115" y="102" text-anchor="middle" font-size="9" fill="var(--svg-fg)">High head, low Q</text>
                    <text x="115" y="122" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">N_s: 500-4000</text>
                    <text x="115" y="142" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Deep wells, high-</text>
                    <text x="115" y="157" text-anchor="middle" font-size="9" fill="var(--svg-muted)">pressure systems</text>
                    <rect x="230" y="45" width="190" height="140" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="325" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-green-accent)">Mixed Flow</text>
                    <text x="325" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Radial + axial components</text>
                    <text x="325" y="102" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Medium head &amp; Q</text>
                    <text x="325" y="122" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">N_s: 4000-10000</text>
                    <text x="325" y="142" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Irrigation pumps,</text>
                    <text x="325" y="157" text-anchor="middle" font-size="9" fill="var(--svg-muted)">medium-depth wells</text>
                    <rect x="440" y="45" width="190" height="140" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="535" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-orange-accent)">Axial Flow</text>
                    <text x="535" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Flow ∥ to shaft axis</text>
                    <text x="535" y="102" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Low head, high Q</text>
                    <text x="535" y="122" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">N_s: &gt; 10000</text>
                    <text x="535" y="142" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Flood pumps,</text>
                    <text x="535" y="157" text-anchor="middle" font-size="9" fill="var(--svg-muted)">drainage, lift stations</text>
                    <text x="325" y="205" text-anchor="middle" font-size="10" fill="var(--svg-fg)">N_s = NQ^(1/2)/H^(3/4) — specific speed determines pump type selection</text>
                </svg>''',
    'Figure 8.3c: Three types of centrifugal pumps classified by flow direction and specific speed — radial for high head, axial for high discharge.')

# 3. Reciprocating Pump
SVGS['8.4.2 Working Principle'] = svg_wrap('''
                <svg width="550" height="220" viewBox="0 0 550 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Reciprocating Pump — Working Principle</text>
                    <rect x="20" y="45" width="240" height="130" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="140" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Suction Stroke</text>
                    <text x="140" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Piston moves backward</text>
                    <text x="140" y="102" text-anchor="middle" font-size="9" fill="var(--svg-fg)">→ Vacuum created in cylinder</text>
                    <text x="140" y="119" text-anchor="middle" font-size="9" fill="var(--svg-fg)">→ Suction valve opens</text>
                    <text x="140" y="136" text-anchor="middle" font-size="9" fill="var(--svg-fg)">→ Water fills cylinder</text>
                    <text x="140" y="158" text-anchor="middle" font-size="9" fill="var(--svg-muted)">(Delivery valve closed)</text>
                    <rect x="290" y="45" width="240" height="130" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="410" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Delivery Stroke</text>
                    <text x="410" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Piston moves forward</text>
                    <text x="410" y="102" text-anchor="middle" font-size="9" fill="var(--svg-fg)">→ Pressure builds in cylinder</text>
                    <text x="410" y="119" text-anchor="middle" font-size="9" fill="var(--svg-fg)">→ Delivery valve opens</text>
                    <text x="410" y="136" text-anchor="middle" font-size="9" fill="var(--svg-fg)">→ Water pushed to delivery</text>
                    <text x="410" y="158" text-anchor="middle" font-size="9" fill="var(--svg-muted)">(Suction valve closed)</text>
                    <text x="275" y="200" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Q = ALN/60 (single-acting) | Q = 2ALN/60 (double-acting)</text>
                    <text x="275" y="218" text-anchor="middle" font-size="9" fill="var(--svg-muted)">A = piston area, L = stroke length, N = RPM — positive displacement pump</text>
                </svg>''',
    'Figure 8.4b: Reciprocating pump operation — alternating suction and delivery strokes with one-way valves, giving pulsating flow at constant Q per revolution.')

# 4. Submersible Pump Components
SVGS['8.5.1 Components'] = svg_wrap('''
                <svg width="500" height="280" viewBox="0 0 500 280" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="250" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Submersible Pump — Key Features</text>
                    <rect x="200" y="40" width="100" height="180" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="2" rx="5"/>
                    <line x1="200" y1="120" x2="300" y2="120" stroke="var(--svg-fg)" stroke-width="1.5" stroke-dasharray="4,3"/>
                    <text x="250" y="80" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-fg)">Multi-stage</text>
                    <text x="250" y="95" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-fg)">pump</text>
                    <text x="250" y="115" text-anchor="middle" font-size="7" fill="var(--svg-muted)">Impellers stacked</text>
                    <text x="250" y="160" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-fg)">Submersible</text>
                    <text x="250" y="175" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-fg)">motor</text>
                    <text x="250" y="200" text-anchor="middle" font-size="7" fill="var(--svg-muted)">Sealed, water-cooled</text>
                    <line x1="250" y1="36" x2="250" y2="20" stroke="var(--svg-accent)" stroke-width="3" marker-end="url(#arr)"/>
                    <text x="260" y="18" font-size="8" fill="var(--svg-accent)">Riser pipe → surface</text>
                    <line x1="300" y1="170" x2="350" y2="170" stroke="var(--svg-red-accent)" stroke-width="2"/>
                    <text x="360" y="168" font-size="8" fill="var(--svg-red-accent)">Power cable</text>
                    <text x="360" y="180" font-size="8" fill="var(--svg-red-accent)">from surface</text>
                    <rect x="30" y="45" width="150" height="175" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="105" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-fg)">Advantages</text>
                    <text x="105" y="82" text-anchor="middle" font-size="8" fill="var(--svg-fg)">No priming needed</text>
                    <text x="105" y="96" text-anchor="middle" font-size="8" fill="var(--svg-fg)">No suction limit</text>
                    <text x="105" y="110" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Quiet operation</text>
                    <text x="105" y="124" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Deep wells (&gt; 50 m)</text>
                    <text x="105" y="140" text-anchor="middle" font-size="8" fill="var(--svg-fg)">High heads possible</text>
                    <text x="105" y="160" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-red-accent)">Limitations</text>
                    <text x="105" y="175" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Difficult to service</text>
                    <text x="105" y="189" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Motor seal failures</text>
                    <text x="105" y="203" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Higher initial cost</text>
                    <text x="250" y="245" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Motor + pump submerged below water level in the well</text>
                    <text x="250" y="265" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Most common pump type for deep tube wells in Nepal</text>
                </svg>''',
    'Figure 8.5b: Submersible pump — motor and multi-stage pump unit are both submerged in the well, eliminating suction head limitations.')

# 5. Airlift Pump
SVGS['8.7.1 Working Principle'] = svg_wrap('''
                <svg width="500" height="260" viewBox="0 0 500 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="250" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Airlift Pump — Working Principle</text>
                    <rect x="180" y="40" width="30" height="180" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="140" y="130" text-anchor="end" font-size="9" fill="var(--svg-fg)">Riser pipe</text>
                    <line x1="142" y1="130" x2="178" y2="130" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="220" y="140" width="15" height="80" fill="var(--svg-bg-fill)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="280" y="185" font-size="9" fill="var(--svg-accent)">Air pipe</text>
                    <line x1="237" y1="180" x2="275" y2="180" stroke="var(--svg-accent)" stroke-width="1"/>
                    <circle cx="192" cy="170" r="3" fill="var(--svg-water-3)"/>
                    <circle cx="196" cy="155" r="4" fill="var(--svg-water-3)"/>
                    <circle cx="190" cy="140" r="3" fill="var(--svg-water-3)"/>
                    <circle cx="198" cy="125" r="5" fill="var(--svg-water-3)"/>
                    <circle cx="188" cy="110" r="4" fill="var(--svg-water-3)"/>
                    <circle cx="195" cy="95" r="3" fill="var(--svg-water-3)"/>
                    <circle cx="192" cy="80" r="4" fill="var(--svg-water-3)"/>
                    <text x="160" y="80" text-anchor="end" font-size="8" fill="var(--svg-water-3)">Air-water</text>
                    <text x="160" y="92" text-anchor="end" font-size="8" fill="var(--svg-water-3)">mixture rises</text>
                    <line x1="195" y1="38" x2="195" y2="20" stroke="var(--svg-green-accent)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="220" y="25" font-size="9" fill="var(--svg-green-accent)">Water out</text>
                    <line x1="90" y1="160" x2="90" y2="220" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="85" y1="160" x2="95" y2="160" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="85" y1="220" x2="95" y2="220" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="70" y="195" text-anchor="end" font-size="9" fill="var(--svg-fg)">Submergence</text>
                    <line x1="50" y1="160" x2="350" y2="160" stroke="var(--svg-water-3)" stroke-width="1.5" stroke-dasharray="5,3"/>
                    <text x="340" y="155" font-size="8" fill="var(--svg-water-3)">Water level</text>
                    <rect x="310" y="90" width="170" height="100" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="395" y="110" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-fg)">Principle</text>
                    <text x="395" y="128" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Air injection → lighter</text>
                    <text x="395" y="142" text-anchor="middle" font-size="8" fill="var(--svg-fg)">mixture in riser</text>
                    <text x="395" y="156" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Density difference</text>
                    <text x="395" y="170" text-anchor="middle" font-size="8" fill="var(--svg-fg)">drives upward flow</text>
                    <text x="395" y="184" text-anchor="middle" font-size="8" fill="var(--svg-muted)">η = 30-40% (low)</text>
                    <text x="250" y="245" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Submergence ratio = submergence/total lift = 0.6 to 0.8 typical</text>
                    <text x="250" y="260" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Used for: well development, sandy/turbid water, corrosive water</text>
                </svg>''',
    'Figure 8.7b: Airlift pump — compressed air creates a lower-density mixture in the riser pipe, causing water to rise by buoyancy; low efficiency but handles sandy water.')

# 6. Hand Pump Types
SVGS['8.7.2 Types of Hand Pumps'] = svg_wrap('''
                <svg width="600" height="220" viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Hand Pump Types for Different Well Depths</text>
                    <rect x="20" y="45" width="170" height="140" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="105" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-accent)">Shallow Well</text>
                    <text x="105" y="82" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Depth: &lt; 15 m</text>
                    <text x="105" y="99" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Suction type</text>
                    <text x="105" y="116" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Cylinder above ground</text>
                    <text x="105" y="136" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Examples: No. 6,</text>
                    <text x="105" y="150" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Tara pump</text>
                    <text x="105" y="170" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">Easy maintenance</text>
                    <rect x="215" y="45" width="170" height="140" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="300" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-green-accent)">Medium Depth</text>
                    <text x="300" y="82" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Depth: 15-45 m</text>
                    <text x="300" y="99" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Force/direct action type</text>
                    <text x="300" y="116" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Cylinder below ground</text>
                    <text x="300" y="136" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Examples: India Mark II,</text>
                    <text x="300" y="150" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Afridev</text>
                    <text x="300" y="170" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">Most common in Nepal</text>
                    <rect x="410" y="45" width="170" height="140" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="2"/>
                    <text x="495" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-red-accent)">Deep Well</text>
                    <text x="495" y="82" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Depth: &gt; 45 m</text>
                    <text x="495" y="99" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Open-top cylinder</text>
                    <text x="495" y="116" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Deep-set mechanism</text>
                    <text x="495" y="136" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Examples: India Mark III,</text>
                    <text x="495" y="150" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Vergnet</text>
                    <text x="495" y="170" text-anchor="middle" font-size="8" fill="var(--svg-red-accent)">Complex maintenance</text>
                    <text x="300" y="205" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Suction limit ≈ 7 m (atmospheric) — deeper wells need downhole cylinders</text>
                </svg>''',
    'Figure 8.7c: Hand pump classification by well depth — shallow (&lt;15m, suction), medium (15-45m, force/direct), and deep (&gt;45m, open-top cylinder).')

# 7. Pump Selection Criteria
SVGS['A. Well Characteristics'] = svg_wrap('''
                <svg width="600" height="250" viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Pump Selection — Decision Factors</text>
                    <rect x="200" y="40" width="200" height="32" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="300" y="60" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">Pump Selection</text>
                    <line x1="100" y1="72" x2="80" y2="100" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="200" y1="72" x2="170" y2="100" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="300" y1="72" x2="300" y2="100" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="400" y1="72" x2="430" y2="100" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="500" y1="72" x2="520" y2="100" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <rect x="15" y="100" width="130" height="60" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="80" y="118" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-accent)">Well Properties</text>
                    <text x="80" y="133" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Depth, diameter,</text>
                    <text x="80" y="146" text-anchor="middle" font-size="8" fill="var(--svg-fg)">available drawdown</text>
                    <rect x="115" y="100" width="115" height="60" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="172" y="118" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-green-accent)">Q &amp; H Required</text>
                    <text x="172" y="133" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Design discharge,</text>
                    <text x="172" y="146" text-anchor="middle" font-size="8" fill="var(--svg-fg)">total head (TDH)</text>
                    <rect x="240" y="100" width="120" height="60" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <text x="300" y="118" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-water-3)">Power Source</text>
                    <text x="300" y="133" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Electricity, diesel,</text>
                    <text x="300" y="146" text-anchor="middle" font-size="8" fill="var(--svg-fg)">solar, manual</text>
                    <rect x="370" y="100" width="120" height="60" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="430" y="118" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-orange-accent)">Water Quality</text>
                    <text x="430" y="133" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Sand content,</text>
                    <text x="430" y="146" text-anchor="middle" font-size="8" fill="var(--svg-fg)">corrosivity</text>
                    <rect x="460" y="100" width="120" height="60" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <text x="520" y="118" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-red-accent)">Economics</text>
                    <text x="520" y="133" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Capital cost,</text>
                    <text x="520" y="146" text-anchor="middle" font-size="8" fill="var(--svg-fg)">O&amp;M, lifecycle</text>
                    <text x="300" y="190" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Match pump type to operating point (Q, H) on pump characteristic curve</text>
                    <text x="300" y="210" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Submersible: deep wells | Centrifugal: shallow, high Q | Hand pump: rural, no electricity</text>
                    <text x="300" y="235" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Always check: duty point falls within high-efficiency range of the pump curve</text>
                </svg>''',
    'Figure 8.8b: Pump selection decision tree — well properties, required Q and H, power availability, water quality, and economics all influence the choice.')

# 8. Total Dynamic Head
SVGS['8.10.1 Total Dynamic Head (TD'] = svg_wrap('''
                <svg width="500" height="300" viewBox="0 0 500 300" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="250" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Total Dynamic Head (TDH)</text>
                    <rect x="50" y="250" width="400" height="15" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="196" y="120" width="8" height="145" fill="var(--svg-fg)"/>
                    <line x1="50" y1="180" x2="450" y2="180" stroke="var(--svg-water-3)" stroke-width="1.5" stroke-dasharray="5,3"/>
                    <text x="460" y="178" font-size="8" fill="var(--svg-water-3)">PWL</text>
                    <line x1="50" y1="140" x2="450" y2="140" stroke="var(--svg-accent)" stroke-width="1.5" stroke-dasharray="5,3"/>
                    <text x="460" y="138" font-size="8" fill="var(--svg-accent)">SWL</text>
                    <line x1="50" y1="60" x2="450" y2="60" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="460" y="58" font-size="8" fill="var(--svg-fg)">GL</text>
                    <line x1="200" y1="55" x2="200" y2="40" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="200" y1="38" x2="380" y2="38" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="380" y1="38" x2="380" y2="50" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="290" y="35" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Delivery pipe</text>
                    <rect x="370" y="50" width="25" height="15" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="420" y="60" font-size="8" fill="var(--svg-fg)">Tank</text>
                    <line x1="80" y1="60" x2="80" y2="180" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <line x1="75" y1="60" x2="85" y2="60" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <line x1="75" y1="180" x2="85" y2="180" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="55" y="125" text-anchor="end" font-size="9" fill="var(--svg-green-accent)">Static</text>
                    <text x="55" y="138" text-anchor="end" font-size="9" fill="var(--svg-green-accent)">suction</text>
                    <line x1="100" y1="140" x2="100" y2="180" stroke="var(--svg-red-accent)" stroke-width="2"/>
                    <line x1="95" y1="140" x2="105" y2="140" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <line x1="95" y1="180" x2="105" y2="180" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <text x="115" y="162" font-size="8" fill="var(--svg-red-accent)">Drawdown</text>
                    <text x="250" y="210" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">TDH = h_s + h_d + h_f + h_v</text>
                    <text x="250" y="230" text-anchor="middle" font-size="9" fill="var(--svg-fg)">h_s = suction lift | h_d = delivery head | h_f = friction loss | h_v = velocity head</text>
                    <text x="250" y="245" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Pumping water level (PWL) = SWL + drawdown during pumping</text>
                    <text x="250" y="290" text-anchor="middle" font-size="9" fill="var(--svg-muted)">P = γQH/η (kW) — power increases linearly with Q and TDH</text>
                </svg>''',
    'Figure 8.10b: Total Dynamic Head components — static suction lift, delivery head, friction losses, and velocity head determine the pump power requirement.')

# 9. Power Required
SVGS['8.10.2 Power Required'] = svg_wrap('''
                <svg width="550" height="230" viewBox="0 0 550 230" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Pump Power Calculations</text>
                    <rect x="30" y="45" width="230" height="70" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="145" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Water Power (P_w)</text>
                    <text x="145" y="85" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">P_w = γQH</text>
                    <text x="145" y="105" text-anchor="middle" font-size="9" fill="var(--svg-muted)">= 9.81 × Q × TDH (kW)</text>
                    <line x1="265" y1="80" x2="290" y2="80" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <rect x="295" y="45" width="230" height="70" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="410" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Shaft Power (P_s)</text>
                    <text x="410" y="85" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">P_s = P_w / η_p</text>
                    <text x="410" y="105" text-anchor="middle" font-size="9" fill="var(--svg-muted)">η_p = pump efficiency (60-85%)</text>
                    <line x1="410" y1="120" x2="410" y2="140" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <rect x="295" y="145" width="230" height="60" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="2"/>
                    <text x="410" y="165" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-orange-accent)">Motor Power (P_m)</text>
                    <text x="410" y="185" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">P_m = P_s / η_m</text>
                    <text x="410" y="200" text-anchor="middle" font-size="9" fill="var(--svg-muted)">η_m = motor efficiency (85-95%)</text>
                    <text x="275" y="225" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Overall: P_m = γQH/(η_p × η_m) — always select next standard motor size UP</text>
                </svg>''',
    'Figure 8.10c: Power calculation chain — from water power (γQH) to shaft power (÷ pump efficiency) to motor power (÷ motor efficiency).')

# 10. Specific Speed
SVGS['8.10.3 Specific Speed'] = svg_wrap('''
                <svg width="550" height="220" viewBox="0 0 550 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Specific Speed — Pump Type Selector</text>
                    <text x="275" y="48" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-accent)">N_s = N√Q / H^(3/4)</text>
                    <text x="275" y="65" text-anchor="middle" font-size="9" fill="var(--svg-muted)">N = RPM, Q = m³/s, H = m (per stage)</text>
                    <line x1="50" y1="110" x2="500" y2="110" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="275" y="100" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Increasing N_s →</text>
                    <rect x="55" y="120" width="130" height="55" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="120" y="138" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-accent)">Radial Flow</text>
                    <text x="120" y="152" text-anchor="middle" font-size="8" fill="var(--svg-fg)">N_s: 500-4000</text>
                    <text x="120" y="165" text-anchor="middle" font-size="8" fill="var(--svg-fg)">High H, Low Q</text>
                    <rect x="200" y="120" width="130" height="55" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="265" y="138" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-green-accent)">Mixed Flow</text>
                    <text x="265" y="152" text-anchor="middle" font-size="8" fill="var(--svg-fg)">N_s: 4000-10000</text>
                    <text x="265" y="165" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Med H, Med Q</text>
                    <rect x="345" y="120" width="130" height="55" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="410" y="138" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-orange-accent)">Axial Flow</text>
                    <text x="410" y="152" text-anchor="middle" font-size="8" fill="var(--svg-fg)">N_s: &gt;10000</text>
                    <text x="410" y="165" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Low H, High Q</text>
                    <text x="275" y="200" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Same N_s → geometrically similar pumps → same efficiency</text>
                    <text x="275" y="218" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Higher N_s pumps are smaller and cheaper for the same power</text>
                </svg>''',
    'Figure 8.10d: Specific speed determines pump impeller type — low N_s selects radial flow, high N_s selects axial flow pumps.')


def inject_svgs(html, svgs):
    count = 0
    for heading_text, svg_html in svgs.items():
        escaped = re.escape(heading_text[:30])
        pattern = re.compile(
            r'(<h3[^>]*>[^<]*' + escaped + r'[^<]*</h3>\s*)',
            re.DOTALL
        )
        match = pattern.search(html)
        if match:
            insert_pos = match.end()
            next_block = re.search(r'(</(?:p|ol|ul|div|table)>)', html[insert_pos:])
            if next_block:
                actual_pos = insert_pos + next_block.end()
                html = html[:actual_pos] + svg_html + html[actual_pos:]
                count += 1
                print(f"  Inserted after '{heading_text[:50]}...'")
        else:
            print(f"  WARNING: not found '{heading_text[:50]}...'")
    return html, count


with open(FILE, 'r', encoding='utf-8') as f:
    html = f.read()

original = html.count('<svg')
html, c = inject_svgs(html, SVGS)
new_count = html.count('<svg')

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nChapter 8: {c} SVGs inserted")
print(f"  Before: {original} SVGs, After: {new_count} SVGs")
print(f"  Net added: {new_count - original}")

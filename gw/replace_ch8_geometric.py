"""Replace text-heavy SVGs in Chapter 8 with geometric diagrams + fix equations."""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from svg_replace_util import find_and_replace_svg_safe as find_and_replace_svg

FILE = r"d:\Final Year\Theory\gw\GW_THE\chapter8.html"

# ============================================================
# 1. CENTRIFUGAL PUMP — proper cross-section
# ============================================================
SVG_CENTRIFUGAL = '''<div class="figure-container">
                <svg width="580" height="340" viewBox="0 0 580 340" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="290" y="20" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Centrifugal Pump — Cross Section</text>

                    <!-- Volute casing (spiral) -->
                    <path d="M180,180 C180,120 240,70 300,70 C370,70 430,120 430,190 C430,250 390,300 320,300 C260,300 180,260 180,180 Z" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2.5"/>
                    <!-- Spiral expansion to discharge -->
                    <path d="M430,150 Q460,130 470,100 L470,80" fill="none" stroke="var(--svg-fg)" stroke-width="2.5"/>
                    <path d="M430,190 Q465,170 475,130 L475,80" fill="none" stroke="var(--svg-fg)" stroke-width="2.5"/>

                    <!-- Discharge pipe -->
                    <rect x="468" y="55" width="10" height="30" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <line x1="468" y1="55" x2="478" y2="55" stroke="var(--svg-fg)" stroke-width="2"/>
                    <line x1="473" y1="45" x2="473" y2="55" stroke="var(--svg-green-accent)" stroke-width="2" marker-start="url(#arr)"/>
                    <text x="490" y="55" font-size="9" font-weight="bold" fill="var(--svg-green-accent)">Delivery</text>

                    <!-- Impeller (vanes) -->
                    <circle cx="300" cy="185" r="65" fill="none" stroke="var(--svg-accent)" stroke-width="2" stroke-dasharray="6,3"/>
                    <circle cx="300" cy="185" r="8" fill="var(--svg-fg)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <!-- Vanes (curved blades) -->
                    <path d="M300,185 C290,160 280,140 260,125" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <path d="M300,185 C320,165 340,155 360,150" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <path d="M300,185 C310,205 320,225 335,240" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <path d="M300,185 C280,195 260,215 245,235" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <path d="M300,185 C285,175 265,175 245,180" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <path d="M300,185 C315,195 340,195 360,195" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="300" y="260" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-accent)">Impeller</text>

                    <!-- Rotation arrow -->
                    <path d="M268,135 A50,50 0 0,1 340,148" fill="none" stroke="var(--svg-red-accent)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="330" y="135" font-size="8" fill="var(--svg-red-accent)">ω</text>

                    <!-- Suction eye -->
                    <line x1="130" y1="185" x2="175" y2="185" stroke="var(--svg-water-3)" stroke-width="3" marker-end="url(#arr)"/>
                    <text x="120" y="182" text-anchor="end" font-size="9" font-weight="bold" fill="var(--svg-water-3)">Suction</text>
                    <text x="120" y="195" text-anchor="end" font-size="8" fill="var(--svg-water-3)">(eye)</text>

                    <!-- Shaft -->
                    <line x1="300" y1="185" x2="300" y2="310" stroke="var(--svg-fg)" stroke-width="4"/>
                    <text x="320" y="302" font-size="8" fill="var(--svg-fg)">Shaft</text>

                    <!-- Mechanical seal -->
                    <rect x="288" y="295" width="24" height="8" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.5" rx="2"/>
                    <text x="320" y="315" font-size="7" fill="var(--svg-muted)">Seal</text>

                    <!-- Labels -->
                    <text x="200" y="90" font-size="8" fill="var(--svg-muted)">Volute casing</text>
                    <text x="200" y="102" font-size="8" fill="var(--svg-muted)">(area expands)</text>

                    <!-- Flow path arrows inside volute -->
                    <path d="M240,150 A80,70 0 0,0 240,230" fill="none" stroke="var(--svg-water)" stroke-width="1" marker-end="url(#arr)" stroke-dasharray="4,3"/>
                    <path d="M360,145 A80,70 0 0,0 355,245" fill="none" stroke="var(--svg-water)" stroke-width="1" marker-end="url(#arr)" stroke-dasharray="4,3"/>

                    <!-- Energy conversion note -->
                    <rect x="30" y="270" width="175" height="55" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-dim)" stroke-width="1"/>
                    <text x="117" y="288" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Energy conversion:</text>
                    <text x="117" y="303" text-anchor="middle" font-size="9" fill="var(--svg-accent)">Impeller: KE ↑ (velocity)</text>
                    <text x="117" y="318" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">Volute: KE → PE (pressure)</text>
                </svg>
                <div class="figcaption">Figure 8.3b: Centrifugal pump cross-section — the impeller vanes throw water outward by centrifugal force; the expanding volute converts velocity to pressure head.</div>
            </div>'''

# ============================================================
# 2. RECIPROCATING PUMP — piston/cylinder/valve diagram
# ============================================================
SVG_RECIP = '''<div class="figure-container">
                <svg width="560" height="330" viewBox="0 0 560 330" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="280" y="20" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Reciprocating Pump — Mechanism</text>

                    <!-- Cylinder body -->
                    <rect x="140" y="90" width="260" height="100" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2.5" rx="3"/>

                    <!-- Piston -->
                    <rect x="280" y="95" width="15" height="90" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="2" rx="2"/>
                    <text x="288" y="88" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--svg-fg)">Piston</text>

                    <!-- Piston rod -->
                    <line x1="295" y1="140" x2="380" y2="140" stroke="var(--svg-fg)" stroke-width="4"/>

                    <!-- Crank mechanism -->
                    <circle cx="420" cy="140" r="40" fill="none" stroke="var(--svg-dim)" stroke-width="1" stroke-dasharray="4,3"/>
                    <circle cx="420" cy="140" r="5" fill="var(--svg-fg)"/>
                    <line x1="420" y1="140" x2="455" y2="120" stroke="var(--svg-fg)" stroke-width="3"/>
                    <circle cx="455" cy="120" r="4" fill="var(--svg-accent)"/>
                    <!-- Connecting rod -->
                    <line x1="380" y1="140" x2="455" y2="120" stroke="var(--svg-fg)" stroke-width="2.5"/>
                    <text x="420" y="195" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Crank</text>

                    <!-- Rotation arrow -->
                    <path d="M445,165 A30,30 0 0,1 395,165" fill="none" stroke="var(--svg-red-accent)" stroke-width="1.5" marker-end="url(#arr)"/>

                    <!-- Water in cylinder -->
                    <rect x="145" y="95" width="133" height="90" fill="var(--svg-water)" fill-opacity="0.2" stroke="none"/>

                    <!-- Suction valve (bottom left) -->
                    <rect x="170" y="190" width="30" height="6" fill="var(--svg-accent)" stroke="var(--svg-fg)" stroke-width="1.5" rx="1"/>
                    <line x1="185" y1="196" x2="185" y2="230" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="185" y="248" text-anchor="middle" font-size="8" fill="var(--svg-accent)">Suction</text>
                    <text x="185" y="260" text-anchor="middle" font-size="8" fill="var(--svg-accent)">valve</text>

                    <!-- Delivery valve (top left) -->
                    <rect x="220" y="84" width="30" height="6" fill="var(--svg-green-accent)" stroke="var(--svg-fg)" stroke-width="1.5" rx="1"/>
                    <line x1="235" y1="84" x2="235" y2="55" stroke="var(--svg-fg)" stroke-width="2"/>
                    <line x1="235" y1="55" x2="235" y2="35" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="258" y="52" font-size="8" fill="var(--svg-green-accent)">Delivery</text>
                    <text x="258" y="64" font-size="8" fill="var(--svg-green-accent)">valve</text>

                    <!-- Suction pipe from below -->
                    <line x1="185" y1="230" x2="185" y2="268" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="185" y="282" text-anchor="middle" font-size="8" fill="var(--svg-water-3)">From source</text>

                    <!-- Flow arrows -->
                    <line x1="185" y1="268" x2="185" y2="200" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)" stroke-dasharray="5,3"/>
                    <text x="145" y="220" text-anchor="end" font-size="7" fill="var(--svg-water-3)">Suction</text>
                    <text x="145" y="232" text-anchor="end" font-size="7" fill="var(--svg-water-3)">stroke ↑</text>

                    <line x1="235" y1="95" x2="235" y2="42" stroke="var(--svg-green-accent)" stroke-width="1.5" marker-end="url(#arr)" stroke-dasharray="5,3"/>
                    <text x="270" y="42" font-size="7" fill="var(--svg-green-accent)">Delivery</text>
                    <text x="270" y="52" font-size="7" fill="var(--svg-green-accent)">stroke ↑</text>

                    <!-- Stroke length dimension -->
                    <line x1="280" y1="205" x2="400" y2="205" stroke="var(--svg-dim)" stroke-width="1"/>
                    <line x1="280" y1="200" x2="280" y2="210" stroke="var(--svg-dim)" stroke-width="1"/>
                    <line x1="400" y1="200" x2="400" y2="210" stroke="var(--svg-dim)" stroke-width="1"/>
                    <text x="340" y="220" text-anchor="middle" font-size="8" fill="var(--svg-dim)">L (stroke)</text>

                    <!-- Equations -->
                    <rect x="80" y="292" width="400" height="30" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="280" y="312" text-anchor="middle" font-size="11" fill="var(--svg-fg)">
                        Q = ALN/60 <tspan font-size="9" fill="var(--svg-muted)">(single-acting)</tspan>
                        <tspan dx="20">Q = 2ALN/60</tspan> <tspan font-size="9" fill="var(--svg-muted)">(double-acting)</tspan>
                    </text>
                </svg>
                <div class="figcaption">Figure 8.4b: Reciprocating pump mechanism — crank rotates → piston reciprocates → alternating suction and delivery strokes with one-way valves.</div>
            </div>'''

# ============================================================
# 3. POWER CHAIN — flowchart with PROPER equations
# ============================================================
SVG_POWER = '''<div class="figure-container">
                <svg width="560" height="250" viewBox="0 0 560 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="280" y="20" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Pump Power Calculation Chain</text>

                    <!-- Water Power box -->
                    <rect x="20" y="55" width="150" height="75" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <text x="95" y="78" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Water Power</text>
                    <text x="95" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="var(--svg-fg)">
                        P<tspan baseline-shift="sub" font-size="75%">w</tspan> = γQH
                    </text>
                    <text x="95" y="120" text-anchor="middle" font-size="8" fill="var(--svg-muted)">= 9.81 × Q × TDH (kW)</text>

                    <!-- Arrow 1 -->
                    <line x1="175" y1="92" x2="210" y2="92" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="193" y="86" text-anchor="middle" font-size="8" fill="var(--svg-red-accent)">÷ η<tspan baseline-shift="sub" font-size="75%">p</tspan></text>

                    <!-- Shaft Power box -->
                    <rect x="215" y="55" width="150" height="75" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2.5"/>
                    <text x="290" y="78" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Shaft Power</text>
                    <text x="290" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="var(--svg-fg)">
                        P<tspan baseline-shift="sub" font-size="75%">s</tspan> = P<tspan baseline-shift="sub" font-size="75%">w</tspan> / η<tspan baseline-shift="sub" font-size="75%">p</tspan>
                    </text>
                    <text x="290" y="120" text-anchor="middle" font-size="8" fill="var(--svg-muted)">η<tspan baseline-shift="sub" font-size="75%">p</tspan> = 60–85%</text>

                    <!-- Arrow 2 -->
                    <line x1="370" y1="92" x2="405" y2="92" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="388" y="86" text-anchor="middle" font-size="8" fill="var(--svg-red-accent)">÷ η<tspan baseline-shift="sub" font-size="75%">m</tspan></text>

                    <!-- Motor Power box -->
                    <rect x="410" y="55" width="140" height="75" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="2.5"/>
                    <text x="480" y="78" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-orange-accent)">Motor Power</text>
                    <text x="480" y="100" text-anchor="middle" font-size="14" font-weight="bold" fill="var(--svg-fg)">
                        P<tspan baseline-shift="sub" font-size="75%">m</tspan> = P<tspan baseline-shift="sub" font-size="75%">s</tspan> / η<tspan baseline-shift="sub" font-size="75%">m</tspan>
                    </text>
                    <text x="480" y="120" text-anchor="middle" font-size="8" fill="var(--svg-muted)">η<tspan baseline-shift="sub" font-size="75%">m</tspan> = 85–95%</text>

                    <!-- Efficiency diagram below -->
                    <rect x="70" y="155" width="420" height="40" rx="3" fill="none" stroke="var(--svg-dim)" stroke-width="1.5"/>
                    <rect x="70" y="155" width="420" height="40" rx="3" fill="var(--svg-green-accent)" fill-opacity="0.08"/>
                    <rect x="70" y="155" width="300" height="40" fill="var(--svg-green-accent)" fill-opacity="0.08"/>
                    <rect x="70" y="155" width="180" height="40" fill="var(--svg-green-accent)" fill-opacity="0.08"/>
                    <line x1="250" y1="155" x2="250" y2="195" stroke="var(--svg-dim)" stroke-width="1" stroke-dasharray="4,3"/>
                    <line x1="370" y1="155" x2="370" y2="195" stroke="var(--svg-dim)" stroke-width="1" stroke-dasharray="4,3"/>
                    <text x="160" y="178" text-anchor="middle" font-size="9" fill="var(--svg-accent)">P<tspan baseline-shift="sub" font-size="75%">w</tspan></text>
                    <text x="310" y="178" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">Pump losses</text>
                    <text x="420" y="178" text-anchor="middle" font-size="9" fill="var(--svg-orange-accent)">Motor losses</text>

                    <!-- Overall equation -->
                    <rect x="100" y="210" width="360" height="30" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="280" y="231" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">
                        P<tspan baseline-shift="sub" font-size="75%">m</tspan> = γQH / (η<tspan baseline-shift="sub" font-size="75%">p</tspan> × η<tspan baseline-shift="sub" font-size="75%">m</tspan>)
                        <tspan dx="10" font-size="9" font-weight="normal" fill="var(--svg-muted)">→ select next standard size UP</tspan>
                    </text>
                </svg>
                <div class="figcaption">Figure 8.10c: Power calculation chain — water power (γQH) divided by pump efficiency gives shaft power, divided by motor efficiency gives motor power.</div>
            </div>'''

# ============================================================
# 4. SPECIFIC SPEED — impeller shapes comparison
# ============================================================
SVG_SPECIFIC_SPEED = '''<div class="figure-container">
                <svg width="560" height="280" viewBox="0 0 560 280" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="280" y="20" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Specific Speed — Impeller Type Selection</text>

                    <!-- Equation -->
                    <text x="280" y="45" text-anchor="middle" font-size="14" font-weight="bold" fill="var(--svg-fg)">
                        N<tspan baseline-shift="sub" font-size="75%">s</tspan> = N√Q / H<tspan baseline-shift="super" font-size="75%">3/4</tspan>
                    </text>
                    <text x="280" y="62" text-anchor="middle" font-size="9" fill="var(--svg-muted)">N = rpm, Q = m³/s, H = m per stage</text>

                    <!-- Scale bar -->
                    <line x1="50" y1="90" x2="510" y2="90" stroke="var(--svg-fg)" stroke-width="2"/>
                    <line x1="50" y1="86" x2="50" y2="94" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="210" y1="86" x2="210" y2="94" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="360" y1="86" x2="360" y2="94" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="510" y1="86" x2="510" y2="94" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="50" y="82" text-anchor="middle" font-size="8" fill="var(--svg-fg)">500</text>
                    <text x="210" y="82" text-anchor="middle" font-size="8" fill="var(--svg-fg)">4000</text>
                    <text x="360" y="82" text-anchor="middle" font-size="8" fill="var(--svg-fg)">10000</text>
                    <text x="510" y="82" text-anchor="middle" font-size="8" fill="var(--svg-fg)">15000+</text>
                    <text x="280" y="78" text-anchor="middle" font-size="8" fill="var(--svg-dim)">N<tspan baseline-shift="sub" font-size="75%">s</tspan> →</text>

                    <!-- RADIAL FLOW impeller (disk shape, wide) -->
                    <ellipse cx="130" cy="155" rx="55" ry="20" fill="var(--svg-accent)" fill-opacity="0.2" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="130" y1="135" x2="130" y2="175" stroke="var(--svg-accent)" stroke-width="1.5" stroke-dasharray="3,2"/>
                    <!-- Vane lines -->
                    <path d="M110,155 C115,148 120,142 130,138" fill="none" stroke="var(--svg-accent)" stroke-width="1.2"/>
                    <path d="M150,155 C145,148 140,142 130,138" fill="none" stroke="var(--svg-accent)" stroke-width="1.2"/>
                    <path d="M110,155 C115,162 120,168 130,172" fill="none" stroke="var(--svg-accent)" stroke-width="1.2"/>
                    <path d="M150,155 C145,162 140,168 130,172" fill="none" stroke="var(--svg-accent)" stroke-width="1.2"/>
                    <text x="130" y="190" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-accent)">Radial Flow</text>
                    <text x="130" y="205" text-anchor="middle" font-size="9" fill="var(--svg-fg)">High H, Low Q</text>
                    <text x="130" y="220" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Flat, wide impeller</text>

                    <!-- MIXED FLOW impeller (cone shape) -->
                    <path d="M250,165 L280,130 L310,165 Z" fill="var(--svg-green-accent)" fill-opacity="0.2" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <ellipse cx="280" cy="165" rx="30" ry="10" fill="none" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <line x1="280" y1="130" x2="280" y2="175" stroke="var(--svg-green-accent)" stroke-width="1.5" stroke-dasharray="3,2"/>
                    <text x="280" y="190" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-green-accent)">Mixed Flow</text>
                    <text x="280" y="205" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Med H, Med Q</text>
                    <text x="280" y="220" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Conical impeller</text>

                    <!-- AXIAL FLOW impeller (propeller) -->
                    <line x1="430" y1="135" x2="430" y2="175" stroke="var(--svg-orange-accent)" stroke-width="2"/>
                    <path d="M430,155 C420,140 405,135 395,140" fill="none" stroke="var(--svg-orange-accent)" stroke-width="2.5"/>
                    <path d="M430,155 C440,140 455,135 465,140" fill="none" stroke="var(--svg-orange-accent)" stroke-width="2.5"/>
                    <path d="M430,155 C420,170 405,175 395,170" fill="none" stroke="var(--svg-orange-accent)" stroke-width="2.5"/>
                    <path d="M430,155 C440,170 455,175 465,170" fill="none" stroke="var(--svg-orange-accent)" stroke-width="2.5"/>
                    <circle cx="430" cy="155" r="3" fill="var(--svg-orange-accent)"/>
                    <text x="430" y="190" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-orange-accent)">Axial Flow</text>
                    <text x="430" y="205" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Low H, High Q</text>
                    <text x="430" y="220" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Propeller blades</text>

                    <!-- Efficiency note -->
                    <rect x="90" y="238" width="380" height="28" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-dim)" stroke-width="1"/>
                    <text x="280" y="257" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Same N<tspan baseline-shift="sub" font-size="75%">s</tspan> → geometrically similar → same peak efficiency</text>
                </svg>
                <div class="figcaption">Figure 8.10d: Specific speed determines impeller shape — low N<tspan baseline-shift="sub" font-size="75%">s</tspan> selects flat radial-flow impellers (high head), high N<tspan baseline-shift="sub" font-size="75%">s</tspan> selects propeller-type axial flow (high discharge).</div>
            </div>'''

with open(FILE, 'r', encoding='utf-8') as f:
    html = f.read()

original = html.count('<svg')

html = find_and_replace_svg(html, 'Centrifugal pump components', SVG_CENTRIFUGAL)
html = find_and_replace_svg(html, 'Reciprocating pump operation', SVG_RECIP)
html = find_and_replace_svg(html, 'Power calculation chain', SVG_POWER)
html = find_and_replace_svg(html, 'Specific speed determines pump impeller type', SVG_SPECIFIC_SPEED)

new_count = html.count('<svg')
with open(FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nChapter 8: Before {original} SVGs, After {new_count} SVGs")

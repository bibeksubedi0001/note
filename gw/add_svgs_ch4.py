"""Add 10 new educational SVG diagrams to Chapter 4 (Well Hydraulics)."""
import re

FILE = r"d:\Final Year\Theory\gw\GW_THE\chapter4.html"

def svg_wrap(svg_content, caption):
    return f'''
            <div class="figure-container">
{svg_content}
                <div class="figcaption">{caption}</div>
            </div>
'''

SVGS = {}

# 1. Radius of influence concept
SVGS['Radius of Influence (R)'] = svg_wrap('''
                <svg width="550" height="250" viewBox="0 0 550 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Radius of Influence &amp; Area of Influence</text>
                    <ellipse cx="275" cy="140" rx="220" ry="90" fill="var(--svg-water)" stroke="var(--svg-accent)" stroke-width="1.5" fill-opacity="0.2"/>
                    <text x="275" y="235" text-anchor="middle" font-size="10" fill="var(--svg-accent)">Area of influence (plan view)</text>
                    <circle cx="275" cy="140" r="6" fill="var(--svg-red-accent)"/>
                    <text x="275" y="125" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-red-accent)">Pumping well</text>
                    <line x1="281" y1="140" x2="495" y2="140" stroke="var(--svg-fg)" stroke-width="1.5" stroke-dasharray="5,3"/>
                    <text x="390" y="135" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">R (radius of influence)</text>
                    <circle cx="370" cy="170" r="4" fill="var(--svg-green-accent)"/>
                    <text x="385" y="175" font-size="9" fill="var(--svg-green-accent)">OW₁ (s &gt; 0)</text>
                    <circle cx="430" cy="115" r="4" fill="var(--svg-green-accent)"/>
                    <text x="450" y="112" font-size="9" fill="var(--svg-green-accent)">OW₂ (s &gt; 0)</text>
                    <circle cx="510" cy="160" r="4" fill="var(--svg-fg)"/>
                    <text x="530" y="160" font-size="9" fill="var(--svg-muted)">No effect</text>
                    <text x="275" y="90" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Inside R: drawdown s &gt; 0</text>
                    <text x="275" y="248" text-anchor="middle" font-size="10" fill="var(--svg-fg)">R depends on: pumping rate Q, aquifer T &amp; S, and time t</text>
                </svg>''',
    'Figure 4.2b: Plan view — radius of influence (R) defines the boundary beyond which pumping has no measurable effect on the water table.')

# 2. Well yield and specific capacity
SVGS['Specific Capacity'] = svg_wrap('''
                <svg width="550" height="250" viewBox="0 0 550 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Specific Capacity — Q/s Relationship</text>
                    <line x1="80" y1="200" x2="500" y2="200" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="80" y1="200" x2="80" y2="40" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="290" y="225" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Drawdown, s (m)</text>
                    <text x="55" y="120" text-anchor="middle" font-size="11" fill="var(--svg-fg)" transform="rotate(-90 55 120)">Discharge, Q (m³/s)</text>
                    <line x1="80" y1="190" x2="300" y2="80" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <path d="M300,80 C350,65 400,55 470,52" fill="none" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <text x="200" y="110" font-size="10" fill="var(--svg-accent)" transform="rotate(-28 200 110)">Linear region</text>
                    <text x="400" y="48" font-size="10" fill="var(--svg-accent)">Nonlinear (well losses)</text>
                    <line x1="150" y1="165" x2="280" y2="80" stroke="var(--svg-green-accent)" stroke-width="1" stroke-dasharray="4,3"/>
                    <text x="185" y="140" font-size="10" fill="var(--svg-green-accent)">Slope = Sc</text>
                    <text x="275" y="240" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Specific Capacity: S_c = Q/s [m²/s or m³/day/m]</text>
                    <rect x="310" y="140" width="170" height="45" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="395" y="158" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Higher S_c = more efficient</text>
                    <text x="395" y="174" text-anchor="middle" font-size="9" fill="var(--svg-fg)">S_c decreases with time &amp; Q</text>
                </svg>''',
    'Figure 4.3b: Specific capacity (Q/s) measures well productivity — it decreases at higher pumping rates due to non-linear well losses.')

# 3. Thiem equation setup with two observation wells
SVGS['General form between two observation wells'] = svg_wrap('''
                <svg width="600" height="300" viewBox="0 0 600 300" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Thiem Equation — Two Observation Wells (Confined)</text>
                    <rect x="50" y="230" width="500" height="20" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <rect x="50" y="60" width="500" height="15" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="50" y="75" width="500" height="155" fill="var(--svg-water)" stroke="none" fill-opacity="0.15"/>
                    <text x="300" y="170" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Confined aquifer (T = Kb)</text>
                    <rect x="296" y="40" width="8" height="210" fill="var(--svg-fg)" stroke="none"/>
                    <text x="300" y="35" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-red-accent)">Pumping Well</text>
                    <line x1="300" y1="45" x2="300" y2="30" stroke="var(--svg-red-accent)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="310" y="30" font-size="9" fill="var(--svg-red-accent)">Q</text>
                    <path d="M50,50 C150,45 250,40 296,48" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <path d="M304,48 C350,40 450,45 550,50" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="130" y="42" font-size="10" fill="var(--svg-accent)">Piezometric surface</text>
                    <rect x="196" y="45" width="3" height="205" fill="var(--svg-green-accent)" stroke="none"/>
                    <text x="196" y="267" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">OW₁ (r₁, h₁)</text>
                    <rect x="426" y="48" width="3" height="202" fill="var(--svg-orange-accent)" stroke="none"/>
                    <text x="428" y="267" text-anchor="middle" font-size="9" fill="var(--svg-orange-accent)">OW₂ (r₂, h₂)</text>
                    <line x1="300" y1="210" x2="198" y2="210" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="250" y="205" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">r₁</text>
                    <line x1="300" y1="215" x2="427" y2="215" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="365" y="225" text-anchor="middle" font-size="9" fill="var(--svg-orange-accent)">r₂</text>
                    <text x="300" y="288" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">T = Q·ln(r₂/r₁) / [2π(h₂−h₁)]</text>
                </svg>''',
    'Figure 4.5b: Thiem equation with two observation wells — T is determined from the measured heads h₁ and h₂ at distances r₁ and r₂.', )

# 4. Confined vs unconfined comparison  
SVGS['Comparison: Confined vs. Unconfined'] = svg_wrap('''
                <svg width="650" height="220" viewBox="0 0 650 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="325" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Thiem vs Dupuit — Steady-State Well Formulas</text>
                    <rect x="20" y="40" width="290" height="160" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="165" y="62" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">CONFINED (Thiem)</text>
                    <line x1="40" y1="70" x2="290" y2="70" stroke="var(--svg-accent)" stroke-width="0.8"/>
                    <text x="165" y="90" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Constant thickness b</text>
                    <text x="165" y="110" text-anchor="middle" font-size="10" fill="var(--svg-fg)">T = Kb (constant)</text>
                    <text x="165" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-accent)">Q = 2πT(h₂−h₁)/ln(r₂/r₁)</text>
                    <text x="165" y="160" text-anchor="middle" font-size="10" fill="var(--svg-fg)">h varies linearly with ln(r)</text>
                    <text x="165" y="180" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Piezometric surface is lowered</text>
                    <text x="165" y="193" text-anchor="middle" font-size="9" fill="var(--svg-muted)">but aquifer stays fully saturated</text>
                    <rect x="340" y="40" width="290" height="160" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="485" y="62" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">UNCONFINED (Dupuit)</text>
                    <line x1="360" y1="70" x2="610" y2="70" stroke="var(--svg-green-accent)" stroke-width="0.8"/>
                    <text x="485" y="90" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Variable thickness h(r)</text>
                    <text x="485" y="110" text-anchor="middle" font-size="10" fill="var(--svg-fg)">T = Kh (varies with r)</text>
                    <text x="485" y="135" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-green-accent)">Q = πK(h₂²−h₁²)/ln(r₂/r₁)</text>
                    <text x="485" y="160" text-anchor="middle" font-size="10" fill="var(--svg-fg)">h² varies linearly with ln(r)</text>
                    <text x="485" y="180" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Water table drops → saturated</text>
                    <text x="485" y="193" text-anchor="middle" font-size="9" fill="var(--svg-muted)">thickness reduces near well</text>
                </svg>''',
    'Figure 4.6b: Comparison of steady-state well equations — Thiem (confined, h-based) vs Dupuit (unconfined, h²-based).')

# 5. Theis type curve concept
SVGS['Theis Type-Curve Method'] = svg_wrap('''
                <svg width="550" height="260" viewBox="0 0 550 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Theis Type-Curve Matching</text>
                    <line x1="60" y1="210" x2="500" y2="210" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="60" y1="210" x2="60" y2="40" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="280" y="237" text-anchor="middle" font-size="10" fill="var(--svg-fg)">1/u  or  r²/t  (log scale)</text>
                    <text x="35" y="125" text-anchor="middle" font-size="10" fill="var(--svg-fg)" transform="rotate(-90 35 125)">W(u)  or  s  (log scale)</text>
                    <path d="M80,200 C120,195 180,180 240,150 C300,120 380,80 470,55" fill="none" stroke="var(--svg-accent)" stroke-width="3"/>
                    <text x="450" y="50" font-size="10" font-weight="bold" fill="var(--svg-accent)">Type curve W(u)</text>
                    <circle cx="200" cy="170" r="3" fill="var(--svg-red-accent)"/>
                    <circle cx="240" cy="155" r="3" fill="var(--svg-red-accent)"/>
                    <circle cx="280" cy="140" r="3" fill="var(--svg-red-accent)"/>
                    <circle cx="310" cy="125" r="3" fill="var(--svg-red-accent)"/>
                    <circle cx="350" cy="108" r="3" fill="var(--svg-red-accent)"/>
                    <circle cx="380" cy="95" r="3" fill="var(--svg-red-accent)"/>
                    <circle cx="420" cy="78" r="3" fill="var(--svg-red-accent)"/>
                    <text x="340" y="165" font-size="10" fill="var(--svg-red-accent)">Field data (s vs r²/t)</text>
                    <circle cx="310" cy="125" r="12" fill="none" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="330" y="140" font-size="9" fill="var(--svg-green-accent)">Match point</text>
                    <text x="275" y="250" text-anchor="middle" font-size="10" fill="var(--svg-fg)">At match: T = QW(u)/(4πs),  S = 4Tu/r²×t</text>
                </svg>''',
    'Figure 4.7b: Theis type-curve matching — overlay field data (s vs r²/t) on the standard W(u) vs 1/u curve to find T and S at the match point.')

# 6. Cooper-Jacob straight line
SVGS['Cooper–Jacob Straight-Line Method'] = svg_wrap('''
                <svg width="500" height="260" viewBox="0 0 500 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="250" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Cooper–Jacob Straight-Line Method</text>
                    <line x1="60" y1="40" x2="60" y2="210" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="60" y1="40" x2="460" y2="40" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="260" y="30" text-anchor="middle" font-size="10" fill="var(--svg-fg)">log(t)</text>
                    <text x="35" y="125" text-anchor="middle" font-size="10" fill="var(--svg-fg)" transform="rotate(-90 35 125)">Drawdown s (↓)</text>
                    <circle cx="100" cy="50" r="3" fill="var(--svg-accent)"/>
                    <circle cx="140" cy="58" r="3" fill="var(--svg-accent)"/>
                    <circle cx="170" cy="67" r="3" fill="var(--svg-accent)"/>
                    <circle cx="200" cy="80" r="3" fill="var(--svg-accent)"/>
                    <circle cx="240" cy="95" r="3" fill="var(--svg-accent)"/>
                    <circle cx="280" cy="110" r="3" fill="var(--svg-accent)"/>
                    <circle cx="320" cy="125" r="3" fill="var(--svg-accent)"/>
                    <circle cx="360" cy="140" r="3" fill="var(--svg-accent)"/>
                    <circle cx="400" cy="155" r="3" fill="var(--svg-accent)"/>
                    <line x1="130" y1="55" x2="430" y2="170" stroke="var(--svg-green-accent)" stroke-width="2.5"/>
                    <text x="420" y="195" font-size="10" fill="var(--svg-green-accent)">Best-fit line</text>
                    <line x1="200" y1="80" x2="200" y2="140" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <line x1="350" y1="80" x2="350" y2="140" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <line x1="200" y1="140" x2="350" y2="140" stroke="var(--svg-red-accent)" stroke-width="1" stroke-dasharray="3,3"/>
                    <text x="275" y="155" text-anchor="middle" font-size="10" fill="var(--svg-red-accent)">Δs per log cycle</text>
                    <line x1="80" y1="43" x2="80" y2="55" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="80" y="65" text-anchor="middle" font-size="8" fill="var(--svg-fg)">t₀</text>
                    <text x="80" y="78" text-anchor="middle" font-size="8" fill="var(--svg-muted)">(s=0)</text>
                    <text x="250" y="210" text-anchor="middle" font-size="11" fill="var(--svg-fg)">T = 2.3Q/(4πΔs)</text>
                    <text x="250" y="230" text-anchor="middle" font-size="11" fill="var(--svg-fg)">S = 2.25Tt₀/r²</text>
                    <text x="250" y="250" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Valid when u &lt; 0.01 (late-time data)</text>
                </svg>''',
    'Figure 4.7c: Cooper–Jacob method — plot s vs log(t), fit a straight line, and compute T from the slope Δs and S from the t₀ intercept.')

# 7. Recovery test
SVGS['Recovery Test'] = svg_wrap('''
                <svg width="550" height="260" viewBox="0 0 550 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Recovery Test — Residual Drawdown Method</text>
                    <line x1="60" y1="40" x2="60" y2="200" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="60" y1="40" x2="500" y2="40" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="280" y="30" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Time</text>
                    <text x="35" y="120" text-anchor="middle" font-size="10" fill="var(--svg-fg)" transform="rotate(-90 35 120)">Drawdown (↓)</text>
                    <path d="M60,45 C100,55 160,90 220,120 C260,140 280,150 280,155" fill="none" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <text x="180" y="85" font-size="9" fill="var(--svg-accent)">Pumping phase</text>
                    <line x1="280" y1="40" x2="280" y2="200" stroke="var(--svg-red-accent)" stroke-width="1.5" stroke-dasharray="5,3"/>
                    <text x="280" y="215" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-red-accent)">Pump OFF (t'=0)</text>
                    <path d="M280,155 C310,145 350,120 400,90 C430,75 470,60 490,55" fill="none" stroke="var(--svg-green-accent)" stroke-width="2.5"/>
                    <text x="420" y="105" font-size="9" fill="var(--svg-green-accent)">Recovery phase</text>
                    <line x1="280" y1="155" x2="490" y2="155" stroke="var(--svg-fg)" stroke-width="0.8" stroke-dasharray="3,3"/>
                    <line x1="420" y1="155" x2="420" y2="85" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="440" y="125" font-size="10" fill="var(--svg-orange-accent)">s' (residual)</text>
                    <text x="275" y="240" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Plot s' vs log(t/t') → T = 2.3Q/(4πΔs')</text>
                    <text x="275" y="255" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Recovery data gives T independent of S — useful for verification</text>
                </svg>''',
    'Figure 4.7d: Recovery test — after the pump is shut off, residual drawdown s\' is plotted vs log(t/t\') to determine T from the straight-line slope.')

# 8. Partially penetrating well
SVGS['Effect on Flow and Drawdown'] = svg_wrap('''
                <svg width="500" height="300" viewBox="0 0 500 300" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="250" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Partially vs Fully Penetrating Well</text>
                    <rect x="30" y="55" width="200" height="15" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="30" y="220" width="200" height="15" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="30" y="70" width="200" height="150" fill="var(--svg-water)" stroke="none" fill-opacity="0.15"/>
                    <rect x="126" y="40" width="8" height="195" fill="var(--svg-fg)" stroke="none"/>
                    <text x="130" y="38" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-fg)">Full</text>
                    <line x1="55" y1="70" x2="55" y2="220" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <text x="45" y="148" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">b</text>
                    <line x1="100" y1="90" x2="126" y2="90" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="100" y1="120" x2="126" y2="120" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="100" y1="150" x2="126" y2="150" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="100" y1="180" x2="126" y2="180" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="100" y1="210" x2="126" y2="210" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="85" y="105" font-size="8" fill="var(--svg-water-3)">Horizontal</text>
                    <text x="85" y="115" font-size="8" fill="var(--svg-water-3)">flow only</text>
                    <rect x="270" y="55" width="200" height="15" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="270" y="220" width="200" height="15" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="270" y="70" width="200" height="150" fill="var(--svg-water)" stroke="none" fill-opacity="0.15"/>
                    <rect x="366" y="40" width="8" height="100" fill="var(--svg-fg)" stroke="none"/>
                    <text x="370" y="38" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-red-accent)">Partial</text>
                    <line x1="295" y1="70" x2="295" y2="140" stroke="var(--svg-red-accent)" stroke-width="1"/>
                    <text x="285" y="108" text-anchor="middle" font-size="9" fill="var(--svg-red-accent)">l</text>
                    <path d="M340,90 C350,95 360,100 366,100" fill="none" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <path d="M330,130 C340,135 355,140 366,135" fill="none" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <path d="M340,170 C350,155 360,145 366,138" fill="none" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <path d="M340,200 C350,185 360,165 366,138" fill="none" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="320" y="210" font-size="8" fill="var(--svg-water-3)">3D flow</text>
                    <text x="320" y="222" font-size="8" fill="var(--svg-water-3)">(vertical comp.)</text>
                    <text x="250" y="255" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Partially penetrating well: s_p &gt; s_f (extra head loss)</text>
                    <text x="250" y="275" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Convergence of flow lines → 3D effects near the well screen</text>
                    <text x="250" y="293" text-anchor="middle" font-size="9" fill="var(--svg-muted)">At distance r &gt; 1.5b, effect of partial penetration vanishes</text>
                </svg>''',
    'Figure 4.8b: Fully penetrating well has horizontal flow only; partially penetrating well develops vertical flow components, increasing drawdown near the well.')

# 9. Well interference / superposition
SVGS['Principle of Superposition'] = svg_wrap('''
                <svg width="600" height="260" viewBox="0 0 600 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Superposition Principle — Multiple Wells</text>
                    <line x1="30" y1="200" x2="570" y2="200" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="300" y="218" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Ground surface</text>
                    <line x1="30" y1="100" x2="570" y2="100" stroke="var(--svg-accent)" stroke-width="1.5" stroke-dasharray="6,3"/>
                    <text x="570" y="95" text-anchor="end" font-size="9" fill="var(--svg-accent)">Static WT</text>
                    <path d="M30,100 C100,105 150,125 200,140" fill="none" stroke="var(--svg-water-3)" stroke-width="1.5" stroke-dasharray="4,3"/>
                    <path d="M200,140 C250,125 300,105 350,105 C400,105 450,120 500,135" fill="none" stroke="var(--svg-water-3)" stroke-width="1.5" stroke-dasharray="4,3"/>
                    <path d="M500,135 C530,115 555,105 570,100" fill="none" stroke="var(--svg-water-3)" stroke-width="1.5" stroke-dasharray="4,3"/>
                    <text x="140" y="162" font-size="9" fill="var(--svg-water-3)">Individual cones</text>
                    <path d="M30,100 C100,110 150,140 200,160 C250,150 300,130 350,135 C400,130 450,150 500,160 C530,130 555,110 570,100" fill="none" stroke="var(--svg-red-accent)" stroke-width="2.5"/>
                    <text x="300" y="170" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-red-accent)">Combined drawdown</text>
                    <rect x="196" y="95" width="8" height="110" fill="var(--svg-fg)" stroke="none"/>
                    <text x="200" y="88" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Well A</text>
                    <rect x="496" y="95" width="8" height="105" fill="var(--svg-fg)" stroke="none"/>
                    <text x="500" y="88" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Well B</text>
                    <text x="300" y="240" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">s_total = s_A + s_B (superposition)</text>
                    <text x="300" y="258" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Valid for linear (confined) aquifers; approximate correction needed for unconfined</text>
                </svg>''',
    'Figure 4.9b: Superposition principle — total drawdown at any point equals the sum of individual drawdowns from each well.')

# 10. Well configurations
SVGS['Uses and Well Configurations'] = svg_wrap('''
                <svg width="600" height="240" viewBox="0 0 600 240" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Common Multi-Well Configurations</text>
                    <rect x="20" y="45" width="170" height="160" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="105" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-accent)">Line of Wells</text>
                    <circle cx="55" cy="130" r="5" fill="var(--svg-red-accent)"/>
                    <circle cx="85" cy="130" r="5" fill="var(--svg-red-accent)"/>
                    <circle cx="115" cy="130" r="5" fill="var(--svg-red-accent)"/>
                    <circle cx="145" cy="130" r="5" fill="var(--svg-red-accent)"/>
                    <text x="105" y="160" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Dewatering along</text>
                    <text x="105" y="174" text-anchor="middle" font-size="9" fill="var(--svg-fg)">excavation / trench</text>
                    <text x="105" y="195" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Interference increases</text>
                    <text x="105" y="198" text-anchor="middle" font-size="9" fill="var(--svg-muted)">total drawdown</text>
                    <rect x="215" y="45" width="170" height="160" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="300" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-green-accent)">Circular Array</text>
                    <circle cx="300" cy="125" r="35" fill="none" stroke="var(--svg-fg)" stroke-width="1" stroke-dasharray="3,3"/>
                    <circle cx="300" cy="90" r="5" fill="var(--svg-red-accent)"/>
                    <circle cx="330" cy="108" r="5" fill="var(--svg-red-accent)"/>
                    <circle cx="330" cy="142" r="5" fill="var(--svg-red-accent)"/>
                    <circle cx="300" cy="160" r="5" fill="var(--svg-red-accent)"/>
                    <circle cx="270" cy="142" r="5" fill="var(--svg-red-accent)"/>
                    <circle cx="270" cy="108" r="5" fill="var(--svg-red-accent)"/>
                    <text x="300" y="180" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Dewatering for</text>
                    <text x="300" y="194" text-anchor="middle" font-size="9" fill="var(--svg-fg)">circular excavation</text>
                    <rect x="410" y="45" width="170" height="160" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="495" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-orange-accent)">Well + Recharge</text>
                    <circle cx="465" cy="125" r="5" fill="var(--svg-red-accent)"/>
                    <text x="465" y="115" text-anchor="middle" font-size="8" fill="var(--svg-red-accent)">−Q</text>
                    <circle cx="525" cy="125" r="5" fill="var(--svg-green-accent)"/>
                    <text x="525" y="115" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">+Q</text>
                    <text x="495" y="160" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Image well for</text>
                    <text x="495" y="174" text-anchor="middle" font-size="9" fill="var(--svg-fg)">boundary effects</text>
                    <text x="300" y="228" text-anchor="middle" font-size="10" font-style="italic" fill="var(--svg-fg)">In all configurations: s_total at any point = Σ individual drawdowns (superposition)</text>
                </svg>''',
    'Figure 4.9c: Common multi-well configurations — line of wells for dewatering, circular arrays, and image wells for boundary simulation.')


def inject_svgs(html, svgs):
    count = 0
    for heading_text, svg_html in svgs.items():
        pattern = re.compile(
            r'(<h3>[^<]*' + re.escape(heading_text[:30]) + r'[^<]*</h3>\s*)',
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

print(f"\nChapter 4: {c} SVGs inserted")
print(f"  Before: {original} SVGs, After: {new_count} SVGs")
print(f"  Net added: {new_count - original}")

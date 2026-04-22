"""Add 10 new educational SVG diagrams to Chapter 2 (Groundwater Motion)."""
import re

FILE = r"d:\Final Year\Theory\gw\GW_THE\chapter2.html"

def svg_wrap(svg_content, caption):
    return f'''
            <div class="figure-container">
{svg_content}
                <div class="figcaption">{caption}</div>
            </div>
'''

SVGS = {}

# 1. Continuum approach — micro vs macro scale
SVGS['Why the Continuum Approach Is Important'] = svg_wrap('''
                <svg width="650" height="240" viewBox="0 0 650 240" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="325" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Microscopic vs Macroscopic (Continuum) View</text>
                    <!-- Micro view -->
                    <rect x="30" y="40" width="260" height="170" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="160" y="62" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Pore-Scale (Microscopic)</text>
                    <!-- Grains and tortuous flow -->
                    <circle cx="80" cy="110" r="18" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <circle cx="130" cy="95" r="22" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <circle cx="180" cy="115" r="20" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <circle cx="110" cy="145" r="16" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <circle cx="155" cy="155" r="19" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <circle cx="210" cy="140" r="17" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <circle cx="240" cy="100" r="15" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <!-- Tortuous path -->
                    <path d="M60,100 C70,80 100,70 115,85 C130,100 140,85 160,95 C180,105 190,90 210,100 C230,110 250,95 270,105" fill="none" stroke="var(--svg-water-3)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="160" y="193" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Tortuous flow paths around grains</text>
                    <!-- Arrow -->
                    <line x1="300" y1="125" x2="350" y2="125" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="325" y="115" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Average</text>
                    <text x="325" y="145" text-anchor="middle" font-size="9" fill="var(--svg-fg)">over REV</text>
                    <!-- Macro view -->
                    <rect x="360" y="40" width="260" height="170" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="490" y="62" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Continuum (Macroscopic)</text>
                    <rect x="390" y="80" width="200" height="80" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="490" y="110" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Uniform medium</text>
                    <text x="490" y="128" text-anchor="middle" font-size="10" fill="var(--svg-fg)">K, n defined at every point</text>
                    <line x1="390" y1="120" x2="590" y2="120" stroke="var(--svg-accent)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="490" y="193" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Smooth velocity field (Darcy flux)</text>
                    <!-- Bottom label -->
                    <text x="325" y="230" text-anchor="middle" font-size="11" font-style="italic" fill="var(--svg-fg)">REV transforms complex pore geometry → tractable continuum equations</text>
                </svg>''',
    'Figure 2.1b: The continuum approach replaces complex pore-scale flow with averaged properties (K, n) defined at every point.')

# 2. Limitations of REV  
SVGS['Limitations of the REV/Continuum Assumption'] = svg_wrap('''
                <svg width="650" height="220" viewBox="0 0 650 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="325" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Where the REV Assumption Breaks Down</text>
                    <!-- Case 1: Fractured rock -->
                    <rect x="20" y="45" width="190" height="140" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <text x="115" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-red-accent)">Fractured Rock</text>
                    <rect x="40" y="75" width="150" height="80" fill="var(--svg-struct-2)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="80" y1="75" x2="90" y2="155" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <line x1="140" y1="75" x2="130" y2="155" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="40" y1="110" x2="190" y2="115" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="115" y="175" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Discrete fractures dominate</text>
                    <!-- Case 2: Karst -->
                    <rect x="230" y="45" width="190" height="140" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <text x="325" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-red-accent)">Karst / Solution Channels</text>
                    <rect x="250" y="75" width="150" height="80" fill="var(--svg-struct-2)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <ellipse cx="300" cy="110" rx="30" ry="15" fill="var(--svg-bg-fill)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <ellipse cx="360" cy="125" rx="20" ry="10" fill="var(--svg-bg-fill)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <line x1="330" y1="110" x2="340" y2="125" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="325" y="175" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Conduit flow, not Darcian</text>
                    <!-- Case 3: Very small scale -->
                    <rect x="440" y="45" width="190" height="140" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <text x="535" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-red-accent)">Scale Too Small</text>
                    <circle cx="490" cy="110" r="20" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <circle cx="535" cy="100" r="18" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <circle cx="560" cy="125" r="16" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="510" y="108" width="8" height="8" fill="var(--svg-accent)" stroke="none"/>
                    <text x="514" y="130" font-size="7" fill="var(--svg-accent)">REV?</text>
                    <text x="535" y="175" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Volume &lt; REV size</text>
                    <text x="325" y="205" text-anchor="middle" font-size="11" font-style="italic" fill="var(--svg-fg)">In these cases, discrete-fracture or pipe-network models are needed instead</text>
                </svg>''',
    'Figure 2.2b: The REV/continuum approach fails in fractured rock, karst systems, and when the sample volume is smaller than the REV.')

# 3. Hydraulic head components
SVGS['Engineering Interpretation'] = svg_wrap('''
                <svg width="550" height="300" viewBox="0 0 550 300" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Components of Hydraulic Head</text>
                    <!-- Datum -->
                    <line x1="50" y1="260" x2="500" y2="260" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="510" y="264" font-size="10" fill="var(--svg-fg)">Datum</text>
                    <!-- Soil column -->
                    <rect x="180" y="80" width="60" height="180" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.5" fill-opacity="0.3"/>
                    <!-- Point P -->
                    <circle cx="210" cy="190" r="5" fill="var(--svg-red-accent)"/>
                    <text x="230" y="194" font-size="11" font-weight="bold" fill="var(--svg-red-accent)">P</text>
                    <!-- Piezometer tube -->
                    <rect x="240" y="50" width="4" height="210" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="240" y1="260" x2="244" y2="260" stroke="var(--svg-accent)" stroke-width="2"/>
                    <!-- Water level in piezometer -->
                    <rect x="238" y="95" width="8" height="165" fill="var(--svg-water)" stroke="none" fill-opacity="0.5"/>
                    <line x1="230" y1="95" x2="256" y2="95" stroke="var(--svg-water-3)" stroke-width="2"/>
                    <text x="268" y="99" font-size="10" fill="var(--svg-water-3)">Water level</text>
                    <!-- Elevation head z -->
                    <line x1="320" y1="260" x2="320" y2="190" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <line x1="315" y1="260" x2="325" y2="260" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <line x1="315" y1="190" x2="325" y2="190" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="345" y="230" text-anchor="start" font-size="12" font-weight="bold" fill="var(--svg-green-accent)">z</text>
                    <text x="345" y="248" font-size="9" fill="var(--svg-green-accent)">Elevation head</text>
                    <!-- Pressure head ψ -->
                    <line x1="380" y1="190" x2="380" y2="95" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="375" y1="190" x2="385" y2="190" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="375" y1="95" x2="385" y2="95" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="405" y="140" text-anchor="start" font-size="12" font-weight="bold" fill="var(--svg-accent)">ψ = p/ρg</text>
                    <text x="405" y="158" font-size="9" fill="var(--svg-accent)">Pressure head</text>
                    <!-- Total head h -->
                    <line x1="440" y1="260" x2="440" y2="95" stroke="var(--svg-fg)" stroke-width="2" stroke-dasharray="4,3"/>
                    <line x1="435" y1="95" x2="445" y2="95" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="460" y="180" text-anchor="start" font-size="12" font-weight="bold" fill="var(--svg-fg)">h</text>
                    <text x="460" y="198" font-size="9" fill="var(--svg-fg)">Total head</text>
                    <!-- Formula -->
                    <text x="275" y="290" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--svg-fg)">h = z + ψ = z + p/(ρg)</text>
                </svg>''',
    'Figure 2.5b: Hydraulic head at point P is the sum of elevation head (z) and pressure head (ψ = p/ρg) — measured by the water level in a piezometer.')

# 4. Non-Darcian flow examples
SVGS['Examples of Non-Darcian Flow in the Subsurface'] = svg_wrap('''
                <svg width="650" height="230" viewBox="0 0 650 230" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="325" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Darcy's Law Validity — Reynolds Number Regimes</text>
                    <!-- Axes -->
                    <line x1="80" y1="185" x2="600" y2="185" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="80" y1="185" x2="80" y2="40" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="340" y="210" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Reynolds Number (Re = ρvd/μ)</text>
                    <text x="60" y="110" text-anchor="middle" font-size="11" fill="var(--svg-fg)" transform="rotate(-90 60 110)">Velocity (v)</text>
                    <!-- Darcy region - linear -->
                    <line x1="80" y1="180" x2="280" y2="80" stroke="var(--svg-green-accent)" stroke-width="3"/>
                    <rect x="130" y="120" width="90" height="22" rx="4" fill="var(--svg-green-lt)" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <text x="175" y="135" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-green-accent)">DARCY (linear)</text>
                    <!-- Transition -->
                    <path d="M280,80 Q320,60 380,55" fill="none" stroke="var(--svg-orange-accent)" stroke-width="3"/>
                    <rect x="290" y="45" width="70" height="18" rx="4" fill="var(--svg-yellow-lt)" stroke="var(--svg-orange-accent)" stroke-width="1"/>
                    <text x="325" y="57" text-anchor="middle" font-size="9" fill="var(--svg-orange-accent)">Transition</text>
                    <!-- Turbulent -->
                    <path d="M380,55 Q440,52 550,50" fill="none" stroke="var(--svg-red-accent)" stroke-width="3"/>
                    <rect x="440" y="60" width="100" height="22" rx="4" fill="var(--svg-red-lt)" stroke="var(--svg-red-accent)" stroke-width="1"/>
                    <text x="490" y="75" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-red-accent)">TURBULENT</text>
                    <!-- Re values -->
                    <line x1="280" y1="180" x2="280" y2="190" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="280" y="205" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Re ≈ 1–10</text>
                    <line x1="380" y1="180" x2="380" y2="190" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="380" y="205" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Re ≈ 100</text>
                    <!-- Examples text -->
                    <text x="175" y="166" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Sands, silts, clays</text>
                    <text x="490" y="95" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Karst, coarse gravel, near-well</text>
                </svg>''',
    'Figure 2.6b: Darcy\'s law is valid only for laminar flow (Re &lt; 1–10). At higher Reynolds numbers, flow becomes non-linear and turbulent.')

# 5. Constant head permeameter
SVGS['Hydraulic Conductivity, K'] = svg_wrap('''
                <svg width="400" height="340" viewBox="0 0 400 340" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="200" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Constant-Head Permeameter</text>
                    <!-- Tank -->
                    <rect x="100" y="50" width="200" height="220" fill="none" stroke="var(--svg-fg)" stroke-width="2"/>
                    <!-- Soil sample -->
                    <rect x="100" y="160" width="200" height="60" fill="url(#dots)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="200" y="195" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Soil Sample</text>
                    <!-- Screen -->
                    <line x1="100" y1="220" x2="300" y2="220" stroke="var(--svg-fg)" stroke-width="2" stroke-dasharray="3,3"/>
                    <line x1="100" y1="160" x2="300" y2="160" stroke="var(--svg-fg)" stroke-width="2" stroke-dasharray="3,3"/>
                    <!-- Water above -->
                    <rect x="102" y="52" width="196" height="108" fill="var(--svg-water)" stroke="none" fill-opacity="0.4"/>
                    <!-- Constant head overflow -->
                    <line x1="300" y1="52" x2="330" y2="52" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="330" y1="52" x2="330" y2="80" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="350" y="65" font-size="8" fill="var(--svg-fg)">Overflow</text>
                    <!-- Outlet -->
                    <line x1="200" y1="270" x2="200" y2="290" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="200" y="305" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Q (collect &amp; measure)</text>
                    <!-- h label -->
                    <line x1="70" y1="52" x2="70" y2="220" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <line x1="65" y1="52" x2="75" y2="52" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <line x1="65" y1="220" x2="75" y2="220" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="55" y="140" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-accent)">Δh</text>
                    <!-- L label -->
                    <line x1="320" y1="160" x2="320" y2="220" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <line x1="315" y1="160" x2="325" y2="160" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <line x1="315" y1="220" x2="325" y2="220" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="340" y="194" font-weight="bold" font-size="13" fill="var(--svg-green-accent)">L</text>
                    <!-- Formula -->
                    <text x="200" y="330" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">K = QL / (AΔh)</text>
                </svg>''',
    'Figure 2.5c: Constant-head permeameter — water flows through the soil sample under constant head difference. K is calculated from measured Q.')

# 6. Falling head permeameter
SVGS['Intrinsic Permeability, k'] = svg_wrap('''
                <svg width="420" height="340" viewBox="0 0 420 340" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="210" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Falling-Head Permeameter</text>
                    <!-- Standpipe -->
                    <rect x="125" y="40" width="16" height="130" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="1.5" fill-opacity="0.4"/>
                    <!-- Water levels -->
                    <line x1="115" y1="55" x2="151" y2="55" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <text x="155" y="52" font-size="9" fill="var(--svg-red-accent)">h₁ (t=0)</text>
                    <line x1="115" y1="120" x2="151" y2="120" stroke="var(--svg-water-3)" stroke-width="1.5" stroke-dasharray="4,3"/>
                    <text x="155" y="117" font-size="9" fill="var(--svg-water-3)">h₂ (t=t)</text>
                    <!-- Standpipe area label -->
                    <text x="92" y="90" text-anchor="middle" font-size="10" fill="var(--svg-accent)">a</text>
                    <!-- Cylinder -->
                    <rect x="80" y="170" width="200" height="100" fill="none" stroke="var(--svg-fg)" stroke-width="2"/>
                    <!-- Soil sample -->
                    <rect x="80" y="200" width="200" height="40" fill="url(#dots)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="180" y="224" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Soil Sample (A, L)</text>
                    <!-- Connection -->
                    <line x1="133" y1="170" x2="133" y2="200" stroke="var(--svg-fg)" stroke-width="1"/>
                    <!-- L label -->
                    <line x1="300" y1="200" x2="300" y2="240" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <line x1="295" y1="200" x2="305" y2="200" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <line x1="295" y1="240" x2="305" y2="240" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="315" y="224" font-weight="bold" font-size="12" fill="var(--svg-green-accent)">L</text>
                    <!-- Outlet -->
                    <line x1="180" y1="270" x2="180" y2="290" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="180" y="305" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Outlet</text>
                    <!-- Formula -->
                    <text x="210" y="330" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">K = (aL)/(At) · ln(h₁/h₂)</text>
                </svg>''',
    'Figure 2.5d: Falling-head permeameter — used for fine-grained soils. Head drops from h₁ to h₂ over time t.')

# We need 10 more diagrams. Let me add some at the h2 section level since there aren't enough h3s.
# I'll inject by searching for specific content patterns.

# 7. Seepage velocity vs Darcy velocity 
SVG_SEEPAGE = svg_wrap('''
                <svg width="600" height="230" viewBox="0 0 600 230" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Darcy Flux (q) vs Seepage Velocity (vₛ)</text>
                    <!-- Left: Darcy flux -->
                    <rect x="30" y="45" width="240" height="150" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="150" y="68" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Darcy Flux q = Q/A</text>
                    <!-- Full cross section -->
                    <rect x="60" y="85" width="180" height="80" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="150" y="120" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Total area A</text>
                    <text x="150" y="138" text-anchor="middle" font-size="9" fill="var(--svg-muted)">(solids + voids)</text>
                    <!-- Flow arrows across full area -->
                    <line x1="55" y1="100" x2="55" y2="155" stroke="var(--svg-accent)" stroke-width="6" stroke-opacity="0.3"/>
                    <!-- Right: Seepage velocity -->
                    <rect x="330" y="45" width="240" height="150" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="450" y="68" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Seepage Velocity vₛ = q/n</text>
                    <!-- Only pore space -->
                    <rect x="360" y="85" width="180" height="80" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <!-- Pore channels -->
                    <rect x="370" y="90" width="12" height="70" fill="var(--svg-water)" stroke="none"/>
                    <rect x="400" y="90" width="8" height="70" fill="var(--svg-water)" stroke="none"/>
                    <rect x="425" y="90" width="15" height="70" fill="var(--svg-water)" stroke="none"/>
                    <rect x="460" y="90" width="10" height="70" fill="var(--svg-water)" stroke="none"/>
                    <rect x="490" y="90" width="12" height="70" fill="var(--svg-water)" stroke="none"/>
                    <rect x="515" y="90" width="9" height="70" fill="var(--svg-water)" stroke="none"/>
                    <text x="450" y="120" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Pore area only</text>
                    <text x="450" y="138" text-anchor="middle" font-size="9" fill="var(--svg-muted)">A_v = nA</text>
                    <!-- Relationship -->
                    <text x="300" y="215" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">vₛ = q/n &gt; q    (since n &lt; 1, actual velocity is higher)</text>
                </svg>''',
    'Figure 2.3b: Darcy flux (q) is computed over the total cross-section; the actual seepage velocity through pores is q/n, always larger since n &lt; 1.')

# 8. Equivalent K for layered systems
SVG_EQUIV_K = svg_wrap('''
                <svg width="650" height="320" viewBox="0 0 650 320" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="325" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Equivalent Hydraulic Conductivity for Layered Systems</text>
                    <!-- Parallel flow (horizontal) -->
                    <text x="170" y="50" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Flow PARALLEL to Layers</text>
                    <rect x="50" y="60" width="240" height="30" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="170" y="80" text-anchor="middle" font-size="9" fill="var(--svg-fg)">K₁, b₁</text>
                    <rect x="50" y="90" width="240" height="40" fill="var(--svg-green-lt)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="170" y="115" text-anchor="middle" font-size="9" fill="var(--svg-fg)">K₂, b₂</text>
                    <rect x="50" y="130" width="240" height="25" fill="var(--svg-yellow-lt)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="170" y="147" text-anchor="middle" font-size="9" fill="var(--svg-fg)">K₃, b₃</text>
                    <!-- Flow arrow -->
                    <line x1="30" y1="105" x2="50" y2="105" stroke="var(--svg-accent)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="30" y="100" font-size="8" fill="var(--svg-accent)">Q</text>
                    <!-- Formula -->
                    <text x="170" y="180" text-anchor="middle" font-size="11" fill="var(--svg-accent)">K_h = Σ(K_i · b_i) / Σb_i</text>
                    <text x="170" y="198" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Weighted arithmetic mean</text>
                    <!-- Perpendicular flow (vertical) -->
                    <text x="490" y="50" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Flow PERPENDICULAR to Layers</text>
                    <rect x="370" y="60" width="240" height="30" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="490" y="80" text-anchor="middle" font-size="9" fill="var(--svg-fg)">K₁, b₁</text>
                    <rect x="370" y="90" width="240" height="40" fill="var(--svg-green-lt)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="490" y="115" text-anchor="middle" font-size="9" fill="var(--svg-fg)">K₂, b₂</text>
                    <rect x="370" y="130" width="240" height="25" fill="var(--svg-yellow-lt)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="490" y="147" text-anchor="middle" font-size="9" fill="var(--svg-fg)">K₃, b₃</text>
                    <!-- Flow arrow down -->
                    <line x1="490" y1="40" x2="490" y2="60" stroke="var(--svg-green-accent)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="500" y="50" font-size="8" fill="var(--svg-green-accent)">Q</text>
                    <!-- Formula -->
                    <text x="490" y="180" text-anchor="middle" font-size="11" fill="var(--svg-green-accent)">K_v = Σb_i / Σ(b_i/K_i)</text>
                    <text x="490" y="198" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Weighted harmonic mean</text>
                    <!-- Bottom comparison -->
                    <rect x="130" y="220" width="390" height="40" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="325" y="242" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">Always: K_h ≥ K_v</text>
                    <text x="325" y="258" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Horizontal flow favors most permeable layer; vertical flow limited by least permeable</text>
                    <!-- Anisotropy note -->
                    <text x="325" y="290" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Anisotropy ratio: K_h/K_v = 2 to 100+ (common in sedimentary deposits)</text>
                </svg>''',
    'Figure 2.6c: Equivalent hydraulic conductivity — arithmetic mean for parallel flow, harmonic mean for perpendicular flow. K_h is always ≥ K_v.')

# 9. Darcy's law sign convention
SVG_SIGN = svg_wrap('''
                <svg width="550" height="200" viewBox="0 0 550 200" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Darcy's Law — Sign Convention</text>
                    <!-- Flow direction -->
                    <rect x="50" y="60" width="450" height="50" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="1.5" fill-opacity="0.3"/>
                    <!-- Head at two points -->
                    <line x1="100" y1="45" x2="100" y2="55" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="100" y="40" text-anchor="middle" font-size="11" fill="var(--svg-accent)">h₁ (high)</text>
                    <line x1="450" y1="45" x2="450" y2="55" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="450" y="40" text-anchor="middle" font-size="11" fill="var(--svg-accent)">h₂ (low)</text>
                    <!-- Head line declining -->
                    <line x1="100" y1="48" x2="450" y2="58" stroke="var(--svg-accent)" stroke-width="2" stroke-dasharray="6,3"/>
                    <!-- Flow arrow -->
                    <line x1="120" y1="85" x2="430" y2="85" stroke="var(--svg-green-accent)" stroke-width="3" marker-end="url(#arr)"/>
                    <text x="275" y="80" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-green-accent)">Flow direction (high → low head)</text>
                    <!-- x-direction -->
                    <line x1="100" y1="115" x2="450" y2="115" stroke="var(--svg-fg)" stroke-width="1" marker-end="url(#arr)"/>
                    <text x="460" y="119" font-size="10" fill="var(--svg-fg)">x</text>
                    <!-- L label -->
                    <line x1="100" y1="120" x2="100" y2="130" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="450" y1="120" x2="450" y2="130" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="275" y="140" text-anchor="middle" font-size="10" fill="var(--svg-fg)">L</text>
                    <!-- Formulas -->
                    <text x="275" y="165" text-anchor="middle" font-size="12" fill="var(--svg-fg)">q = −K(dh/dx) = −K(h₂−h₁)/L = K(h₁−h₂)/L</text>
                    <text x="275" y="185" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Negative sign ensures q is positive in the direction of decreasing head</text>
                </svg>''',
    'Figure 2.3c: Darcy\'s law sign convention — the negative sign ensures flow is in the direction of decreasing hydraulic head.')

# 10. 3D Darcy generalization summary
SVG_3D = svg_wrap('''
                <svg width="550" height="240" viewBox="0 0 550 240" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">3D Generalization of Darcy's Law — K Tensor</text>
                    <!-- K tensor matrix -->
                    <text x="160" y="55" text-anchor="middle" font-size="12" fill="var(--svg-fg)">Anisotropic medium:</text>
                    <text x="100" y="90" text-anchor="end" font-size="14" fill="var(--svg-fg)">q = −</text>
                    <!-- Matrix brackets -->
                    <text x="110" y="105" font-size="50" fill="var(--svg-fg)">[</text>
                    <text x="310" y="105" font-size="50" fill="var(--svg-fg)">]</text>
                    <!-- Matrix contents -->
                    <text x="155" y="80" text-anchor="middle" font-size="12" fill="var(--svg-accent)">K_xx</text>
                    <text x="215" y="80" text-anchor="middle" font-size="12" fill="var(--svg-dim)">K_xy</text>
                    <text x="275" y="80" text-anchor="middle" font-size="12" fill="var(--svg-dim)">K_xz</text>
                    <text x="155" y="100" text-anchor="middle" font-size="12" fill="var(--svg-dim)">K_yx</text>
                    <text x="215" y="100" text-anchor="middle" font-size="12" fill="var(--svg-accent)">K_yy</text>
                    <text x="275" y="100" text-anchor="middle" font-size="12" fill="var(--svg-dim)">K_yz</text>
                    <text x="155" y="120" text-anchor="middle" font-size="12" fill="var(--svg-dim)">K_zx</text>
                    <text x="215" y="120" text-anchor="middle" font-size="12" fill="var(--svg-dim)">K_zy</text>
                    <text x="275" y="120" text-anchor="middle" font-size="12" fill="var(--svg-accent)">K_zz</text>
                    <!-- Gradient vector -->
                    <text x="340" y="100" text-anchor="middle" font-size="14" fill="var(--svg-fg)">∇h</text>
                    <!-- Principal axes -->
                    <text x="275" y="155" text-anchor="middle" font-size="11" fill="var(--svg-fg)">If axes aligned to principal directions:</text>
                    <!-- Simplified diagonal -->
                    <rect x="100" y="165" width="350" height="35" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="275" y="187" text-anchor="middle" font-size="12" fill="var(--svg-accent)">K = diag(K₁, K₂, K₃)  — off-diagonal terms = 0</text>
                    <text x="275" y="220" text-anchor="middle" font-size="11" fill="var(--svg-muted)">Isotropic: K₁ = K₂ = K₃ = K (scalar, simplest case)</text>
                </svg>''',
    'Figure 2.4b: 3D Darcy\'s law uses a hydraulic conductivity tensor. In principal directions, only diagonal terms remain; in isotropic media, K is a scalar.')

# Extra content-level injections for seepage velocity, equiv K, sign convention, 3D
EXTRA_INJECTIONS = {
    'Seepage Velocity': SVG_SEEPAGE,
    'Equivalent Hydraulic Conductivity': SVG_EQUIV_K,
    'Darcy&#8217;s Law': SVG_SIGN,
    'Generalized 3D Form': SVG_3D
}


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
            next_block = re.search(r'(</(?:p|ol|ul|div)>)', html[insert_pos:])
            if next_block:
                actual_pos = insert_pos + next_block.end()
                html = html[:actual_pos] + svg_html + html[actual_pos:]
                count += 1
                print(f"  Inserted after h3 '{heading_text[:50]}...'")
        else:
            print(f"  WARNING: h3 not found '{heading_text[:50]}...'")
    return html, count


def inject_extras(html, extras):
    count = 0
    for search_text, svg_html in extras.items():
        # Search in h3 or h2 or bold text
        pattern = re.compile(
            r'(<h[23][^>]*>[^<]*' + re.escape(search_text[:25]) + r'[^<]*</h[23]>\s*)',
            re.DOTALL
        )
        match = pattern.search(html)
        if match:
            insert_pos = match.end()
            next_block = re.search(r'(</(?:p|ol|ul|div)>)', html[insert_pos:])
            if next_block:
                actual_pos = insert_pos + next_block.end()
                html = html[:actual_pos] + svg_html + html[actual_pos:]
                count += 1
                print(f"  Inserted after '{search_text[:40]}...'")
            else:
                print(f"  WARNING: no block after '{search_text[:40]}...'")
        else:
            print(f"  WARNING: not found '{search_text[:40]}...'")
    return html, count


with open(FILE, 'r', encoding='utf-8') as f:
    html = f.read()

original_svg_count = html.count('<svg')
html, c1 = inject_svgs(html, SVGS)
html, c2 = inject_extras(html, EXTRA_INJECTIONS)
new_svg_count = html.count('<svg')

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nChapter 2: {c1 + c2} SVGs inserted")
print(f"  Before: {original_svg_count} SVGs, After: {new_svg_count} SVGs")
print(f"  Net added: {new_svg_count - original_svg_count}")

"""Add 10 new educational SVG diagrams to Chapter 7 (Water Wells)."""
import re

FILE = r"d:\Final Year\Theory\gw\GW_THE\chapter7.html"

def svg_wrap(svg_content, caption):
    return f'''
            <div class="figure-container">
{svg_content}
                <div class="figcaption">{caption}</div>
            </div>
'''

SVGS = {}

# 1. Components of Tube Well
SVGS['7.3.1 Components of a Tube We'] = svg_wrap('''
                <svg width="400" height="350" viewBox="0 0 400 350" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="200" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Components of a Tube Well</text>
                    <rect x="170" y="40" width="60" height="30" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="200" y="60" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--svg-fg)">Pump</text>
                    <rect x="185" y="70" width="30" height="50" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="270" y="95" font-size="9" fill="var(--svg-fg)">Surface casing</text>
                    <line x1="215" y1="95" x2="265" y2="95" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="185" y="120" width="30" height="55" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="270" y="148" font-size="9" fill="var(--svg-fg)">Casing pipe</text>
                    <line x1="215" y1="148" x2="265" y2="148" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="180" y="115" width="40" height="10" fill="var(--svg-muted)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="130" y="122" text-anchor="end" font-size="8" fill="var(--svg-muted)">Sanitary seal</text>
                    <line x1="133" y1="120" x2="178" y2="120" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="185" y="175" width="30" height="80" fill="var(--svg-bg-fill)" stroke="var(--svg-accent)" stroke-width="1.5" stroke-dasharray="3,2"/>
                    <text x="270" y="218" font-size="9" font-weight="bold" fill="var(--svg-accent)">Well screen</text>
                    <line x1="215" y1="215" x2="265" y2="215" stroke="var(--svg-accent)" stroke-width="1"/>
                    <rect x="175" y="175" width="10" height="80" fill="var(--svg-water)" fill-opacity="0.3" stroke="none"/>
                    <rect x="215" y="175" width="10" height="80" fill="var(--svg-water)" fill-opacity="0.3" stroke="none"/>
                    <text x="130" y="218" text-anchor="end" font-size="8" fill="var(--svg-green-accent)">Gravel pack</text>
                    <line x1="133" y1="215" x2="173" y2="215" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <rect x="185" y="255" width="30" height="20" fill="var(--svg-fg)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="270" y="268" font-size="9" fill="var(--svg-fg)">Bottom cap</text>
                    <line x1="215" y1="265" x2="265" y2="265" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="155" y="275" width="90" height="30" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="200" y="295" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Sump</text>
                    <text x="200" y="335" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Screen placed in aquifer zone, gravel pack fills annulus</text>
                </svg>''',
    'Figure 7.3b: Schematic of a tube well — showing the main components from pump house to bottom cap with gravel-packed screen in the aquifer zone.')

# 2. Step-Drawdown Test Purpose
SVGS['7.5.1 Purpose and Procedure'] = svg_wrap('''
                <svg width="550" height="260" viewBox="0 0 550 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Step-Drawdown Test — Aquifer vs Well Loss</text>
                    <line x1="60" y1="40" x2="60" y2="180" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="60" y1="40" x2="480" y2="40" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="270" y="30" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Pumping Rate Q →</text>
                    <text x="35" y="115" text-anchor="middle" font-size="10" fill="var(--svg-fg)" transform="rotate(-90 35 115)">s_w (↓)</text>
                    <rect x="80" y="40" width="80" height="40" fill="var(--svg-green-accent)" fill-opacity="0.3" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <text x="120" y="65" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">BQ₁</text>
                    <rect x="80" y="80" width="80" height="10" fill="var(--svg-red-accent)" fill-opacity="0.3" stroke="var(--svg-red-accent)" stroke-width="1"/>
                    <text x="120" y="88" text-anchor="middle" font-size="7" fill="var(--svg-red-accent)">CQ₁²</text>
                    <rect x="180" y="40" width="80" height="65" fill="var(--svg-green-accent)" fill-opacity="0.3" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <text x="220" y="75" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">BQ₂</text>
                    <rect x="180" y="105" width="80" height="25" fill="var(--svg-red-accent)" fill-opacity="0.3" stroke="var(--svg-red-accent)" stroke-width="1"/>
                    <text x="220" y="120" text-anchor="middle" font-size="7" fill="var(--svg-red-accent)">CQ₂²</text>
                    <rect x="280" y="40" width="80" height="80" fill="var(--svg-green-accent)" fill-opacity="0.3" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <text x="320" y="85" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">BQ₃</text>
                    <rect x="280" y="120" width="80" height="40" fill="var(--svg-red-accent)" fill-opacity="0.3" stroke="var(--svg-red-accent)" stroke-width="1"/>
                    <text x="320" y="145" text-anchor="middle" font-size="7" fill="var(--svg-red-accent)">CQ₃²</text>
                    <text x="275" y="200" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">s_w = BQ + CQ²</text>
                    <text x="275" y="220" text-anchor="middle" font-size="10" fill="var(--svg-green-accent)">BQ = aquifer loss (laminar)</text>
                    <text x="275" y="238" text-anchor="middle" font-size="10" fill="var(--svg-red-accent)">CQ² = well loss (turbulent, increases with Q²)</text>
                    <text x="275" y="255" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Well efficiency η = BQ/(BQ+CQ²) × 100% — decreases as Q increases</text>
                </svg>''',
    'Figure 7.5b: Step-drawdown test separates aquifer losses (linear BQ) from well losses (turbulent CQ²) — well losses grow disproportionately with pumping rate.')

# 3. Critical Depression Head
SVGS['7.6.2 Critical Depression Hea'] = svg_wrap('''
                <svg width="500" height="250" viewBox="0 0 500 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="250" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Critical Depression Head (CDH)</text>
                    <rect x="50" y="210" width="400" height="15" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="50" y="60" width="400" height="150" fill="var(--svg-water)" stroke="none" fill-opacity="0.15"/>
                    <line x1="50" y1="60" x2="450" y2="60" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="480" y="65" font-size="8" fill="var(--svg-fg)">Static WT</text>
                    <rect x="246" y="40" width="8" height="185" fill="var(--svg-fg)"/>
                    <path d="M50,60 C130,68 200,90 246,130" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <path d="M254,130 C300,90 380,68 450,60" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="70" y1="60" x2="70" y2="130" stroke="var(--svg-red-accent)" stroke-width="2"/>
                    <line x1="65" y1="60" x2="75" y2="60" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <line x1="65" y1="130" x2="75" y2="130" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <text x="50" y="100" text-anchor="end" font-size="10" font-weight="bold" fill="var(--svg-red-accent)">CDH</text>
                    <line x1="50" y1="130" x2="450" y2="130" stroke="var(--svg-red-accent)" stroke-width="1.5" stroke-dasharray="5,3"/>
                    <text x="350" y="125" font-size="9" fill="var(--svg-red-accent)">Maximum safe drawdown level</text>
                    <text x="250" y="165" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Below CDH → sand pumping, air entry</text>
                    <text x="250" y="183" text-anchor="middle" font-size="10" fill="var(--svg-fg)">aquifer dewatering, reduced efficiency</text>
                    <text x="250" y="205" text-anchor="middle" font-size="9" fill="var(--svg-muted)">CDH typically = ⅓ to ½ of saturated thickness</text>
                    <text x="250" y="240" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-fg)">Design Q must keep s &lt; CDH at the well face</text>
                </svg>''',
    'Figure 7.6b: Critical depression head — the maximum allowable drawdown below which sand entry, air entrainment, and aquifer damage begin.')

# 4. Screen Design
SVGS['7.7.1 Design Parameters'] = svg_wrap('''
                <svg width="600" height="220" viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Well Screen Design — Key Parameters</text>
                    <rect x="200" y="40" width="200" height="32" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="300" y="60" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">Screen Design</text>
                    <line x1="120" y1="72" x2="100" y2="95" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="230" y1="72" x2="200" y2="95" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="300" y1="72" x2="300" y2="95" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="370" y1="72" x2="400" y2="95" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="480" y1="72" x2="500" y2="95" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <rect x="20" y="95" width="150" height="60" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="95" y="113" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-accent)">Length</text>
                    <text x="95" y="128" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Confined: 80-90% of b</text>
                    <text x="95" y="143" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Unconfined: lower ⅓-½</text>
                    <rect x="130" y="95" width="140" height="60" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="200" y="113" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-green-accent)">Diameter</text>
                    <text x="200" y="128" text-anchor="middle" font-size="8" fill="var(--svg-fg)">v_screen &lt; 3 cm/s</text>
                    <text x="200" y="143" text-anchor="middle" font-size="8" fill="var(--svg-fg)">A_open = Q/v_allowable</text>
                    <rect x="240" y="95" width="120" height="60" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <text x="300" y="113" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-water-3)">Slot Size</text>
                    <text x="300" y="128" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Retain 40-60% of</text>
                    <text x="300" y="143" text-anchor="middle" font-size="8" fill="var(--svg-fg)">aquifer material</text>
                    <rect x="340" y="95" width="130" height="60" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="405" y="113" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-orange-accent)">Open Area</text>
                    <text x="405" y="128" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Typically 5-20%</text>
                    <text x="405" y="143" text-anchor="middle" font-size="8" fill="var(--svg-fg)">of screen surface</text>
                    <rect x="440" y="95" width="140" height="60" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <text x="510" y="113" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-red-accent)">Material</text>
                    <text x="510" y="128" text-anchor="middle" font-size="8" fill="var(--svg-fg)">SS, PVC, or GI</text>
                    <text x="510" y="143" text-anchor="middle" font-size="8" fill="var(--svg-fg)">based on chemistry</text>
                    <text x="300" y="185" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Good screen design maximizes yield while preventing sand entry</text>
                    <text x="300" y="205" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Entrance velocity v_e = Q/(π × d × L × open_area_fraction)</text>
                </svg>''',
    'Figure 7.7b: Five key screen design parameters — length, diameter, slot size, open area, and material selection for optimal well performance.')

# 5. Screen Types
SVGS['7.8.1 Types of Well Screens'] = svg_wrap('''
                <svg width="600" height="220" viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Common Well Screen Types</text>
                    <rect x="20" y="45" width="170" height="140" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="105" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-accent)">Continuous Slot</text>
                    <text x="105" y="85" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Wire wound on rods</text>
                    <text x="105" y="100" text-anchor="middle" font-size="8" fill="var(--svg-fg)">V-shaped openings</text>
                    <text x="105" y="118" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">Max open area (30-60%)</text>
                    <text x="105" y="135" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">Self-cleaning design</text>
                    <text x="105" y="155" text-anchor="middle" font-size="8" fill="var(--svg-red-accent)">Most expensive</text>
                    <text x="105" y="172" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Best for: high-yield wells</text>
                    <rect x="215" y="45" width="170" height="140" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="300" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-green-accent)">Slotted Pipe</text>
                    <text x="300" y="85" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Machine-cut slots</text>
                    <text x="300" y="100" text-anchor="middle" font-size="8" fill="var(--svg-fg)">in PVC/steel pipe</text>
                    <text x="300" y="118" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">Low cost</text>
                    <text x="300" y="135" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">Easy to fabricate</text>
                    <text x="300" y="155" text-anchor="middle" font-size="8" fill="var(--svg-red-accent)">Low open area (1-5%)</text>
                    <text x="300" y="172" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Best for: low-yield wells</text>
                    <rect x="410" y="45" width="170" height="140" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="495" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-orange-accent)">Louvered / Bridge</text>
                    <text x="495" y="85" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Punched shutters</text>
                    <text x="495" y="100" text-anchor="middle" font-size="8" fill="var(--svg-fg)">in GI pipe</text>
                    <text x="495" y="118" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">Moderate open area</text>
                    <text x="495" y="135" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">Moderate cost</text>
                    <text x="495" y="155" text-anchor="middle" font-size="8" fill="var(--svg-red-accent)">Can clog in fine sand</text>
                    <text x="495" y="172" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Common in Nepal</text>
                    <text x="300" y="208" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Screen selection based on: aquifer material, water chemistry, well yield, budget</text>
                </svg>''',
    'Figure 7.8b: Three common screen types — continuous-slot (best performance), slotted pipe (lowest cost), and louvered/bridge slot (compromise).')

# 6. Gravel Pack Design
SVGS['7.9.3 Gravel Pack Design (PAR'] = svg_wrap('''
                <svg width="550" height="240" viewBox="0 0 550 240" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Gravel Pack Design Criteria</text>
                    <rect x="30" y="45" width="490" height="60" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="275" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Pack-to-Aquifer Ratio (PAR)</text>
                    <text x="275" y="85" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">PAR = D₅₀(pack) / D₅₀(aquifer) = 4 to 6</text>
                    <text x="275" y="100" text-anchor="middle" font-size="9" fill="var(--svg-muted)">(Some references use D₅₀ pack / D₅₀ formation = 5 to 10)</text>
                    <rect x="30" y="120" width="240" height="80" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="150" y="140" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-green-accent)">Uniformity</text>
                    <text x="150" y="158" text-anchor="middle" font-size="9" fill="var(--svg-fg)">C_u = D₆₀/D₁₀ &lt; 2.5</text>
                    <text x="150" y="175" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Well-sorted gravel prevents</text>
                    <text x="150" y="190" text-anchor="middle" font-size="9" fill="var(--svg-fg)">fine migration through pack</text>
                    <rect x="280" y="120" width="240" height="80" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="400" y="140" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-orange-accent)">Thickness</text>
                    <text x="400" y="158" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Minimum: 75 mm (3 inches)</text>
                    <text x="400" y="175" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Typical: 75–200 mm</text>
                    <text x="400" y="190" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Too thick → settles unevenly</text>
                    <text x="275" y="225" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Slot size = D₁₀ of gravel pack (retains ~90% of gravel material)</text>
                </svg>''',
    'Figure 7.9b: Gravel pack design — the pack-to-aquifer ratio determines gravel size, while uniformity coefficient ensures stable filtering.')

# 7. Well Development
SVGS['7.10.1 Well Development'] = svg_wrap('''
                <svg width="600" height="230" viewBox="0 0 600 230" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Well Development Methods</text>
                    <rect x="200" y="40" width="200" height="30" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="300" y="60" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-fg)">Purpose: Remove drilling damage</text>
                    <rect x="20" y="85" width="130" height="60" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="85" y="103" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-accent)">Surging</text>
                    <text x="85" y="118" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Plunger/bailer</text>
                    <text x="85" y="133" text-anchor="middle" font-size="8" fill="var(--svg-fg)">push-pull action</text>
                    <rect x="160" y="85" width="130" height="60" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="225" y="103" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-green-accent)">Backwashing</text>
                    <text x="225" y="118" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Reverse flow</text>
                    <text x="225" y="133" text-anchor="middle" font-size="8" fill="var(--svg-fg)">through screen</text>
                    <rect x="300" y="85" width="130" height="60" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="365" y="103" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-orange-accent)">Jetting</text>
                    <text x="365" y="118" text-anchor="middle" font-size="8" fill="var(--svg-fg)">High-pressure water</text>
                    <text x="365" y="133" text-anchor="middle" font-size="8" fill="var(--svg-fg)">at screen face</text>
                    <rect x="440" y="85" width="140" height="60" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <text x="510" y="103" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-water-3)">Airlift</text>
                    <text x="510" y="118" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Compressed air</text>
                    <text x="510" y="133" text-anchor="middle" font-size="8" fill="var(--svg-fg)">lifts water + fines</text>
                    <text x="300" y="175" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Goal: Remove fines from screen zone → increase permeability → increase specific capacity</text>
                    <text x="300" y="195" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Success indicator: water clears, specific capacity stabilizes</text>
                    <text x="300" y="218" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Chemical development (acid/polyphosphate) used when mechanical methods insufficient</text>
                </svg>''',
    'Figure 7.10b: Well development methods — surging, backwashing, jetting, and airlift all aim to remove drilling fines and increase well efficiency.')

# 8. Infiltration Gallery
SVGS['Yield of an Infiltration Gall'] = svg_wrap('''
                <svg width="550" height="240" viewBox="0 0 550 240" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Infiltration Gallery — Yield Analysis</text>
                    <rect x="30" y="45" width="490" height="40" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="275" y="63" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Horizontal perforated pipe laid below WT in a pervious aquifer</text>
                    <text x="275" y="78" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Collects water by gravity — no pumping needed if elevation difference exists</text>
                    <rect x="30" y="100" width="230" height="60" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="145" y="118" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-accent)">One-Side Flow</text>
                    <text x="145" y="135" text-anchor="middle" font-size="10" fill="var(--svg-fg)">q = K(H²−h²)/(2L)</text>
                    <text x="145" y="150" text-anchor="middle" font-size="8" fill="var(--svg-muted)">per unit length</text>
                    <rect x="290" y="100" width="230" height="60" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="405" y="118" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-green-accent)">Two-Side Flow</text>
                    <text x="405" y="135" text-anchor="middle" font-size="10" fill="var(--svg-fg)">q = K(H²−h²)/L</text>
                    <text x="405" y="150" text-anchor="middle" font-size="8" fill="var(--svg-muted)">per unit length (×2)</text>
                    <text x="275" y="185" text-anchor="middle" font-size="10" fill="var(--svg-fg)">H = original WT height above impervious base</text>
                    <text x="275" y="205" text-anchor="middle" font-size="10" fill="var(--svg-fg)">h = WT height at gallery after drawdown</text>
                    <text x="275" y="228" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Total yield Q = q × gallery length | Typical depth: 3-5 m below WT</text>
                </svg>''',
    'Figure 7.11b: Infiltration gallery yield — the Dupuit formula applies per unit length, with total yield proportional to gallery length.')

# 9. Ranney Well
SVGS['Construction and Components'] = svg_wrap('''
                <svg width="550" height="280" viewBox="0 0 550 280" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Ranney (Radial Collector) Well — Layout</text>
                    <line x1="50" y1="100" x2="500" y2="100" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="275" y="93" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Ground surface</text>
                    <rect x="245" y="60" width="60" height="160" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="275" y="120" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--svg-fg)">Central</text>
                    <text x="275" y="132" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--svg-fg)">caisson</text>
                    <text x="275" y="150" text-anchor="middle" font-size="7" fill="var(--svg-muted)">φ 3-5 m</text>
                    <line x1="245" y1="170" x2="80" y2="170" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <text x="160" y="165" text-anchor="middle" font-size="8" fill="var(--svg-accent)">Lateral screen</text>
                    <line x1="305" y1="170" x2="470" y2="170" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <line x1="245" y1="145" x2="100" y2="125" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="305" y1="145" x2="450" y2="125" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="245" y1="195" x2="120" y2="210" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="305" y1="195" x2="430" y2="210" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="440" y="168" font-size="8" fill="var(--svg-accent)">Perforated pipes</text>
                    <text x="440" y="180" font-size="8" fill="var(--svg-accent)">pushed out radially</text>
                    <rect x="50" y="225" width="450" height="15" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="275" y="238" text-anchor="middle" font-size="7" fill="var(--svg-fg)">Impervious</text>
                    <line x1="275" y1="50" x2="275" y2="30" stroke="var(--svg-red-accent)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="295" y="40" font-size="9" fill="var(--svg-red-accent)">Pump Q</text>
                    <text x="275" y="260" text-anchor="middle" font-size="10" fill="var(--svg-fg)">High yield: Q up to 50,000 m³/day | Laterals: 6-12 nos, 30-60 m long</text>
                    <text x="275" y="276" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Used near rivers for induced recharge — bank filtration effect</text>
                </svg>''',
    'Figure 7.12b: Ranney (radial collector) well — a central caisson with multiple horizontal perforated laterals pushed into the aquifer for high-capacity collection.')

# 10. Dug well construction
SVGS['7.2.1 Description and Constru'] = svg_wrap('''
                <svg width="400" height="300" viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="200" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Open (Dug) Well — Cross Section</text>
                    <line x1="50" y1="55" x2="350" y2="55" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="200" y="48" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Ground surface</text>
                    <rect x="100" y="35" width="200" height="25" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="200" y="52" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Well cover / platform</text>
                    <rect x="130" y="55" width="15" height="130" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <rect x="255" y="55" width="15" height="130" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="320" y="90" font-size="8" fill="var(--svg-fg)">Stone/brick</text>
                    <text x="320" y="102" font-size="8" fill="var(--svg-fg)">lining</text>
                    <line x1="270" y1="95" x2="315" y2="95" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="50" y1="120" x2="130" y2="120" stroke="var(--svg-water-3)" stroke-width="1.5" stroke-dasharray="4,3"/>
                    <line x1="270" y1="120" x2="350" y2="120" stroke="var(--svg-water-3)" stroke-width="1.5" stroke-dasharray="4,3"/>
                    <text x="60" y="115" font-size="8" fill="var(--svg-water-3)">WT</text>
                    <rect x="145" y="120" width="110" height="65" fill="var(--svg-water)" stroke="none" fill-opacity="0.3"/>
                    <text x="200" y="155" text-anchor="middle" font-size="9" fill="var(--svg-water-3)">Water</text>
                    <rect x="130" y="185" width="140" height="20" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="200" y="199" text-anchor="middle" font-size="7" fill="var(--svg-fg)">Flat bottom</text>
                    <line x1="90" y1="95" x2="90" y2="185" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="85" y1="95" x2="95" y2="95" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="85" y1="185" x2="95" y2="185" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="80" y="140" text-anchor="end" font-size="9" fill="var(--svg-fg)">3-20m</text>
                    <line x1="155" y1="210" x2="245" y2="210" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="200" y="225" text-anchor="middle" font-size="9" fill="var(--svg-fg)">φ 1-10 m</text>
                    <text x="200" y="255" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Hand-dug, lined with stone/brick/RCC</text>
                    <text x="200" y="275" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Taps shallow unconfined aquifer only</text>
                    <text x="200" y="292" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Low yield, high contamination risk</text>
                </svg>''',
    'Figure 7.2b: Open (dug) well cross-section — a shallow, large-diameter well with stone/brick lining, typically 3-20 m deep.')


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

print(f"\nChapter 7: {c} SVGs inserted")
print(f"  Before: {original} SVGs, After: {new_count} SVGs")
print(f"  Net added: {new_count - original}")

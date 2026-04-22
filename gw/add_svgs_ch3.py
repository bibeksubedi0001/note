"""Add 10 new educational SVG diagrams to Chapter 3 (Flow Theory)."""
import re

FILE = r"d:\Final Year\Theory\gw\GW_THE\chapter3.html"

def svg_wrap(svg_content, caption):
    return f'''
            <div class="figure-container">
{svg_content}
                <div class="figcaption">{caption}</div>
            </div>
'''

SVGS = {}

# 1. Stream function concept
SVGS['Key Terminology'] = svg_wrap('''
                <svg width="550" height="240" viewBox="0 0 550 240" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Stream Function (ψ) and Velocity Potential (φ)</text>
                    <rect x="30" y="40" width="230" height="160" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="145" y="62" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Stream Function ψ</text>
                    <text x="145" y="82" text-anchor="middle" font-size="10" fill="var(--svg-fg)">ψ = constant along streamlines</text>
                    <text x="145" y="100" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Flow between two streamlines:</text>
                    <text x="145" y="118" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-accent)">Δq = ψ₂ − ψ₁</text>
                    <text x="145" y="140" text-anchor="middle" font-size="9" fill="var(--svg-muted)">v_x = ∂ψ/∂y</text>
                    <text x="145" y="156" text-anchor="middle" font-size="9" fill="var(--svg-muted)">v_y = −∂ψ/∂x</text>
                    <text x="145" y="178" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Exists for any 2D flow</text>
                    <rect x="290" y="40" width="230" height="160" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="405" y="62" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Velocity Potential φ</text>
                    <text x="405" y="82" text-anchor="middle" font-size="10" fill="var(--svg-fg)">φ = constant on equipotentials</text>
                    <text x="405" y="100" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Head drop between two lines:</text>
                    <text x="405" y="118" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-green-accent)">Δh = (φ₂ − φ₁)/K</text>
                    <text x="405" y="140" text-anchor="middle" font-size="9" fill="var(--svg-muted)">v_x = −∂φ/∂x</text>
                    <text x="405" y="156" text-anchor="middle" font-size="9" fill="var(--svg-muted)">v_y = −∂φ/∂y</text>
                    <text x="405" y="178" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Exists only for irrotational flow</text>
                    <text x="275" y="225" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">ψ-lines ⊥ φ-lines → Flow Net</text>
                </svg>''',
    'Figure 3.0b: Stream function and velocity potential — their contours form the flow net when plotted together.')

# 2. Flow net construction rules
SVGS['Construction of a Flow Net'] = svg_wrap('''
                <svg width="600" height="250" viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Flow Net Construction — Essential Rules</text>
                    <rect x="20" y="40" width="170" height="80" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="105" y="60" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-accent)">Rule 1</text>
                    <text x="105" y="78" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Streamlines ⊥</text>
                    <text x="105" y="92" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Equipotential lines</text>
                    <text x="105" y="108" text-anchor="middle" font-size="9" fill="var(--svg-muted)">(90° intersections)</text>
                    <rect x="215" y="40" width="170" height="80" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="300" y="60" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-green-accent)">Rule 2</text>
                    <text x="300" y="78" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Elements should be</text>
                    <text x="300" y="92" text-anchor="middle" font-size="9" fill="var(--svg-fg)">curvilinear squares</text>
                    <text x="300" y="108" text-anchor="middle" font-size="9" fill="var(--svg-muted)">(Δs ≈ Δn)</text>
                    <rect x="410" y="40" width="170" height="80" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="495" y="60" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-orange-accent)">Rule 3</text>
                    <text x="495" y="78" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Impervious boundary</text>
                    <text x="495" y="92" text-anchor="middle" font-size="9" fill="var(--svg-fg)">= streamline</text>
                    <text x="495" y="108" text-anchor="middle" font-size="9" fill="var(--svg-muted)">No flow crosses it</text>
                    <rect x="70" y="140" width="200" height="80" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <text x="170" y="160" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-water-3)">Rule 4</text>
                    <text x="170" y="178" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Constant head boundary</text>
                    <text x="170" y="192" text-anchor="middle" font-size="9" fill="var(--svg-fg)">= equipotential line</text>
                    <text x="170" y="208" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Equal head along it</text>
                    <rect x="330" y="140" width="200" height="80" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-purple-accent)" stroke-width="1.5"/>
                    <text x="430" y="160" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-purple-accent)">Rule 5</text>
                    <text x="430" y="178" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Water table (unconfined)</text>
                    <text x="430" y="192" text-anchor="middle" font-size="9" fill="var(--svg-fg)">= top streamline</text>
                    <text x="430" y="208" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Pressure = atmospheric</text>
                    <text x="300" y="242" text-anchor="middle" font-size="11" font-style="italic" fill="var(--svg-fg)">q = KH(N_f/N_d) where N_f = flow channels, N_d = potential drops</text>
                </svg>''',
    'Figure 3.1b: Five essential rules for constructing a valid flow net — orthogonality, curvilinear squares, and boundary conditions.')

# 3. Three-well triangulation
SVGS['Three-Well Triangulation Procedure'] = svg_wrap('''
                <svg width="500" height="340" viewBox="0 0 500 340" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="250" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Three-Well Triangulation — Finding Flow Direction</text>
                    <polygon points="100,280 400,250 250,80" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <circle cx="100" cy="280" r="8" fill="var(--svg-accent)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="60" y="285" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">A</text>
                    <text x="60" y="300" text-anchor="middle" font-size="10" fill="var(--svg-accent)">h = 48 m</text>
                    <circle cx="400" cy="250" r="8" fill="var(--svg-green-accent)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="440" y="255" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">B</text>
                    <text x="445" y="270" text-anchor="middle" font-size="10" fill="var(--svg-green-accent)">h = 42 m</text>
                    <circle cx="250" cy="80" r="8" fill="var(--svg-red-accent)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="290" y="78" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">C</text>
                    <text x="295" y="95" text-anchor="middle" font-size="10" fill="var(--svg-red-accent)">h = 36 m</text>
                    <circle cx="327" cy="166" r="5" fill="var(--svg-orange-accent)"/>
                    <text x="360" y="160" font-size="10" fill="var(--svg-orange-accent)">D (h=42m)</text>
                    <text x="360" y="175" font-size="9" fill="var(--svg-muted)">interpolated</text>
                    <line x1="327" y1="168" x2="400" y2="252" stroke="var(--svg-green-accent)" stroke-width="2" stroke-dasharray="6,3"/>
                    <text x="380" y="210" font-size="9" fill="var(--svg-green-accent)">Equipotential</text>
                    <text x="380" y="222" font-size="9" fill="var(--svg-green-accent)">h = 42 m</text>
                    <line x1="100" y1="280" x2="340" y2="200" stroke="var(--svg-accent)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <text x="200" y="230" font-size="10" font-weight="bold" fill="var(--svg-accent)">Flow direction</text>
                    <text x="200" y="245" font-size="9" fill="var(--svg-accent)">⊥ to equipotential</text>
                    <text x="250" y="325" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Step: Interpolate equal-head point D on AC, draw BD (equipotential), flow ⊥ from A</text>
                </svg>''',
    'Figure 3.3b: Three-well triangulation — interpolate an equal-head point, draw the equipotential, and find the flow direction perpendicular to it.')

# 4. Dupuit assumptions and seepage face
SVGS['Limitations of the Dupuit Equation and the Seepage Face'] = svg_wrap('''
                <svg width="600" height="280" viewBox="0 0 600 280" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Dupuit Assumption vs Actual Flow — Seepage Face</text>
                    <rect x="40" y="220" width="520" height="30" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="300" y="242" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Impervious Base</text>
                    <line x1="540" y1="60" x2="540" y2="220" stroke="var(--svg-fg)" stroke-width="3"/>
                    <text x="560" y="140" font-size="9" fill="var(--svg-fg)">Dam</text>
                    <rect x="42" y="100" width="100" height="120" fill="var(--svg-water)" stroke="none" fill-opacity="0.3"/>
                    <text x="90" y="165" text-anchor="middle" font-size="9" fill="var(--svg-water-3)">h₁</text>
                    <path d="M140,100 C200,105 350,130 450,170 Q500,190 538,195" fill="none" stroke="var(--svg-accent)" stroke-width="2.5" stroke-dasharray="6,3"/>
                    <text x="350" y="125" font-size="10" fill="var(--svg-accent)">Dupuit (parabolic)</text>
                    <path d="M140,100 C200,108 350,140 450,185 Q500,205 538,150" fill="none" stroke="var(--svg-red-accent)" stroke-width="2.5"/>
                    <text x="430" y="210" font-size="10" fill="var(--svg-red-accent)">Actual phreatic surface</text>
                    <line x1="538" y1="150" x2="538" y2="195" stroke="var(--svg-orange-accent)" stroke-width="4"/>
                    <text x="520" y="145" text-anchor="end" font-size="10" font-weight="bold" fill="var(--svg-orange-accent)">Seepage</text>
                    <text x="520" y="158" text-anchor="end" font-size="10" font-weight="bold" fill="var(--svg-orange-accent)">Face</text>
                    <text x="300" y="268" text-anchor="middle" font-size="10" font-style="italic" fill="var(--svg-fg)">Dupuit assumes horizontal flow (∂h/∂z ≈ 0) — cannot predict the seepage face at exit</text>
                </svg>''',
    'Figure 3.5b: The Dupuit assumption predicts a parabolic water table but cannot capture the seepage face where flow exits the downstream boundary.')

# 5. Horizontal gallery
SVGS['Discharge Equation'] = svg_wrap('''
                <svg width="600" height="280" viewBox="0 0 600 280" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Infiltration Gallery — Cross Section</text>
                    <rect x="50" y="230" width="500" height="25" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="300" y="248" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Impervious layer</text>
                    <rect x="50" y="120" width="500" height="110" fill="var(--svg-water)" stroke="none" fill-opacity="0.2"/>
                    <path d="M50,90 C150,95 250,110 300,120 C350,110 450,95 550,90" fill="none" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <text x="150" y="85" font-size="10" fill="var(--svg-accent)">Water table</text>
                    <line x1="50" y1="60" x2="550" y2="60" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="300" y="55" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Ground surface</text>
                    <rect x="280" y="165" width="40" height="40" rx="20" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <circle cx="290" cy="185" r="2" fill="var(--svg-fg)"/>
                    <circle cx="300" cy="185" r="2" fill="var(--svg-fg)"/>
                    <circle cx="310" cy="185" r="2" fill="var(--svg-fg)"/>
                    <text x="300" y="215" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-fg)">Gallery</text>
                    <line x1="200" y1="150" x2="275" y2="180" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="400" y1="150" x2="325" y2="180" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="180" y="145" font-size="9" fill="var(--svg-water-3)">Seepage</text>
                    <text x="420" y="145" font-size="9" fill="var(--svg-water-3)">Seepage</text>
                    <line x1="70" y1="90" x2="70" y2="230" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <line x1="65" y1="90" x2="75" y2="90" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <line x1="65" y1="230" x2="75" y2="230" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="45" y="165" text-anchor="middle" font-size="10" fill="var(--svg-green-accent)">H</text>
                    <line x1="300" y1="120" x2="300" y2="165" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <text x="315" y="145" font-size="9" fill="var(--svg-red-accent)">s</text>
                    <text x="300" y="270" text-anchor="middle" font-size="11" fill="var(--svg-fg)">q = K(H² − h²)/(2L) per unit length per side</text>
                </svg>''',
    'Figure 3.7b: Infiltration gallery — a horizontal perforated pipe below the water table collects water by gravity flow from both sides.')

# 6. Laplace equation derivation visual
SVGS['Derivation via Conservation of Mass'] = svg_wrap('''
                <svg width="500" height="280" viewBox="0 0 500 280" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="250" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Laplace Equation — Derivation from Continuity</text>
                    <rect x="80" y="50" width="160" height="120" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="160" y="95" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Control volume</text>
                    <text x="160" y="115" text-anchor="middle" font-size="9" fill="var(--svg-muted)">dx × dy × dz</text>
                    <line x1="40" y1="110" x2="78" y2="110" stroke="var(--svg-accent)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="35" y="105" font-size="9" fill="var(--svg-accent)">q_x</text>
                    <line x1="242" y1="110" x2="290" y2="110" stroke="var(--svg-accent)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="295" y="105" font-size="9" fill="var(--svg-accent)">q_x+dx</text>
                    <line x1="160" y1="175" x2="160" y2="210" stroke="var(--svg-green-accent)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="175" y="210" font-size="9" fill="var(--svg-green-accent)">q_y</text>
                    <line x1="160" y1="48" x2="160" y2="30" stroke="var(--svg-green-accent)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="175" y="38" font-size="9" fill="var(--svg-green-accent)">q_y+dy</text>
                    <text x="250" y="195" text-anchor="start" font-size="11" fill="var(--svg-fg)">Continuity (steady, incompressible):</text>
                    <text x="250" y="215" text-anchor="start" font-size="12" fill="var(--svg-accent)">∂q_x/∂x + ∂q_y/∂y + ∂q_z/∂z = 0</text>
                    <text x="250" y="240" text-anchor="start" font-size="11" fill="var(--svg-fg)">Substitute Darcy (q = −K∇h):</text>
                    <text x="250" y="260" text-anchor="start" font-size="12" font-weight="bold" fill="var(--svg-accent)">∂²h/∂x² + ∂²h/∂y² + ∂²h/∂z² = 0</text>
                </svg>''',
    'Figure 3.4b: Laplace equation derived by combining continuity (mass balance) with Darcy\'s law — governs steady-state groundwater flow in homogeneous isotropic media.')

# 7. Water divide concept
SVGS['Location of the Water Table Divide'] = svg_wrap('''
                <svg width="550" height="250" viewBox="0 0 550 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Water Table Divide with Uniform Recharge</text>
                    <rect x="50" y="200" width="450" height="20" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="275" y="215" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Impervious base</text>
                    <rect x="50" y="70" width="15" height="130" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="40" y="140" text-anchor="end" font-size="10" fill="var(--svg-fg)">h₁</text>
                    <rect x="485" y="100" width="15" height="100" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="515" y="155" font-size="10" fill="var(--svg-fg)">h₂</text>
                    <path d="M65,70 C150,55 250,50 300,52 C350,54 430,65 485,100" fill="none" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <text x="200" y="48" font-size="10" fill="var(--svg-accent)">Water table (parabolic)</text>
                    <line x1="120" y1="30" x2="120" y2="55" stroke="var(--svg-water-3)" stroke-width="1" marker-end="url(#arr)"/>
                    <line x1="200" y1="30" x2="200" y2="48" stroke="var(--svg-water-3)" stroke-width="1" marker-end="url(#arr)"/>
                    <line x1="280" y1="30" x2="280" y2="50" stroke="var(--svg-water-3)" stroke-width="1" marker-end="url(#arr)"/>
                    <line x1="360" y1="30" x2="360" y2="53" stroke="var(--svg-water-3)" stroke-width="1" marker-end="url(#arr)"/>
                    <line x1="440" y1="30" x2="440" y2="62" stroke="var(--svg-water-3)" stroke-width="1" marker-end="url(#arr)"/>
                    <text x="275" y="28" text-anchor="middle" font-size="9" fill="var(--svg-water-3)">Recharge W (uniform)</text>
                    <line x1="260" y1="55" x2="260" y2="200" stroke="var(--svg-red-accent)" stroke-width="2" stroke-dasharray="5,3"/>
                    <text x="260" y="235" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-red-accent)">Water divide (d)</text>
                    <line x1="150" y1="75" x2="80" y2="80" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="370" y1="70" x2="470" y2="95" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="110" y="90" font-size="9" fill="var(--svg-fg)">q₁→</text>
                    <text x="430" y="80" font-size="9" fill="var(--svg-fg)">→q₂</text>
                    <text x="275" y="245" text-anchor="middle" font-size="10" fill="var(--svg-fg)">d = L/2 − K(h₁²−h₂²)/(2WL)</text>
                </svg>''',
    'Figure 3.6b: Water table divide — the point where flow splits toward the two canals, shifted from the midpoint when h₁ ≠ h₂.')

# 8. Seepage discharge from flow net
SVGS['Applications of Flow Nets in Engineering'] = svg_wrap('''
                <svg width="580" height="230" viewBox="0 0 580 230" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="290" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Seepage Discharge from a Flow Net</text>
                    <rect x="30" y="40" width="250" height="150" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="155" y="60" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">Flow Net Parameters</text>
                    <rect x="50" y="70" width="30" height="30" fill="none" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="65" y="90" text-anchor="middle" font-size="8" fill="var(--svg-accent)">Δs≈Δn</text>
                    <text x="100" y="82" font-size="10" fill="var(--svg-fg)">Curvilinear square</text>
                    <text x="155" y="110" text-anchor="middle" font-size="10" fill="var(--svg-fg)">N_f = number of flow channels</text>
                    <text x="155" y="130" text-anchor="middle" font-size="10" fill="var(--svg-fg)">N_d = number of potential drops</text>
                    <text x="155" y="150" text-anchor="middle" font-size="10" fill="var(--svg-fg)">H = total head difference</text>
                    <text x="155" y="170" text-anchor="middle" font-size="10" fill="var(--svg-fg)">K = hydraulic conductivity</text>
                    <line x1="290" y1="115" x2="310" y2="115" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <rect x="320" y="55" width="240" height="120" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="440" y="85" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Seepage Formula</text>
                    <text x="440" y="115" text-anchor="middle" font-size="16" font-weight="bold" fill="var(--svg-accent)">q = KH(N_f/N_d)</text>
                    <text x="440" y="140" text-anchor="middle" font-size="10" fill="var(--svg-muted)">per unit width (m³/s per m)</text>
                    <text x="440" y="160" text-anchor="middle" font-size="9" fill="var(--svg-muted)">For total: Q = q × width</text>
                    <text x="290" y="210" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Δh per drop = H/N_d    |    Δq per channel = KΔh = KH/N_d</text>
                </svg>''',
    'Figure 3.2b: Seepage discharge from a flow net — total seepage equals K × H × (N_f/N_d) per unit width of the structure.')

# 9. Confined aquifer flow between two reservoirs
SVGS['A. Constant Thickness'] = svg_wrap('''
                <svg width="550" height="230" viewBox="0 0 550 230" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Steady Flow in Confined Aquifer — Linear Head</text>
                    <rect x="50" y="100" width="450" height="60" fill="var(--svg-water)" stroke="none" fill-opacity="0.3"/>
                    <rect x="50" y="85" width="450" height="18" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <rect x="50" y="158" width="450" height="18" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="275" y="135" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Confined aquifer (K, b)</text>
                    <text x="275" y="80" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Confining layer (aquitard)</text>
                    <line x1="50" y1="50" x2="50" y2="85" stroke="var(--svg-accent)" stroke-width="1.5" stroke-dasharray="4,3"/>
                    <line x1="500" y1="65" x2="500" y2="85" stroke="var(--svg-accent)" stroke-width="1.5" stroke-dasharray="4,3"/>
                    <circle cx="50" cy="50" r="4" fill="var(--svg-accent)"/>
                    <text x="30" y="48" font-size="10" fill="var(--svg-accent)">h₁</text>
                    <circle cx="500" cy="65" r="4" fill="var(--svg-accent)"/>
                    <text x="515" y="63" font-size="10" fill="var(--svg-accent)">h₂</text>
                    <line x1="50" y1="50" x2="500" y2="65" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="275" y="45" text-anchor="middle" font-size="10" fill="var(--svg-accent)">Piezometric surface (linear)</text>
                    <line x1="100" y1="130" x2="460" y2="130" stroke="var(--svg-green-accent)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="280" y="150" text-anchor="middle" font-size="10" fill="var(--svg-green-accent)">Flow Q →</text>
                    <line x1="70" y1="100" x2="70" y2="160" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="65" y1="100" x2="75" y2="100" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="65" y1="160" x2="75" y2="160" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="55" y="135" text-anchor="middle" font-size="10" fill="var(--svg-fg)">b</text>
                    <text x="275" y="200" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">h(x) = h₁ − (h₁−h₂)x/L    (linear head distribution)</text>
                    <text x="275" y="220" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Q = Kb(h₁−h₂)/L = T(h₁−h₂)/L per unit width</text>
                </svg>''',
    'Figure 3.7c: Steady flow in a confined aquifer — head varies linearly with distance, and discharge per unit width equals T(h₁−h₂)/L.')

# 10. Uses of water table contour maps
SVGS['Uses of Water Table Contour Maps'] = svg_wrap('''
                <svg width="600" height="250" viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Applications of Water Table Contour Maps</text>
                    <rect x="200" y="40" width="200" height="35" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="300" y="62" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">WT Contour Map</text>
                    <line x1="200" y1="75" x2="100" y2="105" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="250" y1="75" x2="200" y2="105" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="300" y1="75" x2="300" y2="105" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="350" y1="75" x2="400" y2="105" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="400" y1="75" x2="500" y2="105" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <rect x="30" y="110" width="135" height="55" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="97" y="132" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Flow direction</text>
                    <text x="97" y="148" text-anchor="middle" font-size="9" fill="var(--svg-fg)">⊥ to contours</text>
                    <rect x="175" y="110" width="100" height="55" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="225" y="132" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Hydraulic</text>
                    <text x="225" y="148" text-anchor="middle" font-size="9" fill="var(--svg-fg)">gradient (i)</text>
                    <rect x="285" y="110" width="90" height="55" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <text x="330" y="132" text-anchor="middle" font-size="9" fill="var(--svg-fg)">GW-SW</text>
                    <text x="330" y="148" text-anchor="middle" font-size="9" fill="var(--svg-fg)">interaction</text>
                    <rect x="385" y="110" width="95" height="55" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="432" y="132" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Recharge /</text>
                    <text x="432" y="148" text-anchor="middle" font-size="9" fill="var(--svg-fg)">discharge areas</text>
                    <rect x="490" y="110" width="90" height="55" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <text x="535" y="132" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Well siting /</text>
                    <text x="535" y="148" text-anchor="middle" font-size="9" fill="var(--svg-fg)">pollution track</text>
                    <text x="300" y="195" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Gaining stream: contours curve upstream (GW → river)</text>
                    <text x="300" y="215" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Losing stream: contours curve downstream (river → GW)</text>
                    <text x="300" y="240" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Closely spaced contours → steep gradient → high velocity</text>
                </svg>''',
    'Figure 3.3c: Applications of water table contour maps — flow direction, gradient estimation, GW–SW interaction, and contamination tracking.')


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

print(f"\nChapter 3: {c} SVGs inserted")
print(f"  Before: {original} SVGs, After: {new_count} SVGs")
print(f"  Net added: {new_count - original}")

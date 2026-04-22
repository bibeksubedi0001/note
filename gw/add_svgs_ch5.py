"""Add 10 new educational SVG diagrams to Chapter 5 (Pumping Tests)."""
import re

FILE = r"d:\Final Year\Theory\gw\GW_THE\chapter5.html"

def svg_wrap(svg_content, caption):
    return f'''
            <div class="figure-container">
{svg_content}
                <div class="figcaption">{caption}</div>
            </div>
'''

SVGS = {}

# 1. Test Components
SVGS['Test Components'] = svg_wrap('''
                <svg width="600" height="260" viewBox="0 0 600 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Pumping Test Setup — Key Components</text>
                    <rect x="30" y="200" width="540" height="20" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <rect x="30" y="55" width="540" height="12" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="30" y="67" width="540" height="133" fill="var(--svg-water)" stroke="none" fill-opacity="0.15"/>
                    <rect x="296" y="35" width="8" height="185" fill="var(--svg-fg)"/>
                    <text x="300" y="30" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-red-accent)">Pumping Well</text>
                    <line x1="308" y1="45" x2="340" y2="30" stroke="var(--svg-red-accent)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="345" y="30" font-size="9" fill="var(--svg-red-accent)">Q (measured)</text>
                    <rect x="176" y="40" width="4" height="180" fill="var(--svg-green-accent)"/>
                    <text x="178" y="230" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">OW₁ (r₁)</text>
                    <rect x="426" y="40" width="4" height="180" fill="var(--svg-orange-accent)"/>
                    <text x="428" y="230" text-anchor="middle" font-size="9" fill="var(--svg-orange-accent)">OW₂ (r₂)</text>
                    <line x1="300" y1="180" x2="178" y2="180" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <text x="240" y="175" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">r₁</text>
                    <line x1="300" y1="190" x2="428" y2="190" stroke="var(--svg-orange-accent)" stroke-width="1"/>
                    <text x="365" y="185" text-anchor="middle" font-size="8" fill="var(--svg-orange-accent)">r₂</text>
                    <path d="M30,48 C130,45 250,42 296,52" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <path d="M304,52 C350,42 480,45 570,48" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="500" y="42" font-size="9" fill="var(--svg-accent)">Cone of depression</text>
                    <rect x="100" y="100" width="140" height="55" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="170" y="115" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-fg)">Measurements</text>
                    <text x="170" y="130" text-anchor="middle" font-size="8" fill="var(--svg-fg)">• Q = discharge rate</text>
                    <text x="170" y="142" text-anchor="middle" font-size="8" fill="var(--svg-fg)">• s = drawdown at OWs</text>
                    <text x="170" y="154" text-anchor="middle" font-size="8" fill="var(--svg-fg)">• t = time since pumping</text>
                    <text x="300" y="252" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Minimum 1 observation well needed; 2+ recommended for accuracy</text>
                </svg>''',
    'Figure 5.1b: Pumping test setup — a pumping well with observation wells at known distances r₁ and r₂ to measure drawdown over time.')

# 2. Constant-Rate Test
SVGS['A. Constant-Rate Pumping Tes'] = svg_wrap('''
                <svg width="550" height="240" viewBox="0 0 550 240" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Constant-Rate vs Step-Drawdown Test</text>
                    <rect x="20" y="45" width="240" height="160" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="140" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Constant-Rate Test</text>
                    <line x1="50" y1="80" x2="230" y2="80" stroke="var(--svg-accent)" stroke-width="0.8"/>
                    <text x="140" y="97" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Q = constant throughout</text>
                    <text x="140" y="115" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Duration: 24-72 hours</text>
                    <text x="140" y="135" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Determines: T and S</text>
                    <text x="140" y="155" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Analyses: Theis, Cooper-Jacob</text>
                    <text x="140" y="180" text-anchor="middle" font-size="9" fill="var(--svg-muted)">May include recovery phase</text>
                    <text x="140" y="196" text-anchor="middle" font-size="9" fill="var(--svg-muted)">(pump off, monitor s')</text>
                    <rect x="290" y="45" width="240" height="160" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="410" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Step-Drawdown Test</text>
                    <line x1="320" y1="80" x2="500" y2="80" stroke="var(--svg-green-accent)" stroke-width="0.8"/>
                    <text x="410" y="97" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Q increases in steps</text>
                    <text x="410" y="115" text-anchor="middle" font-size="9" fill="var(--svg-fg)">3-5 steps, 1-2 hrs each</text>
                    <text x="410" y="135" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Determines: B, C, well losses</text>
                    <text x="410" y="155" text-anchor="middle" font-size="9" fill="var(--svg-fg)">s_w = BQ + CQ²</text>
                    <text x="410" y="180" text-anchor="middle" font-size="9" fill="var(--svg-muted)">B = aquifer loss coefficient</text>
                    <text x="410" y="196" text-anchor="middle" font-size="9" fill="var(--svg-muted)">C = well loss coefficient</text>
                    <text x="275" y="228" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Well efficiency = BQ/(BQ + CQ²) × 100%</text>
                </svg>''',
    'Figure 5.2b: Comparison of constant-rate test (determines T and S) versus step-drawdown test (determines well losses and efficiency).')

# 3. Theis Assumptions
SVGS['Assumptions'] = svg_wrap('''
                <svg width="600" height="260" viewBox="0 0 600 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Theis Equation — Key Assumptions</text>
                    <rect x="30" y="40" width="260" height="80" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="160" y="58" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-accent)">Aquifer Properties</text>
                    <text x="160" y="76" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Homogeneous &amp; isotropic</text>
                    <text x="160" y="90" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Confined, uniform thickness b</text>
                    <text x="160" y="104" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Infinite lateral extent</text>
                    <rect x="310" y="40" width="260" height="80" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="440" y="58" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-green-accent)">Well Conditions</text>
                    <text x="440" y="76" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Fully penetrating well</text>
                    <text x="440" y="90" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Infinitesimal well diameter</text>
                    <text x="440" y="104" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Constant pumping rate Q</text>
                    <rect x="100" y="135" width="200" height="55" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <text x="200" y="153" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-water-3)">Flow Conditions</text>
                    <text x="200" y="170" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Transient (unsteady) flow</text>
                    <text x="200" y="184" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Darcy's law is valid</text>
                    <rect x="320" y="135" width="200" height="55" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="420" y="153" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-orange-accent)">Initial/Boundary</text>
                    <text x="420" y="170" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Initially horizontal WT/PS</text>
                    <text x="420" y="184" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• No recharge during test</text>
                    <text x="300" y="215" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">s = Q/(4πT) × W(u),  u = r²S/(4Tt)</text>
                    <text x="300" y="240" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Most assumptions are never perfectly met — results are approximate</text>
                </svg>''',
    'Figure 5.3b: The eight key assumptions behind the Theis equation — violations cause deviations from the theoretical type curve.')

# 4. Physical Meaning of Parameters
SVGS['Physical Meaning of Paramete'] = svg_wrap('''
                <svg width="600" height="250" viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Physical Meaning of T, S, u, and W(u)</text>
                    <rect x="20" y="45" width="135" height="90" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="87" y="63" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">T (m²/s)</text>
                    <text x="87" y="80" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Transmissivity</text>
                    <text x="87" y="95" text-anchor="middle" font-size="8" fill="var(--svg-fg)">= Kb</text>
                    <text x="87" y="112" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Rate of flow through</text>
                    <text x="87" y="125" text-anchor="middle" font-size="8" fill="var(--svg-fg)">full aquifer thickness</text>
                    <rect x="165" y="45" width="135" height="90" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="232" y="63" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">S (—)</text>
                    <text x="232" y="80" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Storativity</text>
                    <text x="232" y="95" text-anchor="middle" font-size="8" fill="var(--svg-fg)">= S_s × b</text>
                    <text x="232" y="112" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Volume released per</text>
                    <text x="232" y="125" text-anchor="middle" font-size="8" fill="var(--svg-fg)">unit area per unit Δh</text>
                    <rect x="310" y="45" width="135" height="90" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="377" y="63" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-orange-accent)">u (—)</text>
                    <text x="377" y="80" text-anchor="middle" font-size="8" fill="var(--svg-fg)">= r²S/(4Tt)</text>
                    <text x="377" y="95" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Dimensionless time</text>
                    <text x="377" y="112" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Small u = late time</text>
                    <text x="377" y="125" text-anchor="middle" font-size="8" fill="var(--svg-fg)">or close to well</text>
                    <rect x="455" y="45" width="135" height="90" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <text x="522" y="63" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-red-accent)">W(u)</text>
                    <text x="522" y="80" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Well function</text>
                    <text x="522" y="95" text-anchor="middle" font-size="8" fill="var(--svg-fg)">= −Ei(−u)</text>
                    <text x="522" y="112" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Dimensionless</text>
                    <text x="522" y="125" text-anchor="middle" font-size="8" fill="var(--svg-fg)">drawdown factor</text>
                    <text x="300" y="165" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">s = [Q/(4πT)] × W(u)</text>
                    <text x="300" y="190" text-anchor="middle" font-size="10" fill="var(--svg-fg)">High T → small s (easy flow) | High S → small s (more storage)</text>
                    <text x="300" y="210" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Small u → large W(u) → large s (near well or late time)</text>
                    <text x="300" y="235" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Typical values: Confined S = 10⁻⁵ to 10⁻³; Unconfined S = 0.01 to 0.30</text>
                </svg>''',
    'Figure 5.3c: Physical meaning of the four key pumping test parameters — transmissivity, storativity, dimensionless time, and well function.')

# 5. Step-by-Step Theis Procedure
SVGS['Step-by-Step Procedure (Exam'] = svg_wrap('''
                <svg width="550" height="280" viewBox="0 0 550 280" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Theis Type-Curve Method — Step-by-Step</text>
                    <rect x="40" y="42" width="470" height="38" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="55" y="58" font-weight="bold" font-size="10" fill="var(--svg-accent)">Step 1:</text>
                    <text x="110" y="58" font-size="9" fill="var(--svg-fg)">Plot W(u) vs 1/u on log-log paper (type curve)</text>
                    <text x="110" y="73" font-size="9" fill="var(--svg-muted)">This is a standard curve — same for all aquifers</text>
                    <rect x="40" y="88" width="470" height="38" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="55" y="104" font-weight="bold" font-size="10" fill="var(--svg-green-accent)">Step 2:</text>
                    <text x="110" y="104" font-size="9" fill="var(--svg-fg)">Plot field data: s vs r²/t on same-scale log-log paper</text>
                    <text x="110" y="119" font-size="9" fill="var(--svg-muted)">Use same paper size and decade spacing</text>
                    <rect x="40" y="134" width="470" height="38" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <text x="55" y="150" font-weight="bold" font-size="10" fill="var(--svg-water-3)">Step 3:</text>
                    <text x="110" y="150" font-size="9" fill="var(--svg-fg)">Overlay and slide field data (keeping axes parallel) until curves match</text>
                    <text x="110" y="165" font-size="9" fill="var(--svg-muted)">Do NOT rotate — only translate horizontally and vertically</text>
                    <rect x="40" y="180" width="470" height="38" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="55" y="196" font-weight="bold" font-size="10" fill="var(--svg-orange-accent)">Step 4:</text>
                    <text x="110" y="196" font-size="9" fill="var(--svg-fg)">Pick any convenient match point and read: W(u), 1/u, s, r²/t</text>
                    <text x="110" y="211" font-size="9" fill="var(--svg-muted)">Match point need NOT be on the curve itself</text>
                    <rect x="40" y="226" width="470" height="38" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <text x="55" y="242" font-weight="bold" font-size="10" fill="var(--svg-red-accent)">Step 5:</text>
                    <text x="110" y="242" font-size="9" fill="var(--svg-fg)">Compute: T = QW(u)/(4πs)  and  S = 4Tu/(r²/t)</text>
                    <text x="110" y="257" font-size="9" fill="var(--svg-muted)">Verify with alternative match points for consistency</text>
                </svg>''',
    'Figure 5.4b: Five-step procedure for the Theis type-curve method — from plotting through overlay matching to parameter computation.')

# 6. Limitations of Thiem
SVGS['Limitations of Thiem'] = svg_wrap('''
                <svg width="550" height="230" viewBox="0 0 550 230" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Thiem Method — Advantages &amp; Limitations</text>
                    <rect x="20" y="45" width="240" height="155" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="140" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Advantages</text>
                    <text x="140" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Simple formula, easy to apply</text>
                    <text x="140" y="102" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• T determined directly</text>
                    <text x="140" y="119" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• No curve matching needed</text>
                    <text x="140" y="136" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Works with 2 OWs</text>
                    <text x="140" y="155" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Good for preliminary</text>
                    <text x="140" y="170" text-anchor="middle" font-size="9" fill="var(--svg-muted)">estimate of T</text>
                    <rect x="290" y="45" width="240" height="155" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="2"/>
                    <text x="410" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-red-accent)">Limitations</text>
                    <text x="410" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Steady-state only</text>
                    <text x="410" y="102" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Cannot determine S</text>
                    <text x="410" y="119" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Requires equilibrium</text>
                    <text x="410" y="136" text-anchor="middle" font-size="9" fill="var(--svg-fg)">  (may take days in confined)</text>
                    <text x="410" y="155" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• R must be estimated</text>
                    <text x="410" y="172" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Needs 2+ observation wells</text>
                    <text x="275" y="220" text-anchor="middle" font-size="10" font-style="italic" fill="var(--svg-fg)">For S determination → use transient methods (Theis, Cooper-Jacob)</text>
                </svg>''',
    'Figure 5.5b: Thiem\'s method — simple and direct for T, but limited to steady-state and cannot determine storativity S.')

# 7. Why Straight Line
SVGS['Why This Is a Straight Line'] = svg_wrap('''
                <svg width="550" height="220" viewBox="0 0 550 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Cooper-Jacob Approximation — Mathematical Basis</text>
                    <rect x="30" y="45" width="490" height="35" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1"/>
                    <text x="275" y="60" text-anchor="middle" font-size="10" fill="var(--svg-fg)">For u &lt; 0.01: W(u) ≈ −0.5772 − ln(u) = ln(1/u) − 0.5772</text>
                    <text x="275" y="75" text-anchor="middle" font-size="9" fill="var(--svg-muted)">(Higher-order terms u − u²/4 + u³/18 − ... are negligible)</text>
                    <line x1="275" y1="80" x2="275" y2="95" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <rect x="30" y="98" width="490" height="35" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <text x="275" y="113" text-anchor="middle" font-size="10" fill="var(--svg-fg)">s = (Q/4πT)[ln(4Tt/r²S) − 0.5772] = (2.3Q/4πT)log(2.25Tt/r²S)</text>
                    <text x="275" y="128" text-anchor="middle" font-size="9" fill="var(--svg-muted)">This is linear in log(t) → straight line on semi-log paper</text>
                    <line x1="275" y1="135" x2="275" y2="148" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <rect x="80" y="150" width="190" height="50" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="175" y="167" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-accent)">Slope gives T</text>
                    <text x="175" y="185" text-anchor="middle" font-size="9" fill="var(--svg-fg)">T = 2.3Q/(4πΔs)</text>
                    <rect x="290" y="150" width="190" height="50" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="385" y="167" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-green-accent)">Intercept gives S</text>
                    <text x="385" y="185" text-anchor="middle" font-size="9" fill="var(--svg-fg)">S = 2.25Tt₀/r²</text>
                    <text x="275" y="215" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Validity: u &lt; 0.01 → use only late-time data or data from wells close to pumping well</text>
                </svg>''',
    'Figure 5.6b: Mathematical derivation of the Cooper-Jacob straight-line approximation — truncating the Theis series for small u yields a linear s vs log(t) relationship.')

# 8. Time-Drawdown vs Distance-Drawdown
SVGS['Time-Drawdown vs Distance-Dr'] = svg_wrap('''
                <svg width="600" height="230" viewBox="0 0 600 230" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Time-Drawdown vs Distance-Drawdown Analysis</text>
                    <rect x="20" y="45" width="265" height="150" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="152" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Time-Drawdown</text>
                    <text x="152" y="83" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Plot s vs log(t) from one OW</text>
                    <text x="152" y="100" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Slope: Δs per log cycle of t</text>
                    <text x="152" y="120" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-accent)">T = 2.3Q/(4πΔs)</text>
                    <text x="152" y="140" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-accent)">S = 2.25Tt₀/r²</text>
                    <text x="152" y="162" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Single well data sufficient</text>
                    <text x="152" y="178" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Determines both T and S</text>
                    <rect x="315" y="45" width="265" height="150" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="447" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Distance-Drawdown</text>
                    <text x="447" y="83" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Plot s vs log(r) at same time t</text>
                    <text x="447" y="100" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Slope: Δs per log cycle of r</text>
                    <text x="447" y="120" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-green-accent)">T = 2.3Q/(2πΔs)</text>
                    <text x="447" y="140" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-green-accent)">S = 2.25Tt/r₀²</text>
                    <text x="447" y="162" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Needs 3+ observation wells</text>
                    <text x="447" y="178" text-anchor="middle" font-size="9" fill="var(--svg-muted)">All at same time snapshot</text>
                    <text x="300" y="215" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Note: Distance formula has 2π (not 4π) because r appears as r² in u</text>
                </svg>''',
    'Figure 5.7b: Two variants of the Cooper-Jacob method — time-drawdown (single well, s vs log t) and distance-drawdown (multiple wells, s vs log r at fixed time).')

# 9. Recovery Test Advantage
SVGS['Advantages of the Recovery Te'] = svg_wrap('''
                <svg width="550" height="230" viewBox="0 0 550 230" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Recovery Test — Why It Works</text>
                    <rect x="30" y="45" width="490" height="80" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="275" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Superposition Principle</text>
                    <text x="275" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Recovery = original pumping well (Q, time t) + imaginary recharge well (−Q, time t')</text>
                    <text x="275" y="102" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Residual drawdown: s' = (Q/4πT)[W(u) − W(u')]  ≈  (2.3Q/4πT)log(t/t')</text>
                    <rect x="30" y="140" width="240" height="60" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="150" y="158" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-green-accent)">Advantages</text>
                    <text x="150" y="175" text-anchor="middle" font-size="9" fill="var(--svg-fg)">No Q measurement during recovery</text>
                    <text x="150" y="190" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Cross-checks pumping phase T</text>
                    <rect x="290" y="140" width="230" height="60" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="405" y="158" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-orange-accent)">Key Point</text>
                    <text x="405" y="175" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Recovery gives T only</text>
                    <text x="405" y="190" text-anchor="middle" font-size="9" fill="var(--svg-fg)">S cannot be obtained</text>
                    <text x="275" y="222" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Plot s' vs log(t/t') → straight line → T = 2.3Q/(4πΔs')</text>
                </svg>''',
    'Figure 5.8b: Recovery test uses superposition to derive T from residual drawdown — independent of Q measurement errors during pumping.')

# 10. Detecting Boundaries
SVGS['Detecting Boundaries from Pum'] = svg_wrap('''
                <svg width="600" height="250" viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Boundary Detection from Pumping Test Data</text>
                    <rect x="20" y="40" width="270" height="175" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="155" y="60" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Barrier (No-Flow) Boundary</text>
                    <line x1="40" y1="130" x2="270" y2="130" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="40" y1="130" x2="40" y2="70" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="155" y="125" text-anchor="middle" font-size="8" fill="var(--svg-muted)">log(t)</text>
                    <text x="35" y="100" text-anchor="middle" font-size="8" fill="var(--svg-muted)" transform="rotate(-90 35 100)">s</text>
                    <line x1="50" y1="125" x2="160" y2="102" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <line x1="160" y1="102" x2="260" y2="75" stroke="var(--svg-red-accent)" stroke-width="2.5"/>
                    <text x="110" y="98" font-size="8" fill="var(--svg-green-accent)">slope = m</text>
                    <text x="225" y="72" font-size="8" fill="var(--svg-red-accent)">slope = 2m</text>
                    <text x="155" y="152" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Slope doubles → drawdown</text>
                    <text x="155" y="166" text-anchor="middle" font-size="9" fill="var(--svg-fg)">increases faster</text>
                    <text x="155" y="185" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Image well: +Q (pumping)</text>
                    <text x="155" y="200" text-anchor="middle" font-size="9" fill="var(--svg-muted)">at mirror distance</text>
                    <rect x="310" y="40" width="270" height="175" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="445" y="60" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Recharge Boundary</text>
                    <line x1="330" y1="130" x2="560" y2="130" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="330" y1="130" x2="330" y2="70" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="445" y="125" text-anchor="middle" font-size="8" fill="var(--svg-muted)">log(t)</text>
                    <text x="325" y="100" text-anchor="middle" font-size="8" fill="var(--svg-muted)" transform="rotate(-90 325 100)">s</text>
                    <line x1="340" y1="125" x2="440" y2="105" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="440" y1="105" x2="550" y2="103" stroke="var(--svg-water-3)" stroke-width="2.5"/>
                    <text x="390" y="100" font-size="8" fill="var(--svg-accent)">slope = m</text>
                    <text x="500" y="98" font-size="8" fill="var(--svg-water-3)">slope → 0</text>
                    <text x="445" y="152" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Slope flattens → drawdown</text>
                    <text x="445" y="166" text-anchor="middle" font-size="9" fill="var(--svg-fg)">stabilizes (recharge)</text>
                    <text x="445" y="185" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Image well: −Q (recharge)</text>
                    <text x="445" y="200" text-anchor="middle" font-size="9" fill="var(--svg-muted)">at mirror distance</text>
                    <text x="300" y="240" text-anchor="middle" font-size="10" fill="var(--svg-fg)">A break in the semi-log straight line signals a boundary — slope change reveals boundary type</text>
                </svg>''',
    'Figure 5.9b: Boundary detection — a barrier boundary doubles the semi-log slope, while a recharge boundary causes the slope to flatten to zero.')


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

print(f"\nChapter 5: {c} SVGs inserted")
print(f"  Before: {original} SVGs, After: {new_count} SVGs")
print(f"  Net added: {new_count - original}")

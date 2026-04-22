"""Add 10 new educational SVG diagrams to Chapter 6 (GW Exploration)."""
import re

FILE = r"d:\Final Year\Theory\gw\GW_THE\chapter6.html"

def svg_wrap(svg_content, caption):
    return f'''
            <div class="figure-container">
{svg_content}
                <div class="figcaption">{caption}</div>
            </div>
'''

SVGS = {}

# 1. Objectives of GW exploration
SVGS['A. Determination of Groundwat'] = svg_wrap('''
                <svg width="600" height="240" viewBox="0 0 600 240" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Objectives of Groundwater Exploration</text>
                    <rect x="200" y="40" width="200" height="32" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="300" y="60" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">GW Exploration</text>
                    <line x1="150" y1="72" x2="100" y2="100" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="250" y1="72" x2="200" y2="100" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="300" y1="72" x2="300" y2="100" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="350" y1="72" x2="400" y2="100" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="450" y1="72" x2="500" y2="100" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <rect x="20" y="100" width="160" height="50" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="100" y="118" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Occurrence &amp;</text>
                    <text x="100" y="133" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Distribution</text>
                    <rect x="125" y="100" width="150" height="50" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="200" y="118" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Quantity &amp;</text>
                    <text x="200" y="133" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Yield Assessment</text>
                    <rect x="230" y="100" width="140" height="50" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <text x="300" y="118" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Water Quality</text>
                    <text x="300" y="133" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Evaluation</text>
                    <rect x="330" y="100" width="140" height="50" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="400" y="118" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Well Site</text>
                    <text x="400" y="133" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Selection</text>
                    <rect x="425" y="100" width="155" height="50" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <text x="502" y="118" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Management &amp;</text>
                    <text x="502" y="133" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Sustainability</text>
                    <text x="300" y="180" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Three-phase approach: Desk Study → Field Investigation → Testing &amp; Analysis</text>
                    <text x="300" y="200" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Surface methods first (non-invasive, low-cost) → Subsurface methods (drilling, pumping tests)</text>
                    <text x="300" y="225" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Key tools: geological maps, geophysics, remote sensing, test drilling, pumping tests</text>
                </svg>''',
    'Figure 6.2b: The five main objectives of groundwater exploration — from occurrence mapping to sustainable management.')

# 2. Geological survey
SVGS['6.3.1 Geological Survey'] = svg_wrap('''
                <svg width="550" height="230" viewBox="0 0 550 230" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Geological &amp; Hydrogeological Survey — Key Outputs</text>
                    <rect x="20" y="45" width="240" height="145" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="140" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Geological Survey</text>
                    <text x="140" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Rock types &amp; stratigraphy</text>
                    <text x="140" y="102" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Structural features (faults, folds)</text>
                    <text x="140" y="119" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Weathering &amp; fracture zones</text>
                    <text x="140" y="136" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Surface drainage patterns</text>
                    <text x="140" y="156" text-anchor="middle" font-size="9" fill="var(--svg-muted)">→ Identifies likely aquifer</text>
                    <text x="140" y="172" text-anchor="middle" font-size="9" fill="var(--svg-muted)">   formations &amp; boundaries</text>
                    <rect x="290" y="45" width="240" height="145" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="410" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Hydrogeological Survey</text>
                    <text x="410" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Spring &amp; seepage inventory</text>
                    <text x="410" y="102" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Well inventory &amp; water levels</text>
                    <text x="410" y="119" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Water quality sampling</text>
                    <text x="410" y="136" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Recharge area mapping</text>
                    <text x="410" y="156" text-anchor="middle" font-size="9" fill="var(--svg-muted)">→ Characterizes GW system</text>
                    <text x="410" y="172" text-anchor="middle" font-size="9" fill="var(--svg-muted)">   behavior &amp; yield potential</text>
                    <text x="275" y="215" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Both surveys are desk + field studies, done BEFORE any drilling or geophysics</text>
                </svg>''',
    'Figure 6.3b: Geological and hydrogeological surveys — the essential first steps that guide subsequent exploration methods.')

# 3. Resistivity principle
SVGS['6.6.1 Principle'] = svg_wrap('''
                <svg width="600" height="270" viewBox="0 0 600 270" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Electrical Resistivity — Measurement Principle</text>
                    <line x1="50" y1="100" x2="550" y2="100" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="300" y="93" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Ground surface</text>
                    <line x1="150" y1="60" x2="150" y2="100" stroke="var(--svg-accent)" stroke-width="3"/>
                    <text x="150" y="52" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-accent)">C₁</text>
                    <line x1="450" y1="60" x2="450" y2="100" stroke="var(--svg-accent)" stroke-width="3"/>
                    <text x="450" y="52" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-accent)">C₂</text>
                    <line x1="250" y1="65" x2="250" y2="100" stroke="var(--svg-green-accent)" stroke-width="3"/>
                    <text x="250" y="57" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-green-accent)">P₁</text>
                    <line x1="350" y1="65" x2="350" y2="100" stroke="var(--svg-green-accent)" stroke-width="3"/>
                    <text x="350" y="57" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-green-accent)">P₂</text>
                    <path d="M150,100 C200,150 250,180 300,185 C350,180 400,150 450,100" fill="none" stroke="var(--svg-water-3)" stroke-width="1.5" stroke-dasharray="5,3"/>
                    <text x="300" y="200" text-anchor="middle" font-size="9" fill="var(--svg-water-3)">Current flow lines</text>
                    <line x1="100" y1="40" x2="200" y2="40" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="150" y="38" text-anchor="middle" font-size="8" fill="var(--svg-accent)">I (current)</text>
                    <line x1="250" y1="42" x2="350" y2="42" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="300" y="40" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">ΔV (measured)</text>
                    <text x="300" y="228" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">ρ_a = K × (ΔV/I)</text>
                    <text x="300" y="248" text-anchor="middle" font-size="10" fill="var(--svg-fg)">K = geometric factor depending on electrode spacing</text>
                    <text x="300" y="265" text-anchor="middle" font-size="9" fill="var(--svg-muted)">C₁,C₂ = current electrodes; P₁,P₂ = potential electrodes</text>
                </svg>''',
    'Figure 6.6b: Electrical resistivity measurement principle — inject current through C₁-C₂, measure potential drop at P₁-P₂, compute apparent resistivity.')

# 4. Typical Resistivity Values
SVGS['6.6.2 Typical Resistivity Val'] = svg_wrap('''
                <svg width="600" height="250" viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Typical Resistivity Values (Ω·m)</text>
                    <line x1="80" y1="55" x2="80" y2="220" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="80" y1="220" x2="560" y2="220" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="320" y="240" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Resistivity (Ω·m) — log scale</text>
                    <text x="95" y="234" font-size="8" fill="var(--svg-muted)">1</text>
                    <text x="175" y="234" font-size="8" fill="var(--svg-muted)">10</text>
                    <text x="255" y="234" font-size="8" fill="var(--svg-muted)">100</text>
                    <text x="335" y="234" font-size="8" fill="var(--svg-muted)">1000</text>
                    <text x="415" y="234" font-size="8" fill="var(--svg-muted)">10⁴</text>
                    <text x="495" y="234" font-size="8" fill="var(--svg-muted)">10⁵</text>
                    <rect x="85" y="60" width="60" height="22" rx="3" fill="var(--svg-water)" fill-opacity="0.5" stroke="var(--svg-water-3)" stroke-width="1"/>
                    <text x="68" y="75" text-anchor="end" font-size="9" fill="var(--svg-fg)">Clay</text>
                    <rect x="95" y="90" width="200" height="22" rx="3" fill="var(--svg-green-lt)" fill-opacity="0.5" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <text x="68" y="105" text-anchor="end" font-size="9" fill="var(--svg-fg)">Sand (wet)</text>
                    <rect x="180" y="120" width="250" height="22" rx="3" fill="var(--svg-yellow-lt)" fill-opacity="0.5" stroke="var(--svg-orange-accent)" stroke-width="1"/>
                    <text x="68" y="135" text-anchor="end" font-size="9" fill="var(--svg-fg)">Gravel</text>
                    <rect x="320" y="150" width="220" height="22" rx="3" fill="var(--svg-red-lt)" fill-opacity="0.5" stroke="var(--svg-red-accent)" stroke-width="1"/>
                    <text x="68" y="165" text-anchor="end" font-size="9" fill="var(--svg-fg)">Sandstone</text>
                    <rect x="380" y="180" width="170" height="22" rx="3" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="68" y="195" text-anchor="end" font-size="9" fill="var(--svg-fg)">Granite</text>
                    <text x="300" y="250" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Low ρ → clay/saline water (conductive) | High ρ → hard rock/dry sand (resistive)</text>
                </svg>''',
    'Figure 6.6c: Typical resistivity ranges for common geological materials — low values indicate clay or saturated sediments, high values indicate hard rock.')

# 5. Types of Resistivity Surveys
SVGS['6.6.4 Types of Resistivity Su'] = svg_wrap('''
                <svg width="600" height="270" viewBox="0 0 600 270" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">VES (Sounding) vs Lateral Profiling</text>
                    <rect x="20" y="45" width="270" height="190" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="155" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">VES (Vertical Sounding)</text>
                    <text x="155" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Fixed center point</text>
                    <text x="155" y="102" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Expand electrode spacing</text>
                    <text x="155" y="119" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Probes deeper with each step</text>
                    <text x="155" y="140" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-accent)">Result:</text>
                    <text x="155" y="157" text-anchor="middle" font-size="9" fill="var(--svg-fg)">ρ_a vs electrode spacing</text>
                    <text x="155" y="174" text-anchor="middle" font-size="9" fill="var(--svg-fg)">→ Vertical layer boundaries</text>
                    <text x="155" y="195" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Best for: layered aquifers</text>
                    <text x="155" y="210" text-anchor="middle" font-size="9" fill="var(--svg-muted)">determining depth to bedrock</text>
                    <rect x="310" y="45" width="270" height="190" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="445" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Lateral Profiling</text>
                    <text x="445" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Fixed electrode spacing</text>
                    <text x="445" y="102" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Move entire array along line</text>
                    <text x="445" y="119" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Constant depth of investigation</text>
                    <text x="445" y="140" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-green-accent)">Result:</text>
                    <text x="445" y="157" text-anchor="middle" font-size="9" fill="var(--svg-fg)">ρ_a vs horizontal position</text>
                    <text x="445" y="174" text-anchor="middle" font-size="9" fill="var(--svg-fg)">→ Lateral boundaries/changes</text>
                    <text x="445" y="195" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Best for: fault detection,</text>
                    <text x="445" y="210" text-anchor="middle" font-size="9" fill="var(--svg-muted)">mapping lateral extent</text>
                    <text x="300" y="255" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Often combined: VES at multiple stations along a profile for 2D imaging</text>
                </svg>''',
    'Figure 6.6d: Two types of resistivity surveys — VES probes vertically by expanding spacing, while lateral profiling maps horizontal variations at constant depth.')

# 6. Seismic refraction principle
SVGS['6.7.1 Principle'] = svg_wrap('''
                <svg width="600" height="280" viewBox="0 0 600 280" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Seismic Refraction — Principle</text>
                    <line x1="50" y1="100" x2="550" y2="100" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="300" y="93" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Ground surface</text>
                    <rect x="50" y="100" width="500" height="70" fill="var(--svg-bg-soft)" stroke="none"/>
                    <text x="300" y="140" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Layer 1: V₁ (soil/alluvium)</text>
                    <line x1="50" y1="170" x2="550" y2="170" stroke="var(--svg-accent)" stroke-width="2" stroke-dasharray="6,3"/>
                    <rect x="50" y="170" width="500" height="60" fill="var(--svg-water)" stroke="none" fill-opacity="0.15"/>
                    <text x="300" y="205" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Layer 2: V₂ &gt; V₁ (bedrock/saturated)</text>
                    <circle cx="100" cy="98" r="6" fill="var(--svg-red-accent)"/>
                    <text x="100" y="85" text-anchor="middle" font-size="9" fill="var(--svg-red-accent)">Shot</text>
                    <line x1="106" y1="100" x2="200" y2="170" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="140" y="145" font-size="8" fill="var(--svg-accent)">Direct</text>
                    <line x1="200" y1="170" x2="400" y2="170" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="300" y="165" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">Refracted (along interface at V₂)</text>
                    <line x1="400" y1="170" x2="450" y2="100" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <circle cx="200" cy="98" r="3" fill="var(--svg-fg)"/>
                    <circle cx="250" cy="98" r="3" fill="var(--svg-fg)"/>
                    <circle cx="300" cy="98" r="3" fill="var(--svg-fg)"/>
                    <circle cx="350" cy="98" r="3" fill="var(--svg-fg)"/>
                    <circle cx="400" cy="98" r="3" fill="var(--svg-fg)"/>
                    <circle cx="450" cy="98" r="3" fill="var(--svg-fg)"/>
                    <text x="500" y="95" font-size="8" fill="var(--svg-fg)">Geophones</text>
                    <text x="300" y="245" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Near geophones: direct wave arrives first (travel through V₁)</text>
                    <text x="300" y="262" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Far geophones: refracted wave arrives first (faster V₂ compensates longer path)</text>
                    <text x="300" y="278" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Crossover distance x_c tells depth to interface: z = x_c/2 × √[(V₂−V₁)/(V₂+V₁)]</text>
                </svg>''',
    'Figure 6.7b: Seismic refraction principle — the refracted wave arrives first at distant geophones because it travels along the faster deeper layer.')

# 7. Snell's Law
SVGS['6.7.2 Snell'] = svg_wrap('''
                <svg width="500" height="250" viewBox="0 0 500 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="250" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Snell's Law of Refraction</text>
                    <line x1="50" y1="120" x2="450" y2="120" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="350" y="115" font-size="9" fill="var(--svg-fg)">Interface</text>
                    <line x1="250" y1="40" x2="250" y2="200" stroke="var(--svg-fg)" stroke-width="1" stroke-dasharray="4,3"/>
                    <text x="260" y="50" font-size="8" fill="var(--svg-muted)">Normal</text>
                    <line x1="160" y1="45" x2="250" y2="120" stroke="var(--svg-accent)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <text x="175" y="70" font-size="10" fill="var(--svg-accent)">Incident</text>
                    <path d="M250,85 A35,35 0 0,0 228,73" fill="none" stroke="var(--svg-accent)" stroke-width="1"/>
                    <text x="220" y="90" font-size="10" fill="var(--svg-accent)">i₁</text>
                    <line x1="250" y1="120" x2="370" y2="195" stroke="var(--svg-green-accent)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <text x="340" y="165" font-size="10" fill="var(--svg-green-accent)">Refracted</text>
                    <path d="M250,150 A30,30 0 0,1 275,160" fill="none" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <text x="275" y="155" font-size="10" fill="var(--svg-green-accent)">i₂</text>
                    <text x="150" y="112" font-size="10" fill="var(--svg-fg)">V₁</text>
                    <text x="150" y="138" font-size="10" fill="var(--svg-fg)">V₂ &gt; V₁</text>
                    <text x="250" y="225" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">sin(i₁)/V₁ = sin(i₂)/V₂</text>
                    <text x="250" y="245" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Critical angle: i₁ = sin⁻¹(V₁/V₂) → total refraction along interface</text>
                </svg>''',
    'Figure 6.7c: Snell\'s law of seismic refraction — at the critical angle, the refracted ray travels along the interface at velocity V₂.')

# 8. Comparison Electrical vs Seismic
SVGS['6.7.7 Comparison: Electrical'] = svg_wrap('''
                <svg width="650" height="230" viewBox="0 0 650 230" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="325" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Electrical Resistivity vs Seismic Refraction</text>
                    <rect x="20" y="40" width="295" height="170" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="167" y="60" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Electrical Resistivity</text>
                    <text x="167" y="80" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Measures: electrical resistance</text>
                    <text x="167" y="97" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Differentiates: clay vs sand vs rock</text>
                    <text x="167" y="114" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Detects: fresh vs saline water</text>
                    <text x="167" y="131" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Equipment: simple, portable</text>
                    <text x="167" y="148" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Cost: lower</text>
                    <text x="167" y="170" text-anchor="middle" font-size="9" fill="var(--svg-red-accent)">Limitation: affected by surface</text>
                    <text x="167" y="184" text-anchor="middle" font-size="9" fill="var(--svg-red-accent)">water, buried metals, power lines</text>
                    <rect x="335" y="40" width="295" height="170" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="482" y="60" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Seismic Refraction</text>
                    <text x="482" y="80" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Measures: wave velocity</text>
                    <text x="482" y="97" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Best for: depth to bedrock</text>
                    <text x="482" y="114" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Cannot distinguish: water quality</text>
                    <text x="482" y="131" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Equipment: more complex</text>
                    <text x="482" y="148" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Cost: higher</text>
                    <text x="482" y="170" text-anchor="middle" font-size="9" fill="var(--svg-red-accent)">Limitation: V must increase</text>
                    <text x="482" y="184" text-anchor="middle" font-size="9" fill="var(--svg-red-accent)">with depth (no velocity inversion)</text>
                    <text x="325" y="225" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Best practice: use BOTH methods together for cross-validation</text>
                </svg>''',
    'Figure 6.7d: Comparison of the two main geophysical methods for groundwater exploration — resistivity excels at lithology and water quality, seismic at depth to bedrock.')

# 9. GPR
SVGS['6.8.1 Ground-Penetrating Rada'] = svg_wrap('''
                <svg width="550" height="220" viewBox="0 0 550 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Other Geophysical Methods — Overview</text>
                    <rect x="20" y="45" width="160" height="85" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="100" y="63" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-accent)">GPR</text>
                    <text x="100" y="80" text-anchor="middle" font-size="8" fill="var(--svg-fg)">EM waves reflected</text>
                    <text x="100" y="93" text-anchor="middle" font-size="8" fill="var(--svg-fg)">from interfaces</text>
                    <text x="100" y="110" text-anchor="middle" font-size="8" fill="var(--svg-muted)">High resolution,</text>
                    <text x="100" y="122" text-anchor="middle" font-size="8" fill="var(--svg-muted)">shallow depth (&lt;30 m)</text>
                    <rect x="195" y="45" width="160" height="85" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="275" y="63" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-green-accent)">Gravity Survey</text>
                    <text x="275" y="80" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Measures g variations</text>
                    <text x="275" y="93" text-anchor="middle" font-size="8" fill="var(--svg-fg)">→ density contrasts</text>
                    <text x="275" y="110" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Detects buried valleys,</text>
                    <text x="275" y="122" text-anchor="middle" font-size="8" fill="var(--svg-muted)">basalt intrusions</text>
                    <rect x="370" y="45" width="160" height="85" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="450" y="63" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-orange-accent)">EM Methods</text>
                    <text x="450" y="80" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Induced EM fields</text>
                    <text x="450" y="93" text-anchor="middle" font-size="8" fill="var(--svg-fg)">No ground contact</text>
                    <text x="450" y="110" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Fast reconnaissance,</text>
                    <text x="450" y="122" text-anchor="middle" font-size="8" fill="var(--svg-muted)">airborne possible</text>
                    <rect x="110" y="145" width="160" height="50" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <text x="190" y="163" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-water-3)">Magnetic Survey</text>
                    <text x="190" y="180" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Detects basalt, iron-rich</text>
                    <text x="190" y="190" text-anchor="middle" font-size="8" fill="var(--svg-fg)">formations; limits in GW</text>
                    <rect x="290" y="145" width="160" height="50" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-purple-accent)" stroke-width="1.5"/>
                    <text x="370" y="163" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-purple-accent)">Remote Sensing</text>
                    <text x="370" y="180" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Satellite imagery for</text>
                    <text x="370" y="190" text-anchor="middle" font-size="8" fill="var(--svg-fg)">lineaments, land use, GIS</text>
                    <text x="275" y="215" text-anchor="middle" font-size="9" fill="var(--svg-fg)">All methods are complementary — no single method is sufficient for complete GW characterization</text>
                </svg>''',
    'Figure 6.8b: Overview of other geophysical methods — GPR, gravity, EM, magnetic, and remote sensing each provide different subsurface information.')

# 10. Test drilling
SVGS['6.4.1 Test Drilling (Explorat'] = svg_wrap('''
                <svg width="550" height="280" viewBox="0 0 550 280" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Subsurface Exploration — Test Drilling &amp; Well Logging</text>
                    <rect x="30" y="45" width="230" height="200" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="145" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Test Drilling</text>
                    <text x="145" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Direct investigation method</text>
                    <text x="145" y="105" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Identifies lithology</text>
                    <text x="145" y="120" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Collects soil/rock samples</text>
                    <text x="145" y="135" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Measures water levels</text>
                    <text x="145" y="150" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Defines aquifer depth</text>
                    <text x="145" y="170" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Methods:</text>
                    <text x="145" y="185" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Percussion, rotary, DTH</text>
                    <text x="145" y="205" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Produces: borehole log</text>
                    <text x="145" y="225" text-anchor="middle" font-size="9" fill="var(--svg-fg)">with depth vs material</text>
                    <rect x="290" y="45" width="230" height="200" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="405" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Geophysical Well Logging</text>
                    <text x="405" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Downhole measurements</text>
                    <text x="405" y="105" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Resistivity log → lithology</text>
                    <text x="405" y="120" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• SP log → clay content</text>
                    <text x="405" y="135" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Gamma log → clay/sand</text>
                    <text x="405" y="150" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Caliper → borehole diameter</text>
                    <text x="405" y="170" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Run in open borehole</text>
                    <text x="405" y="185" text-anchor="middle" font-size="9" fill="var(--svg-muted)">before casing installed</text>
                    <text x="405" y="205" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Used to: select screen</text>
                    <text x="405" y="225" text-anchor="middle" font-size="9" fill="var(--svg-fg)">position &amp; gravel pack</text>
                    <text x="275" y="265" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Test drilling is the only DIRECT method — confirms all geophysical interpretations</text>
                </svg>''',
    'Figure 6.4b: Subsurface exploration methods — test drilling provides direct samples, while geophysical well logging characterizes formations in-situ.')


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

print(f"\nChapter 6: {c} SVGs inserted")
print(f"  Before: {original} SVGs, After: {new_count} SVGs")
print(f"  Net added: {new_count - original}")

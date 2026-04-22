"""Add 10 new educational SVG diagrams to Chapter 1 (Occurrence of Groundwater)."""
import re

FILE = r"d:\Final Year\Theory\gw\GW_THE\chapter1.html"

def svg_wrap(svg_content, caption, fig_id=""):
    """Wrap SVG in figure-container with figcaption."""
    id_attr = f' id="{fig_id}"' if fig_id else ''
    return f'''
            <div class="figure-container"{id_attr}>
{svg_content}
                <div class="figcaption">{caption}</div>
            </div>
'''

# All SVGs use CSS variables for dark mode
SVGS = {}

# 1. Advantages vs Disadvantages comparison visual — after "Advantages" section
SVGS['Advantages of Groundwater over Surface Water'] = svg_wrap('''
                <svg width="680" height="300" viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="340" y="25" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Groundwater vs Surface Water — Key Advantages</text>
                    <!-- GW column -->
                    <rect x="30" y="45" width="290" height="240" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="175" y="70" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-accent)">GROUNDWATER</text>
                    <line x1="50" y1="80" x2="300" y2="80" stroke="var(--svg-accent)" stroke-width="1"/>
                    <circle cx="60" cy="100" r="6" fill="var(--svg-green-accent)"/><text x="75" y="104" font-size="10" fill="var(--svg-fg)">Naturally filtered — minimal treatment</text>
                    <circle cx="60" cy="125" r="6" fill="var(--svg-green-accent)"/><text x="75" y="129" font-size="10" fill="var(--svg-fg)">Drought-resistant, reliable supply</text>
                    <circle cx="60" cy="150" r="6" fill="var(--svg-green-accent)"/><text x="75" y="154" font-size="10" fill="var(--svg-fg)">Low evaporation losses</text>
                    <circle cx="60" cy="175" r="6" fill="var(--svg-green-accent)"/><text x="75" y="179" font-size="10" fill="var(--svg-fg)">Available near point of use</text>
                    <circle cx="60" cy="200" r="6" fill="var(--svg-green-accent)"/><text x="75" y="204" font-size="10" fill="var(--svg-fg)">Lower development cost</text>
                    <circle cx="60" cy="225" r="6" fill="var(--svg-green-accent)"/><text x="75" y="229" font-size="10" fill="var(--svg-fg)">Uniform temperature</text>
                    <circle cx="60" cy="250" r="6" fill="var(--svg-green-accent)"/><text x="75" y="254" font-size="10" fill="var(--svg-fg)">Wide availability underground</text>
                    <!-- SW column -->
                    <rect x="360" y="45" width="290" height="240" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="2"/>
                    <text x="505" y="70" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-water-3)">SURFACE WATER</text>
                    <line x1="380" y1="80" x2="630" y2="80" stroke="var(--svg-water-3)" stroke-width="1"/>
                    <circle cx="390" cy="100" r="6" fill="var(--svg-red-accent)"/><text x="405" y="104" font-size="10" fill="var(--svg-fg)">Turbid — requires treatment</text>
                    <circle cx="390" cy="125" r="6" fill="var(--svg-red-accent)"/><text x="405" y="129" font-size="10" fill="var(--svg-fg)">Seasonal — affected by drought</text>
                    <circle cx="390" cy="150" r="6" fill="var(--svg-red-accent)"/><text x="405" y="154" font-size="10" fill="var(--svg-fg)">High evaporation from reservoirs</text>
                    <circle cx="390" cy="175" r="6" fill="var(--svg-green-accent)"/><text x="405" y="179" font-size="10" fill="var(--svg-fg)">Higher yield capacity</text>
                    <circle cx="390" cy="200" r="6" fill="var(--svg-green-accent)"/><text x="405" y="204" font-size="10" fill="var(--svg-fg)">Easily visible and measurable</text>
                    <circle cx="390" cy="225" r="6" fill="var(--svg-green-accent)"/><text x="405" y="229" font-size="10" fill="var(--svg-fg)">Quick remediation if polluted</text>
                    <circle cx="390" cy="250" r="6" fill="var(--svg-red-accent)"/><text x="405" y="254" font-size="10" fill="var(--svg-fg)">Expensive infrastructure needed</text>
                </svg>''',
    'Figure 1.0b: Comparison of groundwater and surface water — advantages and limitations.')

# 2. Hydrological cycle components — infiltration breakdown
SVGS['Components of the Hydrological Cycle Relevant to Groundwater'] = svg_wrap('''
                <svg width="700" height="320" viewBox="0 0 700 320" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="350" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Rainfall Partitioning — Fate of Precipitation</text>
                    <!-- Rain cloud -->
                    <ellipse cx="350" cy="55" rx="60" ry="20" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="350" y="60" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Precipitation (P)</text>
                    <!-- Arrows down -->
                    <line x1="280" y1="75" x2="120" y2="140" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="350" y1="75" x2="350" y2="140" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="420" y1="75" x2="580" y2="140" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <!-- Three boxes -->
                    <rect x="50" y="145" width="140" height="45" rx="6" fill="var(--svg-water)" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <text x="120" y="165" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">Runoff (R)</text>
                    <text x="120" y="180" text-anchor="middle" font-size="9" fill="var(--svg-fg)">→ streams, rivers</text>
                    <rect x="280" y="145" width="140" height="45" rx="6" fill="var(--svg-green-lt)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="350" y="165" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">Infiltration (F)</text>
                    <text x="350" y="180" text-anchor="middle" font-size="9" fill="var(--svg-fg)">→ enters soil</text>
                    <rect x="510" y="145" width="140" height="45" rx="6" fill="var(--svg-yellow-lt)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="580" y="165" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">Evapotranspiration</text>
                    <text x="580" y="180" text-anchor="middle" font-size="9" fill="var(--svg-fg)">→ back to atmosphere</text>
                    <!-- Infiltration breakdown -->
                    <line x1="320" y1="190" x2="200" y2="240" stroke="var(--svg-fg)" stroke-width="1.2" marker-end="url(#arr)"/>
                    <line x1="380" y1="190" x2="500" y2="240" stroke="var(--svg-fg)" stroke-width="1.2" marker-end="url(#arr)"/>
                    <rect x="120" y="245" width="160" height="40" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="200" y="263" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Soil Moisture (vadose)</text>
                    <text x="200" y="278" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Used by plants / evaporates</text>
                    <rect x="420" y="245" width="160" height="40" rx="6" fill="var(--svg-water)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="500" y="263" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-fg)">Deep Percolation</text>
                    <text x="500" y="278" text-anchor="middle" font-size="9" fill="var(--svg-accent)">→ GROUNDWATER RECHARGE</text>
                    <!-- Water budget -->
                    <text x="350" y="310" text-anchor="middle" font-size="11" font-style="italic" fill="var(--svg-fg)">Water Budget: P = R + ET + ΔS (where ΔS includes GW recharge)</text>
                </svg>''',
    'Figure 1.1b: Partitioning of precipitation — infiltration leads to groundwater recharge through deep percolation.')

# 3. Groundwater age — residence time scale
SVGS['Origin and Age of Groundwater'] = svg_wrap('''
                <svg width="680" height="200" viewBox="0 0 680 200" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="340" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Residence Time of Water in Different Reservoirs</text>
                    <!-- Timeline bar -->
                    <line x1="40" y1="100" x2="650" y2="100" stroke="var(--svg-fg)" stroke-width="2"/>
                    <!-- Tick marks and labels -->
                    <line x1="60" y1="95" x2="60" y2="105" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="60" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Days</text>
                    <rect x="40" y="110" width="40" height="25" rx="4" fill="var(--svg-water)" stroke="var(--svg-water-3)" stroke-width="1"/>
                    <text x="60" y="127" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Atmosphere</text>
                    <text x="60" y="150" text-anchor="middle" font-size="8" fill="var(--svg-muted)">~9 days</text>
                    <line x1="160" y1="95" x2="160" y2="105" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="160" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Weeks</text>
                    <rect x="140" y="110" width="40" height="25" rx="4" fill="var(--svg-green-lt)" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <text x="160" y="127" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Soil moist.</text>
                    <text x="160" y="150" text-anchor="middle" font-size="8" fill="var(--svg-muted)">2–50 wks</text>
                    <line x1="280" y1="95" x2="280" y2="105" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="280" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Years</text>
                    <rect x="250" y="110" width="60" height="25" rx="4" fill="var(--svg-blue-lt)" stroke="var(--svg-blue-accent)" stroke-width="1"/>
                    <text x="280" y="127" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Rivers/Lakes</text>
                    <text x="280" y="150" text-anchor="middle" font-size="8" fill="var(--svg-muted)">2–200 yrs</text>
                    <line x1="420" y1="95" x2="420" y2="105" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="420" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">100s–1000s yrs</text>
                    <rect x="385" y="110" width="70" height="25" rx="4" fill="var(--svg-accent)" stroke="var(--svg-accent)" stroke-width="1.5" fill-opacity="0.2"/>
                    <text x="420" y="127" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--svg-fg)">Groundwater</text>
                    <text x="420" y="150" text-anchor="middle" font-size="8" fill="var(--svg-accent)">100–10,000 yrs</text>
                    <line x1="570" y1="95" x2="570" y2="105" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="570" y="85" text-anchor="middle" font-size="9" fill="var(--svg-fg)">10,000+ yrs</text>
                    <rect x="540" y="110" width="60" height="25" rx="4" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="570" y="127" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Ice caps</text>
                    <text x="570" y="150" text-anchor="middle" font-size="8" fill="var(--svg-muted)">~15,000 yrs</text>
                    <!-- Arrow showing increasing residence time -->
                    <line x1="50" y1="175" x2="640" y2="175" stroke="var(--svg-accent)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="345" y="192" text-anchor="middle" font-size="10" font-style="italic" fill="var(--svg-accent)">Increasing Residence Time →</text>
                </svg>''',
    'Figure 1.1c: Residence time of water in various reservoirs — groundwater has centuries to millennia of storage.')

# 4. Vadose zone detail diagram
SVGS['A. Zone of Aeration (Vadose Zone / Unsaturated Zone)'] = svg_wrap('''
                <svg width="500" height="340" viewBox="0 0 500 340" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="250" y="20" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Vadose Zone — Sub-zones in Detail</text>
                    <!-- Ground surface -->
                    <line x1="80" y1="50" x2="420" y2="50" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="440" y="54" font-size="10" fill="var(--svg-fg)">Ground Surface</text>
                    <!-- Soil water zone -->
                    <rect x="80" y="50" width="340" height="60" fill="var(--svg-green-lt)" stroke="none"/>
                    <text x="250" y="75" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">Soil Water Zone</text>
                    <text x="250" y="95" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Root zone — 1 to 2 m depth — evapotranspiration active</text>
                    <!-- Intermediate vadose zone -->
                    <rect x="80" y="110" width="340" height="80" fill="var(--svg-yellow-lt)" stroke="none"/>
                    <line x1="80" y1="110" x2="420" y2="110" stroke="var(--svg-fg)" stroke-width="1" stroke-dasharray="5,3"/>
                    <text x="250" y="140" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">Intermediate Vadose Zone</text>
                    <text x="250" y="160" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Gravity drainage — water percolates downward</text>
                    <text x="250" y="175" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Variable thickness (may be absent in shallow WT areas)</text>
                    <!-- Capillary fringe -->
                    <rect x="80" y="190" width="340" height="50" fill="var(--svg-blue-lt)" stroke="none"/>
                    <line x1="80" y1="190" x2="420" y2="190" stroke="var(--svg-fg)" stroke-width="1" stroke-dasharray="5,3"/>
                    <text x="250" y="212" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">Capillary Fringe</text>
                    <text x="250" y="230" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Saturated by capillary rise — pressure &lt; atmospheric</text>
                    <!-- Water table -->
                    <line x1="80" y1="240" x2="420" y2="240" stroke="var(--svg-accent)" stroke-width="3"/>
                    <text x="440" y="244" font-size="10" font-weight="bold" fill="var(--svg-accent)">Water Table</text>
                    <!-- Saturated zone -->
                    <rect x="80" y="240" width="340" height="70" fill="var(--svg-water)" stroke="none"/>
                    <text x="250" y="275" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">Saturated Zone (Phreatic)</text>
                    <text x="250" y="295" text-anchor="middle" font-size="9" fill="var(--svg-muted)">All pores filled — p = atmospheric at WT</text>
                    <!-- Brace for vadose -->
                    <text x="50" y="152" text-anchor="middle" font-size="28" fill="var(--svg-fg)">}</text>
                    <text x="25" y="155" text-anchor="middle" font-size="10" fill="var(--svg-fg)" transform="rotate(-90 25 155)">VADOSE ZONE</text>
                    <!-- Border -->
                    <rect x="80" y="50" width="340" height="260" fill="none" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <!-- Downward arrows -->
                    <line x1="150" y1="65" x2="150" y2="100" stroke="var(--svg-fg)" stroke-width="0.8" marker-end="url(#arr)"/>
                    <line x1="150" y1="125" x2="150" y2="180" stroke="var(--svg-fg)" stroke-width="0.8" marker-end="url(#arr)"/>
                    <line x1="350" y1="65" x2="350" y2="100" stroke="var(--svg-fg)" stroke-width="0.8" marker-end="url(#arr)"/>
                    <line x1="350" y1="125" x2="350" y2="180" stroke="var(--svg-fg)" stroke-width="0.8" marker-end="url(#arr)"/>
                </svg>''',
    'Figure 1.2b: Sub-zones within the vadose (unsaturated) zone — soil water zone, intermediate zone, and capillary fringe above the water table.')

# 5. Water-bearing formations classification
SVGS['Water-Bearing Formations — Basic Terminology'] = svg_wrap('''
                <svg width="650" height="280" viewBox="0 0 650 280" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="325" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Classification of Geological Formations by Water-Bearing Capacity</text>
                    <!-- Top: Formation type -->
                    <rect x="200" y="40" width="250" height="35" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="325" y="62" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-fg)">Geological Formation</text>
                    <!-- Branches -->
                    <line x1="225" y1="75" x2="110" y2="115" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="325" y1="75" x2="325" y2="115" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="425" y1="75" x2="540" y2="115" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <!-- Aquifer -->
                    <rect x="30" y="120" width="160" height="50" rx="6" fill="var(--svg-green-lt)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="110" y="142" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">AQUIFER</text>
                    <text x="110" y="158" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Stores + transmits water</text>
                    <!-- Aquitard -->
                    <rect x="245" y="120" width="160" height="50" rx="6" fill="var(--svg-yellow-lt)" stroke="var(--svg-orange-accent)" stroke-width="2"/>
                    <text x="325" y="142" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">AQUITARD</text>
                    <text x="325" y="158" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Transmits slowly (leaky)</text>
                    <!-- Aquiclude / Aquifuge -->
                    <rect x="460" y="120" width="160" height="50" rx="6" fill="var(--svg-red-lt)" stroke="var(--svg-red-accent)" stroke-width="2"/>
                    <text x="540" y="142" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">AQUICLUDE</text>
                    <text x="540" y="158" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Stores but does not transmit</text>
                    <!-- Examples row -->
                    <text x="110" y="195" text-anchor="middle" font-size="10" font-style="italic" fill="var(--svg-fg)">Sand, gravel,</text>
                    <text x="110" y="210" text-anchor="middle" font-size="10" font-style="italic" fill="var(--svg-fg)">sandstone, limestone</text>
                    <text x="325" y="195" text-anchor="middle" font-size="10" font-style="italic" fill="var(--svg-fg)">Sandy clay, silt,</text>
                    <text x="325" y="210" text-anchor="middle" font-size="10" font-style="italic" fill="var(--svg-fg)">shale</text>
                    <text x="540" y="195" text-anchor="middle" font-size="10" font-style="italic" fill="var(--svg-fg)">Clay, dense</text>
                    <text x="540" y="210" text-anchor="middle" font-size="10" font-style="italic" fill="var(--svg-fg)">unfractured rock</text>
                    <!-- K values -->
                    <text x="110" y="235" text-anchor="middle" font-size="10" fill="var(--svg-accent)">K &gt; 10⁻⁴ m/s</text>
                    <text x="325" y="235" text-anchor="middle" font-size="10" fill="var(--svg-orange-accent)">K ≈ 10⁻⁷–10⁻⁴ m/s</text>
                    <text x="540" y="235" text-anchor="middle" font-size="10" fill="var(--svg-red-accent)">K &lt; 10⁻⁹ m/s</text>
                    <!-- Bottom: Aquifuge -->
                    <rect x="200" y="250" width="250" height="25" rx="4" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="325" y="267" text-anchor="middle" font-size="10" fill="var(--svg-fg)">AQUIFUGE — neither stores nor transmits (e.g., massive granite)</text>
                </svg>''',
    'Figure 1.4b: Classification of geological formations — aquifer, aquitard, aquiclude, and aquifuge with typical hydraulic conductivity ranges.')

# 6. Porosity types diagram
SVGS['1. Porosity'] = svg_wrap('''
                <svg width="650" height="260" viewBox="0 0 650 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="325" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Primary vs Secondary Porosity</text>
                    <!-- Primary porosity -->
                    <rect x="30" y="45" width="270" height="190" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="165" y="68" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-accent)">Primary Porosity</text>
                    <!-- Grains with pore spaces -->
                    <circle cx="100" cy="120" r="22" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <circle cx="148" cy="110" r="20" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <circle cx="195" cy="125" r="23" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <circle cx="115" cy="160" r="18" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <circle cx="160" cy="155" r="21" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <circle cx="205" cy="165" r="19" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <circle cx="245" cy="130" r="16" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="165" y="205" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Intergranular voids</text>
                    <text x="165" y="220" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Sand, gravel, sandstone</text>
                    <!-- Secondary porosity -->
                    <rect x="350" y="45" width="270" height="190" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="485" y="68" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-red-accent)">Secondary Porosity</text>
                    <!-- Rock with fractures -->
                    <rect x="380" y="90" width="210" height="110" fill="var(--svg-struct-2)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="420" y1="90" x2="440" y2="200" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <line x1="500" y1="90" x2="480" y2="200" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="380" y1="140" x2="590" y2="145" stroke="var(--svg-accent)" stroke-width="1.8"/>
                    <line x1="540" y1="100" x2="560" y2="190" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <!-- Solution channel -->
                    <ellipse cx="460" cy="165" rx="20" ry="12" fill="var(--svg-bg-fill)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="485" y="205" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Fractures, joints, solution</text>
                    <text x="485" y="220" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Limestone, granite, basalt</text>
                    <!-- Bottom formula -->
                    <text x="325" y="252" text-anchor="middle" font-size="12" fill="var(--svg-fg)">n = V_v / V_T × 100%    (total porosity)</text>
                </svg>''',
    'Figure 1.6b: Primary porosity (intergranular voids in unconsolidated sediments) vs secondary porosity (fractures, joints, and solution channels in rock).')

# 7. Specific storage concept
SVGS['3. Specific Storage'] = svg_wrap('''
                <svg width="600" height="250" viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Specific Storage — Mechanisms of Water Release in Confined Aquifer</text>
                    <!-- Confined aquifer box -->
                    <rect x="50" y="50" width="220" height="170" rx="6" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="160" y="72" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">Before Pumping</text>
                    <!-- Confining layers -->
                    <rect x="50" y="40" width="220" height="15" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="50" y="215" width="220" height="15" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <!-- Water under pressure -->
                    <text x="160" y="110" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Water under pressure</text>
                    <text x="160" y="130" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Skeleton supports load</text>
                    <!-- Piezometric level -->
                    <line x1="50" y1="30" x2="270" y2="30" stroke="var(--svg-accent)" stroke-width="1.5" stroke-dasharray="6,3"/>
                    <text x="160" y="26" text-anchor="middle" font-size="9" fill="var(--svg-accent)">Piezometric surface</text>
                    <!-- Arrow -->
                    <line x1="290" y1="135" x2="340" y2="135" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="315" y="125" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Pump</text>
                    <!-- After pumping -->
                    <rect x="360" y="50" width="220" height="170" rx="6" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="470" y="72" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">After Pumping</text>
                    <rect x="360" y="40" width="220" height="15" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="360" y="215" width="220" height="15" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <!-- Lowered piezometric -->
                    <line x1="360" y1="38" x2="580" y2="38" stroke="var(--svg-red-accent)" stroke-width="1.5" stroke-dasharray="6,3"/>
                    <text x="470" y="34" text-anchor="middle" font-size="9" fill="var(--svg-red-accent)">Lowered piezometric surface</text>
                    <!-- Mechanism labels -->
                    <text x="470" y="100" text-anchor="middle" font-size="9" fill="var(--svg-fg)">① Water expands slightly</text>
                    <text x="470" y="118" text-anchor="middle" font-size="9" fill="var(--svg-fg)">② Skeleton compresses</text>
                    <text x="470" y="136" text-anchor="middle" font-size="9" fill="var(--svg-fg)">→ Both release water</text>
                    <!-- Formula -->
                    <text x="300" y="248" text-anchor="middle" font-size="11" fill="var(--svg-accent)">Sₛ = ρg(α + nβ)  [units: m⁻¹]</text>
                </svg>''',
    'Figure 1.6c: Specific storage in a confined aquifer — water is released by aquifer compression and water expansion when head drops.')

# 8. Transmissivity concept
SVGS['5. Transmissivity'] = svg_wrap('''
                <svg width="550" height="220" viewBox="0 0 550 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Transmissivity — Concept</text>
                    <!-- Aquifer block -->
                    <rect x="100" y="50" width="350" height="100" rx="0" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <!-- Confining layers -->
                    <rect x="100" y="35" width="350" height="18" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <rect x="100" y="148" width="350" height="18" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <!-- b label -->
                    <line x1="80" y1="50" x2="80" y2="150" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <line x1="75" y1="50" x2="85" y2="50" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <line x1="75" y1="150" x2="85" y2="150" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="65" y="104" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-accent)">b</text>
                    <!-- K label inside -->
                    <text x="275" y="90" text-anchor="middle" font-size="12" fill="var(--svg-fg)">Hydraulic Conductivity = K</text>
                    <text x="275" y="110" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Aquifer thickness = b</text>
                    <!-- Flow arrow -->
                    <line x1="460" y1="100" x2="520" y2="100" stroke="var(--svg-accent)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <text x="490" y="90" text-anchor="middle" font-size="10" fill="var(--svg-accent)">Q</text>
                    <!-- Formula -->
                    <text x="275" y="190" text-anchor="middle" font-size="14" font-weight="bold" fill="var(--svg-fg)">T = K × b</text>
                    <text x="275" y="210" text-anchor="middle" font-size="10" fill="var(--svg-muted)">[m²/s] — rate of flow through full thickness per unit width per unit gradient</text>
                </svg>''',
    'Figure 1.6d: Transmissivity (T) represents the ability of the full aquifer thickness to transmit water — product of hydraulic conductivity and saturated thickness.')

# 9. Permeability vs hydraulic conductivity
SVGS['6. Permeability'] = svg_wrap('''
                <svg width="620" height="220" viewBox="0 0 620 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="310" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Intrinsic Permeability (k) vs Hydraulic Conductivity (K)</text>
                    <!-- k box -->
                    <rect x="30" y="50" width="250" height="130" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="155" y="75" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-accent)">Intrinsic Permeability (k)</text>
                    <line x1="50" y1="82" x2="260" y2="82" stroke="var(--svg-accent)" stroke-width="0.8"/>
                    <text x="155" y="100" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Property of the MEDIUM only</text>
                    <text x="155" y="118" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Independent of fluid</text>
                    <text x="155" y="136" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Units: m² (or darcy)</text>
                    <text x="155" y="160" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Depends on: grain size, packing,</text>
                    <text x="155" y="174" text-anchor="middle" font-size="10" fill="var(--svg-muted)">shape, sorting</text>
                    <!-- Arrow -->
                    <line x1="285" y1="115" x2="335" y2="115" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="310" y="105" text-anchor="middle" font-size="9" fill="var(--svg-fg)">× ρg/μ</text>
                    <!-- K box -->
                    <rect x="340" y="50" width="250" height="130" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="465" y="75" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-green-accent)">Hydraulic Conductivity (K)</text>
                    <line x1="360" y1="82" x2="570" y2="82" stroke="var(--svg-green-accent)" stroke-width="0.8"/>
                    <text x="465" y="100" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Property of MEDIUM + FLUID</text>
                    <text x="465" y="118" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Depends on viscosity &amp; density</text>
                    <text x="465" y="136" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Units: m/s (or m/day)</text>
                    <text x="465" y="160" text-anchor="middle" font-size="10" fill="var(--svg-muted)">K = kρg/μ = kg/ν</text>
                    <text x="465" y="174" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Used in Darcy's law</text>
                    <!-- Bottom formula -->
                    <text x="310" y="208" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">K = k · (ρg/μ)     where ρ = fluid density, μ = dynamic viscosity</text>
                </svg>''',
    'Figure 1.6e: Intrinsic permeability depends only on the porous medium; hydraulic conductivity also depends on the fluid properties.')

# 10. Fracture-based groundwater in rock
SVGS['7. Geological Structures and Rock Joint Fractures'] = svg_wrap('''
                <svg width="620" height="280" viewBox="0 0 620 280" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="310" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Groundwater in Fractured Rock — Dual Porosity</text>
                    <!-- Rock block -->
                    <rect x="50" y="45" width="520" height="200" fill="var(--svg-struct-2)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <!-- Fracture network -->
                    <line x1="150" y1="45" x2="160" y2="245" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="300" y1="45" x2="290" y2="245" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <line x1="450" y1="45" x2="460" y2="245" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="50" y1="100" x2="570" y2="105" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <line x1="50" y1="180" x2="570" y2="175" stroke="var(--svg-accent)" stroke-width="2"/>
                    <!-- Diagonal fractures -->
                    <line x1="200" y1="60" x2="370" y2="170" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <line x1="400" y1="80" x2="520" y2="200" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <!-- Labels -->
                    <rect x="80" y="130" width="45" height="28" rx="3" fill="var(--svg-label-bg)"/>
                    <text x="102" y="148" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-fg)">Matrix</text>
                    <rect x="175" y="60" width="70" height="18" rx="3" fill="var(--svg-label-bg)"/>
                    <text x="210" y="73" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-accent)">Fracture</text>
                    <!-- Legend boxes below -->
                    <rect x="80" y="258" width="15" height="12" fill="var(--svg-struct-2)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="100" y="269" font-size="10" fill="var(--svg-fg)">Rock matrix — low K, high storage</text>
                    <rect x="350" y="258" width="15" height="12" fill="var(--svg-accent)" stroke="var(--svg-accent)" stroke-width="1"/>
                    <text x="370" y="269" font-size="10" fill="var(--svg-fg)">Fractures — high K, low storage</text>
                    <!-- Flow arrows in fractures -->
                    <line x1="155" y1="130" x2="155" y2="160" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="295" y1="120" x2="295" y2="150" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="200" y1="103" x2="260" y2="103" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                </svg>''',
    'Figure 1.6f: Dual-porosity system in fractured rock — fractures provide flow pathways while the rock matrix stores water.')

# 11. GW characteristics comparison table/visual  
SVGS['General Characteristics of Groundwater'] = svg_wrap('''
                <svg width="650" height="260" viewBox="0 0 650 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="325" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Physical &amp; Chemical Characteristics of Groundwater</text>
                    <!-- Temperature -->
                    <rect x="20" y="45" width="190" height="95" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <text x="115" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-water-3)">Temperature</text>
                    <text x="115" y="85" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Nearly constant</text>
                    <text x="115" y="100" text-anchor="middle" font-size="10" fill="var(--svg-fg)">(10–25°C typically)</text>
                    <text x="115" y="118" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Reflects mean annual air temp.</text>
                    <text x="115" y="133" text-anchor="middle" font-size="9" fill="var(--svg-muted)">at shallow depths</text>
                    <!-- Turbidity -->
                    <rect x="230" y="45" width="190" height="95" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="325" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-green-accent)">Turbidity</text>
                    <text x="325" y="85" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Very low (clear)</text>
                    <text x="325" y="100" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Natural filtration</text>
                    <text x="325" y="118" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Suspended solids removed</text>
                    <text x="325" y="133" text-anchor="middle" font-size="9" fill="var(--svg-muted)">by percolation through soil</text>
                    <!-- Dissolved minerals -->
                    <rect x="440" y="45" width="190" height="95" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="535" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-orange-accent)">Minerals</text>
                    <text x="535" y="85" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Higher dissolved solids</text>
                    <text x="535" y="100" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Ca²⁺, Mg²⁺, Fe²⁺, HCO₃⁻</text>
                    <text x="535" y="118" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Prolonged rock–water</text>
                    <text x="535" y="133" text-anchor="middle" font-size="9" fill="var(--svg-muted)">interaction dissolves minerals</text>
                    <!-- Bottom row -->
                    <rect x="80" y="160" width="210" height="85" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <text x="185" y="180" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-red-accent)">Contamination Risk</text>
                    <text x="185" y="200" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Once polluted, very slow</text>
                    <text x="185" y="215" text-anchor="middle" font-size="10" fill="var(--svg-fg)">natural cleanup</text>
                    <text x="185" y="233" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Arsenic, nitrate, fluoride</text>
                    <rect x="360" y="160" width="210" height="85" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-purple-accent)" stroke-width="1.5"/>
                    <text x="465" y="180" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-purple-accent)">Biological Quality</text>
                    <text x="465" y="200" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Generally free from</text>
                    <text x="465" y="215" text-anchor="middle" font-size="10" fill="var(--svg-fg)">pathogens and bacteria</text>
                    <text x="465" y="233" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Natural soil filtration acts</text>
                    <text x="465" y="248" text-anchor="middle" font-size="9" fill="var(--svg-muted)">as a biological barrier</text>
                </svg>''',
    'Figure 1.7b: Key physical and chemical characteristics of groundwater — temperature stability, natural filtration, mineral content, and contamination risks.')


def inject_svgs(html, svgs):
    """Inject SVGs after the first paragraph following matching h3 headings."""
    count = 0
    for heading_text, svg_html in svgs.items():
        # Find the h3 heading
        pattern = re.compile(
            r'(<h3>[^<]*' + re.escape(heading_text[:30]) + r'[^<]*</h3>\s*)',
            re.DOTALL
        )
        match = pattern.search(html)
        if match:
            insert_pos = match.end()
            # Find end of next paragraph or list after heading
            next_block = re.search(r'(</(?:p|ol|ul|div)>)', html[insert_pos:])
            if next_block:
                actual_pos = insert_pos + next_block.end()
                html = html[:actual_pos] + svg_html + html[actual_pos:]
                count += 1
                print(f"  Inserted after '{heading_text[:50]}...'")
            else:
                print(f"  WARNING: Could not find insertion point after '{heading_text[:50]}...'")
        else:
            print(f"  WARNING: Could not find heading '{heading_text[:50]}...'")
    return html, count


with open(FILE, 'r', encoding='utf-8') as f:
    html = f.read()

original_svg_count = html.count('<svg')
html, inserted = inject_svgs(html, SVGS)
new_svg_count = html.count('<svg')

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nChapter 1: {inserted} SVGs inserted")
print(f"  Before: {original_svg_count} SVGs, After: {new_svg_count} SVGs")
print(f"  Net added: {new_svg_count - original_svg_count}")

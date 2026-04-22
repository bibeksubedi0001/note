"""Add 10 new educational SVG diagrams to Chapter 9 (GW in Nepal)."""
import re

FILE = r"d:\Final Year\Theory\gw\GW_THE\chapter9.html"

def svg_wrap(svg_content, caption):
    return f'''
            <div class="figure-container">
{svg_content}
                <div class="figcaption">{caption}</div>
            </div>
'''

SVGS = {}

# 1. Geological Setting
SVGS['9.2.1 Geological Setting'] = svg_wrap('''
                <svg width="600" height="260" viewBox="0 0 600 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Nepal — Geological Zones (North to South)</text>
                    <rect x="30" y="40" width="105" height="70" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="82" y="60" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-fg)">High Himalayas</text>
                    <text x="82" y="75" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Gneiss, schist</text>
                    <text x="82" y="88" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Limited GW</text>
                    <text x="82" y="103" text-anchor="middle" font-size="8" fill="var(--svg-water-3)">Springs only</text>
                    <line x1="137" y1="75" x2="150" y2="75" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <rect x="155" y="40" width="105" height="70" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="207" y="60" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-accent)">Middle Hills</text>
                    <text x="207" y="75" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Phyllite, quartzite</text>
                    <text x="207" y="88" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Fractured aquifers</text>
                    <text x="207" y="103" text-anchor="middle" font-size="8" fill="var(--svg-water-3)">Springs + dug wells</text>
                    <line x1="262" y1="75" x2="275" y2="75" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <rect x="280" y="40" width="105" height="70" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="332" y="60" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-green-accent)">Siwalik Hills</text>
                    <text x="332" y="75" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Sandstone, siltstone</text>
                    <text x="332" y="88" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Moderate GW</text>
                    <text x="332" y="103" text-anchor="middle" font-size="8" fill="var(--svg-water-3)">Fractured + alluvial</text>
                    <line x1="387" y1="75" x2="400" y2="75" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <rect x="405" y="40" width="170" height="70" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="2"/>
                    <text x="490" y="60" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-water-3)">Terai Plain</text>
                    <text x="490" y="75" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Alluvial sand, gravel, clay</text>
                    <text x="490" y="88" text-anchor="middle" font-size="8" fill="var(--svg-fg)">BEST aquifers in Nepal</text>
                    <text x="490" y="103" text-anchor="middle" font-size="8" fill="var(--svg-water-3)">Tube wells, T = 500-5000 m²/d</text>
                    <text x="300" y="135" text-anchor="middle" font-size="11" fill="var(--svg-fg)">↑ Elevation (N)                                                        ↓ Elevation (S)</text>
                    <rect x="30" y="150" width="540" height="30" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5" rx="3"/>
                    <text x="300" y="170" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Main Boundary Thrust (MBT) separates Middle Hills from Siwalik</text>
                    <text x="300" y="200" text-anchor="middle" font-size="10" fill="var(--svg-fg)">~80% of Nepal's GW potential lies in the Terai alluvial aquifer system</text>
                    <text x="300" y="220" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Terai aquifer thickness: 100-600 m | Replenished by rivers from Himalayas</text>
                    <text x="300" y="250" text-anchor="middle" font-size="9" fill="var(--svg-muted)">GW development in hills is limited — mainly springs and shallow dug wells</text>
                </svg>''',
    'Figure 9.2b: Nepal\'s geological zones from north to south — groundwater potential increases dramatically in the southern Terai alluvial plains.')

# 2. Aquifer Characteristics
SVGS['9.2.2 Aquifer Characteristics'] = svg_wrap('''
                <svg width="600" height="240" viewBox="0 0 600 240" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Terai Aquifer System — Layered Structure</text>
                    <rect x="50" y="45" width="500" height="25" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="300" y="62" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Surface soil / top clay (3-10 m)</text>
                    <rect x="50" y="70" width="500" height="30" fill="var(--svg-water)" stroke="var(--svg-accent)" stroke-width="1.5" fill-opacity="0.2"/>
                    <text x="300" y="90" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-accent)">Shallow Aquifer (sand/gravel) — 10-60 m</text>
                    <rect x="50" y="100" width="500" height="18" fill="var(--svg-muted)" stroke="var(--svg-fg)" stroke-width="1" fill-opacity="0.3"/>
                    <text x="300" y="113" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Clay/silt confining layer (aquitard)</text>
                    <rect x="50" y="118" width="500" height="30" fill="var(--svg-water-3)" stroke="var(--svg-green-accent)" stroke-width="1.5" fill-opacity="0.2"/>
                    <text x="300" y="137" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-green-accent)">Deep Aquifer (gravel/sand) — 60-300+ m</text>
                    <rect x="50" y="148" width="500" height="15" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="300" y="160" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Bedrock / basement</text>
                    <line x1="570" y1="75" x2="570" y2="95" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="580" y="88" font-size="7" fill="var(--svg-accent)">STW</text>
                    <line x1="580" y1="75" x2="580" y2="143" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="590" y="115" font-size="7" fill="var(--svg-green-accent)">DTW</text>
                    <text x="300" y="190" text-anchor="middle" font-size="10" fill="var(--svg-fg)">STW (Shallow Tube Well): &lt;60 m, unconfined/semi-confined</text>
                    <text x="300" y="208" text-anchor="middle" font-size="10" fill="var(--svg-fg)">DTW (Deep Tube Well): 60-300+ m, confined, artesian in some areas</text>
                    <text x="300" y="228" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Arsenic contamination common in shallow aquifers (&lt;50 m) of inner Terai</text>
                </svg>''',
    'Figure 9.2c: Terai aquifer system — shallow (unconfined) and deep (confined) aquifers separated by clay aquitards, with arsenic risk in shallow zones.')

# 3. GW Development
SVGS['9.2.3 Groundwater Development'] = svg_wrap('''
                <svg width="550" height="220" viewBox="0 0 550 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">GW Development in Nepal — Timeline</text>
                    <line x1="60" y1="80" x2="500" y2="80" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <circle cx="100" cy="80" r="5" fill="var(--svg-accent)"/>
                    <text x="100" y="70" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--svg-accent)">1960s</text>
                    <text x="100" y="100" text-anchor="middle" font-size="7" fill="var(--svg-fg)">First tube wells</text>
                    <text x="100" y="112" text-anchor="middle" font-size="7" fill="var(--svg-fg)">UNDP survey</text>
                    <circle cx="200" cy="80" r="5" fill="var(--svg-green-accent)"/>
                    <text x="200" y="70" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--svg-green-accent)">1970s</text>
                    <text x="200" y="100" text-anchor="middle" font-size="7" fill="var(--svg-fg)">GW exploration</text>
                    <text x="200" y="112" text-anchor="middle" font-size="7" fill="var(--svg-fg)">GWRDB formed</text>
                    <circle cx="300" cy="80" r="5" fill="var(--svg-orange-accent)"/>
                    <text x="300" y="70" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--svg-orange-accent)">1980-90s</text>
                    <text x="300" y="100" text-anchor="middle" font-size="7" fill="var(--svg-fg)">STW expansion</text>
                    <text x="300" y="112" text-anchor="middle" font-size="7" fill="var(--svg-fg)">Irrigation DTWs</text>
                    <circle cx="400" cy="80" r="5" fill="var(--svg-water-3)"/>
                    <text x="400" y="70" text-anchor="middle" font-size="8" font-weight="bold" fill="var(--svg-water-3)">2000s+</text>
                    <text x="400" y="100" text-anchor="middle" font-size="7" fill="var(--svg-fg)">Arsenic testing</text>
                    <text x="400" y="112" text-anchor="middle" font-size="7" fill="var(--svg-fg)">Quality focus</text>
                    <rect x="50" y="130" width="450" height="60" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="275" y="150" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-fg)">Current Status</text>
                    <text x="275" y="168" text-anchor="middle" font-size="9" fill="var(--svg-fg)">~750,000+ STWs | ~1,500 DTWs | 70%+ Terai irrigation from GW</text>
                    <text x="275" y="183" text-anchor="middle" font-size="9" fill="var(--svg-muted)">GWRDB, DoI, KUKL are key GW development agencies</text>
                    <text x="275" y="210" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Shift from "quantity-first" to "quantity + quality + sustainability"</text>
                </svg>''',
    'Figure 9.2d: Timeline of groundwater development in Nepal — from initial UNDP surveys in the 1960s to the current focus on quality and sustainability.')

# 4. Northern vs Southern Terai
SVGS['9.3.3 Northern vs. Southern'] = svg_wrap('''
                <svg width="600" height="230" viewBox="0 0 600 230" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Northern Terai (Bhabar) vs Southern Terai</text>
                    <rect x="20" y="40" width="265" height="150" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="152" y="60" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Bhabar Zone (North)</text>
                    <text x="152" y="80" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Coarse gravel/boulder deposits</text>
                    <text x="152" y="96" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• WT very deep (15-30+ m)</text>
                    <text x="152" y="112" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• High K, high recharge</text>
                    <text x="152" y="128" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Rivers disappear underground</text>
                    <text x="152" y="147" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">DTW needed (deep WT)</text>
                    <text x="152" y="165" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">Good quality water</text>
                    <text x="152" y="182" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Width: 8-12 km</text>
                    <rect x="315" y="40" width="265" height="150" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="2"/>
                    <text x="447" y="60" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-water-3)">Southern Terai</text>
                    <text x="447" y="80" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Fine sand/silt/clay layers</text>
                    <text x="447" y="96" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• WT shallow (2-8 m)</text>
                    <text x="447" y="112" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Lower K, confined aquifers</text>
                    <text x="447" y="128" text-anchor="middle" font-size="9" fill="var(--svg-fg)">• Artesian conditions possible</text>
                    <text x="447" y="147" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">STW common (shallow WT)</text>
                    <text x="447" y="165" text-anchor="middle" font-size="9" fill="var(--svg-red-accent)">Arsenic risk in some areas</text>
                    <text x="447" y="182" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Width: 20-30 km</text>
                    <text x="300" y="210" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Bhabar → recharge zone | Southern Terai → discharge/utilization zone</text>
                    <text x="300" y="228" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Bhabar protection is critical for sustaining the entire Terai aquifer system</text>
                </svg>''',
    'Figure 9.3b: Comparison of Bhabar (northern) and southern Terai zones — contrasting aquifer materials, water table depths, and groundwater characteristics.')

# 5. Current Issues
SVGS['9.3.4 Current Issues and Chal'] = svg_wrap('''
                <svg width="600" height="240" viewBox="0 0 600 240" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">GW Issues &amp; Challenges in Terai</text>
                    <rect x="20" y="45" width="170" height="80" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="2"/>
                    <text x="105" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-red-accent)">Arsenic</text>
                    <text x="105" y="82" text-anchor="middle" font-size="8" fill="var(--svg-fg)">WHO limit: 10 μg/L</text>
                    <text x="105" y="96" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Nepal std: 50 μg/L</text>
                    <text x="105" y="112" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Nawalparasi, Bara worst</text>
                    <rect x="215" y="45" width="170" height="80" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="2"/>
                    <text x="300" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-orange-accent)">Iron/Manganese</text>
                    <text x="300" y="82" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Fe &gt; 0.3 mg/L common</text>
                    <text x="300" y="96" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Taste, staining issues</text>
                    <text x="300" y="112" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Aeration + filtration</text>
                    <rect x="410" y="45" width="170" height="80" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="495" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-accent)">Declining WT</text>
                    <text x="495" y="82" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Kathmandu: 2-3 m/yr</text>
                    <text x="495" y="96" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Over-extraction</text>
                    <text x="495" y="112" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Urbanization reducing R</text>
                    <rect x="110" y="140" width="170" height="70" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="2"/>
                    <text x="195" y="160" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-water-3)">Contamination</text>
                    <text x="195" y="177" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Bacterial (shallow wells)</text>
                    <text x="195" y="192" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Nitrate from agriculture</text>
                    <text x="195" y="205" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Industrial pollutants</text>
                    <rect x="320" y="140" width="170" height="70" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-muted)" stroke-width="2"/>
                    <text x="405" y="160" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-muted)">Institutional</text>
                    <text x="405" y="177" text-anchor="middle" font-size="8" fill="var(--svg-fg)">No regulatory framework</text>
                    <text x="405" y="192" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Unregistered STWs</text>
                    <text x="405" y="205" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Monitoring gaps</text>
                    <text x="300" y="232" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Integrated Water Resource Management (IWRM) approach needed</text>
                </svg>''',
    'Figure 9.3c: Five major groundwater challenges in the Terai — arsenic, iron/manganese, declining water tables, contamination, and institutional gaps.')

# 6. Middle Hills GW
SVGS['9.4.1 Middle Hills'] = svg_wrap('''
                <svg width="550" height="220" viewBox="0 0 550 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="275" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Middle Hills — Groundwater Sources</text>
                    <rect x="30" y="45" width="150" height="120" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="105" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-accent)">Springs</text>
                    <text x="105" y="82" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Contact springs</text>
                    <text x="105" y="96" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Depression springs</text>
                    <text x="105" y="112" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Fault-controlled springs</text>
                    <text x="105" y="130" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">Primary source for</text>
                    <text x="105" y="145" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">hill communities</text>
                    <text x="105" y="160" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Q: 0.1-5 L/s</text>
                    <rect x="200" y="45" width="150" height="120" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="275" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-green-accent)">Dug Wells</text>
                    <text x="275" y="82" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Shallow (&lt;15 m)</text>
                    <text x="275" y="96" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Valley fill deposits</text>
                    <text x="275" y="112" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Terraces/colluvium</text>
                    <text x="275" y="130" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">Seasonal variation</text>
                    <text x="275" y="145" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">in yield</text>
                    <text x="275" y="160" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Contamination risk</text>
                    <rect x="370" y="45" width="160" height="120" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="2"/>
                    <text x="450" y="65" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-water-3)">Bore Wells</text>
                    <text x="450" y="82" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Fractured rock</text>
                    <text x="450" y="96" text-anchor="middle" font-size="8" fill="var(--svg-fg)">aquifers only</text>
                    <text x="450" y="112" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Success rate: 40-60%</text>
                    <text x="450" y="130" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">Limited to favorable</text>
                    <text x="450" y="145" text-anchor="middle" font-size="8" fill="var(--svg-green-accent)">geology</text>
                    <text x="450" y="160" text-anchor="middle" font-size="8" fill="var(--svg-muted)">VES for siting</text>
                    <text x="275" y="190" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Springs are declining across Nepal's Middle Hills due to climate change</text>
                    <text x="275" y="210" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Spring-shed protection and recharge enhancement are priority interventions</text>
                </svg>''',
    'Figure 9.4b: Middle Hills groundwater sources — springs (primary), dug wells, and bore wells in fractured rock; springs are declining due to climate change.')

# 7. High Himalayas
SVGS['9.4.2 High Himalayas'] = svg_wrap('''
                <svg width="500" height="200" viewBox="0 0 500 200" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="250" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">High Himalayas — GW Characteristics</text>
                    <rect x="30" y="45" width="440" height="110" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="250" y="65" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">Very Limited Groundwater</text>
                    <text x="125" y="88" text-anchor="middle" font-size="9" fill="var(--svg-red-accent)">Challenges</text>
                    <text x="125" y="105" text-anchor="middle" font-size="8" fill="var(--svg-fg)">• Hard crystalline rock</text>
                    <text x="125" y="118" text-anchor="middle" font-size="8" fill="var(--svg-fg)">• Very low permeability</text>
                    <text x="125" y="131" text-anchor="middle" font-size="8" fill="var(--svg-fg)">• Steep terrain, thin soil</text>
                    <text x="125" y="144" text-anchor="middle" font-size="8" fill="var(--svg-fg)">• Glacial melt dependent</text>
                    <text x="375" y="88" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">Available Sources</text>
                    <text x="375" y="105" text-anchor="middle" font-size="8" fill="var(--svg-fg)">• Snow/glacier-fed springs</text>
                    <text x="375" y="118" text-anchor="middle" font-size="8" fill="var(--svg-fg)">• Moraine deposits (limited)</text>
                    <text x="375" y="131" text-anchor="middle" font-size="8" fill="var(--svg-fg)">• Fault-line springs</text>
                    <text x="375" y="144" text-anchor="middle" font-size="8" fill="var(--svg-fg)">• Karst in limestone areas</text>
                    <text x="250" y="175" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Population density is low — small spring sources adequate for settlements</text>
                    <text x="250" y="195" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Climate change threatens glacier-fed springs — long-term sustainability concern</text>
                </svg>''',
    'Figure 9.4c: High Himalayan groundwater — very limited due to hard crystalline rock; population relies on glacier-fed springs and fault-controlled sources.')

# 8. Urban GW Issues
SVGS['9.5.1 General Urban Groundwate'] = svg_wrap('''
                <svg width="600" height="250" viewBox="0 0 600 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Urban GW Issues — Kathmandu Valley</text>
                    <rect x="200" y="40" width="200" height="32" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="2"/>
                    <text x="300" y="60" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-red-accent)">Crisis Indicators</text>
                    <rect x="20" y="85" width="170" height="70" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="105" y="103" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-accent)">WT Decline</text>
                    <text x="105" y="118" text-anchor="middle" font-size="8" fill="var(--svg-fg)">2-3 m/yr in some areas</text>
                    <text x="105" y="133" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Many wells going dry</text>
                    <text x="105" y="148" text-anchor="middle" font-size="8" fill="var(--svg-red-accent)">Demand &gt;&gt; recharge</text>
                    <rect x="210" y="85" width="180" height="70" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="300" y="103" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-orange-accent)">Quality Degradation</text>
                    <text x="300" y="118" text-anchor="middle" font-size="8" fill="var(--svg-fg)">NH₃, NO₃, Fe, coliform</text>
                    <text x="300" y="133" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Sewage + septic seepage</text>
                    <text x="300" y="148" text-anchor="middle" font-size="8" fill="var(--svg-red-accent)">Most wells: not potable</text>
                    <rect x="410" y="85" width="170" height="70" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <text x="495" y="103" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-water-3)">Subsidence Risk</text>
                    <text x="495" y="118" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Compaction of clay layers</text>
                    <text x="495" y="133" text-anchor="middle" font-size="8" fill="var(--svg-fg)">from WT decline</text>
                    <text x="495" y="148" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Irreversible damage</text>
                    <rect x="80" y="170" width="440" height="45" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="300" y="188" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-green-accent)">Needed: Managed Aquifer Recharge (MAR)</text>
                    <text x="300" y="205" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Rain harvesting, recharge ponds, injection wells, reduced paving</text>
                    <text x="300" y="240" text-anchor="middle" font-size="9" fill="var(--svg-muted)">KUKL supplies only 30-40% of Kathmandu's water demand — rest from private GW</text>
                </svg>''',
    'Figure 9.5b: Kathmandu Valley groundwater crisis — declining water tables, quality degradation, and subsidence risk; MAR urgently needed.')

# 9. Mitigation Measures
SVGS['9.6.1 Key Formulae and Design'] = svg_wrap('''
                <svg width="600" height="230" viewBox="0 0 600 230" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">GW Management — Key Design Principles for Nepal</text>
                    <rect x="20" y="45" width="170" height="70" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="105" y="62" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-accent)">Safe Yield</text>
                    <text x="105" y="80" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Extraction ≤ Recharge</text>
                    <text x="105" y="95" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Monitor WT trends</text>
                    <text x="105" y="108" text-anchor="middle" font-size="8" fill="var(--svg-muted)">+ environmental flows</text>
                    <rect x="215" y="45" width="170" height="70" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="300" y="62" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-green-accent)">Well Spacing</text>
                    <text x="300" y="80" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Avoid interference</text>
                    <text x="300" y="95" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Min. distance = 2R</text>
                    <text x="300" y="108" text-anchor="middle" font-size="8" fill="var(--svg-muted)">R = radius of influence</text>
                    <rect x="410" y="45" width="170" height="70" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <text x="495" y="62" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-orange-accent)">Quality Protection</text>
                    <text x="495" y="80" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Wellhead protection</text>
                    <text x="495" y="95" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Sanitary seal depth</text>
                    <text x="495" y="108" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Regular testing</text>
                    <rect x="110" y="130" width="170" height="70" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <text x="195" y="148" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-water-3)">Recharge Enhancement</text>
                    <text x="195" y="165" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Rain harvesting ponds</text>
                    <text x="195" y="180" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Permeable pavements</text>
                    <text x="195" y="195" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Spring-shed mgmt</text>
                    <rect x="320" y="130" width="170" height="70" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <text x="405" y="148" text-anchor="middle" font-weight="bold" font-size="9" fill="var(--svg-red-accent)">Regulation</text>
                    <text x="405" y="165" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Well registration</text>
                    <text x="405" y="180" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Extraction permits</text>
                    <text x="405" y="195" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Monitoring network</text>
                    <text x="300" y="222" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Sustainable GW management = safe yield + quality protection + institutional governance</text>
                </svg>''',
    'Figure 9.6b: Five pillars of groundwater management in Nepal — safe yield, well spacing, quality protection, recharge enhancement, and regulation.')

# 10. Development Possibilities
SVGS['9.2.4 Development Possibiliti'] = svg_wrap('''
                <svg width="600" height="220" viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">GW Development Possibilities by Region</text>
                    <rect x="30" y="50" width="160" height="130" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-water-3)" stroke-width="2"/>
                    <text x="110" y="70" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-water-3)">Terai</text>
                    <text x="110" y="88" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">Highest potential</text>
                    <text x="110" y="105" text-anchor="middle" font-size="8" fill="var(--svg-fg)">STW: irrigation</text>
                    <text x="110" y="118" text-anchor="middle" font-size="8" fill="var(--svg-fg)">DTW: municipal supply</text>
                    <text x="110" y="131" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Available: ~12 BCM/yr</text>
                    <text x="110" y="148" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Used: ~3-4 BCM/yr</text>
                    <text x="110" y="168" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Still &lt; 30% developed</text>
                    <rect x="220" y="50" width="160" height="130" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="300" y="70" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-accent)">Inner Terai / Dun</text>
                    <text x="300" y="88" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">Moderate potential</text>
                    <text x="300" y="105" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Alluvial valleys</text>
                    <text x="300" y="118" text-anchor="middle" font-size="8" fill="var(--svg-fg)">STW/DTW feasible</text>
                    <text x="300" y="135" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Small-scale irrigation</text>
                    <text x="300" y="152" text-anchor="middle" font-size="8" fill="var(--svg-red-accent)">Arsenic in some areas</text>
                    <text x="300" y="168" text-anchor="middle" font-size="8" fill="var(--svg-muted)">~20% developed</text>
                    <rect x="410" y="50" width="160" height="130" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="490" y="70" text-anchor="middle" font-weight="bold" font-size="10" fill="var(--svg-fg)">Hills &amp; Mountains</text>
                    <text x="490" y="88" text-anchor="middle" font-size="9" fill="var(--svg-red-accent)">Low potential</text>
                    <text x="490" y="105" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Springs: primary source</text>
                    <text x="490" y="118" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Limited bore wells</text>
                    <text x="490" y="135" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Karst where limestone</text>
                    <text x="490" y="152" text-anchor="middle" font-size="8" fill="var(--svg-fg)">Seasonal variability</text>
                    <text x="490" y="168" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Focus on spring mgmt</text>
                    <text x="300" y="200" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Nepal's total GW potential: ~12 BCM/yr | Only 25-30% currently developed</text>
                    <text x="300" y="218" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Sustainable development requires zoning, monitoring, and demand management</text>
                </svg>''',
    'Figure 9.2e: Groundwater development possibilities by region — Terai has highest potential but is still less than 30% developed.')


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

print(f"\nChapter 9: {c} SVGs inserted")
print(f"  Before: {original} SVGs, After: {new_count} SVGs")
print(f"  Net added: {new_count - original}")

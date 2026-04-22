"""Replace text-heavy SVGs in Chapter 7 with geometric diagrams. Self-contained."""
import re

FILE = r"d:\Final Year\Theory\gw\GW_THE\chapter7.html"

with open(FILE, 'r', encoding='utf-8') as f:
    html = f.read()

print(f"File loaded: {len(html)} chars, {html.count('<svg')} SVGs")

def safe_replace(html, caption_text, new_html):
    """Replace figure-container by finding figcaption text, then working outward."""
    pos = html.find(caption_text)
    if pos == -1:
        print(f"  X Caption not found: {caption_text[:50]}")
        return html
    
    # Find <div class="figcaption"> before this text
    fc_start = html.rfind('<div class="figcaption">', 0, pos)
    # Find </div> after the caption text
    fc_end_pos = html.find('</div>', pos)
    if fc_end_pos == -1 or fc_start == -1:
        print(f"  X No figcaption div for: {caption_text[:50]}")
        return html
    fc_end = fc_end_pos + len('</div>')
    
    # Find the CLOSEST <div class="figure-container"> before fc_start
    search_start = max(0, fc_start - 10000)  # max 10KB back
    region = html[search_start:fc_start]
    
    # Find the LAST occurrence of figure-container in this region
    fc_tag = '<div class="figure-container">'
    last_pos = region.rfind(fc_tag)
    if last_pos == -1:
        print(f"  X No figure-container for: {caption_text[:50]}")
        return html
    container_start = search_start + last_pos
    
    # But verify there's no INTERVENING </div>\n</div> that would close an earlier container
    # Check if there's another figure-container closer
    between = html[container_start + len(fc_tag):fc_start]
    closer = between.rfind(fc_tag)
    if closer != -1:
        container_start = container_start + len(fc_tag) + closer
    
    # Find container close: after fc_end, skip whitespace, find </div>
    after = html[fc_end:]
    m = re.match(r'\s*</div>', after)
    if m:
        container_end = fc_end + m.end()
    else:
        container_end = fc_end
    
    old = html[container_start:container_end]
    old_svgs = old.count('<svg')
    
    html = html[:container_start] + new_html + html[container_end:]
    print(f"  OK Replaced ({old_svgs} SVGs, {len(old)} chars): {caption_text[:50]}")
    return html

# === REPLACEMENT SVGs ===

STEP_DRAWDOWN = '''<div class="figure-container">
                <svg width="580" height="340" viewBox="0 0 580 340" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="290" y="20" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Step-Drawdown Test</text>
                    <line x1="70" y1="50" x2="70" y2="280" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="70" y1="50" x2="540" y2="50" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="70" y1="280" x2="540" y2="280" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="305" y="298" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Time</text>
                    <text x="20" y="170" text-anchor="middle" font-size="10" fill="var(--svg-fg)" transform="rotate(-90 20 170)">Pumping Rate Q</text>
                    <text x="560" y="170" text-anchor="middle" font-size="10" fill="var(--svg-fg)" transform="rotate(90 560 170)">Drawdown s</text>
                    <line x1="200" y1="47" x2="200" y2="283" stroke="var(--svg-dim)" stroke-width="0.8" stroke-dasharray="4,4"/>
                    <line x1="340" y1="47" x2="340" y2="283" stroke="var(--svg-dim)" stroke-width="0.8" stroke-dasharray="4,4"/>
                    <line x1="470" y1="47" x2="470" y2="283" stroke="var(--svg-dim)" stroke-width="0.8" stroke-dasharray="4,4"/>
                    <line x1="70" y1="130" x2="200" y2="130" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <line x1="200" y1="130" x2="200" y2="100" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <line x1="200" y1="100" x2="340" y2="100" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <line x1="340" y1="100" x2="340" y2="70" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <line x1="340" y1="70" x2="470" y2="70" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <text x="135" y="125" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-accent)">Q&#x2081;</text>
                    <text x="270" y="95" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-accent)">Q&#x2082;</text>
                    <text x="405" y="65" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-accent)">Q&#x2083;</text>
                    <path d="M70,160 C100,195 150,205 200,210" fill="none" stroke="var(--svg-water-3)" stroke-width="2.5"/>
                    <path d="M200,210 C210,218 220,230 230,237 C260,245 310,248 340,250" fill="none" stroke="var(--svg-water-3)" stroke-width="2.5"/>
                    <path d="M340,250 C350,255 360,262 380,266 C410,272 440,275 470,276" fill="none" stroke="var(--svg-water-3)" stroke-width="2.5"/>
                    <line x1="195" y1="160" x2="195" y2="210" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <line x1="190" y1="160" x2="200" y2="160" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <line x1="190" y1="210" x2="200" y2="210" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <text x="185" y="188" text-anchor="end" font-size="9" fill="var(--svg-green-accent)">s&#x2081;</text>
                    <line x1="335" y1="160" x2="335" y2="250" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <line x1="330" y1="160" x2="340" y2="160" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <line x1="330" y1="250" x2="340" y2="250" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <text x="325" y="208" text-anchor="end" font-size="9" fill="var(--svg-green-accent)">s&#x2082;</text>
                    <line x1="465" y1="160" x2="465" y2="276" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <line x1="460" y1="160" x2="470" y2="160" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <line x1="460" y1="276" x2="470" y2="276" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <text x="455" y="222" text-anchor="end" font-size="9" fill="var(--svg-green-accent)">s&#x2083;</text>
                    <line x1="70" y1="160" x2="540" y2="160" stroke="var(--svg-dim)" stroke-width="1" stroke-dasharray="6,3"/>
                    <text x="540" y="157" text-anchor="end" font-size="8" fill="var(--svg-dim)">SWL</text>
                    <rect x="100" y="305" width="380" height="28" rx="4" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="290" y="324" text-anchor="middle" font-size="12" fill="var(--svg-fg)">s<tspan baseline-shift="sub" font-size="75%">w</tspan> = BQ + CQ<tspan baseline-shift="super" font-size="75%">2</tspan>   <tspan fill="var(--svg-green-accent)">aquifer</tspan> + <tspan fill="var(--svg-red-accent)">well loss</tspan></text>
                    <line x1="490" y1="200" x2="530" y2="200" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <text x="492" y="215" font-size="8" fill="var(--svg-fg)">Q(t)</text>
                    <line x1="490" y1="230" x2="530" y2="230" stroke="var(--svg-water-3)" stroke-width="2.5"/>
                    <text x="492" y="245" font-size="8" fill="var(--svg-fg)">s(t)</text>
                </svg>
                <div class="figcaption">Figure 7.5b: Step-drawdown test &#8212; pumping rate Q is increased in steps while drawdown s is recorded; well losses (CQ&#xB2;) grow disproportionately.</div>
            </div>'''

SCREEN_DESIGN = '''<div class="figure-container">
                <svg width="520" height="340" viewBox="0 0 520 340" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="260" y="20" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Well Screen &#8212; Design Parameters</text>
                    <rect x="30" y="40" width="460" height="240" fill="url(#dots)" stroke="none"/>
                    <rect x="145" y="40" width="230" height="240" fill="url(#dots-coarse)" stroke="none" opacity="0.5"/>
                    <rect x="195" y="40" width="130" height="240" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <line x1="195" y1="65" x2="195" y2="75" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="195" y1="90" x2="195" y2="100" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="195" y1="115" x2="195" y2="125" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="195" y1="140" x2="195" y2="150" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="195" y1="165" x2="195" y2="175" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="195" y1="190" x2="195" y2="200" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="195" y1="215" x2="195" y2="225" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="195" y1="240" x2="195" y2="250" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="325" y1="65" x2="325" y2="75" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="325" y1="90" x2="325" y2="100" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="325" y1="115" x2="325" y2="125" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="325" y1="140" x2="325" y2="150" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="325" y1="165" x2="325" y2="175" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="325" y1="190" x2="325" y2="200" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="325" y1="215" x2="325" y2="225" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="325" y1="240" x2="325" y2="250" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="165" y1="70" x2="190" y2="70" stroke="var(--svg-water-3)" stroke-width="1.2" marker-end="url(#arr)"/>
                    <line x1="165" y1="145" x2="190" y2="145" stroke="var(--svg-water-3)" stroke-width="1.2" marker-end="url(#arr)"/>
                    <line x1="165" y1="220" x2="190" y2="220" stroke="var(--svg-water-3)" stroke-width="1.2" marker-end="url(#arr)"/>
                    <line x1="355" y1="95" x2="330" y2="95" stroke="var(--svg-water-3)" stroke-width="1.2" marker-end="url(#arr)"/>
                    <line x1="355" y1="170" x2="330" y2="170" stroke="var(--svg-water-3)" stroke-width="1.2" marker-end="url(#arr)"/>
                    <line x1="355" y1="245" x2="330" y2="245" stroke="var(--svg-water-3)" stroke-width="1.2" marker-end="url(#arr)"/>
                    <line x1="430" y1="40" x2="430" y2="280" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <line x1="425" y1="40" x2="435" y2="40" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="425" y1="280" x2="435" y2="280" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="440" y="165" font-size="11" font-weight="bold" fill="var(--svg-fg)">L</text>
                    <line x1="195" y1="295" x2="325" y2="295" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <line x1="195" y1="290" x2="195" y2="300" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="325" y1="290" x2="325" y2="300" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="260" y="310" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">d</text>
                    <line x1="145" y1="295" x2="195" y2="295" stroke="var(--svg-green-accent)" stroke-width="1.2"/>
                    <line x1="145" y1="290" x2="145" y2="300" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <text x="170" y="310" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">t<tspan baseline-shift="sub" font-size="75%">gp</tspan></text>
                    <rect x="38" y="120" width="60" height="80" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="1.5" rx="3"/>
                    <line x1="42" y1="140" x2="94" y2="140" stroke="var(--svg-fg)" stroke-width="3"/>
                    <line x1="42" y1="155" x2="94" y2="155" stroke="var(--svg-fg)" stroke-width="3"/>
                    <line x1="42" y1="170" x2="94" y2="170" stroke="var(--svg-fg)" stroke-width="3"/>
                    <line x1="55" y1="143" x2="55" y2="152" stroke="var(--svg-accent)" stroke-width="1"/>
                    <line x1="52" y1="143" x2="58" y2="143" stroke="var(--svg-accent)" stroke-width="0.8"/>
                    <line x1="52" y1="152" x2="58" y2="152" stroke="var(--svg-accent)" stroke-width="0.8"/>
                    <text x="68" y="150" font-size="7" fill="var(--svg-accent)">slot</text>
                    <text x="68" y="130" font-size="7" fill="var(--svg-fg)">Detail:</text>
                    <text x="70" y="50" font-size="9" fill="var(--svg-muted)">Aquifer</text>
                    <text x="70" y="62" font-size="9" fill="var(--svg-muted)">material</text>
                    <text x="160" y="50" font-size="8" fill="var(--svg-green-accent)">Gravel</text>
                    <text x="160" y="62" font-size="8" fill="var(--svg-green-accent)">pack</text>
                    <text x="260" y="333" text-anchor="middle" font-size="10" fill="var(--svg-fg)">v<tspan baseline-shift="sub" font-size="75%">e</tspan> = Q / (&#x3C0;&#xB7;d&#xB7;L&#xB7;O<tspan baseline-shift="sub" font-size="75%">a</tspan>) &lt; 3 cm/s</text>
                </svg>
                <div class="figcaption">Figure 7.7b: Well screen cross-section showing slot openings, gravel pack, and flow arrows; entrance velocity must be kept below 3 cm/s.</div>
            </div>'''

GRAVEL_PACK = '''<div class="figure-container">
                <svg width="500" height="340" viewBox="0 0 500 340" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="250" y="20" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Gravel Pack &#8212; Plan View</text>
                    <circle cx="160" cy="175" r="100" fill="url(#dots)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="160" y="82" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Aquifer formation</text>
                    <circle cx="160" cy="175" r="70" fill="url(#dots-coarse)" stroke="var(--svg-green-accent)" stroke-width="2" opacity="0.6"/>
                    <text x="90" y="120" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-green-accent)">Gravel</text>
                    <text x="90" y="132" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-green-accent)">pack</text>
                    <circle cx="160" cy="175" r="35" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="2.5"/>
                    <line x1="125" y1="172" x2="125" y2="178" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="195" y1="172" x2="195" y2="178" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="157" y1="140" x2="163" y2="140" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="157" y1="210" x2="163" y2="210" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="135" y1="150" x2="139" y2="154" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="181" y1="196" x2="185" y2="200" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="135" y1="200" x2="139" y2="196" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="181" y1="154" x2="185" y2="150" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="160" y="178" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-fg)">Screen</text>
                    <line x1="160" y1="175" x2="195" y2="175" stroke="var(--svg-fg)" stroke-width="1" stroke-dasharray="3,2"/>
                    <text x="180" y="190" text-anchor="middle" font-size="8" fill="var(--svg-fg)">r<tspan baseline-shift="sub" font-size="75%">s</tspan></text>
                    <line x1="160" y1="165" x2="230" y2="165" stroke="var(--svg-green-accent)" stroke-width="1" stroke-dasharray="3,2"/>
                    <text x="218" y="160" font-size="8" fill="var(--svg-green-accent)">r<tspan baseline-shift="sub" font-size="75%">gp</tspan></text>
                    <line x1="160" y1="155" x2="260" y2="155" stroke="var(--svg-muted)" stroke-width="1" stroke-dasharray="3,2"/>
                    <text x="248" y="150" font-size="8" fill="var(--svg-muted)">r<tspan baseline-shift="sub" font-size="75%">b</tspan></text>
                    <line x1="260" y1="175" x2="235" y2="175" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="160" y1="75" x2="160" y2="100" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="160" y1="275" x2="160" y2="250" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="60" y1="175" x2="85" y2="175" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <rect x="290" y="55" width="200" height="220" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="390" y="78" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">Design Criteria</text>
                    <text x="300" y="100" font-size="10" fill="var(--svg-fg)">Pack-Aquifer Ratio:</text>
                    <text x="390" y="122" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--svg-accent)">D<tspan baseline-shift="sub" font-size="70%">50(pack)</tspan> / D<tspan baseline-shift="sub" font-size="70%">50(aq)</tspan> = 4&#x2013;6</text>
                    <text x="300" y="150" font-size="10" fill="var(--svg-fg)">Uniformity:</text>
                    <text x="390" y="170" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-green-accent)">C<tspan baseline-shift="sub" font-size="70%">u</tspan> = D<tspan baseline-shift="sub" font-size="70%">60</tspan>/D<tspan baseline-shift="sub" font-size="70%">10</tspan> &lt; 2.5</text>
                    <text x="300" y="198" font-size="10" fill="var(--svg-fg)">Thickness:</text>
                    <text x="300" y="215" font-size="10" fill="var(--svg-fg)">  75&#x2013;200 mm (min 75)</text>
                    <text x="300" y="240" font-size="10" fill="var(--svg-fg)">Slot size:</text>
                    <text x="300" y="257" font-size="10" fill="var(--svg-fg)">  = D<tspan baseline-shift="sub" font-size="70%">10</tspan> of gravel</text>
                    <text x="250" y="330" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Water flows radially inward: aquifer &#x2192; gravel pack &#x2192; screen &#x2192; well</text>
                </svg>
                <div class="figcaption">Figure 7.9b: Gravel pack plan view showing concentric zones with design criteria for D&#x2085;&#x2080; ratio and uniformity coefficient.</div>
            </div>'''

GALLERY = '''<div class="figure-container">
                <svg width="560" height="320" viewBox="0 0 560 320" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="280" y="20" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Infiltration Gallery &#8212; Cross Section</text>
                    <rect x="30" y="260" width="500" height="20" fill="url(#hatch)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="280" y="295" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Impervious layer</text>
                    <rect x="30" y="60" width="500" height="200" fill="url(#dots)" stroke="none" opacity="0.4"/>
                    <line x1="30" y1="60" x2="530" y2="60" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="280" y="52" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Ground Surface</text>
                    <path d="M30,110 L530,110" fill="none" stroke="var(--svg-water-3)" stroke-width="2" stroke-dasharray="8,4"/>
                    <text x="535" y="108" font-size="8" fill="var(--svg-water-3)">Original WT</text>
                    <path d="M30,110 C100,112 180,130 220,155 C240,170 255,180 270,190 C275,193 278,195 280,195 C282,195 285,193 290,190 C305,180 320,170 340,155 C380,130 460,112 530,110" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="480" y="128" font-size="8" fill="var(--svg-accent)">Depressed WT</text>
                    <path d="M30,110 C100,112 180,130 220,155 C240,170 255,180 270,190 C275,193 278,195 280,195 C282,195 285,193 290,190 C305,180 320,170 340,155 C380,130 460,112 530,110 L530,260 L30,260 Z" fill="var(--svg-water)" fill-opacity="0.15" stroke="none"/>
                    <circle cx="280" cy="200" r="12" fill="var(--svg-bg-fill)" stroke="var(--svg-fg)" stroke-width="2.5"/>
                    <circle cx="268" cy="200" r="1.5" fill="var(--svg-accent)"/>
                    <circle cx="292" cy="200" r="1.5" fill="var(--svg-accent)"/>
                    <circle cx="280" cy="188" r="1.5" fill="var(--svg-accent)"/>
                    <circle cx="280" cy="212" r="1.5" fill="var(--svg-accent)"/>
                    <text x="280" y="230" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-fg)">Gallery pipe</text>
                    <circle cx="280" cy="200" r="25" fill="none" stroke="var(--svg-green-accent)" stroke-width="1.5" stroke-dasharray="4,3"/>
                    <text x="320" y="218" font-size="7" fill="var(--svg-green-accent)">gravel</text>
                    <line x1="180" y1="165" x2="250" y2="195" stroke="var(--svg-water-3)" stroke-width="1.2" marker-end="url(#arr)"/>
                    <line x1="380" y1="165" x2="310" y2="195" stroke="var(--svg-water-3)" stroke-width="1.2" marker-end="url(#arr)"/>
                    <line x1="280" y1="140" x2="280" y2="172" stroke="var(--svg-water-3)" stroke-width="1.2" marker-end="url(#arr)"/>
                    <line x1="50" y1="110" x2="50" y2="260" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <line x1="45" y1="110" x2="55" y2="110" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="45" y1="260" x2="55" y2="260" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="42" y="190" text-anchor="end" font-size="12" font-weight="bold" fill="var(--svg-fg)">H</text>
                    <line x1="240" y1="195" x2="240" y2="260" stroke="var(--svg-red-accent)" stroke-width="1.2"/>
                    <line x1="235" y1="195" x2="245" y2="195" stroke="var(--svg-red-accent)" stroke-width="1"/>
                    <line x1="235" y1="260" x2="245" y2="260" stroke="var(--svg-red-accent)" stroke-width="1"/>
                    <text x="232" y="230" text-anchor="end" font-size="12" font-weight="bold" fill="var(--svg-red-accent)">h</text>
                    <line x1="50" y1="42" x2="280" y2="42" stroke="var(--svg-dim)" stroke-width="1"/>
                    <line x1="50" y1="38" x2="50" y2="46" stroke="var(--svg-dim)" stroke-width="1"/>
                    <line x1="280" y1="38" x2="280" y2="46" stroke="var(--svg-dim)" stroke-width="1"/>
                    <text x="165" y="40" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-dim)">L</text>
                    <text x="280" y="312" text-anchor="middle" font-size="11" fill="var(--svg-fg)">q = K(H<tspan baseline-shift="super" font-size="75%">2</tspan> &#x2212; h<tspan baseline-shift="super" font-size="75%">2</tspan>) / 2L  <tspan font-size="9" fill="var(--svg-muted)">(one side)</tspan></text>
                </svg>
                <div class="figcaption">Figure 7.11b: Infiltration gallery cross-section with Dupuit flow; water flows radially inward toward the horizontal perforated pipe.</div>
            </div>'''

WELL_DEV = '''<div class="figure-container">
                <svg width="560" height="310" viewBox="0 0 560 310" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="280" y="20" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">Well Development &#8212; Surging Method</text>
                    <rect x="30" y="40" width="210" height="230" fill="url(#dots)" stroke="none" opacity="0.4"/>
                    <rect x="310" y="40" width="210" height="230" fill="url(#dots)" stroke="none" opacity="0.4"/>
                    <rect x="240" y="40" width="8" height="80" fill="var(--svg-fg)"/>
                    <rect x="302" y="40" width="8" height="80" fill="var(--svg-fg)"/>
                    <rect x="240" y="120" width="8" height="150" fill="none" stroke="var(--svg-accent)" stroke-width="2" stroke-dasharray="4,3"/>
                    <rect x="302" y="120" width="8" height="150" fill="none" stroke="var(--svg-accent)" stroke-width="2" stroke-dasharray="4,3"/>
                    <rect x="220" y="120" width="20" height="150" fill="url(#dots-coarse)" stroke="none" opacity="0.5"/>
                    <rect x="310" y="120" width="20" height="150" fill="url(#dots-coarse)" stroke="none" opacity="0.5"/>
                    <rect x="252" y="140" width="46" height="15" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="2" rx="2"/>
                    <text x="275" y="152" text-anchor="middle" font-size="7" font-weight="bold" fill="var(--svg-fg)">Plunger</text>
                    <line x1="275" y1="30" x2="275" y2="140" stroke="var(--svg-fg)" stroke-width="3"/>
                    <text x="290" y="50" font-size="9" fill="var(--svg-fg)">Surge rod</text>
                    <line x1="275" y1="25" x2="275" y2="10" stroke="var(--svg-red-accent)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <line x1="285" y1="10" x2="285" y2="25" stroke="var(--svg-red-accent)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <text x="310" y="20" font-size="8" fill="var(--svg-red-accent)">Push-pull</text>
                    <rect x="248" y="85" width="54" height="185" fill="var(--svg-water)" fill-opacity="0.15" stroke="none"/>
                    <line x1="248" y1="165" x2="215" y2="165" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="310" y1="165" x2="340" y2="165" stroke="var(--svg-water-3)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="370" y="168" font-size="7" fill="var(--svg-water-3)">Down: push</text>
                    <line x1="215" y1="200" x2="243" y2="200" stroke="var(--svg-accent)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="340" y1="200" x2="315" y2="200" stroke="var(--svg-accent)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="370" y="203" font-size="7" fill="var(--svg-accent)">Up: pull + fines</text>
                    <rect x="200" y="130" width="20" height="130" fill="var(--svg-orange-accent)" fill-opacity="0.15" stroke="none"/>
                    <rect x="330" y="130" width="20" height="130" fill="var(--svg-orange-accent)" fill-opacity="0.15" stroke="none"/>
                    <text x="390" y="235" font-size="8" fill="var(--svg-orange-accent)">Disturbed zone</text>
                    <text x="390" y="248" font-size="8" fill="var(--svg-orange-accent)">(fines removed)</text>
                    <text x="110" y="85" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Aquifer</text>
                    <text x="159" y="150" font-size="8" fill="var(--svg-green-accent)">Gravel</text>
                    <text x="159" y="162" font-size="8" fill="var(--svg-green-accent)">pack</text>
                    <text x="180" y="220" font-size="8" fill="var(--svg-accent)">Screen</text>
                    <rect x="30" y="278" width="500" height="25" rx="4" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="280" y="295" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Surging removes drilling fines &#x2192; increases K near screen &#x2192; higher specific capacity</text>
                </svg>
                <div class="figcaption">Figure 7.10b: Well development by surging &#8212; the plunger creates alternating push-pull flow through the screen, removing fine particles.</div>
            </div>'''

# Apply replacements
html = safe_replace(html, 'Step-drawdown test separates aquifer losses', STEP_DRAWDOWN)
html = safe_replace(html, 'Five key screen design parameters', SCREEN_DESIGN)
html = safe_replace(html, 'Gravel pack design', GRAVEL_PACK)
html = safe_replace(html, 'Infiltration gallery yield', GALLERY)
html = safe_replace(html, 'Well development methods', WELL_DEV)

with open(FILE, 'w', encoding='utf-8') as f:
    f.write(html)

print(f"\nDone! {html.count('<svg')} SVGs in file")

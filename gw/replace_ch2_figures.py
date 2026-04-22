#!/usr/bin/env python3
"""Replace all 21 figures in GW_THE/chapter2.html with improved SVGs."""
import re

FILE = r"GW_THE/chapter2.html"

with open(FILE, "r", encoding="utf-8") as f:
    html = f.read()

# Build mapping: figcaption substring → new figure-container HTML
# We locate each <div class="figure-container"> ... </div> block by its figcaption text

REPLACEMENTS = {}

# ──────────────────────── FIGURE 2.1 ────────────────────────
REPLACEMENTS["Figure 2.1:"] = '''<div class="figure-container">
                <svg width="760" height="280" viewBox="0 0 760 280" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <!-- Panel 1: Pore Scale -->
                    <rect x="15" y="40" width="210" height="170" rx="10" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="120" y="30" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-accent)">Pore Scale</text>
                    <!-- Grains -->
                    <circle cx="55" cy="90" r="20" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <circle cx="110" cy="80" r="24" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <circle cx="170" cy="95" r="22" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <circle cx="75" cy="145" r="26" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <circle cx="140" cy="150" r="18" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <circle cx="185" cy="160" r="24" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <!-- Tortuous flow path -->
                    <path d="M30,100 C45,75 80,65 100,80 C120,95 130,85 155,95 C180,105 195,90 215,100" fill="none" stroke="var(--svg-water-3)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <!-- REV dashed box -->
                    <rect x="75" y="100" width="80" height="65" fill="none" stroke="var(--svg-accent)" stroke-width="2" stroke-dasharray="6,4" rx="4"/>
                    <text x="115" y="118" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-accent)">REV</text>
                    <text x="120" y="195" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Complex grain + pore geometry</text>

                    <!-- Arrow 1 -->
                    <line x1="232" y1="125" x2="278" y2="125" stroke="var(--svg-fg)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <text x="255" y="115" text-anchor="middle" font-size="10" font-style="italic" fill="var(--svg-fg)">Average</text>
                    <text x="255" y="142" text-anchor="middle" font-size="9" fill="var(--svg-muted)">over REV</text>

                    <!-- Panel 2: REV Scale -->
                    <rect x="285" y="40" width="210" height="170" rx="10" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="390" y="30" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-green-accent)">REV Scale</text>
                    <!-- Smoothed property graph -->
                    <line x1="310" y1="180" x2="470" y2="180" stroke="var(--svg-fg)" stroke-width="1" marker-end="url(#arr)"/>
                    <line x1="310" y1="180" x2="310" y2="65" stroke="var(--svg-fg)" stroke-width="1" marker-end="url(#arr)"/>
                    <path d="M315,165 Q330,70 350,120 Q370,160 390,110 Q400,95 420,100 Q440,105 460,100" fill="none" stroke="var(--svg-green-accent)" stroke-width="2.5"/>
                    <line x1="390" y1="65" x2="390" y2="180" stroke="var(--svg-fg)" stroke-width="1" stroke-dasharray="5,3"/>
                    <text x="390" y="58" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-fg)">REV size</text>
                    <text x="345" y="78" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Fluctuates</text>
                    <text x="440" y="90" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Stable</text>
                    <text x="390" y="198" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Averaged head &amp; flux meaningful</text>

                    <!-- Arrow 2 -->
                    <line x1="502" y1="125" x2="548" y2="125" stroke="var(--svg-fg)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <text x="525" y="115" text-anchor="middle" font-size="10" font-style="italic" fill="var(--svg-fg)">Model</text>

                    <!-- Panel 3: Continuum -->
                    <rect x="555" y="40" width="190" height="170" rx="10" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="650" y="30" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-orange-accent)">Continuum</text>
                    <rect x="580" y="70" width="140" height="110" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="1" fill-opacity="0.25"/>
                    <!-- Smooth flow arrow -->
                    <line x1="595" y1="155" x2="700" y2="90" stroke="var(--svg-orange-accent)" stroke-width="3" marker-end="url(#arr)"/>
                    <text x="650" y="105" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">h(x,y,z)</text>
                    <text x="650" y="165" text-anchor="middle" font-size="11" fill="var(--svg-fg)">q = &minus;K&nabla;h</text>
                    <text x="650" y="198" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Smooth, tractable equations</text>

                    <!-- Bottom label -->
                    <rect x="180" y="240" width="400" height="28" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="380" y="259" text-anchor="middle" font-size="11" font-style="italic" fill="var(--svg-fg)">Pore complexity &#x2192; REV averaging &#x2192; Continuum PDEs</text>
                </svg>
                <div class="figcaption">Figure 2.1: Groundwater modeling moves from pore-scale complexity to REV-based averaging and finally to a continuum description.</div>
            </div>'''

# ──────────────────────── FIGURE 2.2 ────────────────────────
REPLACEMENTS["Figure 2.2:"] = '''<div class="figure-container">
                <svg width="680" height="300" viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="340" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">REV Threshold — Property Stabilization</text>
                    <!-- Axes -->
                    <line x1="80" y1="240" x2="640" y2="240" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <line x1="80" y1="240" x2="80" y2="45" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="360" y="275" text-anchor="middle" font-size="12" fill="var(--svg-fg)">Sample volume used for averaging</text>
                    <text x="30" y="145" text-anchor="middle" font-size="11" fill="var(--svg-fg)" transform="rotate(-90 30 145)">Measured porosity / K</text>
                    <!-- Fluctuating region -->
                    <rect x="81" y="55" width="230" height="184" fill="var(--svg-red-lt)" fill-opacity="0.3" stroke="none"/>
                    <text x="195" y="72" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-red-accent)">Large fluctuations</text>
                    <!-- Stable region -->
                    <rect x="310" y="55" width="320" height="184" fill="var(--svg-green-lt)" fill-opacity="0.3" stroke="none"/>
                    <text x="470" y="72" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-green-accent)">Property stabilizes</text>
                    <!-- Data line -->
                    <polyline points="95,200 120,100 145,195 170,115 200,175 230,135 260,150 290,145 320,148 350,147 380,146 410,147 440,148 470,147 500,147 530,147 560,146 590,147 620,147" fill="none" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <!-- REV threshold -->
                    <line x1="310" y1="50" x2="310" y2="240" stroke="var(--svg-fg)" stroke-width="2" stroke-dasharray="8,5"/>
                    <rect x="270" y="35" width="80" height="22" rx="4" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="310" y="51" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-fg)">REV</text>
                    <!-- Stable value line -->
                    <line x1="310" y1="147" x2="630" y2="147" stroke="var(--svg-green-accent)" stroke-width="1.5" stroke-dasharray="4,3"/>
                    <text x="636" y="142" font-size="9" fill="var(--svg-green-accent)">n&#x0304;</text>
                </svg>
                <div class="figcaption">Figure 2.2: The REV is reached when the averaged property becomes practically stable with increasing sample size.</div>
            </div>'''

# ──────────────────────── FIGURE 2.1b ────────────────────────
REPLACEMENTS["Figure 2.1b:"] = '''<div class="figure-container">
                <svg width="700" height="260" viewBox="0 0 700 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="350" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Microscopic vs Macroscopic (Continuum) View</text>
                    <!-- LEFT: Microscopic -->
                    <rect x="25" y="40" width="280" height="180" rx="10" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="165" y="62" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-accent)">Pore-Scale (Microscopic)</text>
                    <!-- Realistic grains with shading -->
                    <circle cx="75" cy="110" r="22" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <circle cx="130" cy="95" r="26" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <circle cx="195" cy="115" r="24" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <circle cx="105" cy="155" r="20" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <circle cx="165" cy="165" r="23" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <circle cx="235" cy="145" r="21" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <circle cx="260" cy="100" r="18" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <!-- Tortuous flow path -->
                    <path d="M40,105 C55,80 95,70 120,88 C145,106 155,90 180,100 C205,110 220,95 245,105 C265,115 280,100 295,110" fill="none" stroke="var(--svg-water-3)" stroke-width="2.5" stroke-dasharray="none" marker-end="url(#arr)"/>
                    <text x="165" y="205" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Tortuous flow paths around grains</text>

                    <!-- Arrow -->
                    <line x1="315" y1="130" x2="380" y2="130" stroke="var(--svg-fg)" stroke-width="3" marker-end="url(#arr)"/>
                    <text x="348" y="118" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Average</text>
                    <text x="348" y="148" text-anchor="middle" font-size="9" fill="var(--svg-muted)">over REV</text>

                    <!-- RIGHT: Macroscopic -->
                    <rect x="390" y="40" width="280" height="180" rx="10" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="530" y="62" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-green-accent)">Continuum (Macroscopic)</text>
                    <rect x="420" y="80" width="220" height="90" rx="6" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="1" fill-opacity="0.2"/>
                    <text x="530" y="115" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Uniform medium</text>
                    <text x="530" y="135" text-anchor="middle" font-size="10" fill="var(--svg-fg)">K, n defined at every point</text>
                    <line x1="420" y1="125" x2="640" y2="125" stroke="var(--svg-green-accent)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <text x="530" y="205" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Smooth Darcy flux field</text>

                    <!-- Bottom summary -->
                    <rect x="150" y="235" width="400" height="22" rx="4" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="350" y="251" text-anchor="middle" font-size="11" font-style="italic" fill="var(--svg-fg)">REV transforms complex pore geometry &#x2192; tractable continuum equations</text>
                </svg>
                <div class="figcaption">Figure 2.1b: The continuum approach replaces complex pore-scale flow with averaged properties (K, n) defined at every point.</div>
            </div>'''

# ──────────────────────── FIGURE 2.2b ────────────────────────
REPLACEMENTS["Figure 2.2b:"] = '''<div class="figure-container">
                <svg width="700" height="250" viewBox="0 0 700 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="350" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Where the REV Assumption Breaks Down</text>
                    <!-- Case 1: Fractured Rock -->
                    <rect x="20" y="42" width="200" height="155" rx="10" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="2"/>
                    <text x="120" y="62" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-red-accent)">Fractured Rock</text>
                    <rect x="45" y="75" width="150" height="90" fill="var(--svg-struct-2)" stroke="var(--svg-fg)" stroke-width="1" rx="4"/>
                    <line x1="85" y1="75" x2="95" y2="165" stroke="var(--svg-accent)" stroke-width="3"/>
                    <line x1="145" y1="75" x2="135" y2="165" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <line x1="45" y1="120" x2="195" y2="125" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="120" y="185" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Discrete fractures dominate flow</text>
                    <!-- Case 2: Karst -->
                    <rect x="250" y="42" width="200" height="155" rx="10" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="2"/>
                    <text x="350" y="62" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-red-accent)">Karst / Solution Channels</text>
                    <rect x="275" y="75" width="150" height="90" fill="var(--svg-struct-2)" stroke="var(--svg-fg)" stroke-width="1" rx="4"/>
                    <ellipse cx="330" cy="110" rx="35" ry="18" fill="var(--svg-water)" stroke="var(--svg-accent)" stroke-width="2" fill-opacity="0.5"/>
                    <ellipse cx="370" cy="140" rx="25" ry="12" fill="var(--svg-water)" stroke="var(--svg-accent)" stroke-width="1.5" fill-opacity="0.5"/>
                    <path d="M295,110 C310,105 320,112 330,108 C340,104 345,115 365,113" fill="none" stroke="var(--svg-water-3)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="350" y="185" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Conduit flow, not porous-media</text>
                    <!-- Case 3: Too small sample -->
                    <rect x="480" y="42" width="200" height="155" rx="10" fill="var(--svg-bg-soft)" stroke="var(--svg-red-accent)" stroke-width="2"/>
                    <text x="580" y="62" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-red-accent)">Sample &lt; REV</text>
                    <circle cx="540" cy="115" r="14" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <circle cx="575" cy="105" r="16" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <circle cx="610" cy="120" r="13" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <circle cx="560" cy="145" r="15" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <rect x="548" y="98" width="40" height="35" fill="none" stroke="var(--svg-red-accent)" stroke-width="2" stroke-dasharray="5,3"/>
                    <text x="568" y="92" text-anchor="middle" font-size="8" fill="var(--svg-red-accent)">Too small</text>
                    <text x="580" y="185" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Property fluctuates wildly</text>
                    <!-- Bottom -->
                    <rect x="140" y="215" width="420" height="24" rx="5" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="350" y="232" text-anchor="middle" font-size="11" font-style="italic" fill="var(--svg-fg)">In these cases, discrete-fracture or pipe-network models are needed</text>
                </svg>
                <div class="figcaption">Figure 2.2b: The REV/continuum approach fails in fractured rock, karst systems, and when the sample volume is smaller than the REV.</div>
            </div>'''

# ──────────────────────── FIGURE 2.3 ────────────────────────
REPLACEMENTS["Figure 2.3:"] = '''<div class="figure-container">
                <svg width="720" height="340" viewBox="0 0 720 340" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="360" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Darcy&#x2019;s Sand Column Experiment (1856)</text>
                    <!-- Sand column body -->
                    <rect x="160" y="90" width="380" height="110" rx="6" fill="url(#dots)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="350" y="150" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">Saturated Sand</text>
                    <!-- Inlet reservoir -->
                    <rect x="60" y="70" width="100" height="145" rx="6" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="2" fill-opacity="0.3"/>
                    <path d="M65,95 Q80,88 95,95 Q110,102 125,95 Q140,88 155,95" fill="none" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <text x="110" y="55" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Inflow</text>
                    <!-- Outlet reservoir -->
                    <rect x="540" y="95" width="120" height="100" rx="6" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="2" fill-opacity="0.3"/>
                    <path d="M545,118 Q560,111 575,118 Q590,125 605,118 Q620,111 635,118 Q650,125 655,118" fill="none" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <text x="600" y="55" text-anchor="middle" font-weight="bold" font-size="11" fill="var(--svg-accent)">Outflow</text>
                    <!-- Piezometer 1 -->
                    <rect x="248" y="28" width="4" height="62" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <rect x="246" y="35" width="8" height="55" fill="var(--svg-water)" fill-opacity="0.4" stroke="none"/>
                    <line x1="238" y1="35" x2="258" y2="35" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="250" y="23" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-accent)">h&#x2081;</text>
                    <!-- Piezometer 2 -->
                    <rect x="448" y="48" width="4" height="42" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <rect x="446" y="55" width="8" height="35" fill="var(--svg-water)" fill-opacity="0.4" stroke="none"/>
                    <line x1="438" y1="55" x2="458" y2="55" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="450" y="43" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-accent)">h&#x2082;</text>
                    <!-- Head difference line -->
                    <line x1="250" y1="35" x2="450" y2="55" stroke="var(--svg-red-accent)" stroke-width="2" stroke-dasharray="6,4"/>
                    <text x="350" y="40" text-anchor="middle" font-size="10" fill="var(--svg-red-accent)">&#x394;h = h&#x2081; &#x2212; h&#x2082;</text>
                    <!-- Length L -->
                    <line x1="160" y1="225" x2="540" y2="225" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="160" y1="218" x2="160" y2="232" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="540" y1="218" x2="540" y2="232" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="350" y="245" text-anchor="middle" font-weight="bold" font-size="13" fill="var(--svg-fg)">L</text>
                    <!-- Flow arrow -->
                    <line x1="220" y1="145" x2="480" y2="145" stroke="var(--svg-green-accent)" stroke-width="3" marker-end="url(#arr)"/>
                    <text x="350" y="175" text-anchor="middle" font-size="11" fill="var(--svg-green-accent)">Q</text>
                    <!-- Cross-section -->
                    <line x1="160" y1="260" x2="160" y2="300" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="160" y="315" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Area = A</text>
                    <!-- Formula -->
                    <rect x="230" y="275" width="260" height="30" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="1.5"/>
                    <text x="360" y="296" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--svg-fg)">Q = KA(h&#x2081; &#x2212; h&#x2082;)/L</text>
                </svg>
                <div class="figcaption">Figure 2.3: Darcy&#x2019;s original experiment with a saturated sand column and piezometric head measurements.</div>
            </div>'''

# ──────────────────────── FIGURE 2.3d ────────────────────────
REPLACEMENTS["Figure 2.3d:"] = '''<div class="figure-container">
                <svg width="620" height="260" viewBox="0 0 620 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="310" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Darcy&#x2019;s Key Experimental Findings</text>
                    <!-- Q vs i graph -->
                    <rect x="20" y="35" width="270" height="200" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="65" y1="210" x2="260" y2="210" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="65" y1="210" x2="65" y2="55" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="162" y="240" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Hydraulic gradient, i</text>
                    <text x="42" y="130" text-anchor="middle" font-size="10" fill="var(--svg-fg)" transform="rotate(-90 42 130)">Discharge, Q</text>
                    <line x1="65" y1="205" x2="245" y2="70" stroke="var(--svg-accent)" stroke-width="3"/>
                    <circle cx="105" cy="180" r="4" fill="var(--svg-accent)"/>
                    <circle cx="145" cy="155" r="4" fill="var(--svg-accent)"/>
                    <circle cx="185" cy="130" r="4" fill="var(--svg-accent)"/>
                    <circle cx="225" cy="90" r="4" fill="var(--svg-accent)"/>
                    <text x="175" y="102" font-size="11" fill="var(--svg-accent)" transform="rotate(-34 175 102)">Q = KAi</text>
                    <text x="162" y="50" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">Q &#x221D; i (linear)</text>
                    <!-- Q vs A graph -->
                    <rect x="330" y="35" width="270" height="200" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="375" y1="210" x2="570" y2="210" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <line x1="375" y1="210" x2="375" y2="55" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="472" y="240" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Cross-sectional area, A</text>
                    <text x="352" y="130" text-anchor="middle" font-size="10" fill="var(--svg-fg)" transform="rotate(-90 352 130)">Discharge, Q</text>
                    <line x1="375" y1="205" x2="555" y2="75" stroke="var(--svg-green-accent)" stroke-width="3"/>
                    <circle cx="415" cy="180" r="4" fill="var(--svg-green-accent)"/>
                    <circle cx="455" cy="155" r="4" fill="var(--svg-green-accent)"/>
                    <circle cx="495" cy="120" r="4" fill="var(--svg-green-accent)"/>
                    <circle cx="535" cy="90" r="4" fill="var(--svg-green-accent)"/>
                    <text x="490" y="102" font-size="11" fill="var(--svg-green-accent)" transform="rotate(-34 490 102)">Q = KAi</text>
                    <text x="472" y="50" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">Q &#x221D; A (linear)</text>
                </svg>
                <div class="figcaption">Figure 2.3d: Darcy&#x2019;s experimental findings &#x2014; discharge is linearly proportional to both hydraulic gradient and cross-sectional area.</div>
            </div>'''

# ──────────────────────── FIGURE 2.3b ────────────────────────
REPLACEMENTS["Figure 2.3b:"] = '''<div class="figure-container">
                <svg width="650" height="260" viewBox="0 0 650 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="325" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Darcy Flux (q) vs Seepage Velocity (v&#x209B;)</text>
                    <!-- LEFT: Darcy Flux -->
                    <rect x="25" y="42" width="270" height="170" rx="10" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="160" y="65" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-accent)">Darcy Flux q = Q/A</text>
                    <rect x="55" y="85" width="200" height="90" rx="6" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <text x="155" y="125" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Total area A</text>
                    <text x="155" y="145" text-anchor="middle" font-size="9" fill="var(--svg-muted)">(solids + voids together)</text>
                    <!-- Flow arrows across full width -->
                    <line x1="45" y1="130" x2="265" y2="130" stroke="var(--svg-accent)" stroke-width="2.5" stroke-opacity="0.5" marker-end="url(#arr)"/>

                    <!-- RIGHT: Seepage Velocity -->
                    <rect x="355" y="42" width="270" height="170" rx="10" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="490" y="65" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-green-accent)">Seepage Velocity v&#x209B; = q/n</text>
                    <rect x="385" y="85" width="200" height="90" rx="6" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.2"/>
                    <!-- Pore channels only -->
                    <rect x="395" y="90" width="14" height="80" fill="var(--svg-water)" stroke="none" fill-opacity="0.6"/>
                    <rect x="425" y="90" width="10" height="80" fill="var(--svg-water)" stroke="none" fill-opacity="0.6"/>
                    <rect x="455" y="90" width="16" height="80" fill="var(--svg-water)" stroke="none" fill-opacity="0.6"/>
                    <rect x="490" y="90" width="12" height="80" fill="var(--svg-water)" stroke="none" fill-opacity="0.6"/>
                    <rect x="520" y="90" width="14" height="80" fill="var(--svg-water)" stroke="none" fill-opacity="0.6"/>
                    <rect x="550" y="90" width="10" height="80" fill="var(--svg-water)" stroke="none" fill-opacity="0.6"/>
                    <text x="490" y="125" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Pore area only</text>
                    <text x="490" y="145" text-anchor="middle" font-size="9" fill="var(--svg-muted)">A&#x1D65; = nA</text>

                    <!-- Bottom formula -->
                    <rect x="140" y="228" width="370" height="26" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="325" y="247" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--svg-fg)">v&#x209B; = q/n &gt; q  (since n &lt; 1, actual velocity is higher)</text>
                </svg>
                <div class="figcaption">Figure 2.3b: Darcy flux (q) is computed over the total cross-section; the actual seepage velocity through pores is q/n, always larger since n &lt; 1.</div>
            </div>'''

# ──────────────────────── FIGURE 2.3c ────────────────────────
REPLACEMENTS["Figure 2.3c:"] = '''<div class="figure-container">
                <svg width="600" height="220" viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="300" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Darcy&#x2019;s Law &#x2014; Sign Convention</text>
                    <!-- Aquifer strip -->
                    <rect x="50" y="60" width="500" height="55" rx="6" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="1.5" fill-opacity="0.2"/>
                    <!-- h1 and h2 -->
                    <line x1="100" y1="40" x2="100" y2="60" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <text x="100" y="35" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-accent)">h&#x2081; (high)</text>
                    <line x1="500" y1="50" x2="500" y2="60" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <text x="500" y="35" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-accent)">h&#x2082; (low)</text>
                    <!-- Hydraulic grade line -->
                    <line x1="100" y1="42" x2="500" y2="52" stroke="var(--svg-red-accent)" stroke-width="2" stroke-dasharray="7,4"/>
                    <!-- Flow arrow -->
                    <line x1="120" y1="88" x2="480" y2="88" stroke="var(--svg-green-accent)" stroke-width="3.5" marker-end="url(#arr)"/>
                    <text x="300" y="82" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-green-accent)">Flow direction (high &#x2192; low head)</text>
                    <!-- x-axis -->
                    <line x1="100" y1="125" x2="500" y2="125" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="510" y="129" font-size="11" fill="var(--svg-fg)">x</text>
                    <!-- L dimension -->
                    <line x1="100" y1="140" x2="500" y2="140" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="100" y1="135" x2="100" y2="145" stroke="var(--svg-fg)" stroke-width="1"/>
                    <line x1="500" y1="135" x2="500" y2="145" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="300" y="157" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-fg)">L</text>
                    <!-- Formula -->
                    <rect x="100" y="170" width="400" height="28" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="300" y="190" text-anchor="middle" font-size="12" fill="var(--svg-fg)">q = &#x2212;K(dh/dx) = &#x2212;K(h&#x2082;&#x2212;h&#x2081;)/L = K(h&#x2081;&#x2212;h&#x2082;)/L</text>
                    <text x="300" y="212" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Negative sign ensures q is positive in direction of decreasing head</text>
                </svg>
                <div class="figcaption">Figure 2.3c: Darcy&#x2019;s law sign convention &#x2014; the negative sign ensures flow is in the direction of decreasing hydraulic head.</div>
            </div>'''

# ──────────────────────── FIGURE 2.4 ────────────────────────
REPLACEMENTS["Figure 2.4:"] = '''<div class="figure-container">
                <svg width="700" height="340" viewBox="0 0 700 340" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="350" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">3D Differential Control Volume</text>
                    <!-- 3D box (isometric) -->
                    <polygon points="180,230 380,230 480,170 280,170" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="2" fill-opacity="0.15"/>
                    <polygon points="180,230 180,110 280,55 280,170" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="2" fill-opacity="0.1"/>
                    <polygon points="280,170 480,170 480,55 280,55" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="2" fill-opacity="0.2"/>
                    <!-- dx, dy, dz labels -->
                    <text x="280" y="248" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">dx</text>
                    <text x="215" y="175" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">dy</text>
                    <text x="170" y="165" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">dz</text>
                    <!-- Axes -->
                    <line x1="360" y1="260" x2="470" y2="260" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="480" y="265" font-size="12" fill="var(--svg-fg)">x</text>
                    <line x1="360" y1="260" x2="360" y2="130" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="365" y="125" font-size="12" fill="var(--svg-fg)">z</text>
                    <line x1="360" y1="260" x2="270" y2="220" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="260" y="215" font-size="12" fill="var(--svg-fg)">y</text>
                    <!-- Flux arrows on faces -->
                    <line x1="230" y1="142" x2="330" y2="100" stroke="var(--svg-accent)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <text x="265" y="110" font-size="10" fill="var(--svg-accent)">q&#x2093;</text>
                    <line x1="180" y1="170" x2="230" y2="195" stroke="var(--svg-green-accent)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <text x="195" y="198" font-size="10" fill="var(--svg-green-accent)">q&#x1D67;</text>
                    <line x1="330" y1="200" x2="330" y2="150" stroke="var(--svg-orange-accent)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <text x="340" y="170" font-size="10" fill="var(--svg-orange-accent)">q&#x1D6A;</text>
                    <!-- Head labels -->
                    <text x="220" y="195" font-size="10" fill="var(--svg-fg)">h + dh</text>
                    <text x="435" y="155" font-size="10" fill="var(--svg-fg)">h</text>
                    <!-- Bottom text -->
                    <text x="350" y="310" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Flow components governed by head gradients along x, y, and z</text>
                    <rect x="180" y="318" width="340" height="22" rx="4" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="350" y="334" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">q&#x20D7; = &#x2212;K&#x2207;h</text>
                </svg>
                <div class="figcaption">Figure 2.4: Differential control volume showing directional head gradients and the vector nature of Darcy flow.</div>
            </div>'''

# ──────────────────────── FIGURE 2.5 ────────────────────────
REPLACEMENTS["Figure 2.5:"] = '''<div class="figure-container">
                <svg width="700" height="280" viewBox="0 0 700 280" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="350" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Hydraulic Head Components</text>
                    <!-- Datum -->
                    <line x1="60" y1="230" x2="650" y2="230" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="660" y="234" font-size="11" fill="var(--svg-fg)">Datum</text>
                    <!-- Porous medium block -->
                    <rect x="200" y="110" width="160" height="120" rx="6" fill="url(#dots)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="280" y="175" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Porous medium</text>
                    <!-- Piezometer tubes -->
                    <rect x="258" y="40" width="5" height="70" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <rect x="256" y="50" width="9" height="60" fill="var(--svg-water)" fill-opacity="0.4" stroke="none"/>
                    <line x1="248" y1="50" x2="270" y2="50" stroke="var(--svg-water-3)" stroke-width="2"/>
                    <rect x="308" y="60" width="5" height="50" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <rect x="306" y="75" width="9" height="35" fill="var(--svg-water)" fill-opacity="0.4" stroke="none"/>
                    <line x1="298" y1="75" x2="320" y2="75" stroke="var(--svg-water-3)" stroke-width="2"/>
                    <!-- h1 h2 labels -->
                    <text x="260" y="38" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-accent)">h&#x2081;</text>
                    <text x="310" y="55" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-accent)">h&#x2082;</text>
                    <!-- Elevation head -->
                    <line x1="420" y1="230" x2="420" y2="110" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <line x1="415" y1="230" x2="425" y2="230" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <line x1="415" y1="110" x2="425" y2="110" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="440" y="175" font-size="12" font-weight="bold" fill="var(--svg-green-accent)">z</text>
                    <text x="440" y="192" font-size="9" fill="var(--svg-green-accent)">Elevation head</text>
                    <!-- Pressure head -->
                    <line x1="490" y1="110" x2="490" y2="50" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="485" y1="110" x2="495" y2="110" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="485" y1="50" x2="495" y2="50" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="510" y="80" font-size="12" font-weight="bold" fill="var(--svg-accent)">p/&#x3B3;</text>
                    <text x="510" y="97" font-size="9" fill="var(--svg-accent)">Pressure head</text>
                    <!-- Total head -->
                    <line x1="560" y1="230" x2="560" y2="50" stroke="var(--svg-fg)" stroke-width="2" stroke-dasharray="5,3"/>
                    <line x1="555" y1="50" x2="565" y2="50" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="580" y="140" font-size="12" font-weight="bold" fill="var(--svg-fg)">h</text>
                    <text x="580" y="157" font-size="9" fill="var(--svg-fg)">Total head</text>
                    <!-- Formula -->
                    <rect x="170" y="248" width="360" height="26" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="350" y="266" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--svg-fg)">h = z + p/&#x3B3;  (GW flows from larger h to smaller h)</text>
                </svg>
                <div class="figcaption">Figure 2.5: Hydraulic head is the sum of elevation head and pressure head, and head difference is the driving force for groundwater motion.</div>
            </div>'''

# ──────────────────────── FIGURE 2.5b ────────────────────────
REPLACEMENTS["Figure 2.5b:"] = '''<div class="figure-container">
                <svg width="580" height="320" viewBox="0 0 580 320" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="290" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Piezometer &#x2014; Measuring Hydraulic Head at Point P</text>
                    <!-- Datum -->
                    <line x1="40" y1="275" x2="530" y2="275" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="540" y="279" font-size="10" fill="var(--svg-fg)">Datum</text>
                    <!-- Soil column -->
                    <rect x="140" y="80" width="70" height="195" rx="4" fill="var(--svg-struct)" stroke="var(--svg-fg)" stroke-width="1.5" fill-opacity="0.3"/>
                    <text x="175" y="280" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Soil</text>
                    <!-- Point P -->
                    <circle cx="175" cy="200" r="6" fill="var(--svg-red-accent)"/>
                    <text x="195" y="204" font-size="12" font-weight="bold" fill="var(--svg-red-accent)">P</text>
                    <!-- Piezometer tube -->
                    <rect x="215" y="50" width="5" height="225" fill="none" stroke="var(--svg-accent)" stroke-width="2"/>
                    <!-- Water in piezometer -->
                    <rect x="213" y="100" width="9" height="175" fill="var(--svg-water)" fill-opacity="0.4" stroke="none"/>
                    <line x1="205" y1="100" x2="230" y2="100" stroke="var(--svg-water-3)" stroke-width="2.5"/>
                    <text x="240" y="104" font-size="10" fill="var(--svg-water-3)">Water level</text>
                    <!-- z (elevation head) -->
                    <line x1="320" y1="275" x2="320" y2="200" stroke="var(--svg-green-accent)" stroke-width="2.5"/>
                    <line x1="314" y1="275" x2="326" y2="275" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <line x1="314" y1="200" x2="326" y2="200" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="345" y="242" font-size="13" font-weight="bold" fill="var(--svg-green-accent)">z</text>
                    <text x="345" y="258" font-size="9" fill="var(--svg-green-accent)">Elevation head</text>
                    <!-- psi (pressure head) -->
                    <line x1="390" y1="200" x2="390" y2="100" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <line x1="384" y1="200" x2="396" y2="200" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="384" y1="100" x2="396" y2="100" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="415" y="150" font-size="13" font-weight="bold" fill="var(--svg-accent)">&#x3C8; = p/&#x3C1;g</text>
                    <text x="415" y="168" font-size="9" fill="var(--svg-accent)">Pressure head</text>
                    <!-- h (total head) -->
                    <line x1="465" y1="275" x2="465" y2="100" stroke="var(--svg-fg)" stroke-width="2" stroke-dasharray="5,3"/>
                    <line x1="459" y1="100" x2="471" y2="100" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="485" y="190" font-size="13" font-weight="bold" fill="var(--svg-fg)">h</text>
                    <text x="485" y="207" font-size="9" fill="var(--svg-fg)">Total head</text>
                    <!-- Formula -->
                    <rect x="130" y="290" width="320" height="26" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="290" y="308" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--svg-fg)">h = z + &#x3C8; = z + p/(&#x3C1;g)</text>
                </svg>
                <div class="figcaption">Figure 2.5b: Hydraulic head at point P is the sum of elevation head (z) and pressure head (&#x3C8; = p/&#x3C1;g) &#x2014; measured by the water level in a piezometer.</div>
            </div>'''

# ──────────────────────── FIGURE 2.6 ────────────────────────
REPLACEMENTS["Figure 2.6:"] = '''<div class="figure-container">
                <svg width="680" height="300" viewBox="0 0 680 300" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="340" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Darcy vs Non-Darcian Flow Regimes</text>
                    <!-- Axes -->
                    <line x1="80" y1="250" x2="640" y2="250" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <line x1="80" y1="250" x2="80" y2="40" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="360" y="280" text-anchor="middle" font-size="12" fill="var(--svg-fg)">Hydraulic gradient, i</text>
                    <text x="30" y="148" text-anchor="middle" font-size="11" fill="var(--svg-fg)" transform="rotate(-90 30 148)">Specific discharge, q</text>
                    <!-- Darcy region (linear) -->
                    <line x1="80" y1="240" x2="380" y2="105" stroke="var(--svg-green-accent)" stroke-width="3.5"/>
                    <rect x="160" y="145" width="120" height="24" rx="5" fill="var(--svg-green-lt)" stroke="var(--svg-green-accent)" stroke-width="1.2"/>
                    <text x="220" y="162" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-green-accent)">DARCY (linear)</text>
                    <!-- Non-Darcy region (curve) -->
                    <path d="M380,105 Q440,80 500,90 Q560,105 610,160" fill="none" stroke="var(--svg-red-accent)" stroke-width="3.5"/>
                    <rect x="465" y="68" width="140" height="24" rx="5" fill="var(--svg-red-lt)" stroke="var(--svg-red-accent)" stroke-width="1.2"/>
                    <text x="535" y="85" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-red-accent)">NON-DARCIAN</text>
                    <!-- Deviation point -->
                    <line x1="380" y1="60" x2="380" y2="250" stroke="var(--svg-fg)" stroke-width="1.5" stroke-dasharray="7,5"/>
                    <circle cx="380" cy="105" r="5" fill="var(--svg-orange-accent)"/>
                    <text x="395" y="55" text-anchor="start" font-size="10" font-weight="bold" fill="var(--svg-fg)">Deviation begins</text>
                    <text x="395" y="70" text-anchor="start" font-size="9" fill="var(--svg-muted)">Re &#x2248; 1&#x2013;10</text>
                </svg>
                <div class="figcaption">Figure 2.6: Darcy&#x2019;s law is linear only over the laminar-flow range; at high gradients inertial effects cause nonlinear behavior.</div>
            </div>'''

# ──────────────────────── FIGURE 2.7 ────────────────────────
REPLACEMENTS["Figure 2.7:"] = '''<div class="figure-container">
                <svg width="680" height="320" viewBox="0 0 680 320" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="340" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Darcy Validity Domain Around a Pumping Well</text>
                    <!-- Well -->
                    <circle cx="340" cy="165" r="18" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2.5"/>
                    <text x="340" y="169" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-fg)">Well</text>
                    <!-- Zone 1: Invalid (near well) -->
                    <circle cx="340" cy="165" r="50" fill="var(--svg-red-lt)" fill-opacity="0.3" stroke="var(--svg-red-accent)" stroke-width="1.5" stroke-dasharray="5,3"/>
                    <!-- Zone 2: r_min boundary -->
                    <circle cx="340" cy="165" r="90" fill="none" stroke="var(--svg-orange-accent)" stroke-width="2.5"/>
                    <!-- Zone 3: Darcy valid -->
                    <circle cx="340" cy="165" r="140" fill="none" stroke="var(--svg-green-accent)" stroke-width="1" stroke-dasharray="4,3"/>
                    <!-- Outer boundary -->
                    <circle cx="340" cy="165" r="135" fill="var(--svg-green-lt)" fill-opacity="0.15" stroke="none"/>
                    <!-- Radius line -->
                    <line x1="340" y1="165" x2="540" y2="165" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="445" y="155" font-size="11" fill="var(--svg-fg)">r</text>
                    <!-- r_min label -->
                    <line x1="340" y1="165" x2="430" y2="165" stroke="var(--svg-accent)" stroke-width="1" stroke-dasharray="4,3"/>
                    <text x="435" y="180" font-size="10" font-weight="bold" fill="var(--svg-orange-accent)">r&#x2098;&#x1D62;&#x2099;</text>
                    <!-- Labels -->
                    <text x="340" y="230" text-anchor="middle" font-size="9" fill="var(--svg-red-accent)">High velocity near well</text>
                    <text x="340" y="245" text-anchor="middle" font-size="9" fill="var(--svg-red-accent)">Darcy law may fail</text>
                    <text x="550" y="100" text-anchor="middle" font-size="10" fill="var(--svg-orange-accent)">Re = Re&#x1D9C;&#x1D63;</text>
                    <text x="550" y="260" text-anchor="middle" font-size="10" fill="var(--svg-green-accent)">Darcy flow is valid here</text>
                    <!-- Formula -->
                    <rect x="140" y="285" width="400" height="28" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="340" y="305" text-anchor="middle" font-size="11" fill="var(--svg-fg)">r&#x2098;&#x1D62;&#x2099; = Qd&#x2098; / (2&#x3C0;b&#x3BD;Re&#x1D9C;&#x1D63;) &#x2014; Darcy valid for r &#x2265; r&#x2098;&#x1D62;&#x2099;</text>
                </svg>
                <div class="figcaption">Figure 2.7: The radial velocity is highest near the well, so the Darcy-valid domain usually starts outside a minimum radius.</div>
            </div>'''

# ──────────────────────── FIGURE 2.6b ────────────────────────
REPLACEMENTS["Figure 2.6b:"] = '''<div class="figure-container">
                <svg width="680" height="260" viewBox="0 0 680 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="340" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Darcy&#x2019;s Law Validity &#x2014; Reynolds Number Regimes</text>
                    <!-- Axes -->
                    <line x1="80" y1="200" x2="620" y2="200" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <line x1="80" y1="200" x2="80" y2="40" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="350" y="230" text-anchor="middle" font-size="12" fill="var(--svg-fg)">Reynolds Number (Re = &#x3C1;vd/&#x3BC;)</text>
                    <text x="50" y="120" text-anchor="middle" font-size="11" fill="var(--svg-fg)" transform="rotate(-90 50 120)">Velocity (v)</text>
                    <!-- Darcy zone -->
                    <rect x="81" y="45" width="195" height="154" fill="var(--svg-green-lt)" fill-opacity="0.25" stroke="none"/>
                    <line x1="80" y1="195" x2="275" y2="80" stroke="var(--svg-green-accent)" stroke-width="3.5"/>
                    <rect x="130" y="128" width="100" height="22" rx="5" fill="var(--svg-green-lt)" stroke="var(--svg-green-accent)" stroke-width="1"/>
                    <text x="180" y="143" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-green-accent)">DARCY (linear)</text>
                    <!-- Transition zone -->
                    <path d="M275,80 Q320,60 380,55" fill="none" stroke="var(--svg-orange-accent)" stroke-width="3"/>
                    <rect x="290" y="40" width="78" height="20" rx="4" fill="var(--svg-yellow-lt)" stroke="var(--svg-orange-accent)" stroke-width="1"/>
                    <text x="329" y="54" text-anchor="middle" font-size="9" font-weight="bold" fill="var(--svg-orange-accent)">Transition</text>
                    <!-- Turbulent zone -->
                    <rect x="380" y="45" width="230" height="154" fill="var(--svg-red-lt)" fill-opacity="0.15" stroke="none"/>
                    <path d="M380,55 Q440,52 560,50" fill="none" stroke="var(--svg-red-accent)" stroke-width="3"/>
                    <rect x="450" y="60" width="110" height="22" rx="5" fill="var(--svg-red-lt)" stroke="var(--svg-red-accent)" stroke-width="1"/>
                    <text x="505" y="75" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-red-accent)">TURBULENT</text>
                    <!-- Re markers -->
                    <line x1="275" y1="195" x2="275" y2="205" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="275" y="220" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Re &#x2248; 1&#x2013;10</text>
                    <line x1="380" y1="195" x2="380" y2="205" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="380" y="220" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Re &#x2248; 100</text>
                    <!-- Examples -->
                    <text x="180" y="180" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Sands, silts, clays</text>
                    <text x="505" y="100" text-anchor="middle" font-size="8" fill="var(--svg-muted)">Karst, coarse gravel, near-well</text>
                </svg>
                <div class="figcaption">Figure 2.6b: Darcy&#x2019;s law is valid only for laminar flow (Re &lt; 1&#x2013;10). At higher Reynolds numbers, flow becomes non-linear and turbulent.</div>
            </div>'''

# ──────────────────────── FIGURE 2.5c ────────────────────────
REPLACEMENTS["Figure 2.5c:"] = '''<div class="figure-container">
                <svg width="440" height="370" viewBox="0 0 440 370" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="220" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Constant-Head Permeameter</text>
                    <!-- Main tank -->
                    <rect x="110" y="55" width="220" height="230" rx="6" fill="none" stroke="var(--svg-fg)" stroke-width="2"/>
                    <!-- Water above sample -->
                    <rect x="112" y="57" width="216" height="118" fill="var(--svg-water)" fill-opacity="0.3" stroke="none"/>
                    <!-- Wave surface -->
                    <path d="M112,57 Q150,50 180,57 Q210,64 240,57 Q270,50 300,57 Q320,64 328,57" fill="none" stroke="var(--svg-water-3)" stroke-width="1.5"/>
                    <!-- Soil sample -->
                    <rect x="110" y="175" width="220" height="65" fill="url(#dots)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="220" y="212" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">Soil Sample</text>
                    <!-- Screens -->
                    <line x1="110" y1="175" x2="330" y2="175" stroke="var(--svg-fg)" stroke-width="2" stroke-dasharray="4,3"/>
                    <line x1="110" y1="240" x2="330" y2="240" stroke="var(--svg-fg)" stroke-width="2" stroke-dasharray="4,3"/>
                    <!-- Constant head overflow -->
                    <line x1="330" y1="57" x2="365" y2="57" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <line x1="365" y1="57" x2="365" y2="85" stroke="var(--svg-fg)" stroke-width="1.5" marker-end="url(#arr)"/>
                    <text x="382" y="72" font-size="9" fill="var(--svg-muted)">Overflow</text>
                    <!-- Outlet -->
                    <line x1="220" y1="285" x2="220" y2="310" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="220" y="325" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Q (collect &amp; measure)</text>
                    <!-- Delta h -->
                    <line x1="80" y1="57" x2="80" y2="240" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="74" y1="57" x2="86" y2="57" stroke="var(--svg-accent)" stroke-width="2"/>
                    <line x1="74" y1="240" x2="86" y2="240" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="60" y="152" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-accent)">&#x394;h</text>
                    <!-- L -->
                    <line x1="350" y1="175" x2="350" y2="240" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <line x1="345" y1="175" x2="355" y2="175" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <line x1="345" y1="240" x2="355" y2="240" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="370" y="212" font-weight="bold" font-size="14" fill="var(--svg-green-accent)">L</text>
                    <!-- Formula -->
                    <rect x="120" y="340" width="200" height="26" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="220" y="358" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--svg-fg)">K = QL / (A&#x394;h)</text>
                </svg>
                <div class="figcaption">Figure 2.5c: Constant-head permeameter &#x2014; water flows through the soil sample under constant head difference. K is calculated from measured Q.</div>
            </div>'''

# ──────────────────────── FIGURE 2.5d ────────────────────────
REPLACEMENTS["Figure 2.5d:"] = '''<div class="figure-container">
                <svg width="460" height="370" viewBox="0 0 460 370" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="230" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Falling-Head Permeameter</text>
                    <!-- Standpipe -->
                    <rect x="145" y="45" width="18" height="140" fill="none" stroke="var(--svg-fg)" stroke-width="2"/>
                    <rect x="147" y="55" width="14" height="130" fill="var(--svg-water)" fill-opacity="0.3" stroke="none"/>
                    <!-- h1 level -->
                    <line x1="130" y1="60" x2="175" y2="60" stroke="var(--svg-red-accent)" stroke-width="2"/>
                    <text x="185" y="57" font-size="10" fill="var(--svg-red-accent)">h&#x2081; (t=0)</text>
                    <!-- h2 level -->
                    <line x1="130" y1="130" x2="175" y2="130" stroke="var(--svg-water-3)" stroke-width="1.5" stroke-dasharray="5,3"/>
                    <text x="185" y="127" font-size="10" fill="var(--svg-water-3)">h&#x2082; (t=t)</text>
                    <!-- Standpipe area label -->
                    <text x="115" y="100" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-accent)">a</text>
                    <!-- Main cylinder -->
                    <rect x="90" y="185" width="220" height="110" rx="6" fill="none" stroke="var(--svg-fg)" stroke-width="2"/>
                    <!-- Soil sample -->
                    <rect x="90" y="215" width="220" height="45" fill="url(#dots)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="200" y="242" text-anchor="middle" font-size="10" font-weight="bold" fill="var(--svg-fg)">Soil Sample (A, L)</text>
                    <!-- Connection pipe -->
                    <line x1="154" y1="185" x2="154" y2="215" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <!-- L label -->
                    <line x1="330" y1="215" x2="330" y2="260" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <line x1="324" y1="215" x2="336" y2="215" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <line x1="324" y1="260" x2="336" y2="260" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="348" y="242" font-weight="bold" font-size="13" fill="var(--svg-green-accent)">L</text>
                    <!-- Outlet -->
                    <line x1="200" y1="295" x2="200" y2="318" stroke="var(--svg-fg)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="200" y="332" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Outlet</text>
                    <!-- Formula -->
                    <rect x="85" y="345" width="290" height="22" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="230" y="361" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-fg)">K = (aL)/(At) &#xB7; ln(h&#x2081;/h&#x2082;)</text>
                </svg>
                <div class="figcaption">Figure 2.5d: Falling-head permeameter &#x2014; used for fine-grained soils. Head drops from h&#x2081; to h&#x2082; over time t.</div>
            </div>'''

# ──────────────────────── FIGURE 2.8 ────────────────────────
REPLACEMENTS["Figure 2.8:"] = '''<div class="figure-container">
                <svg width="700" height="370" viewBox="0 0 700 370" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="350" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Hydraulic Conductivity Range by Material Type</text>
                    <!-- Axes -->
                    <line x1="130" y1="42" x2="130" y2="310" stroke="var(--svg-fg)" stroke-width="2"/>
                    <line x1="130" y1="310" x2="660" y2="310" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="395" y="345" text-anchor="middle" font-size="12" fill="var(--svg-fg)">Material type (increasing grain size &#x2192;)</text>
                    <text x="55" y="180" text-anchor="middle" font-size="11" fill="var(--svg-fg)" transform="rotate(-90 55 180)">Hydraulic conductivity K (log scale)</text>
                    <!-- Y-axis labels -->
                    <text x="118" y="286" text-anchor="end" font-size="10" fill="var(--svg-fg)">10&#x207B;&#xB9;&#x2070;</text>
                    <text x="118" y="236" text-anchor="end" font-size="10" fill="var(--svg-fg)">10&#x207B;&#x2078;</text>
                    <text x="118" y="186" text-anchor="end" font-size="10" fill="var(--svg-fg)">10&#x207B;&#x2076;</text>
                    <text x="118" y="136" text-anchor="end" font-size="10" fill="var(--svg-fg)">10&#x207B;&#x2074;</text>
                    <text x="118" y="86" text-anchor="end" font-size="10" fill="var(--svg-fg)">10&#x207B;&#xB2;</text>
                    <!-- Bars with gradient fills -->
                    <rect x="160" y="258" width="70" height="48" rx="4" fill="var(--svg-red-lt)" stroke="var(--svg-red-accent)" stroke-width="1.5"/>
                    <rect x="260" y="225" width="70" height="82" rx="4" fill="var(--svg-orange-lt)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <rect x="360" y="172" width="70" height="135" rx="4" fill="var(--svg-yellow-lt)" stroke="var(--svg-orange-accent)" stroke-width="1.5"/>
                    <rect x="460" y="118" width="70" height="189" rx="4" fill="var(--svg-green-lt)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <rect x="560" y="72" width="70" height="235" rx="4" fill="var(--svg-water)" stroke="var(--svg-accent)" stroke-width="1.5" fill-opacity="0.4"/>
                    <!-- Bar labels -->
                    <text x="195" y="325" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">Clay</text>
                    <text x="295" y="325" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">Silt</text>
                    <text x="395" y="325" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">Fine sand</text>
                    <text x="495" y="325" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">Coarse sand</text>
                    <text x="595" y="325" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-fg)">Gravel</text>
                    <!-- Quality labels on bars -->
                    <text x="195" y="252" text-anchor="middle" font-size="9" fill="var(--svg-red-accent)">Very low</text>
                    <text x="295" y="219" text-anchor="middle" font-size="9" fill="var(--svg-orange-accent)">Low</text>
                    <text x="395" y="166" text-anchor="middle" font-size="9" fill="var(--svg-fg)">Moderate</text>
                    <text x="495" y="112" text-anchor="middle" font-size="9" fill="var(--svg-green-accent)">High</text>
                    <text x="595" y="66" text-anchor="middle" font-size="9" fill="var(--svg-accent)">Very high</text>
                </svg>
                <div class="figcaption">Figure 2.8: Typical hydraulic-conductivity range increases strongly as grain size and pore connectivity increase.</div>
            </div>'''

# ──────────────────────── FIGURE 2.9 ────────────────────────
REPLACEMENTS["Figure 2.9:"] = '''<div class="figure-container">
                <svg width="720" height="250" viewBox="0 0 720 250" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="360" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">k &#x2192; K &#x2192; T: Conceptual Distinction</text>
                    <!-- Box 1: k -->
                    <rect x="35" y="50" width="180" height="140" rx="10" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="125" y="75" text-anchor="middle" font-weight="bold" font-size="16" fill="var(--svg-accent)">k</text>
                    <text x="125" y="100" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Intrinsic Permeability</text>
                    <line x1="55" y1="110" x2="195" y2="110" stroke="var(--svg-fg)" stroke-width="0.5"/>
                    <text x="125" y="128" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Depends on pore</text>
                    <text x="125" y="143" text-anchor="middle" font-size="10" fill="var(--svg-fg)">geometry only</text>
                    <text x="125" y="165" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Independent of fluid</text>
                    <text x="125" y="182" text-anchor="middle" font-size="10" fill="var(--svg-muted)">[m&#xB2;]</text>
                    <!-- Arrow 1 -->
                    <line x1="222" y1="120" x2="268" y2="120" stroke="var(--svg-fg)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <text x="245" y="108" text-anchor="middle" font-size="9" font-style="italic" fill="var(--svg-fg)">&#xD7; &#x3C1;g/&#x3BC;</text>
                    <!-- Box 2: K -->
                    <rect x="275" y="50" width="180" height="140" rx="10" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="365" y="75" text-anchor="middle" font-weight="bold" font-size="16" fill="var(--svg-green-accent)">K</text>
                    <text x="365" y="100" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Hydraulic Conductivity</text>
                    <line x1="295" y1="110" x2="435" y2="110" stroke="var(--svg-fg)" stroke-width="0.5"/>
                    <text x="365" y="128" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Depends on medium</text>
                    <text x="365" y="143" text-anchor="middle" font-size="10" fill="var(--svg-fg)">AND fluid</text>
                    <text x="365" y="165" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Flux per unit gradient</text>
                    <text x="365" y="182" text-anchor="middle" font-size="10" fill="var(--svg-muted)">[m/s]</text>
                    <!-- Arrow 2 -->
                    <line x1="462" y1="120" x2="508" y2="120" stroke="var(--svg-fg)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <text x="485" y="108" text-anchor="middle" font-size="9" font-style="italic" fill="var(--svg-fg)">&#xD7; b</text>
                    <!-- Box 3: T -->
                    <rect x="515" y="50" width="180" height="140" rx="10" fill="var(--svg-bg-soft)" stroke="var(--svg-orange-accent)" stroke-width="2"/>
                    <text x="605" y="75" text-anchor="middle" font-weight="bold" font-size="16" fill="var(--svg-orange-accent)">T</text>
                    <text x="605" y="100" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Transmissivity</text>
                    <line x1="535" y1="110" x2="675" y2="110" stroke="var(--svg-fg)" stroke-width="0.5"/>
                    <text x="605" y="128" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Whole aquifer</text>
                    <text x="605" y="143" text-anchor="middle" font-size="10" fill="var(--svg-fg)">thickness effect</text>
                    <text x="605" y="165" text-anchor="middle" font-size="10" fill="var(--svg-muted)">T = Kb</text>
                    <text x="605" y="182" text-anchor="middle" font-size="10" fill="var(--svg-muted)">[m&#xB2;/s]</text>
                    <!-- Bottom summary -->
                    <rect x="130" y="210" width="460" height="28" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="360" y="229" text-anchor="middle" font-size="11" fill="var(--svg-fg)">k = medium only &#x2192; K = medium + fluid &#x2192; T = K &#xD7; saturated thickness</text>
                </svg>
                <div class="figcaption">Figure 2.9: Conceptual distinction between intrinsic permeability, hydraulic conductivity, and transmissivity.</div>
            </div>'''

# ──────────────────────── FIGURE 2.10 ────────────────────────
REPLACEMENTS["Figure 2.10:"] = '''<div class="figure-container">
                <svg width="720" height="310" viewBox="0 0 720 310" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="360" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Anisotropy in Layered Deposits</text>
                    <!-- LEFT: Layered deposit -->
                    <rect x="60" y="55" width="270" height="175" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="195" y="48" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-fg)">Layered Deposit</text>
                    <!-- Layers -->
                    <rect x="62" y="57" width="266" height="40" fill="var(--svg-water)" fill-opacity="0.2" stroke="var(--svg-fg)" stroke-width="0.5"/>
                    <text x="195" y="82" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Fine sand (K&#x2081;)</text>
                    <rect x="62" y="97" width="266" height="45" fill="var(--svg-green-lt)" fill-opacity="0.4" stroke="var(--svg-fg)" stroke-width="0.5"/>
                    <text x="195" y="125" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Silty sand (K&#x2082;)</text>
                    <rect x="62" y="142" width="266" height="40" fill="var(--svg-water)" fill-opacity="0.2" stroke="var(--svg-fg)" stroke-width="0.5"/>
                    <text x="195" y="167" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Fine sand (K&#x2083;)</text>
                    <rect x="62" y="182" width="266" height="46" fill="var(--svg-yellow-lt)" fill-opacity="0.4" stroke="var(--svg-fg)" stroke-width="0.5"/>
                    <text x="195" y="210" text-anchor="middle" font-size="10" fill="var(--svg-fg)">Clayey silt (K&#x2084;)</text>
                    <!-- Kh arrow -->
                    <line x1="100" y1="140" x2="280" y2="140" stroke="var(--svg-accent)" stroke-width="3" marker-end="url(#arr)"/>
                    <text x="190" y="134" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-accent)">K&#x2095; large</text>
                    <!-- Kv arrow -->
                    <line x1="320" y1="220" x2="320" y2="65" stroke="var(--svg-green-accent)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="338" y="145" font-size="10" font-weight="bold" fill="var(--svg-green-accent)">K&#x1D65; small</text>

                    <!-- RIGHT: Conductivity ellipse -->
                    <rect x="400" y="55" width="280" height="175" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="2"/>
                    <text x="540" y="48" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-fg)">Conductivity Ellipse</text>
                    <ellipse cx="540" cy="142" rx="110" ry="55" fill="none" stroke="var(--svg-accent)" stroke-width="2.5"/>
                    <!-- Kh direction -->
                    <line x1="540" y1="142" x2="645" y2="142" stroke="var(--svg-accent)" stroke-width="2.5" marker-end="url(#arr)"/>
                    <text x="652" y="138" font-size="11" font-weight="bold" fill="var(--svg-accent)">K&#x2095;</text>
                    <!-- Kv direction -->
                    <line x1="540" y1="142" x2="540" y2="92" stroke="var(--svg-green-accent)" stroke-width="2" marker-end="url(#arr)"/>
                    <text x="550" y="82" font-size="11" font-weight="bold" fill="var(--svg-green-accent)">K&#x1D65;</text>
                    <!-- Axes -->
                    <line x1="430" y1="142" x2="650" y2="142" stroke="var(--svg-fg)" stroke-width="0.5" stroke-dasharray="4,3"/>
                    <line x1="540" y1="65" x2="540" y2="220" stroke="var(--svg-fg)" stroke-width="0.5" stroke-dasharray="4,3"/>

                    <!-- Bottom label -->
                    <rect x="120" y="260" width="480" height="40" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="360" y="278" text-anchor="middle" font-size="11" fill="var(--svg-fg)">K&#x2095; &gt; K&#x1D65; in stratified sediments</text>
                    <text x="360" y="295" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Horizontal flow favors most permeable layer; vertical limited by least permeable</text>
                </svg>
                <div class="figcaption">Figure 2.10: Anisotropy commonly develops in layered deposits because horizontal flow encounters less resistance than vertical flow across bedding.</div>
            </div>'''

# ──────────────────────── FIGURE 2.10b ────────────────────────
REPLACEMENTS["Figure 2.10b:"] = '''<div class="figure-container">
                <svg width="680" height="320" viewBox="0 0 680 320" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="340" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">Equivalent K for Layered Systems</text>
                    <!-- LEFT: Parallel flow -->
                    <rect x="20" y="40" width="300" height="200" rx="10" fill="var(--svg-bg-soft)" stroke="var(--svg-accent)" stroke-width="2"/>
                    <text x="170" y="60" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-accent)">Flow PARALLEL to Layers</text>
                    <rect x="50" y="75" width="240" height="30" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="1" fill-opacity="0.3"/>
                    <text x="170" y="95" text-anchor="middle" font-size="10" fill="var(--svg-fg)">K&#x2081;, b&#x2081;</text>
                    <rect x="50" y="105" width="240" height="40" fill="var(--svg-green-lt)" stroke="var(--svg-fg)" stroke-width="1" fill-opacity="0.5"/>
                    <text x="170" y="130" text-anchor="middle" font-size="10" fill="var(--svg-fg)">K&#x2082;, b&#x2082;</text>
                    <rect x="50" y="145" width="240" height="25" fill="var(--svg-yellow-lt)" stroke="var(--svg-fg)" stroke-width="1" fill-opacity="0.5"/>
                    <text x="170" y="162" text-anchor="middle" font-size="10" fill="var(--svg-fg)">K&#x2083;, b&#x2083;</text>
                    <line x1="30" y1="118" x2="50" y2="118" stroke="var(--svg-accent)" stroke-width="3" marker-end="url(#arr)"/>
                    <text x="170" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-accent)">K&#x2095; = &#x2211;(K&#x1D62;b&#x1D62;)/&#x2211;b&#x1D62;</text>
                    <text x="170" y="215" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Weighted arithmetic mean</text>
                    <!-- RIGHT: Perpendicular flow -->
                    <rect x="360" y="40" width="300" height="200" rx="10" fill="var(--svg-bg-soft)" stroke="var(--svg-green-accent)" stroke-width="2"/>
                    <text x="510" y="60" text-anchor="middle" font-weight="bold" font-size="12" fill="var(--svg-green-accent)">Flow PERPENDICULAR to Layers</text>
                    <rect x="390" y="75" width="240" height="30" fill="var(--svg-water)" stroke="var(--svg-fg)" stroke-width="1" fill-opacity="0.3"/>
                    <text x="510" y="95" text-anchor="middle" font-size="10" fill="var(--svg-fg)">K&#x2081;, b&#x2081;</text>
                    <rect x="390" y="105" width="240" height="40" fill="var(--svg-green-lt)" stroke="var(--svg-fg)" stroke-width="1" fill-opacity="0.5"/>
                    <text x="510" y="130" text-anchor="middle" font-size="10" fill="var(--svg-fg)">K&#x2082;, b&#x2082;</text>
                    <rect x="390" y="145" width="240" height="25" fill="var(--svg-yellow-lt)" stroke="var(--svg-fg)" stroke-width="1" fill-opacity="0.5"/>
                    <text x="510" y="162" text-anchor="middle" font-size="10" fill="var(--svg-fg)">K&#x2083;, b&#x2083;</text>
                    <line x1="510" y1="55" x2="510" y2="75" stroke="var(--svg-green-accent)" stroke-width="3" marker-end="url(#arr)"/>
                    <text x="510" y="195" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-green-accent)">K&#x1D65; = &#x2211;b&#x1D62;/&#x2211;(b&#x1D62;/K&#x1D62;)</text>
                    <text x="510" y="215" text-anchor="middle" font-size="9" fill="var(--svg-muted)">Weighted harmonic mean</text>
                    <!-- Bottom key result -->
                    <rect x="140" y="260" width="400" height="48" rx="8" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="340" y="282" text-anchor="middle" font-size="13" font-weight="bold" fill="var(--svg-fg)">Always: K&#x2095; &#x2265; K&#x1D65;</text>
                    <text x="340" y="300" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Anisotropy ratio K&#x2095;/K&#x1D65; = 2 to 100+ in sedimentary deposits</text>
                </svg>
                <div class="figcaption">Figure 2.10b: Equivalent hydraulic conductivity &#x2014; arithmetic mean for parallel flow, harmonic mean for perpendicular flow. K_h is always &#x2265; K_v.</div>
            </div>'''

# ──────────────────────── FIGURE 2.10c ────────────────────────
REPLACEMENTS["Figure 2.10c:"] = '''<div class="figure-container">
                <svg width="580" height="260" viewBox="0 0 580 260" xmlns="http://www.w3.org/2000/svg" style="font-family:'Times New Roman',Times,serif">
                    <text x="290" y="22" text-anchor="middle" font-weight="bold" font-size="14" fill="var(--svg-fg)">3D Generalization of Darcy&#x2019;s Law &#x2014; K Tensor</text>
                    <text x="150" y="55" text-anchor="middle" font-size="12" fill="var(--svg-fg)">Anisotropic medium:</text>
                    <!-- Matrix display -->
                    <rect x="80" y="68" width="280" height="90" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1.5"/>
                    <text x="68" y="115" text-anchor="end" font-size="14" font-weight="bold" fill="var(--svg-fg)">q = &#x2212;</text>
                    <!-- Row 1 -->
                    <text x="125" y="95" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-accent)">K&#x2093;&#x2093;</text>
                    <text x="200" y="95" text-anchor="middle" font-size="12" fill="var(--svg-dim)">K&#x2093;&#x2099;</text>
                    <text x="275" y="95" text-anchor="middle" font-size="12" fill="var(--svg-dim)">K&#x2093;&#x1D6A;</text>
                    <!-- Row 2 -->
                    <text x="125" y="118" text-anchor="middle" font-size="12" fill="var(--svg-dim)">K&#x2099;&#x2093;</text>
                    <text x="200" y="118" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-accent)">K&#x2099;&#x2099;</text>
                    <text x="275" y="118" text-anchor="middle" font-size="12" fill="var(--svg-dim)">K&#x2099;&#x1D6A;</text>
                    <!-- Row 3 -->
                    <text x="125" y="141" text-anchor="middle" font-size="12" fill="var(--svg-dim)">K&#x1D6A;&#x2093;</text>
                    <text x="200" y="141" text-anchor="middle" font-size="12" fill="var(--svg-dim)">K&#x1D6A;&#x2099;</text>
                    <text x="275" y="141" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-accent)">K&#x1D6A;&#x1D6A;</text>
                    <!-- grad h -->
                    <text x="375" y="115" text-anchor="middle" font-size="14" font-weight="bold" fill="var(--svg-fg)">&#x2207;h</text>
                    <!-- Right side: isotropic simplification -->
                    <rect x="420" y="68" width="145" height="90" rx="6" fill="var(--svg-green-lt)" stroke="var(--svg-green-accent)" stroke-width="1.5"/>
                    <text x="492" y="88" text-anchor="middle" font-size="11" font-weight="bold" fill="var(--svg-green-accent)">Isotropic:</text>
                    <text x="492" y="112" text-anchor="middle" font-size="12" fill="var(--svg-fg)">K&#x2093;&#x2093; = K&#x2099;&#x2099; = K&#x1D6A;&#x1D6A; = K</text>
                    <text x="492" y="132" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Off-diag = 0</text>
                    <text x="492" y="150" text-anchor="middle" font-size="12" font-weight="bold" fill="var(--svg-green-accent)">q = &#x2212;K&#x2207;h</text>
                    <!-- Bottom note -->
                    <rect x="80" y="175" width="420" height="38" rx="6" fill="var(--svg-bg-soft)" stroke="var(--svg-fg)" stroke-width="1"/>
                    <text x="290" y="193" text-anchor="middle" font-size="11" fill="var(--svg-fg)">Diagonal terms = principal conductivities</text>
                    <text x="290" y="208" text-anchor="middle" font-size="10" fill="var(--svg-muted)">Off-diagonal terms vanish when axes align with principal directions</text>
                    <text x="290" y="242" text-anchor="middle" font-size="11" font-style="italic" fill="var(--svg-fg)">Most groundwater problems assume K&#x2093;&#x2093; &#x2260; K&#x1D6A;&#x1D6A; (2D anisotropy) with K&#x2093;&#x2099; = 0</text>
                </svg>
                <div class="figcaption">Figure 2.10c: In fully anisotropic media, Darcy&#x2019;s law requires a 3&#xD7;3 conductivity tensor. For isotropic media it reduces to a scalar K.</div>
            </div>'''


# ─────────── Now perform all replacements ───────────
def replace_figure(html_content, figcaption_key, new_html):
    """Replace the <div class="figure-container">..figcaption_key..</div> block."""
    # Find the figcaption
    idx = html_content.find(figcaption_key)
    if idx == -1:
        print(f"  WARNING: '{figcaption_key}' not found!")
        return html_content
    
    # Find the closing </div> of figcaption, then closing </div> of figure-container
    end_figcaption = html_content.find('</div>', idx)
    end_container = html_content.find('</div>', end_figcaption + 6)
    if end_container == -1:
        # Sometimes the </div> for figcaption IS the container close
        end_container = end_figcaption
    end_pos = end_container + len('</div>')
    
    # Find the start: search backward for <div class="figure-container">
    search_start = html_content.rfind('<div class="figure-container">', 0, idx)
    if search_start == -1:
        print(f"  WARNING: Could not find figure-container start for '{figcaption_key}'!")
        return html_content
    
    old_block = html_content[search_start:end_pos]
    print(f"  Replacing '{figcaption_key}' ({len(old_block)} chars)")
    return html_content[:search_start] + new_html + html_content[end_pos:]


count = 0
for key, new_html in REPLACEMENTS.items():
    old_len = len(html)
    html = replace_figure(html, key, new_html)
    if len(html) != old_len:
        count += 1

with open(FILE, "w", encoding="utf-8") as f:
    f.write(html)

print(f"\nDone! Replaced {count}/{len(REPLACEMENTS)} figures.")

"""
Add 5-8 new SVG figures to each chapter (7-12) at their correct inline positions.
Each figure uses <div class="figure"><figure> wrapper consistent with existing bottom-placed figures.
"""
import re, os

BASE = r"d:\Final Year\gis and remote sensing\sa"

# ──────────────────── HELPER ────────────────────
def insert_before(content, anchor, figure_html):
    """Insert figure HTML before the first occurrence of anchor text."""
    idx = content.find(anchor)
    if idx == -1:
        print(f"    WARNING: anchor not found: {anchor[:60]}")
        return content
    before = content[:idx].rstrip('\n')
    after = content[idx:]
    return before + '\n\n' + figure_html + '\n\n    ' + after

def insert_after(content, anchor, figure_html):
    """Insert figure HTML after the first occurrence of anchor text."""
    idx = content.find(anchor)
    if idx == -1:
        print(f"    WARNING: anchor not found: {anchor[:60]}")
        return content
    end = idx + len(anchor)
    before = content[:end]
    after = content[end:].lstrip('\n')
    return before + '\n\n' + figure_html + '\n\n' + after

# ──────────────────── CHAPTER 7 ────────────────────
def fix_ch7():
    path = os.path.join(BASE, "chapter7.html")
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()

    # Fig 7.11 – Interpolation Workflow (Points → DEM)
    # Insert after: "creating a solid, continuous topographic surface from isolated data.</p>"
    fig_7_11 = '''    <div class="figure">
      <figure>
        <svg viewBox="0 0 700 140" xmlns="http://www.w3.org/2000/svg" style="max-width:700px">
          <defs><filter id="f711"><feDropShadow dx="1" dy="1.5" stdDeviation="1.5" flood-opacity=".12"/></filter></defs>
          <text x="350" y="16" text-anchor="middle" font-size="11" font-weight="bold" fill="#1a3c5e">From Scattered Points to Continuous DEM Surface</text>
          <!-- Step 1: Survey Points -->
          <g filter="url(#f711)"><rect x="15" y="28" width="190" height="100" rx="8" fill="#e8f4fd" stroke="#1a3c5e" stroke-width="1.2"/>
          <text x="110" y="46" text-anchor="middle" font-size="9" font-weight="bold" fill="#1a3c5e">1. Scattered Survey Points</text>
          <circle cx="50" cy="62" r="4" fill="#1a3c5e"/><text x="50" y="76" text-anchor="middle" font-size="6" fill="#555">820m</text>
          <circle cx="100" cy="70" r="4" fill="#1a3c5e"/><text x="100" y="84" text-anchor="middle" font-size="6" fill="#555">785m</text>
          <circle cx="145" cy="58" r="4" fill="#1a3c5e"/><text x="145" y="72" text-anchor="middle" font-size="6" fill="#555">910m</text>
          <circle cx="75" cy="100" r="4" fill="#1a3c5e"/><text x="75" y="114" text-anchor="middle" font-size="6" fill="#555">750m</text>
          <circle cx="170" cy="95" r="4" fill="#1a3c5e"/><text x="170" y="109" text-anchor="middle" font-size="6" fill="#555">860m</text>
          <text x="110" y="126" text-anchor="middle" font-size="7" fill="#888" font-style="italic">GPS / LiDAR / Survey</text></g>
          <!-- Arrow 1 -->
          <polygon points="215,78 235,70 235,74 260,74 260,82 235,82 235,86" fill="#b8860b"/>
          <text x="238" y="66" font-size="7" fill="#b8860b" font-weight="bold">Interpolation</text>
          <!-- Step 2: Algorithm -->
          <g filter="url(#f711)"><rect x="265" y="28" width="160" height="100" rx="8" fill="#fff5ec" stroke="#b8860b" stroke-width="1.2"/>
          <text x="345" y="46" text-anchor="middle" font-size="9" font-weight="bold" fill="#b8860b">2. Algorithm Fills Gaps</text>
          <text x="345" y="66" text-anchor="middle" font-size="8" fill="#555">IDW / Spline / Kriging</text>
          <text x="345" y="82" text-anchor="middle" font-size="20" fill="#b8860b">&#x2234;</text>
          <text x="345" y="106" text-anchor="middle" font-size="7.5" fill="#555">Estimates unknown</text>
          <text x="345" y="118" text-anchor="middle" font-size="7.5" fill="#555">values between points</text></g>
          <!-- Arrow 2 -->
          <polygon points="435,78 455,70 455,74 480,74 480,82 455,82 455,86" fill="#2d7d46"/>
          <text x="458" y="66" font-size="7" fill="#2d7d46" font-weight="bold">Output</text>
          <!-- Step 3: DEM -->
          <g filter="url(#f711)"><rect x="485" y="28" width="200" height="100" rx="8" fill="#edf7f0" stroke="#2d7d46" stroke-width="1.2"/>
          <text x="585" y="46" text-anchor="middle" font-size="9" font-weight="bold" fill="#2d7d46">3. Continuous Raster DEM</text>
          <g transform="translate(500,52)">
            <rect x="0" y="0" width="22" height="16" fill="#2a6e2a" stroke="#fff" stroke-width=".5"/><text x="11" y="12" text-anchor="middle" font-size="6" fill="#fff">910</text>
            <rect x="22" y="0" width="22" height="16" fill="#3a8e3a" stroke="#fff" stroke-width=".5"/><text x="33" y="12" text-anchor="middle" font-size="6" fill="#fff">880</text>
            <rect x="44" y="0" width="22" height="16" fill="#4aae4a" stroke="#fff" stroke-width=".5"/><text x="55" y="12" text-anchor="middle" font-size="6" fill="#fff">855</text>
            <rect x="66" y="0" width="22" height="16" fill="#5ac85a" stroke="#fff" stroke-width=".5"/><text x="77" y="12" text-anchor="middle" font-size="6" fill="#fff">830</text>
            <rect x="88" y="0" width="22" height="16" fill="#6ae06a" stroke="#fff" stroke-width=".5"/><text x="99" y="12" text-anchor="middle" font-size="6">820</text>
            <rect x="0" y="16" width="22" height="16" fill="#3a8e3a" stroke="#fff" stroke-width=".5"/><text x="11" y="28" text-anchor="middle" font-size="6" fill="#fff">870</text>
            <rect x="22" y="16" width="22" height="16" fill="#5aae5a" stroke="#fff" stroke-width=".5"/><text x="33" y="28" text-anchor="middle" font-size="6">845</text>
            <rect x="44" y="16" width="22" height="16" fill="#7ac87a" stroke="#fff" stroke-width=".5"/><text x="55" y="28" text-anchor="middle" font-size="6">810</text>
            <rect x="66" y="16" width="22" height="16" fill="#90d890" stroke="#fff" stroke-width=".5"/><text x="77" y="28" text-anchor="middle" font-size="6">785</text>
            <rect x="88" y="16" width="22" height="16" fill="#a8e8a8" stroke="#fff" stroke-width=".5"/><text x="99" y="28" text-anchor="middle" font-size="6">760</text>
            <rect x="0" y="32" width="22" height="16" fill="#5aae5a" stroke="#fff" stroke-width=".5"/><text x="11" y="44" text-anchor="middle" font-size="6">840</text>
            <rect x="22" y="32" width="22" height="16" fill="#7ac87a" stroke="#fff" stroke-width=".5"/><text x="33" y="44" text-anchor="middle" font-size="6">800</text>
            <rect x="44" y="32" width="22" height="16" fill="#a0d468" stroke="#fff" stroke-width=".5"/><text x="55" y="44" text-anchor="middle" font-size="6">775</text>
            <rect x="66" y="32" width="22" height="16" fill="#b8e888" stroke="#fff" stroke-width=".5"/><text x="77" y="44" text-anchor="middle" font-size="6">755</text>
            <rect x="88" y="32" width="22" height="16" fill="#d0f0a8" stroke="#fff" stroke-width=".5"/><text x="99" y="44" text-anchor="middle" font-size="6">750</text>
          </g>
          <text x="585" y="120" text-anchor="middle" font-size="7" fill="#2d7d46" font-weight="bold">Every pixel has elevation</text></g>
        </svg>
        <figcaption>Fig 7.11 &ndash; Interpolation workflow: scattered survey points are processed by an algorithm to produce a continuous raster DEM where every pixel holds an elevation value</figcaption>
      </figure>
    </div>'''
    c = insert_after(c, "creating a solid, continuous topographic surface from isolated data.</p>", fig_7_11)

    # Fig 7.12 – Engineering Applications Hub
    fig_7_12 = '''    <div class="figure">
      <figure>
        <svg viewBox="0 0 600 220" xmlns="http://www.w3.org/2000/svg" style="max-width:600px">
          <defs><filter id="f712"><feDropShadow dx="1" dy="1.5" stdDeviation="1.5" flood-opacity=".12"/></filter></defs>
          <text x="300" y="16" text-anchor="middle" font-size="11" font-weight="bold" fill="#1a3c5e">Spatial Interpolation in Engineering Fields</text>
          <!-- Central node -->
          <circle cx="300" cy="115" r="38" fill="#1a3c5e" filter="url(#f712)"/>
          <text x="300" y="110" text-anchor="middle" font-size="8" fill="#fff" font-weight="bold">Spatial</text>
          <text x="300" y="122" text-anchor="middle" font-size="8" fill="#fff" font-weight="bold">Interpolation</text>
          <!-- Hydrology -->
          <line x1="262" y1="100" x2="120" y2="55" stroke="#1a3c5e" stroke-width="1.2"/>
          <g filter="url(#f712)"><rect x="20" y="30" width="200" height="50" rx="8" fill="#e8f4fd" stroke="#1a3c5e" stroke-width="1"/>
          <text x="120" y="48" text-anchor="middle" font-size="9" font-weight="bold" fill="#1a3c5e">&#x1F4A7; Hydrology</text>
          <text x="120" y="62" text-anchor="middle" font-size="7" fill="#555">Rainfall surface from weather stations</text>
          <text x="120" y="73" text-anchor="middle" font-size="7" fill="#888" font-style="italic">Method: IDW / Kriging</text></g>
          <!-- Geotechnical -->
          <line x1="338" y1="100" x2="480" y2="55" stroke="#8b2500" stroke-width="1.2"/>
          <g filter="url(#f712)"><rect x="380" y="30" width="200" height="50" rx="8" fill="#fdf0ec" stroke="#8b2500" stroke-width="1"/>
          <text x="480" y="48" text-anchor="middle" font-size="9" font-weight="bold" fill="#8b2500">&#x1F3D7; Geotechnical</text>
          <text x="480" y="62" text-anchor="middle" font-size="7" fill="#555">Vs30 map from borehole logs</text>
          <text x="480" y="73" text-anchor="middle" font-size="7" fill="#888" font-style="italic">Method: Kriging (with error map)</text></g>
          <!-- Water Resources -->
          <line x1="262" y1="130" x2="120" y2="175" stroke="#2d7d46" stroke-width="1.2"/>
          <g filter="url(#f712)"><rect x="20" y="150" width="200" height="50" rx="8" fill="#edf7f0" stroke="#2d7d46" stroke-width="1"/>
          <text x="120" y="168" text-anchor="middle" font-size="9" font-weight="bold" fill="#2d7d46">&#x1F30A; Water Resources</text>
          <text x="120" y="182" text-anchor="middle" font-size="7" fill="#555">Riverbed bathymetry for HEC-RAS</text>
          <text x="120" y="193" text-anchor="middle" font-size="7" fill="#888" font-style="italic">Method: Spline / TIN</text></g>
          <!-- Environmental -->
          <line x1="338" y1="130" x2="480" y2="175" stroke="#6c4f9e" stroke-width="1.2"/>
          <g filter="url(#f712)"><rect x="380" y="150" width="200" height="50" rx="8" fill="#f5f0ff" stroke="#6c4f9e" stroke-width="1"/>
          <text x="480" y="168" text-anchor="middle" font-size="9" font-weight="bold" fill="#6c4f9e">&#x1F32B; Environmental</text>
          <text x="480" y="182" text-anchor="middle" font-size="7" fill="#555">Pollution plume from monitoring wells</text>
          <text x="480" y="193" text-anchor="middle" font-size="7" fill="#888" font-style="italic">Method: IDW / Kriging</text></g>
        </svg>
        <figcaption>Fig 7.12 &ndash; Spatial interpolation applications across four engineering disciplines, each with the most suitable interpolation method</figcaption>
      </figure>
    </div>'''
    c = insert_before(c, "<!-- Part 5: The Numerical Question -->", fig_7_12)

    # Fig 7.13 – Raster vs Vector Comparison
    fig_7_13 = '''    <div class="figure">
      <figure>
        <svg viewBox="0 0 650 200" xmlns="http://www.w3.org/2000/svg" style="max-width:650px">
          <text x="325" y="16" text-anchor="middle" font-size="11" font-weight="bold" fill="#1a3c5e">Raster vs Vector: Key Differences</text>
          <!-- Headers -->
          <rect x="20" y="28" width="130" height="24" rx="4" fill="#1a3c5e"/><text x="85" y="45" text-anchor="middle" font-size="8" fill="#fff" font-weight="bold">Property</text>
          <rect x="155" y="28" width="230" height="24" rx="4" fill="#2d7d46"/><text x="270" y="45" text-anchor="middle" font-size="8" fill="#fff" font-weight="bold">RASTER (Grid Cells)</text>
          <rect x="390" y="28" width="240" height="24" rx="4" fill="#8b2500"/><text x="510" y="45" text-anchor="middle" font-size="8" fill="#fff" font-weight="bold">VECTOR (Points/Lines/Polygons)</text>
          <!-- Rows -->
          <rect x="20" y="56" width="610" height="22" rx="2" fill="#f5f0e8"/>
          <text x="85" y="71" text-anchor="middle" font-size="7.5" fill="#333" font-weight="bold">Data Structure</text>
          <text x="270" y="71" text-anchor="middle" font-size="7.5" fill="#555">Regular grid of equal-sized pixels</text>
          <text x="510" y="71" text-anchor="middle" font-size="7.5" fill="#555">Coordinate-based geometry (x,y)</text>
          <rect x="20" y="82" width="610" height="22" rx="2" fill="#fff"/>
          <text x="85" y="97" text-anchor="middle" font-size="7.5" fill="#333" font-weight="bold">Best For</text>
          <text x="270" y="97" text-anchor="middle" font-size="7.5" fill="#2d7d46">Continuous surfaces (DEM, rainfall)</text>
          <text x="510" y="97" text-anchor="middle" font-size="7.5" fill="#8b2500">Discrete features (roads, parcels)</text>
          <rect x="20" y="108" width="610" height="22" rx="2" fill="#f5f0e8"/>
          <text x="85" y="123" text-anchor="middle" font-size="7.5" fill="#333" font-weight="bold">Overlay Method</text>
          <text x="270" y="123" text-anchor="middle" font-size="7.5" fill="#555">Pixel-by-pixel Map Algebra</text>
          <text x="510" y="123" text-anchor="middle" font-size="7.5" fill="#555">Geometric intersection (Clip/Union)</text>
          <rect x="20" y="134" width="610" height="22" rx="2" fill="#fff"/>
          <text x="85" y="149" text-anchor="middle" font-size="7.5" fill="#333" font-weight="bold">Boundary Precision</text>
          <text x="270" y="149" text-anchor="middle" font-size="7.5" fill="#8b2500">&#x2717; Pixelated stair-step edges</text>
          <text x="510" y="149" text-anchor="middle" font-size="7.5" fill="#2d7d46">&#x2713; Crisp, exact boundaries</text>
          <rect x="20" y="160" width="610" height="22" rx="2" fill="#f5f0e8"/>
          <text x="85" y="175" text-anchor="middle" font-size="7.5" fill="#333" font-weight="bold">File Size</text>
          <text x="270" y="175" text-anchor="middle" font-size="7.5" fill="#8b2500">&#x2717; Large at high resolution</text>
          <text x="510" y="175" text-anchor="middle" font-size="7.5" fill="#2d7d46">&#x2713; Compact for sparse features</text>
          <rect x="20" y="186" width="610" height="22" rx="2" fill="#fff"/>
          <text x="85" y="201" text-anchor="middle" font-size="7.5" fill="#333" font-weight="bold">Network Analysis</text>
          <text x="270" y="201" text-anchor="middle" font-size="7.5" fill="#8b2500">&#x2717; Inefficient</text>
          <text x="510" y="201" text-anchor="middle" font-size="7.5" fill="#2d7d46">&#x2713; Natural fit (topology)</text>
        </svg>
        <figcaption>Fig 7.13 &ndash; Raster vs Vector comparison: raster excels at continuous surfaces, vector at discrete features and networks</figcaption>
      </figure>
    </div>'''
    c = insert_before(c, "<h4>2. Map Overlay vs. Map Calculations</h4>", fig_7_13)

    # Fig 7.14 – Map Overlay vs Map Algebra
    fig_7_14 = '''    <div class="figure">
      <figure>
        <svg viewBox="0 0 680 175" xmlns="http://www.w3.org/2000/svg" style="max-width:680px">
          <text x="340" y="16" text-anchor="middle" font-size="11" font-weight="bold" fill="#1a3c5e">Map Overlay (Vector) vs Map Algebra (Raster)</text>
          <!-- Left: Vector Overlay -->
          <rect x="15" y="28" width="310" height="135" rx="8" fill="#fdf0ec" stroke="#8b2500" stroke-width="1"/>
          <text x="170" y="46" text-anchor="middle" font-size="9" font-weight="bold" fill="#8b2500">Vector Overlay (Intersect)</text>
          <!-- Input polygons -->
          <rect x="30" y="58" width="55" height="45" rx="4" fill="#8b2500" opacity=".15" stroke="#8b2500" stroke-width=".8"/>
          <text x="57" y="85" text-anchor="middle" font-size="7" fill="#8b2500">Land Use</text>
          <text x="100" y="82" font-size="14" fill="#8b2500">&#x2229;</text>
          <rect x="112" y="58" width="55" height="45" rx="4" fill="#1a3c5e" opacity=".15" stroke="#1a3c5e" stroke-width=".8"/>
          <text x="139" y="85" text-anchor="middle" font-size="7" fill="#1a3c5e">Flood Zone</text>
          <text x="180" y="82" font-size="14" fill="#333">&#x2192;</text>
          <!-- Output: new geometry -->
          <g transform="translate(195,58)">
            <rect x="0" y="0" width="55" height="45" rx="4" fill="#fff" stroke="#333" stroke-width=".8"/>
            <path d="M5,20 L25,5 L50,15 L45,40 L15,40 Z" fill="#b8860b" opacity=".3" stroke="#b8860b" stroke-width=".8"/>
          </g>
          <text x="222" y="115" text-anchor="middle" font-size="7" fill="#b8860b" font-weight="bold">New geometry</text>
          <text x="170" y="135" text-anchor="middle" font-size="7" fill="#8b2500">Creates new polygon shapes</text>
          <text x="170" y="148" text-anchor="middle" font-size="7" fill="#8b2500">by cutting boundaries</text>
          <!-- Right: Raster Map Algebra -->
          <rect x="355" y="28" width="310" height="135" rx="8" fill="#edf7f0" stroke="#2d7d46" stroke-width="1"/>
          <text x="510" y="46" text-anchor="middle" font-size="9" font-weight="bold" fill="#2d7d46">Raster Map Algebra (Add)</text>
          <!-- Input grids -->
          <g transform="translate(370,55)">
            <rect x="0" y="0" width="18" height="14" fill="#5aae5a" stroke="#fff" stroke-width=".4"/><text x="9" y="11" text-anchor="middle" font-size="5" fill="#fff">10</text>
            <rect x="18" y="0" width="18" height="14" fill="#7ac87a" stroke="#fff" stroke-width=".4"/><text x="27" y="11" text-anchor="middle" font-size="5">5</text>
            <rect x="0" y="14" width="18" height="14" fill="#a0d468" stroke="#fff" stroke-width=".4"/><text x="9" y="25" text-anchor="middle" font-size="5">3</text>
            <rect x="18" y="14" width="18" height="14" fill="#c0e8a0" stroke="#fff" stroke-width=".4"/><text x="27" y="25" text-anchor="middle" font-size="5">8</text>
          </g>
          <text x="413" y="95" text-anchor="middle" font-size="6" fill="#555">Jan Rain</text>
          <text x="428" y="72" font-size="14" fill="#2d7d46">+</text>
          <g transform="translate(445,55)">
            <rect x="0" y="0" width="18" height="14" fill="#4488cc" stroke="#fff" stroke-width=".4"/><text x="9" y="11" text-anchor="middle" font-size="5" fill="#fff">12</text>
            <rect x="18" y="0" width="18" height="14" fill="#6699dd" stroke="#fff" stroke-width=".4"/><text x="27" y="11" text-anchor="middle" font-size="5" fill="#fff">7</text>
            <rect x="0" y="14" width="18" height="14" fill="#88aaee" stroke="#fff" stroke-width=".4"/><text x="9" y="25" text-anchor="middle" font-size="5">4</text>
            <rect x="18" y="14" width="18" height="14" fill="#aaccff" stroke="#fff" stroke-width=".4"/><text x="27" y="25" text-anchor="middle" font-size="5">9</text>
          </g>
          <text x="488" y="95" text-anchor="middle" font-size="6" fill="#555">Feb Rain</text>
          <text x="503" y="72" font-size="14" fill="#333">&#x2192;</text>
          <g transform="translate(520,55)">
            <rect x="0" y="0" width="18" height="14" fill="#b8860b" stroke="#fff" stroke-width=".4"/><text x="9" y="11" text-anchor="middle" font-size="5" fill="#fff">22</text>
            <rect x="18" y="0" width="18" height="14" fill="#c8960b" stroke="#fff" stroke-width=".4"/><text x="27" y="11" text-anchor="middle" font-size="5" fill="#fff">12</text>
            <rect x="0" y="14" width="18" height="14" fill="#d8a60b" stroke="#fff" stroke-width=".4"/><text x="9" y="25" text-anchor="middle" font-size="5">7</text>
            <rect x="18" y="14" width="18" height="14" fill="#e8b60b" stroke="#fff" stroke-width=".4"/><text x="27" y="25" text-anchor="middle" font-size="5">17</text>
          </g>
          <text x="563" y="95" text-anchor="middle" font-size="6" fill="#555">Total</text>
          <text x="510" y="128" text-anchor="middle" font-size="7" fill="#2d7d46">Grid structure stays fixed;</text>
          <text x="510" y="141" text-anchor="middle" font-size="7" fill="#2d7d46">pixel-by-pixel arithmetic</text>
        </svg>
        <figcaption>Fig 7.14 &ndash; Vector overlay creates new geometry by intersecting boundaries; Raster Map Algebra performs pixel-by-pixel arithmetic on stacked grids</figcaption>
      </figure>
    </div>'''
    c = insert_before(c, "<!-- Part 2: The Four Tiers of Raster Operations -->", fig_7_14)

    # Fig 7.15 – Hillshade & Viewshed
    fig_7_15 = '''    <div class="figure">
      <figure>
        <svg viewBox="0 0 680 165" xmlns="http://www.w3.org/2000/svg" style="max-width:680px">
          <text x="340" y="16" text-anchor="middle" font-size="11" font-weight="bold" fill="#1a3c5e">Hillshade vs Viewshed: Two DEM-Derived Surfaces</text>
          <!-- LEFT: Hillshade -->
          <rect x="15" y="28" width="310" height="125" rx="8" fill="#f5f0e8" stroke="#b8860b" stroke-width="1"/>
          <text x="170" y="46" text-anchor="middle" font-size="9" font-weight="bold" fill="#b8860b">Hillshade (3D Visualization)</text>
          <!-- Sun -->
          <circle cx="50" cy="55" r="12" fill="#e8b60b" opacity=".6"/><text x="50" y="59" text-anchor="middle" font-size="10">&#x2600;</text>
          <line x1="62" y1="58" x2="100" y2="78" stroke="#b8860b" stroke-width="1" stroke-dasharray="3,2"/>
          <line x1="62" y1="62" x2="145" y2="100" stroke="#b8860b" stroke-width="1" stroke-dasharray="3,2"/>
          <!-- Terrain -->
          <path d="M30,130 L80,90 L130,70 L180,85 L220,65 L260,80 L300,130" fill="#d4cfc5" stroke="#888" stroke-width="1.5"/>
          <!-- Shadow area -->
          <path d="M180,130 L180,85 L220,65 L220,130 Z" fill="#333" opacity=".2"/>
          <text x="200" y="124" text-anchor="middle" font-size="6" fill="#555">Shadow</text>
          <text x="100" y="82" font-size="6" fill="#b8860b">Lit slope</text>
          <text x="170" y="150" text-anchor="middle" font-size="7" fill="#888" font-style="italic">Input: DEM + Sun azimuth &amp; altitude</text>
          <!-- RIGHT: Viewshed -->
          <rect x="355" y="28" width="310" height="125" rx="8" fill="#edf7f0" stroke="#2d7d46" stroke-width="1"/>
          <text x="510" y="46" text-anchor="middle" font-size="9" font-weight="bold" fill="#2d7d46">Viewshed (Line of Sight)</text>
          <!-- Observer -->
          <circle cx="400" cy="80" r="5" fill="#2d7d46"/><text x="400" y="74" text-anchor="middle" font-size="6" fill="#2d7d46">Observer</text>
          <!-- Terrain -->
          <path d="M380,130 L400,85 L440,110 L490,70 L540,90 L580,75 L640,130" fill="#d4cfc5" stroke="#888" stroke-width="1.5"/>
          <!-- Visible lines -->
          <line x1="400" y1="80" x2="450" y2="100" stroke="#2d7d46" stroke-width="1" stroke-dasharray="3,2"/>
          <line x1="400" y1="80" x2="580" y2="75" stroke="#2d7d46" stroke-width="1" stroke-dasharray="3,2"/>
          <!-- Blocked -->
          <line x1="400" y1="80" x2="490" y2="70" stroke="#8b2500" stroke-width="1"/>
          <line x1="490" y1="70" x2="540" y2="90" stroke="#8b2500" stroke-width="1" stroke-dasharray="2,2" opacity=".4"/>
          <rect x="520" y="88" width="30" height="12" rx="2" fill="#8b2500" opacity=".15"/>
          <text x="535" y="97" text-anchor="middle" font-size="5" fill="#8b2500">Blocked</text>
          <rect x="560" y="68" width="30" height="12" rx="2" fill="#2d7d46" opacity=".15"/>
          <text x="575" y="77" text-anchor="middle" font-size="5" fill="#2d7d46">Visible</text>
          <text x="510" y="150" text-anchor="middle" font-size="7" fill="#888" font-style="italic">Output: Binary (Visible=1 / Not=0)</text>
        </svg>
        <figcaption>Fig 7.15 &ndash; Hillshade simulates sun illumination for 3D relief; Viewshed identifies which cells are visible from an observer point</figcaption>
      </figure>
    </div>'''
    c = insert_before(c, "<h4>3. Euclidean Distance and Cost Path</h4>", fig_7_15)

    # Fig 7.16 – Euclidean Distance vs Cost Path
    fig_7_16 = '''    <div class="figure">
      <figure>
        <svg viewBox="0 0 680 165" xmlns="http://www.w3.org/2000/svg" style="max-width:680px">
          <text x="340" y="16" text-anchor="middle" font-size="11" font-weight="bold" fill="#1a3c5e">Euclidean Distance vs Cost Path Analysis</text>
          <!-- LEFT -->
          <rect x="15" y="28" width="310" height="125" rx="8" fill="#e8f4fd" stroke="#1a3c5e" stroke-width="1"/>
          <text x="170" y="46" text-anchor="middle" font-size="9" font-weight="bold" fill="#1a3c5e">Euclidean Distance</text>
          <!-- Concentric rings -->
          <circle cx="140" cy="95" r="8" fill="#1a3c5e"/>
          <text x="140" y="98" text-anchor="middle" font-size="6" fill="#fff">Source</text>
          <circle cx="140" cy="95" r="22" fill="none" stroke="#1a3c5e" stroke-width=".8" opacity=".5"/>
          <text x="164" y="85" font-size="5" fill="#1a3c5e">500m</text>
          <circle cx="140" cy="95" r="36" fill="none" stroke="#1a3c5e" stroke-width=".8" opacity=".3"/>
          <text x="178" y="78" font-size="5" fill="#1a3c5e">1km</text>
          <circle cx="140" cy="95" r="50" fill="none" stroke="#1a3c5e" stroke-width=".6" opacity=".2"/>
          <text x="192" y="70" font-size="5" fill="#1a3c5e">1.5km</text>
          <text x="260" y="75" font-size="7" fill="#555">Each pixel =</text>
          <text x="260" y="87" font-size="7" fill="#555">straight-line</text>
          <text x="260" y="99" font-size="7" fill="#555">distance to</text>
          <text x="260" y="111" font-size="7" fill="#555">nearest source</text>
          <text x="170" y="148" text-anchor="middle" font-size="7" fill="#888" font-style="italic">"As the crow flies" &ndash; ignores terrain</text>
          <!-- RIGHT -->
          <rect x="355" y="28" width="310" height="125" rx="8" fill="#fff5ec" stroke="#b8860b" stroke-width="1"/>
          <text x="510" y="46" text-anchor="middle" font-size="9" font-weight="bold" fill="#b8860b">Cost Path (Least Cost Route)</text>
          <!-- Friction surface -->
          <g transform="translate(375,55)">
            <rect x="0" y="0" width="35" height="25" fill="#a0d468" opacity=".5"/><text x="17" y="16" text-anchor="middle" font-size="5" fill="#333">Low</text>
            <rect x="35" y="0" width="35" height="25" fill="#e8b60b" opacity=".5"/><text x="52" y="16" text-anchor="middle" font-size="5" fill="#333">Med</text>
            <rect x="70" y="0" width="35" height="25" fill="#ed5565" opacity=".5"/><text x="87" y="16" text-anchor="middle" font-size="5" fill="#fff">High</text>
            <rect x="0" y="25" width="35" height="25" fill="#e8b60b" opacity=".5"/>
            <rect x="35" y="25" width="35" height="25" fill="#ed5565" opacity=".5"/>
            <rect x="70" y="25" width="35" height="25" fill="#a0d468" opacity=".5"/>
            <rect x="0" y="50" width="35" height="25" fill="#a0d468" opacity=".5"/>
            <rect x="35" y="50" width="35" height="25" fill="#a0d468" opacity=".5"/>
            <rect x="70" y="50" width="35" height="25" fill="#e8b60b" opacity=".5"/>
          </g>
          <!-- Optimal path -->
          <circle cx="385" cy="62" r="5" fill="#2d7d46"/><text x="385" y="65" text-anchor="middle" font-size="5" fill="#fff">A</text>
          <path d="M385,67 L390,80 L395,95 L405,105 L420,110 L440,115 L455,110 L465,100 L470,85 L475,70" fill="none" stroke="#2d7d46" stroke-width="2.5" stroke-linecap="round"/>
          <circle cx="475" cy="70" r="5" fill="#8b2500"/><text x="475" y="73" text-anchor="middle" font-size="5" fill="#fff">B</text>
          <text x="540" y="75" font-size="7" fill="#555">Avoids high-</text>
          <text x="540" y="87" font-size="7" fill="#555">cost cells</text>
          <text x="540" y="99" font-size="7" fill="#555">(steep slopes,</text>
          <text x="540" y="111" font-size="7" fill="#555">rivers, forests)</text>
          <text x="510" y="148" text-anchor="middle" font-size="7" fill="#888" font-style="italic">Follows path of least resistance</text>
        </svg>
        <figcaption>Fig 7.16 &ndash; Euclidean Distance measures straight-line proximity; Cost Path finds the optimal route through a friction surface</figcaption>
      </figure>
    </div>'''
    c = insert_before(c, "<h4>4. Reclassify and Map Algebra</h4>", fig_7_16)

    # Fig 7.17 – Reclassify Process
    fig_7_17 = '''    <div class="figure">
      <figure>
        <svg viewBox="0 0 680 155" xmlns="http://www.w3.org/2000/svg" style="max-width:680px">
          <text x="340" y="16" text-anchor="middle" font-size="11" font-weight="bold" fill="#1a3c5e">Reclassification: Continuous &#x2192; Discrete Classes</text>
          <!-- Input: continuous slope -->
          <g transform="translate(25,30)">
            <text x="60" y="0" text-anchor="middle" font-size="8" font-weight="bold" fill="#1a3c5e">Input: Slope (0&#xb0;&#x2013;90&#xb0;)</text>
            <rect x="0" y="6" width="24" height="20" fill="#e8f4fd"/><text x="12" y="20" text-anchor="middle" font-size="6" fill="#333">5&#xb0;</text>
            <rect x="24" y="6" width="24" height="20" fill="#b0d4f4"/><text x="36" y="20" text-anchor="middle" font-size="6" fill="#333">12&#xb0;</text>
            <rect x="48" y="6" width="24" height="20" fill="#88b8e8"/><text x="60" y="20" text-anchor="middle" font-size="6" fill="#fff">22&#xb0;</text>
            <rect x="72" y="6" width="24" height="20" fill="#5588cc"/><text x="84" y="20" text-anchor="middle" font-size="6" fill="#fff">35&#xb0;</text>
            <rect x="96" y="6" width="24" height="20" fill="#3366aa"/><text x="108" y="20" text-anchor="middle" font-size="6" fill="#fff">48&#xb0;</text>
            <rect x="0" y="26" width="24" height="20" fill="#d0e8f8"/><text x="12" y="40" text-anchor="middle" font-size="6" fill="#333">8&#xb0;</text>
            <rect x="24" y="26" width="24" height="20" fill="#b0d4f4"/><text x="36" y="40" text-anchor="middle" font-size="6" fill="#333">18&#xb0;</text>
            <rect x="48" y="26" width="24" height="20" fill="#5588cc"/><text x="60" y="40" text-anchor="middle" font-size="6" fill="#fff">28&#xb0;</text>
            <rect x="72" y="26" width="24" height="20" fill="#3366aa"/><text x="84" y="40" text-anchor="middle" font-size="6" fill="#fff">42&#xb0;</text>
            <rect x="96" y="26" width="24" height="20" fill="#224488"/><text x="108" y="40" text-anchor="middle" font-size="6" fill="#fff">55&#xb0;</text>
            <rect x="0" y="46" width="24" height="20" fill="#e8f4fd"/><text x="12" y="60" text-anchor="middle" font-size="6" fill="#333">3&#xb0;</text>
            <rect x="24" y="46" width="24" height="20" fill="#d0e8f8"/><text x="36" y="60" text-anchor="middle" font-size="6" fill="#333">10&#xb0;</text>
            <rect x="48" y="46" width="24" height="20" fill="#88b8e8"/><text x="60" y="60" text-anchor="middle" font-size="6" fill="#fff">20&#xb0;</text>
            <rect x="72" y="46" width="24" height="20" fill="#5588cc"/><text x="84" y="60" text-anchor="middle" font-size="6" fill="#fff">32&#xb0;</text>
            <rect x="96" y="46" width="24" height="20" fill="#3366aa"/><text x="108" y="60" text-anchor="middle" font-size="6" fill="#fff">45&#xb0;</text>
          </g>
          <!-- Lookup Table -->
          <g transform="translate(220,30)">
            <text x="80" y="0" text-anchor="middle" font-size="8" font-weight="bold" fill="#b8860b">Lookup Table</text>
            <rect x="10" y="8" width="140" height="18" rx="3" fill="#2d7d46" opacity=".15" stroke="#2d7d46" stroke-width=".6"/>
            <text x="80" y="21" text-anchor="middle" font-size="7" fill="#2d7d46">0&#xb0;&#x2013;15&#xb0; &#x2192; Class 1 (Safe)</text>
            <rect x="10" y="30" width="140" height="18" rx="3" fill="#b8860b" opacity=".15" stroke="#b8860b" stroke-width=".6"/>
            <text x="80" y="43" text-anchor="middle" font-size="7" fill="#b8860b">15&#xb0;&#x2013;30&#xb0; &#x2192; Class 2 (Moderate)</text>
            <rect x="10" y="52" width="140" height="18" rx="3" fill="#8b2500" opacity=".15" stroke="#8b2500" stroke-width=".6"/>
            <text x="80" y="65" text-anchor="middle" font-size="7" fill="#8b2500">&gt;30&#xb0; &#x2192; Class 3 (High Risk)</text>
          </g>
          <!-- Arrow -->
          <polygon points="435,75 455,67 455,71 475,71 475,79 455,79 455,83" fill="#1a3c5e"/>
          <!-- Output: classified -->
          <g transform="translate(490,30)">
            <text x="60" y="0" text-anchor="middle" font-size="8" font-weight="bold" fill="#1a3c5e">Output: Risk Classes</text>
            <rect x="0" y="6" width="24" height="20" fill="#2d7d46" opacity=".4"/><text x="12" y="20" text-anchor="middle" font-size="7" fill="#fff" font-weight="bold">1</text>
            <rect x="24" y="6" width="24" height="20" fill="#2d7d46" opacity=".4"/><text x="36" y="20" text-anchor="middle" font-size="7" fill="#fff" font-weight="bold">1</text>
            <rect x="48" y="6" width="24" height="20" fill="#b8860b" opacity=".4"/><text x="60" y="20" text-anchor="middle" font-size="7" font-weight="bold">2</text>
            <rect x="72" y="6" width="24" height="20" fill="#8b2500" opacity=".4"/><text x="84" y="20" text-anchor="middle" font-size="7" fill="#fff" font-weight="bold">3</text>
            <rect x="96" y="6" width="24" height="20" fill="#8b2500" opacity=".4"/><text x="108" y="20" text-anchor="middle" font-size="7" fill="#fff" font-weight="bold">3</text>
            <rect x="0" y="26" width="24" height="20" fill="#2d7d46" opacity=".4"/><text x="12" y="40" text-anchor="middle" font-size="7" fill="#fff" font-weight="bold">1</text>
            <rect x="24" y="26" width="24" height="20" fill="#b8860b" opacity=".4"/><text x="36" y="40" text-anchor="middle" font-size="7" font-weight="bold">2</text>
            <rect x="48" y="26" width="24" height="20" fill="#b8860b" opacity=".4"/><text x="60" y="40" text-anchor="middle" font-size="7" font-weight="bold">2</text>
            <rect x="72" y="26" width="24" height="20" fill="#8b2500" opacity=".4"/><text x="84" y="40" text-anchor="middle" font-size="7" fill="#fff" font-weight="bold">3</text>
            <rect x="96" y="26" width="24" height="20" fill="#8b2500" opacity=".4"/><text x="108" y="40" text-anchor="middle" font-size="7" fill="#fff" font-weight="bold">3</text>
            <rect x="0" y="46" width="24" height="20" fill="#2d7d46" opacity=".4"/><text x="12" y="60" text-anchor="middle" font-size="7" fill="#fff" font-weight="bold">1</text>
            <rect x="24" y="46" width="24" height="20" fill="#2d7d46" opacity=".4"/><text x="36" y="60" text-anchor="middle" font-size="7" fill="#fff" font-weight="bold">1</text>
            <rect x="48" y="46" width="24" height="20" fill="#b8860b" opacity=".4"/><text x="60" y="60" text-anchor="middle" font-size="7" font-weight="bold">2</text>
            <rect x="72" y="46" width="24" height="20" fill="#8b2500" opacity=".4"/><text x="84" y="60" text-anchor="middle" font-size="7" fill="#fff" font-weight="bold">3</text>
            <rect x="96" y="46" width="24" height="20" fill="#8b2500" opacity=".4"/><text x="108" y="60" text-anchor="middle" font-size="7" fill="#fff" font-weight="bold">3</text>
          </g>
          <!-- Legend -->
          <g transform="translate(235,100)">
            <rect x="0" y="0" width="14" height="10" fill="#2d7d46" opacity=".4" stroke="#2d7d46" stroke-width=".5"/><text x="20" y="9" font-size="7" fill="#333">1 = Safe (0&#xb0;&#x2013;15&#xb0;)</text>
            <rect x="110" y="0" width="14" height="10" fill="#b8860b" opacity=".4" stroke="#b8860b" stroke-width=".5"/><text x="130" y="9" font-size="7" fill="#333">2 = Moderate (15&#xb0;&#x2013;30&#xb0;)</text>
            <rect x="250" y="0" width="14" height="10" fill="#8b2500" opacity=".4" stroke="#8b2500" stroke-width=".5"/><text x="270" y="9" font-size="7" fill="#333">3 = High Risk (&gt;30&#xb0;)</text>
          </g>
        </svg>
        <figcaption>Fig 7.17 &ndash; Reclassification transforms continuous slope values into discrete risk classes using a lookup table</figcaption>
      </figure>
    </div>'''
    c = insert_before(c, "<!-- Part 4: The 14-Mark Numerical (Weighted Overlay) -->", fig_7_17)

    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print("  Chapter 7: 7 figures added")

fix_ch7()
print("Chapter 7 done.")

"""
Phase 2: Deduplication for TES chapters 5 and 6.
Uses content-matching (not line numbers) for robustness.
"""
import re

def dedup_ch5():
    with open('chapter5.html', 'r', encoding='utf-8') as f:
        c = f.read()
    orig = len(c)

    # 1. Section 5.1: Remove Q3's restated F-diagram summary (keep Q1's detailed version)
    # Q3 starts with "The fecal-oral transmission route is illustrated by the <strong>F-Diagram</strong>"
    # and ends before the SVG figure
    block = '    <p>The fecal-oral transmission route is illustrated by the <strong>F-Diagram</strong>'
    end = 'open defecation free (ODF) campaigns to address these issues.</p>\n'
    i = c.find(block)
    j = c.find(end)
    if i != -1 and j != -1:
        c = c[:i] + c[j + len(end):]

    # 2. Section 5.5: Remove misplaced organic/inorganic definitions + IAP section
    block = '    <p><strong>Organic Pollutant:</strong> A pollutant derived from living organisms'
    end_marker = 'government policy.\n    </ol>\n'
    # Look for this IAP block that's misplaced in 5.5
    i = c.find(block)
    if i != -1:
        j = c.find(end_marker, i)
        if j != -1:
            c = c[:i] + c[j + len(end_marker):]

    # 3. Section 5.6: Remove second industrial waste block (starts "Industrial waste and sludge are major sources")
    block = '    <p><strong>Industrial waste and sludge</strong> are major sources of water pollution globally'
    # Keep looking for the exact text
    i = c.find(block)
    if i == -1:
        block = '    <p>Industrial waste and sludge are major sources of water pollution globally'
        i = c.find(block)
    if i != -1:
        # Find the end - look for the next <h2> or <p><strong>Industrial Wastewater
        end1 = c.find('<p><strong>Industrial Wastewater:', i)
        if end1 != -1 and end1 - i < 2000:
            c = c[:i] + c[end1:]

    # 4. Section 5.6: Remove duplicate Industrial Wastewater treatment block
    block = '    <p><strong>Industrial Wastewater:</strong> Industrial wastewater is the water discharged'
    i = c.find(block)
    if i != -1:
        # Find end - next heading or Bagmati section
        end = '    <p><strong>Major Causes of Bagmati River Pollution:</strong></p>'
        j = c.find(end, i)
        if j != -1:
            c = c[:i] + c[j:]

    # 5. Section 5.7: Remove condensed 3-line summary (D8)
    block = '    <p><strong>Sources:</strong> Vehicular emissions (largest in urban areas), industrial emissions (brick kilns'
    end = 'Impacts:</strong> Respiratory and cardiovascular diseases, acid rain, global warming, ozone depletion, smog, crop damage, material corrosion.</p>\n'
    i = c.find(block)
    j = c.find(end)
    if i != -1 and j != -1 and j - i < 600:
        c = c[:i] + c[j + len(end):]

    # 6. Section 5.7: Remove second air pollution definition + pollutant effects (D9)
    block = '    <p><strong>Air pollution</strong> is the contamination of the atmosphere by gaseous, liquid, or solid wastes'
    end = 'Hydrocarbons:</strong> Respiratory problems, smog formation; some are carcinogenic (benzene, 1,3-butadiene)</li>\n    </ul>\n'
    i = c.find(block)
    j = c.find(end)
    if i != -1 and j != -1 and j - i < 2000:
        c = c[:i] + c[j + len(end):]

    # 7. Section 5.7: Remove automobile pollution block (D10) - mostly duplicate
    block = '    <p><strong>Air Pollution from Automobiles:</strong> Motor vehicles are the largest source'
    end = 'sulfur oxides form acid rain harmful to vegetation and aquatic life.</p>\n'
    i = c.find(block)
    j = c.find(end)
    if i != -1 and j != -1 and j - i < 2000:
        c = c[:i] + c[j + len(end):]

    # 8. Section 5.7: Remove one-line sources restatement (D11)
    line = '    <p><strong>Sources of Air Pollution:</strong> Vehicular emissions, industrial processes (brick kilns, cement factories), power plants, domestic cooking (biomass, coal), waste burning, construction dust, agricultural burning, natural sources.</p>\n'
    c = c.replace(line, '')

    # 9. Section 5.7: Remove misplaced water pollution sources (D12)
    block = '    <p><strong>Sources of Water Pollution:</strong></p>\n    <ul>\n      <li><strong>Point sources:</strong>'
    end_marker = 'atmospheric deposition (acid rain)</li>\n    </ul>\n'
    i = c.find(block)
    j = c.find(end_marker)
    if i != -1 and j != -1:
        c = c[:i] + c[j + len(end_marker):]

    # 10. Section 5.7: Remove duplicate KTM water pollution (D14)
    block = '    <p><strong>Water Pollution in Kathmandu Valley:</strong></p>\n    <ul>'
    i = c.find(block)
    if i != -1:
        j = c.find('    </ul>\n', i + 10)
        if j != -1:
            c = c[:i] + c[j + len('    </ul>\n'):]

    # 11. Section 5.7: Remove "Reasons for Air Pollution" + "Reasons for Water Pollution" condensed (D15)
    block = '    <p><strong>Reasons for Air Pollution:</strong>'
    i = c.find(block)
    if i != -1:
        # Remove until after "Reasons for Water Pollution" paragraph
        end = '</p>\n'
        j = c.find('Reasons for Water Pollution:', i)
        if j != -1:
            k = c.find(end, j)
            if k != -1:
                c = c[:i] + c[k + len(end):]

    # 12. Section 5.7: Remove duplicate mitigation measures in air section (D16)
    block = '    <p><strong>Mitigation Measures for Air Pollution:</strong></p>\n    <ul>'
    i = c.find(block)
    if i != -1:
        # Find end - after Water Pollution mitigation list
        end = 'Mitigation Measures for Water Pollution:'
        j = c.find(end, i)
        if j != -1:
            k = c.find('    </ul>\n', j)
            if k != -1:
                c = c[:i] + c[k + len('    </ul>\n'):]

    # 13. Section 5.7: Remove third air pollution definition (D17)
    block = '    <p><strong>Air pollution</strong> is the introduction of chemicals, particulate matter'
    i = c.find(block)
    if i != -1:
        # This is a short block - find next paragraph after it
        j = c.find('</p>\n', i)
        if j != -1:
            # Check if there are more one-liner paras after
            next_chunk = c[j+5:j+500]
            # Remove consecutive one-line summary paragraphs
            end_pos = j + 5
            while next_chunk.strip().startswith('<p>') and '</p>' in next_chunk[:300]:
                pp = c.find('</p>\n', end_pos)
                if pp != -1:
                    end_pos = pp + 5
                    next_chunk = c[end_pos:end_pos+500]
                else:
                    break
            c = c[:i] + c[end_pos:]

    # 14. Section 5.8: Remove one-line summary (D18)
    line = '    <p>Key measures: Catalytic converters and emission testing for vehicles, scrubbers and bag filters for industries, promotion of electric vehicles and public transport, use of cleaner fuels, enforcement of emission standards, afforestation, and public awareness.</p>\n'
    c = c.replace(line, '')

    # 15. Section 5.8: Remove 2-line condensed summary (D20)
    block = '    <p><strong>Air pollution mitigation:</strong> Vehicle emission standards, catalytic converters'
    i = c.find(block)
    if i != -1:
        end = '    <p><strong>Water pollution mitigation:</strong>'
        j = c.find(end, i)
        if j != -1:
            k = c.find('</p>\n', j)
            if k != -1:
                c = c[:i] + c[k + len('</p>\n'):]

    final = len(c)
    print(f"Chapter 5: {orig} -> {final} chars (removed {orig-final}, {(orig-final)/orig*100:.1f}%)")
    with open('chapter5.html', 'w', encoding='utf-8') as f:
        f.write(c)


def dedup_ch6():
    with open('chapter6.html', 'r', encoding='utf-8') as f:
        c = f.read()
    orig = len(c)

    # Section 6.1: Keep lines up to the GHG table end, then the Nepal Impacts block,
    # then the "Think Globally Act Locally" block. Remove everything else in between.

    # 1. Remove weak CC definition at line ~53
    c = c.replace(
        '    <p><strong>Climate Change</strong> refers to seasonal changes over a long period of time. Besides natural causes, competition for economic growth and development, industrial revolution, technological advancement, and most of all population growth is the genesis of climate change.</p>\n',
        '')

    # 2. Remove duplicate CC definition "refers to seasonal changes... global warming"
    c = c.replace(
        '    <p><strong>Climate Change</strong> refers to seasonal changes over a long period of time caused by natural and artificial factors. The major effect of climate change is <strong>global warming</strong> &mdash; the gradual increase in temperature attributed to the greenhouse effect.</p>\n',
        '')

    # 3. Remove 1-line causes summary
    c = c.replace(
        '    <p><strong>Causes:</strong> Natural (volcanic eruptions, ocean currents, orbital changes, forest fires, meteor impacts) and Artificial (deforestation, fossil fuel burning, automobile emissions, suburbanization, greenhouse gas emissions).</p>\n',
        '')

    # 4. Remove bullet causes+impacts summary ("Natural: Volcanic eruptions..." and "Impacts:" ul)
    block = '    <p><strong>Causes:</strong></p>\n    <ul>\n      <li><strong>Natural:</strong> Volcanic eruptions (release GHGs'
    end = 'Species extinction and migration of tropical diseases (malaria, dengue)</li>\n    </ul>\n'
    i = c.find(block)
    j = c.find(end)
    if i != -1 and j != -1:
        c = c[:i] + c[j + len(end):]

    # 5. Remove "Factors Contributing" paragraph causes (keep greenhouse effect explanation)
    block = '    <p><strong>Factors Contributing to Climate Change:</strong></p>\n    <p><strong>Natural Causes:</strong> Volcanic eruptions'
    end = 'emission of greenhouse gases (CO2 57%, CFCs 25%, CH4 12%, N2O 6%).</p>\n'
    i = c.find(block)
    j = c.find(end)
    if i != -1 and j != -1:
        c = c[:i] + c[j + len(end):]

    # 6. Remove "Effects of Climate Change:" first duplicate ul
    block = '    <p><strong>Effects of Climate Change:</strong></p>\n    <ul>'
    i = c.find(block)
    if i != -1:
        j = c.find('    </ul>\n', i + 10)
        if j != -1:
            c = c[:i] + c[j + len('    </ul>\n'):]

    # 7. Remove "Major Symptoms of Climate Change in Nepal:" duplicate + "Key climate change challenges"
    block = '    <p><strong>Climate Change</strong> refers to long-term changes in seasonal patterns caused by natural factors'
    end = 'Spread of vector-borne diseases (malaria, dengue) to higher elevations</li>\n    </ul>\n'
    i = c.find(block)
    j = c.find(end)
    if i != -1 and j != -1:
        c = c[:i] + c[j + len(end):]

    # 8. Remove second GHG table (smaller 3-column version)
    block = '    <p><strong>Factors Contributing to Global Warming:</strong></p>\n    <table>\n      <thead><tr><th>Gas</th><th>GH Contribution</th>'
    end = '</table>\n'
    i = c.find(block)
    if i != -1:
        j = c.find(end, i)
        if j != -1:
            c = c[:i] + c[j + len(end):]

    # 9. Remove duplicate Impacts ol after GHG table
    block = '    <p><strong>Impacts:</strong></p>\n    <ol>\n      <li>Global temperature rise (~1.1'
    i = c.find(block)
    if i != -1:
        j = c.find('    </ol>\n', i)
        if j != -1:
            end_pos = j + len('    </ol>\n')
            c = c[:i] + c[end_pos:]

    # 10. Remove Mitigation in 6.1 (3-item ol starting "Carbon Capture: Tree plantation")
    block = '    <p><strong>Mitigation Measures:</strong></p>\n    <ol>\n      <li><strong>Carbon Capture:</strong> Tree plantation (single tree absorbs 48 lb'
    i = c.find(block)
    if i != -1:
        j = c.find('    </ol>\n', i)
        if j != -1:
            c = c[:i] + c[j + len('    </ol>\n'):]

    # 11. Remove "Major Symptoms in Nepal:" 5-item ol
    block = '    <p><strong>Climate Change:</strong> Long-term changes in seasonal weather patterns caused by both natural factors (volcanic eruptions, ocean currents, orbital changes) and human activities (fossil fuel burning, deforestation, GHG emissions). Global warming is the major manifestation.</p>\n    <p><strong>Major Symptoms in Nepal:</strong></p>'
    i = c.find(block)
    if i != -1:
        j = c.find('    </ol>\n', i)
        if j != -1:
            c = c[:i] + c[j + len('    </ol>\n'):]

    # 12. Remove "Climate Change: Long-term alteration..." + Impacts + Mitigation
    block = '    <p><strong>Climate Change:</strong> Long-term alteration of temperature and typical weather patterns'
    i = c.find(block)
    if i != -1:
        # Find end after the Sectoral Measures ul
        end = '</ul>\n'
        # Find multiple ending points
        pos = i
        for _ in range(4):  # Skip past impacts ul and mitigation ul
            pos = c.find(end, pos + 1)
        if pos != -1:
            c = c[:i] + c[pos + len(end):]

    # 13. Remove "Climate Change: Long-term changes... primarily through emission"
    block = '    <p><strong>Climate Change:</strong> Long-term changes in seasonal weather patterns caused by natural and human factors, primarily through emission of greenhouse gases'
    i = c.find(block)
    if i != -1:
        j = c.find('    </ol>\n', i)
        if j != -1:
            # Also remove the next ol (Nepal mitigation measures)
            k = c.find('    </ol>\n', j + 10)
            if k != -1 and k - j < 3000:
                c = c[:i] + c[k + len('    </ol>\n'):]

    # 14. Remove remaining duplicate "Climate Change: Refers to long-term..." + Impacts + Mitigation
    block = '    <p><strong>Climate Change:</strong> Refers to long-term changes in seasonal weather patterns. Caused by natural factors'
    i = c.find(block)
    if i != -1:
        j = c.find('    </ol>\n', i)
        if j != -1:
            # Skip past Impacts ol and Mitigation ol
            k = c.find('    </ol>\n', j + 10)
            if k != -1 and k - j < 5000:
                c = c[:i] + c[k + len('    </ol>\n'):]

    # 15. Section 6.2: Remove "Nepal is highly vulnerable" paragraph
    c = c.replace(
        '    <p><strong>Climate Change in Nepal:</strong></p>\n    <p>Nepal is highly vulnerable to climate change despite contributing minimally to global GHG emissions. Symptoms include: glacial retreat and GLOF threats, erratic monsoon patterns, rising temperatures at higher altitudes, floods, landslides, droughts, declining agricultural productivity, biodiversity loss, and spread of vector-borne diseases to higher elevations.</p>\n',
        '')

    # 16. Section 6.2: Remove duplicate mitigation summary (keep main + sectoral table)
    block = '    <p>Climate change mitigation aims to stabilize atmospheric GHG concentrations. Key measures:</p>\n    <ol>\n      <li><strong>Carbon Capture:</strong> Tree plantation (48 lb CO2/tree/yr)'
    end = '<li><strong>Sectoral Measures:</strong></li>\n    </ol>\n'
    i = c.find(block)
    j = c.find(end)
    if i != -1 and j != -1:
        c = c[:i] + c[j + len(end):]

    # 17. Section 6.2: Remove 1-line Impacts + 1-line Mitigation
    c = c.replace(
        '    <p><strong>Impacts:</strong> Global temperature rise, sea level rise, glacial retreat, extreme weather events, ocean acidification, species extinction, health risks.</p>\n',
        '')
    c = c.replace(
        '    <p><strong>Mitigation Measures:</strong> Carbon capture (tree plantation, CCS); shift to renewable energy (solar, wind, hydro); Hybrid Electric Vehicles; international agreements (UNFCCC, Kyoto Protocol); improved agriculture and building efficiency.</p>\n',
        '')

    # 18. Section 6.3: Remove ALL duplicate lists, keep only the most comprehensive one
    # Keep the detailed 5-item ol + company options
    # Remove the brief lists

    # Remove first brief ul
    block = '    <p>Key international efforts to combat climate change:</p>\n    <ul>\n      <li><strong>UNFCCC (1992):</strong> Global legal instrument'
    i = c.find(block)
    if i != -1:
        j = c.find('    </ul>\n', i)
        if j != -1:
            c = c[:i] + c[j + len('    </ul>\n'):]

    # Remove second brief ul (informal, no bold)
    block = '    <ul>\n      <li>UNFCCC (1992) &mdash; global framework convention with 196 countries</li>'
    i = c.find(block)
    if i != -1:
        j = c.find('    </ul>\n', i)
        if j != -1:
            c = c[:i] + c[j + len('    </ul>\n'):]

    # Remove 4th ol (summary)
    block = '    <ol>\n      <li><strong>UNFCCC (1992):</strong> Global framework for GHG control. 196 countries. Provides funding'
    i = c.find(block)
    if i != -1:
        j = c.find('    </ol>\n', i)
        if j != -1:
            c = c[:i] + c[j + len('    </ol>\n'):]

    # Remove 5th ol (medium)
    block = '    <ol>\n      <li><strong>UNFCCC (1992):</strong> Treaty adopted in 1992 with 196 countries to stabilize'
    i = c.find(block)
    if i != -1:
        j = c.find('    </ol>\n', i)
        if j != -1:
            c = c[:i] + c[j + len('    </ol>\n'):]

    # Remove brief ul (4 items, UNFCCC/Kyoto/Cancun/GCF)
    block = '    <ul>\n      <li><strong>UNFCCC (1992):</strong> Global convention for climate protection; 196 countries; annual COP conferences.</li>'
    i = c.find(block)
    if i != -1:
        j = c.find('    </ul>\n', i)
        if j != -1:
            c = c[:i] + c[j + len('    </ul>\n'):]

    # Remove "International Efforts:" + brief ul (3 items) + "National Efforts (Nepal):" ul
    block = '    <p><strong>International Efforts:</strong></p>\n    <ul>\n      <li>UNFCCC (1992) &mdash; global framework convention, 196 countries</li>'
    i = c.find(block)
    if i != -1:
        # Find end after National Efforts ul
        end = '10 national parks, 6 conservation areas, 3 wildlife reserves</li>\n    </ul>\n'
        j = c.find(end, i)
        if j != -1:
            c = c[:i] + c[j + len(end):]

    # Remove "International Efforts:" ol (4 items) + "National Efforts (Nepal):" ol
    block = '    <p><strong>International Efforts:</strong></p>\n    <ol>\n      <li><strong>UNFCCC (1992):</strong> 196 countries committed'
    i = c.find(block)
    if i != -1:
        end = '10 national parks, 6 conservation areas, 3 wildlife reserves.</li>\n    </ol>\n'
        j = c.find(end, i)
        if j != -1:
            c = c[:i] + c[j + len(end):]

    # Remove duplicate intl efforts in "Key International Efforts" (keep "How Nepal Can Be Streamlined" after it)
    # Actually, the most detailed 6-item list + "How Nepal" should remain
    # Remove any remaining CC definition inside 6.3
    block = '    <p><strong>Climate Change:</strong> Long-term changes in weather patterns caused by natural (volcanic eruptions'
    i = c.find(block)
    if i != -1:
        j = c.find('</p>\n', i)
        if j != -1:
            c = c[:i] + c[j + len('</p>\n'):]

    # Remove remaining duplicate International Efforts ol (5 items after "How Nepal")
    block = '    <p><strong>International Efforts:</strong></p>\n    <ol>\n      <li><strong>UNFCCC (1992):</strong> 196 countries; stabilize GHG concentrations'
    i = c.find(block)
    if i != -1:
        j = c.find('    </ol>\n', i)
        if j != -1:
            c = c[:i] + c[j + len('    </ol>\n'):]

    # Remove last remaining brief ul (4 items)
    block = '    <ul>\n      <li><strong>UNFCCC (1992):</strong> 196-country framework convention for GHG control'
    i = c.find(block)
    if i != -1:
        j = c.find('    </ul>\n', i)
        if j != -1:
            c = c[:i] + c[j + len('    </ul>\n'):]

    # Remove duplicate Weather definition before Think Globally
    c = c.replace(
        '    <p><strong>Weather:</strong> The state of the atmosphere at any given instant &mdash; it is short term and can change rapidly (temperature, humidity, precipitation, wind at a specific time and place).</p>\n',
        '')
    c = c.replace(
        '    <p><strong>Climate Change:</strong> Refers to long-term changes in seasonal weather patterns caused by both natural factors (volcanic eruptions, ocean currents, orbital changes) and artificial factors (human activities, emission of greenhouse gases, deforestation). It is the long-term alteration of temperature and typical weather patterns.</p>\n',
        '')
    c = c.replace(
        '    <p><strong>Climate Variability:</strong> Natural variations in climate over shorter time scales (year-to-year or decade-to-decade), such as El Ni&ntilde;o and La Ni&ntilde;a events. Unlike climate change, variability represents natural fluctuations around the long-term average without a persistent directional shift.</p>\n',
        '')

    final = len(c)
    print(f"Chapter 6: {orig} -> {final} chars (removed {orig-final}, {(orig-final)/orig*100:.1f}%)")
    with open('chapter6.html', 'w', encoding='utf-8') as f:
        f.write(c)


if __name__ == '__main__':
    dedup_ch5()
    dedup_ch6()
    print("Done!")

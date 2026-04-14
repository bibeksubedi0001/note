"""
Phase 2b: Second-pass deduplication for remaining duplicates in ch5 and ch6.
"""
import re

def dedup2_ch5():
    with open('chapter5.html', 'r', encoding='utf-8') as f:
        c = f.read()
    orig = len(c)

    # Remove misplaced organic/inorganic definitions + IAP block in section 5.5
    # This block starts at "Organic Pollutant: A pollutant derived" and ends before section 5.6
    old = """    <p><strong>Organic Pollutant:</strong> A pollutant derived from living organisms, containing carbon as the basic chemical element. Organic pollutants consist of proteins, carbohydrates, fats, and nucleic acids. When they enter water bodies, microorganisms decompose them, consuming dissolved oxygen (measured by BOD).</p>
    <ul>
      <li><strong>Examples:</strong> Domestic sewage, food processing waste, animal manure, crop residues, petroleum products, lubricants.</li>
    </ul>
    <p><strong>Inorganic Pollutant:</strong> A pollutant of mineral origin that is not of basically carbon structure. Inorganic pollutants include minerals, metals, and chemical compounds that contaminate the environment.</p>
    <ul>
      <li><strong>Examples:</strong> Nitrate (NO&sub3;&sup1;), fluoride, iron, manganese, arsenic, heavy metals (lead, mercury, cadmium), insecticides, pesticides.</li>
    </ul>
    <p><strong>Mitigative Measures of Indoor Air Pollution (Nepal Context):</strong></p>
    <p>Indoor air pollution (IAP) is a critical issue in Nepal where ~90% of total energy comes from traditional biomass fuels. People spend about 90% of their time indoors, and indoor pollutant levels can be 2&ndash;5 times (sometimes 100+ times) higher than outdoor levels.</p>
    <ol>
      <li><strong>Improved Cooking Stoves (ICS):</strong> Replace traditional open-fire stoves with improved designs that have chimneys and better combustion efficiency &mdash; reducing smoke by 50&ndash;70%.</li>
      <li><strong>Biogas as Alternative Fuel:</strong> Promote biogas plants in rural areas to replace firewood and dung-cake burning with clean-burning methane gas.</li>
      <li><strong>Improved Ventilation:</strong> Install windows, ventilation holes, and chimneys in kitchens. Traditional houses often lack ventilation in cooking areas.</li>
      <li><strong>Separate Kitchen Design:</strong> Move cooking areas away from living and sleeping spaces to reduce exposure.</li>
      <li><strong>Alternative Energy Sources:</strong> Promote LPG, solar cookers, and electric cooking where grid electricity is available.</li>
      <li><strong>Health Education:</strong> Awareness programs about the health risks of indoor smoke (respiratory diseases, eye problems, lung cancer) and available alternatives.</li>
      <li><strong>Reforestation Programs:</strong> Ensure sustainable fuel wood supply through community forestry programs.</li>
      <li><strong>Government Policy:</strong> Subsidies for clean cooking technologies and enforcement of building codes requiring proper ventilation.</li>
    </ol>"""
    c = c.replace(old, '')

    final = len(c)
    print(f"Chapter 5: {orig} -> {final} chars (removed {orig-final}, {(orig-final)/orig*100:.1f}%)")
    with open('chapter5.html', 'w', encoding='utf-8') as f:
        f.write(c)


def dedup2_ch6():
    with open('chapter6.html', 'r', encoding='utf-8') as f:
        c = f.read()
    orig = len(c)

    # 1. Section 6.3: Remove duplicate "Key International Efforts" condensed list
    # Keep the first detailed 5-item list, remove the second condensed 6-item one
    old = """    <p><strong>Key International Efforts:</strong></p>
    <ol>
      <li><strong>UNFCCC (1992):</strong> Global legal instrument for GHG management. 196 countries. Provides funding, insurance, and technology transfer. Annual COP conferences for policy development and review.</li>
      <li><strong>Kyoto Protocol (1997):</strong> Binding commitments for developed countries &mdash; 5.2% GHG reduction by 2012 (vs 1990). Three mechanisms:
        <ul>
          <li>ETS (Emissions Trading System) &mdash; tradable Assigned Amount Units</li>
          <li>CDM (Clean Development Mechanism) &mdash; invest in developing country projects</li>
          <li>JI (Joint Implementation) &mdash; developed-to-transition country projects</li>
        </ul>
        Companies have 4 options: (1) pay expensive fines, (2) process improvement, (3) buy emissions credits on CO2 market, (4) technology transfers via CDM/JI.</li>
      <li><strong>Cancun Adaptation Framework (COP 16, 2010):</strong> Country-driven, gender-sensitive, participatory and transparent approach. NAPA implementation. Building resilience in most vulnerable developing countries.</li>
      <li><strong>Green Climate Fund:</strong> Established COP 16, operational COP 17. Paradigm shift towards low-emission development. Includes GEF Trust Fund, LDCF, SCCF.</li>
      <li><strong>Adaptation Fund:</strong> Financed from CDM and developed country donations. Supports adaptation programmes in developing countries. Operational since 2010.</li>
      <li><strong>COP 17&ndash;23 (Durban to Bonn):</strong> Low-carbon society development; Warsaw Loss and Damage Mechanism; agricultural improvement; disaster risk reduction strategies.</li>
    </ol>"""
    # But the COP 17-23 info is unique - add it to the first list
    cop_item = """      <li><strong>COP 17&ndash;23 (Durban to Bonn):</strong> Low-carbon society development; Warsaw Loss and Damage Mechanism; agricultural improvement; disaster risk reduction strategies.</li>"""
    # First, add COP 17-23 to the first list
    c = c.replace(
        '      <li><strong>Adaptation Fund:</strong> Set up under UNFCCC Green Climate Fund. Supports adaptation programmes in developing countries. Financed from CDM projects and developed country donations. Fully operational in 2010.</li>\n    </ol>',
        '      <li><strong>Adaptation Fund:</strong> Set up under UNFCCC Green Climate Fund. Supports adaptation programmes in developing countries. Financed from CDM projects and developed country donations. Fully operational in 2010.</li>\n' + cop_item + '\n    </ol>'
    )
    # Then remove the duplicate block
    c = c.replace(old, '')

    # 2. Section 6.4: Remove duplicate condensed biogas block
    old = """    <p><strong>Biogas:</strong> Produced from fermentation of biodegradable materials (sewage, manure, wastewater). Components: CH4 (50&ndash;70%), CO2 (30&ndash;40%). A renewable energy used for electricity, heat, cooking, and organic fertilizer production.</p>
    <p><strong>Suitability in Terai Region:</strong></p>
    <ol>
      <li><strong>Warm Climate:</strong> Biogas digestion requires 20&ndash;35&deg;C. Terai's warm tropical climate is ideal for year-round biogas production with optimal retention period (40&ndash;100 days).</li>
      <li><strong>Livestock Availability:</strong> Terai has high concentration of cattle and buffalo, providing abundant raw material (manure).</li>
      <li><strong>Agricultural Base:</strong> Terai is Nepal's agricultural heartland. Biogas produces organic fertilizer as a by-product, benefiting farming.</li>
      <li><strong>Flat Terrain:</strong> Easy construction of biogas plants on flat land.</li>
      <li><strong>Reducing Deforestation:</strong> Replaces fuelwood, reducing pressure on Terai's Chure range forests.</li>
      <li><strong>Health Benefits:</strong> Reduces indoor air pollution from traditional cooking, improving living standards especially for women and children.</li>
    </ol>
    <p><strong>History:</strong> Introduced in Nepal 1974/75 by United Missions. Gobar Gas Company founded 1977. Nepal's first commercial CNG plant (Envipower Energy) began operations Jan 6, 2018.</p>"""
    # The Terai suitability content is unique - merge into the main biogas section
    # Add Terai suitability after the Risks paragraph
    terai_block = """
    <p><strong>Suitability in Terai Region:</strong></p>
    <ol>
      <li><strong>Warm Climate:</strong> Biogas digestion requires 20&ndash;35&deg;C. Terai's warm tropical climate is ideal for year-round biogas production with optimal retention period (40&ndash;100 days).</li>
      <li><strong>Livestock Availability:</strong> Terai has high concentration of cattle and buffalo, providing abundant raw material (manure).</li>
      <li><strong>Agricultural Base:</strong> Terai is Nepal's agricultural heartland. Biogas produces organic fertilizer as a by-product, benefiting farming.</li>
      <li><strong>Flat Terrain:</strong> Easy construction of biogas plants on flat land.</li>
      <li><strong>Reducing Deforestation:</strong> Replaces fuelwood, reducing pressure on Terai's Chure range forests.</li>
      <li><strong>Health Benefits:</strong> Reduces indoor air pollution from traditional cooking, improving living standards especially for women and children.</li>
    </ol>"""
    c = c.replace(old, '')
    # Insert Terai block after Risks paragraph
    c = c.replace(
        '    <p><strong>Risks:</strong> Potential gas leaks, fires, explosions; compressed biogas can corrode metals. Safety measures: regularly check for leaks, provide ventilation around gas lines, maintain positive pressure.</p>',
        '    <p><strong>Risks:</strong> Potential gas leaks, fires, explosions; compressed biogas can corrode metals. Safety measures: regularly check for leaks, provide ventilation around gas lines, maintain positive pressure.</p>' + terai_block
    )

    # 3. Section 6.6: Remove duplicate national park definition + importance second pass
    old = """    <p><strong>National Park:</strong> An area of special scenic, historical, or scientific importance, set aside and maintained by a national government. It is a reserve of natural, semi-natural, or developed land used for conservation purposes.</p>
    <p><strong>Nepal has 10 national parks</strong> (e.g., Chitwan National Park, Sagarmatha National Park, Shey Phoksundo National Park &mdash; 3,555 km&sup2;), <strong>6 conservation areas</strong> (e.g., Annapurna Conservation Area), and <strong>3 wildlife reserves</strong>.</p>
    <p><strong>Importance:</strong></p>
    <ol>
      <li><strong>Environmental Protection:</strong> Protect native plants, animals, and their habitats. Serve as carbon sinks (Nepal's forests store 1.054 billion tons of carbon).</li>
      <li><strong>Biodiversity Conservation:</strong> Provide habitat and protection from hunting for threatened and endangered species. 80% of documented species live in forests.</li>
      <li><strong>Water &amp; Soil Conservation:</strong> Protect river and water catchments; prevent erosion and maintain soil fertility.</li>
      <li><strong>Economic Value:</strong> Attract tourists; visitor spending benefits nearby towns. Ecotourism generates revenue for conservation and local communities.</li>
      <li><strong>Heritage Preservation:</strong> Protect signs of human history and cultural significance.</li>
      <li><strong>Health &amp; Recreation:</strong> Therapeutic recreation; parks improve moods, reduce stress, enhance sense of wellness.</li>
      <li><strong>Future Generations:</strong> Preserve natural resources for future generations to enjoy and learn from (intrinsic value).</li>
    </ol>"""
    c = c.replace(old, '')

    final = len(c)
    print(f"Chapter 6: {orig} -> {final} chars (removed {orig-final}, {(orig-final)/orig*100:.1f}%)")
    with open('chapter6.html', 'w', encoding='utf-8') as f:
        f.write(c)


if __name__ == '__main__':
    dedup2_ch5()
    dedup2_ch6()
    print("Done!")

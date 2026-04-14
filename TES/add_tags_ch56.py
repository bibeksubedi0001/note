"""
Phase 3: Add year-tags to h2 headings and numbered h3 subtopics for chapters 5 and 6.
Pattern: h2 gets all exam years as <span class="year-tag">20XX</span>
         h3 subtopics numbered X.Y.Z, with selective year-tags
"""
import re

def tag(years):
    """Generate year-tag HTML from list of years."""
    return ''.join(f' <span class="year-tag">{y}</span>' for y in years)

def add_tags_ch5():
    with open('chapter5.html', 'r', encoding='utf-8') as f:
        c = f.read()

    # ── H2 year-tags ──
    reps = [
        ('5.1 Fecal-Oral Infection Transmission Route</h2>',
         f'5.1 Fecal-Oral Infection Transmission Route{tag(["2080","2076","2072"])}</h2>'),
        ('5.2 Preventive Measures</h2>',
         f'5.2 Preventive Measures{tag(["2076"])}</h2>'),
        # 5.3 has no exam questions — no tags
        ('5.4 Importance of Health Education</h2>',
         f'5.4 Importance of Health Education{tag(["2073","2072"])}</h2>'),
        ('5.5 Organic Pollution</h2>',
         f'5.5 Organic Pollution{tag(["2081","2073"])}</h2>'),
        ('5.6 Inorganic Pollution</h2>',
         f'5.6 Inorganic Pollution{tag(["2073","2071","2070","2069"])}</h2>'),
        ('5.7 Sources, Causes &amp; Impacts of Air Pollution</h2>',
         f'5.7 Sources, Causes &amp; Impacts of Air Pollution{tag(["2079","2078","2077","2075","2073","2072","2071","2070","2069"])}</h2>'),
        ('5.8 Mitigation Measures</h2>',
         f'5.8 Mitigation Measures{tag(["2079","2078","2075","2074","2072","2071","2070"])}</h2>'),
        ('5.9 Indoor Air Pollution</h2>',
         f'5.9 Indoor Air Pollution{tag(["2071"])}</h2>'),
        ('5.10 Severity of Its Problems in Nepal</h2>',
         f'5.10 Severity of Its Problems in Nepal{tag(["2079"])}</h2>'),
    ]
    for old, new in reps:
        c = c.replace(old, new)

    # ── H3 subtopics ──

    # 5.1: F-Diagram, Primary/Secondary Barriers, Diseases, Pathogens
    c = c.replace(
        '    <p><strong>The F-Diagram (Feces–Fluids–Fields–Flies–Fingers–Food–New Host):</strong></p>',
        f'    <h3>5.1.1 The F-Diagram{tag(["2080","2076","2072"])}</h3>')
    c = c.replace(
        '    <p><strong>Primary Barriers</strong> (prevent feces from entering the environment):</p>',
        f'    <h3>5.1.2 Primary &amp; Secondary Barriers{tag(["2080"])}</h3>\n    <p><strong>Primary Barriers</strong> (prevent feces from entering the environment):</p>')
    c = c.replace(
        '    <p><strong>Common fecal-oral diseases and their causative agents:</strong></p>',
        f'    <h3>5.1.3 Common Fecal-Oral Diseases</h3>')

    # 5.2: Numbered preventive measures
    c = c.replace(
        '    <p><strong>1. Safe Water Supply:</strong></p>',
        f'    <h3>5.2.1 Safe Water Supply{tag(["2076"])}</h3>')
    c = c.replace(
        '    <p><strong>2. Sanitation:</strong></p>',
        '    <h3>5.2.2 Sanitation</h3>')
    c = c.replace(
        '    <p><strong>3. Personal &amp; Food Hygiene:</strong></p>',
        '    <h3>5.2.3 Personal &amp; Food Hygiene</h3>')
    c = c.replace(
        '    <p><strong>4. Environmental Sanitation:</strong></p>',
        '    <h3>5.2.4 Environmental Sanitation</h3>')
    c = c.replace(
        '    <p><strong>5. Health Education:</strong></p>',
        '    <h3>5.2.5 Health Education</h3>')

    # 5.3: On-site sanitation subtopics
    c = c.replace(
        '    <p><strong>Types of On-Site Sanitation Systems:</strong></p>',
        '    <h3>5.3.1 Types of On-Site Sanitation Systems</h3>')
    c = c.replace(
        '    <p><strong>a) Dry System (Pit Latrines &amp; Composting Toilets):</strong></p>',
        '    <h3>5.3.2 Dry System (Pit Latrines &amp; Composting Toilets)</h3>')
    c = c.replace(
        '    <p><strong>b) Wet System (Pour-Flush &amp; Septic Tanks):</strong></p>',
        '    <h3>5.3.3 Wet System (Pour-Flush &amp; Septic Tanks)</h3>')
    c = c.replace(
        '    <p><strong>Eco-Sanitation (Ecological Sanitation &mdash; ECOSAN):</strong></p>',
        '    <h3>5.3.4 Eco-Sanitation (ECOSAN)</h3>')

    # 5.4: Health education subtopics
    c = c.replace(
        '    <p><strong>Importance of Health Education:</strong></p>',
        '    <h3>5.4.1 Importance of Health Education</h3>')
    c = c.replace(
        '    <p><strong>Status of Health Education in Nepal:</strong></p>',
        f'    <h3>5.4.2 Status in Nepal{tag(["2073"])}</h3>')

    # 5.5: Organic pollution subtopics
    c = c.replace(
        '    <p><strong>Sources of organic pollution:</strong></p>',
        '    <h3>5.5.1 Sources &amp; Effects</h3>')
    c = c.replace(
        '    <p><strong>Aerobic Digestion:</strong></p>',
        f'    <h3>5.5.2 Aerobic Digestion{tag(["2073"])}</h3>')
    c = c.replace(
        '    <p><strong>Anaerobic Digestion:</strong></p>',
        f'    <h3>5.5.3 Anaerobic Digestion{tag(["2073"])}</h3>')

    # 5.6: Inorganic pollution subtopics
    c = c.replace(
        '    <p><strong>Major Inorganic Pollutants and Their Effects:</strong></p>',
        f'    <h3>5.6.1 Major Inorganic Pollutants</h3>')
    c = c.replace(
        '    <p><strong>Pollution from Sludge and Industrial Waste:</strong></p>',
        f'    <h3>5.6.2 Pollution from Sludge &amp; Industrial Waste{tag(["2073","2070"])}</h3>')
    # Pesticide hazards
    c = c.replace(
        '    <p><strong>Pesticide hazards</strong> arise from the use of insecticides, herbicides, and fungicides in agriculture that contaminate water, soil, and food.</p>\n    <p><strong>Situation in Nepal:</strong></p>',
        f'    <h3>5.6.3 Pesticide Hazards in Nepal{tag(["2071"])}</h3>\n    <p><strong>Pesticide hazards</strong> arise from the use of insecticides, herbicides, and fungicides in agriculture that contaminate water, soil, and food.</p>')
    c = c.replace(
        '    <p><strong>Industrial Wastewater:</strong></p>',
        f'    <h3>5.6.4 Industrial Wastewater &amp; Treatment{tag(["2069"])}</h3>')
    c = c.replace(
        '    <p><strong>Major Causes of Bagmati River Pollution:</strong></p>',
        f'    <h3>5.6.5 Bagmati River Pollution{tag(["2069"])}</h3>')

    # 5.7: Air pollution subtopics
    c = c.replace(
        '    <p><strong>Sources of Air Pollution (10 major sources):</strong></p>',
        f'    <h3>5.7.1 Sources of Air Pollution{tag(["2079","2078","2073","2070"])}</h3>')
    c = c.replace(
        '    <p><strong>Causes (Pollutants):</strong></p>',
        f'    <h3>5.7.2 Causes (Pollutants){tag(["2079","2078","2075","2073","2072","2071"])}</h3>')
    c = c.replace(
        '    <p><strong>Impacts of Air Pollution:</strong></p>',
        f'    <h3>5.7.3 Impacts of Air Pollution{tag(["2079","2078","2075","2073","2072","2071"])}</h3>')
    c = c.replace(
        '    <p><strong>Sources of Water Pollution:</strong></p>',
        f'    <h3>5.7.4 Sources of Water Pollution{tag(["2070"])}</h3>')
    c = c.replace(
        '    <p><strong>Air Pollution in Kathmandu Valley:</strong></p>',
        f'    <h3>5.7.5 Air &amp; Water Pollution in Kathmandu Valley{tag(["2078","2077"])}</h3>')
    c = c.replace(
        '    <p><strong>Acid Rain:</strong> Acid rain is the deposition',
        f'    <h3>5.7.6 Acid Rain{tag(["2069"])}</h3>\n    <p>Acid rain is the deposition')

    # 5.8: Mitigation subtopics
    c = c.replace(
        '    <p><strong>1. Vehicular Emission Control:</strong></p>',
        f'    <h3>5.8.1 Vehicular Emission Control{tag(["2079","2075","2072","2071"])}</h3>')
    c = c.replace(
        '    <p><strong>2. Industrial Emission Control:</strong></p>',
        f'    <h3>5.8.2 Industrial Emission Control</h3>')
    c = c.replace(
        '    <p><strong>3. Policy &amp; Planning:</strong></p>',
        '    <h3>5.8.3 Policy &amp; Planning</h3>')
    c = c.replace(
        '    <p><strong>4. Alternative Energy:</strong></p>',
        '    <h3>5.8.4 Alternative Energy</h3>')
    c = c.replace(
        '    <p><strong>Kathmandu-specific mitigation measures:</strong></p>',
        f'    <h3>5.8.5 Kathmandu-Specific Measures{tag(["2078","2077","2074"])}</h3>')

    # 5.9: Indoor air pollution subtopics
    c = c.replace(
        '    <p><strong>Sources of Indoor Air Pollution:</strong></p>',
        f'    <h3>5.9.1 Sources of Indoor Air Pollution</h3>')
    c = c.replace(
        '    <p><strong>Causes of Indoor Air Pollution (Nepal context):</strong></p>',
        f'    <h3>5.9.2 Causes (Nepal Context){tag(["2071"])}</h3>')
    c = c.replace(
        '    <p><strong>Health effects:</strong></p>',
        '    <h3>5.9.3 Health Effects</h3>')
    c = c.replace(
        '    <p><strong>Control Strategies for Indoor Air Pollution:</strong></p>',
        '    <h3>5.9.4 Control Strategies</h3>')
    c = c.replace(
        '    <p><strong>Measures to Reduce Indoor Air Pollution in Rural Nepal:</strong></p>',
        f'    <h3>5.9.5 Measures for Rural Nepal{tag(["2071"])}</h3>')

    # 5.10: Severity subtopics
    c = c.replace(
        '    <p><strong>Legislative Measures:</strong></p>',
        f'    <h3>5.10.1 Legislative Measures{tag(["2079"])}</h3>')
    c = c.replace(
        '    <p><strong>Institutional Measures:</strong></p>',
        '    <h3>5.10.2 Institutional Measures</h3>')
    c = c.replace(
        '    <p><strong>Programmatic Measures:</strong></p>',
        '    <h3>5.10.3 Programmatic Measures</h3>')

    with open('chapter5.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Chapter 5: year-tags and subtopics added")


def add_tags_ch6():
    with open('chapter6.html', 'r', encoding='utf-8') as f:
        c = f.read()

    # ── H2 year-tags ──
    reps = [
        ('6.1 Definition, Causes &amp; Impacts of Climate Change</h2>',
         f'6.1 Definition, Causes &amp; Impacts of Climate Change{tag(["2081","2080","2078","2076","2075","2074","2073","2072","2071","2070","2069"])}</h2>'),
        ('6.2 Mitigation Measures of Climate Change</h2>',
         f'6.2 Mitigation Measures of Climate Change{tag(["2078","2073","2072","2069"])}</h2>'),
        ('6.3 International Efforts to Mitigate Climate Change</h2>',
         f'6.3 International Efforts to Mitigate Climate Change{tag(["2080","2079","2078","2077","2076","2075","2073","2070","2069"])}</h2>'),
        ('6.4 Bio-Gas &amp; Organic Farming</h2>',
         f'6.4 Bio-Gas &amp; Organic Farming{tag(["2079","2077"])}</h2>'),
        ('6.5 Deforestation and Its Consequences</h2>',
         f'6.5 Deforestation and Its Consequences{tag(["2077"])}</h2>'),
        ('6.6 Importance of National Parks, Conservation Areas &amp; Forestation in Nepal</h2>',
         f'6.6 Importance of National Parks, Conservation Areas &amp; Forestation in Nepal{tag(["2078","2074","2071"])}</h2>'),
    ]
    for old, new in reps:
        c = c.replace(old, new)

    # ── H3 subtopics ──

    # 6.1: Definition, Causes, Impacts
    c = c.replace(
        '    <p><strong>Difference between Weather and Climate:</strong></p>',
        f'    <h3>6.1.1 Weather vs Climate{tag(["2081"])}</h3>')
    c = c.replace(
        '    <p><strong>Climate Change:</strong> Refers to seasonal changes over a long period',
        f'    <h3>6.1.2 Climate Change &amp; Climate Variability{tag(["2081","2080","2078","2073","2072","2071","2070","2069"])}</h3>\n    <p><strong>Climate Change:</strong> Refers to seasonal changes over a long period')
    c = c.replace(
        '    <p><strong>Examples of Extreme Events:</strong></p>',
        f'    <h3>6.1.3 Extreme Events{tag(["2078"])}</h3>')
    c = c.replace(
        '    <p><strong>A. Natural Causes:</strong></p>',
        f'    <h3>6.1.4 Causes — Natural &amp; Artificial{tag(["2075","2074","2072"])}</h3>\n    <p><strong>A. Natural Causes:</strong></p>')
    c = c.replace(
        '    <p><strong>Impacts (Effects of Global Warming):</strong></p>',
        f'    <h3>6.1.5 Impacts of Climate Change{tag(["2076","2074","2072","2071","2070","2069"])}</h3>')
    c = c.replace(
        '    <p><strong>Climate Change (Greenhouse) Gases:</strong></p>',
        f'    <h3>6.1.6 Greenhouse Gases{tag(["2076"])}</h3>')
    c = c.replace(
        '    <p><strong>Impacts of Climate Change in Nepal:</strong></p>',
        f'    <h3>6.1.7 Impacts in Nepal{tag(["2080","2074","2073","2071","2070"])}</h3>')
    c = c.replace(
        '    <p><strong>Why Act Locally:</strong></p>',
        f'    <h3>6.1.8 Think Globally, Act Locally{tag(["2081"])}</h3>')

    # 6.2: Mitigation
    c = c.replace(
        '    <p><strong>Appropriate Mitigation Measures:</strong></p>',
        f'    <h3>6.2.1 Mitigation Measures{tag(["2078","2072","2069"])}</h3>')
    c = c.replace(
        '    <p><strong>Adaptation Measures from Nepalese Perspective:</strong></p>',
        f'    <h3>6.2.2 Adaptation from Nepalese Perspective{tag(["2073"])}</h3>')

    # 6.3: International Efforts — individual items are already in an ol, just add section-level h3
    c = c.replace(
        '    <p><strong>How Nepal Can Be Streamlined:</strong></p>',
        f'    <h3>6.3.1 Nepal\'s Alignment with International Efforts{tag(["2080","2079","2076","2073","2070"])}</h3>')

    # 6.4: Biogas and Organic Farming
    c = c.replace(
        '    <p><strong>A. Biogas:</strong></p>',
        f'    <h3>6.4.1 Biogas — Production, Uses &amp; Climate Benefits{tag(["2079","2077"])}</h3>')
    c = c.replace(
        '    <p><strong>B. Organic Farming:</strong></p>',
        f'    <h3>6.4.2 Organic Farming{tag(["2079"])}</h3>')

    # 6.5: Deforestation
    c = c.replace(
        '    <p><strong>Key Facts:</strong></p>',
        f'    <h3>6.5.1 Key Facts{tag(["2077"])}</h3>')
    c = c.replace(
        '    <p><strong>Causes of Deforestation:</strong></p>',
        '    <h3>6.5.2 Causes of Deforestation</h3>')
    c = c.replace(
        '    <p><strong>Consequences:</strong></p>',
        '    <h3>6.5.3 Consequences</h3>')
    c = c.replace(
        '    <p><strong>Deforestation in Nepal:</strong></p>',
        '    <h3>6.5.4 Deforestation in Nepal</h3>')
    c = c.replace(
        '    <p><strong>Mitigation Measures:</strong></p>',
        '    <h3>6.5.5 Mitigation Measures</h3>')

    # 6.6: National Parks
    c = c.replace(
        '    <p><strong>National Parks:</strong> Areas of special scenic',
        f'    <h3>6.6.1 National Parks &amp; Conservation Areas</h3>\n    <p><strong>National Parks:</strong> Areas of special scenic')
    c = c.replace(
        '    <p><strong>Importance as GHG Reduction Strategy:</strong></p>',
        f'    <h3>6.6.2 Importance as GHG Reduction Strategy{tag(["2071"])}</h3>')
    c = c.replace(
        '    <p><strong>Forestation Programs:</strong></p>',
        '    <h3>6.6.3 Forestation Programs</h3>')

    with open('chapter6.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Chapter 6: year-tags and subtopics added")


if __name__ == '__main__':
    add_tags_ch5()
    add_tags_ch6()
    print("Done!")

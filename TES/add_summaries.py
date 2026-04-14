"""
Add Quick-Revision Summary with exam frequency table to end of each chapter.
Inserts before </main> tag.
"""

SUMMARIES = {
    "chapter1_updated.html": {
        "title": "Chapter 1 — Technology and Society",
        "total_q": 42,
        "sections": [
            ("1.1", "Definition of Technology", "Defines technology; engineering technology; foundation of civilization", 7, "★★★★"),
            ("1.2", "Impact on Environment &amp; Society", "Positive/negative impacts of technology on environment and society", 8, "★★★★★"),
            ("1.3", "Benefits of New Inventions", "Research, application in transport/health/education/civil engineering", 3, "★★"),
            ("1.4", "Conflict of Technology &amp; Opportunity", "Technology creates conflicts but also enables social transformation", 1, "★"),
            ("1.5", "Appropriate Technology", "Technology suited to local conditions; LDC relevance; indigenous tech in Nepal", 8, "★★★★★"),
            ("1.6", "Intermediate, Labor Based &amp; Intensive", "Definitions and advantages/disadvantages of labor-based vs labor-intensive", 2, "★★"),
            ("1.7", "Shifts in Employment", "Agriculture → Industry → Service → Knowledge economy shifts", 2, "★★"),
            ("1.8", "Unmasking Social Problems &amp; Price Control", "Technology reveals hidden problems; controls commodity prices", 3, "★★"),
            ("1.10", "Technology Is Irreversible", "Once adopted, technology cannot be reversed; breeds further technology", 1, "★"),
            ("1.11", "Agricultural, Industrial &amp; Information Age", "Three-age comparison: resources, economy, social structure", 3, "★★"),
            ("1.12", "Characteristics of Information Society", "Information as economic resource; knowledge workers; global networks", 4, "★★★"),
        ],
        "key_points": [
            "Technology = application of scientific knowledge for practical purposes",
            "Appropriate technology: small-scale, labor-intensive, locally maintainable, affordable",
            "Technology is irreversible — once adopted, it breeds further technology",
            "Information society: knowledge replaces capital as primary resource",
            "Nepal context: biogas, micro-hydro, Rajkulo, terraced farming as indigenous sustainable tech",
            "LEP approach: Labor-based, Environment-friendly, Participatory",
        ]
    },
    "chapter2.html": {
        "title": "Chapter 2 — Development Approaches &amp; Participatory Methods",
        "total_q": 28,
        "sections": [
            ("2.1", "Development Approaches — LEP", "Labor-based, Equipment-intensive, Participatory; merits/demerits", 9, "★★★★★"),
            ("2.2", "Community Management &amp; Engineer as Facilitator", "Community ownership; 8 roles of engineer as facilitator", 8, "★★★★★"),
            ("2.3", "Infrastructure Development Policies of Nepal", "Nepal&rsquo;s 5-year plans, 3 I&rsquo;s, infrastructure policies", 2, "★★"),
            ("2.4", "Ethnographic Approach", "Qualitative research via prolonged community engagement; data methods", 3, "★★"),
            ("2.5", "Participatory Approach as Empowerment", "Community empowerment through participation; evidence from Nepal", 5, "★★★★"),
            ("2.6", "Participatory Tools, FGD &amp; KII", "PRA, KII, FGD, MSC, Outcome Mapping tools (not directly examined)", 0, "—"),
            ("2.7", "Participatory Observation &amp; Questionnaire", "Data collection through observation and structured questionnaires", 0, "—"),
            ("2.8", "Resource Mapping &amp; Wealth Ranking", "Identifying and mobilizing community resources; poverty definition", 1, "★"),
        ],
        "key_points": [
            "LEP = Labor-based + Environment-friendly + Participatory",
            "Engineer as facilitator (not dictator): enables community decision-making",
            "Steps to participation: Manipulation → Information → Consultation → Partnership → Delegated Power",
            "Empowerment = gaining control socially, politically, economically through skills &amp; knowledge",
            "Nepal evidence: community forestry (29% → 40.36%), LEP roads 30–40% lower maintenance costs",
            "Ethnographic approach: participant observation, in-depth interviews, immersive fieldwork",
        ]
    },
    "chapter3.html": {
        "title": "Chapter 3 — Brief History of Human Civilization",
        "total_q": 18,
        "sections": [
            ("3.1", "Early Civilization", "Stone → Bronze → Iron → Middle → Modern ages", 1, "★"),
            ("3.2", "Renaissance of Europe (1300s–1600s)", "Cultural revival; printing press; telescope; scientific revolution", 2, "★★"),
            ("3.3", "Industrial Revolution (1660–1815)", "Steam engine, factories, urbanization, environmental consequences", 4, "★★★"),
            ("3.4", "Industrial → Information Society", "Digital revolution; computers, internet, challenges &amp; opportunities", 5, "★★★★"),
            ("3.5", "World War I &amp; II, Population Explosion", "War technology advances, positive/negative impacts on civilization", 3, "★★"),
            ("3.6", "Rise of Environmental Issues", "Pollution, global warming, ozone depletion, acid rain (not examined)", 0, "—"),
            ("3.7", "Climate Change as Threat", "Drought, disease, food insecurity, extreme weather — with examples", 3, "★★"),
        ],
        "key_points": [
            "Five ages: Stone → Bronze → Iron → Middle → Modern",
            "Renaissance: rebirth of arts/science; Gutenberg press, Copernicus, Galileo, da Vinci",
            "Industrial Revolution: hand production → machine manufacturing; started Britain ~1760",
            "Information society: knowledge replaces capital; internet-connected global village",
            "WWI/WWII: radar, nuclear energy, computers, rocketry; UN/WHO/IMF as positive outcomes",
            "Climate change threatens food security, water supply, health, biodiversity globally",
        ]
    },
    "chapter4.html": {
        "title": "Chapter 4 — Environment &amp; Ecology",
        "total_q": 21,
        "sections": [
            ("4.1", "Definition of Environment", "Physical, chemical, biological surroundings of organisms", 2, "★★"),
            ("4.2", "Importance, Ecology &amp; Ecosystem", "Ecology, food chains, ecosystem characteristics, human disturbance", 5, "★★★★"),
            ("4.3", "Conservation of Environment", "Principles of environmental conservation (not directly examined)", 0, "—"),
            ("4.4", "Optimum Utilization of Natural Resources", "Sustainable resource use; objectives; Nepal examples", 2, "★★"),
            ("4.5", "Renewable &amp; Non-Renewable Resources", "Classification, comparison, examples of each type", 2, "★★"),
            ("4.6", "Conflict of Resources", "Resource conflicts between development &amp; conservation; 5 causes", 2, "★★"),
            ("4.7", "Global Environmental Issues", "Ozone depletion, global warming, biodiversity loss, desertification", 2, "★★"),
            ("4.8", "Environmental Issues of Nepal", "Deforestation, air/water pollution, KTM valley, acid rain, mitigation", 6, "★★★★★"),
        ],
        "key_points": [
            "Environment = totality of external conditions affecting life (physical + chemical + biological)",
            "Ecosystem: nutrient cycling + energy flow + structure; self-regulating, dynamic",
            "Optimum utilization: use resources at minimum cost on a sustainable basis",
            "Renewable (forests, fisheries) vs Non-renewable (coal, oil, gas, minerals)",
            "Nepal: forest cover 29% (1994) → 40.36% (2015); community forestry success",
            "Acid rain: SO₂ + NOₓ → H₂SO₄ + HNO₃; pH &lt; 5.0; damages aquatic life, forests, buildings",
        ]
    },
    "chapter5.html": {
        "title": "Chapter 5 — Water &amp; Air Pollution",
        "total_q": 34,
        "sections": [
            ("5.1", "Fecal-Oral Transmission Route", "F-diagram; 5Fs; primary &amp; secondary barriers", 3, "★★"),
            ("5.2", "Preventive Measures", "WASH: safe water, sanitation, hygiene, health education", 1, "★"),
            ("5.3", "On-Site Sanitation &amp; Eco-Sanitation", "VIP latrines, septic tanks, eco-san (not directly examined)", 0, "—"),
            ("5.4", "Importance of Health Education", "Behavior change, disease prevention, Nepal context", 2, "★★"),
            ("5.5", "Organic Pollution", "BOD, DO sag curve, aerobic/anaerobic digestion", 2, "★★"),
            ("5.6", "Inorganic Pollution", "Heavy metals, nitrate, fluoride, arsenic, pesticides, Bagmati", 4, "★★★"),
            ("5.7", "Sources, Causes &amp; Impacts of Air Pollution", "10 sources, 7 pollutants, health/environmental impacts, KTM valley", 12, "★★★★★"),
            ("5.8", "Mitigation Measures (Air &amp; Water)", "Vehicular, industrial, policy measures; KTM-specific; water mitigation", 8, "★★★★★"),
            ("5.9", "Indoor Air Pollution", "Biomass burning; IAP in Nepal; ICS, biogas, ventilation solutions", 1, "★"),
            ("5.10", "Severity in Nepal", "Yale ranking, brick kilns, health costs, legislative measures", 1, "★"),
        ],
        "key_points": [
            "F-Diagram: Feces → Fluids/Fields/Flies/Fingers/Food → New Host",
            "BOD = Biochemical Oxygen Demand; measures organic pollution strength",
            "10 air pollution sources: fossil fuels, vehicles, combustion, garbage, natural, dust, radioactive, volcanoes, smog, powerlines",
            "Key pollutants: PM₂.₅, CO, SO₂, NOₓ, VOCs, Lead, O₃",
            "KTM valley: bowl-shaped geography traps pollutants; 100+ brick kilns; 1 million+ vehicles",
            "Nepal: 2nd worst air quality (Yale 2014); ~90% energy from biomass; ODF status 2019",
        ]
    },
    "chapter6.html": {
        "title": "Chapter 6 — Climate Change",
        "total_q": 36,
        "sections": [
            ("6.1", "Definition, Causes &amp; Impacts", "Weather vs climate; GHGs; natural/artificial causes; Nepal impacts", 15, "★★★★★"),
            ("6.2", "Mitigation Measures", "Carbon capture, renewables, HEVs; Nepal adaptation strategies", 4, "★★★"),
            ("6.3", "International Efforts", "UNFCCC, Kyoto Protocol, Cancun, GCF, COP 17–23; Nepal alignment", 11, "★★★★★"),
            ("6.4", "Bio-Gas &amp; Organic Farming", "Biogas production/uses/climate benefits; organic farming; Terai suitability", 2, "★★"),
            ("6.5", "Deforestation &amp; Consequences", "Causes, consequences, Nepal data, mitigation measures", 1, "★"),
            ("6.6", "National Parks &amp; Forestation", "Protected areas as GHG sinks; forest programs; how to protect", 3, "★★"),
        ],
        "key_points": [
            "Climate change = long-term alteration of temperature &amp; weather patterns (natural + human causes)",
            "Climate variability ≠ climate change — variability is short-term natural fluctuations",
            "GHG contribution: CO₂ 57%, CFCs 25%, CH₄ 12%, N₂O 6%",
            "Kyoto mechanisms: ETS (Emissions Trading), CDM (Clean Development), JI (Joint Implementation)",
            "Nepal: 1.054 billion tons carbon in forests; 40.36% forest cover; NAPA launched 2010",
            "Biogas: CH₄ 50–70%; introduced Nepal 1974/75; 400,000+ plants installed",
        ]
    }
}


def generate_summary(data):
    """Generate HTML summary section."""
    rows = ""
    for sec_no, title, summary, q_count, freq in data["sections"]:
        bar_width = min(q_count * 6, 100)  # max 100%
        freq_class = "high" if q_count >= 6 else "med" if q_count >= 3 else "low" if q_count >= 1 else "zero"
        rows += f"""        <tr>
          <td><strong>{sec_no}</strong></td>
          <td>{title}</td>
          <td>{summary}</td>
          <td style="text-align:center"><strong>{q_count}</strong></td>
          <td style="text-align:center;white-space:nowrap">{freq}</td>
        </tr>
"""

    key_items = ""
    for pt in data["key_points"]:
        key_items += f"      <li>{pt}</li>\n"

    return f"""
    <!-- ═══ QUICK-REVISION SUMMARY ═══ -->
    <hr style="margin:3rem 0 2rem;border:none;border-top:3px double var(--accent)">
    <h2 style="text-align:center">Quick-Revision Summary</h2>
    <p style="text-align:center;color:var(--muted);margin-bottom:1.5rem">{data["title"]} &mdash; <strong>{data["total_q"]} past exam questions</strong></p>

    <div class="table-wrap">
      <table>
        <thead>
          <tr><th>Section</th><th>Topic</th><th>Key Content</th><th>Qs</th><th>Freq.</th></tr>
        </thead>
        <tbody>
{rows}        </tbody>
      </table>
    </div>

    <h3 style="margin-top:1.5rem">Key Points to Remember</h3>
    <ol>
{key_items}    </ol>

"""


def insert_summary(filename, data):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    summary_html = generate_summary(data)

    # Insert before </main>
    # Handle both indented and non-indented </main>
    import re
    match = re.search(r'\n(\s*)</main>', content)
    if match:
        indent = match.group(1)
        insert_pos = match.start() + 1  # after the newline
        content = content[:insert_pos] + summary_html + content[insert_pos:]
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  {filename}: Summary inserted ({data['total_q']}q, {len(data['sections'])} sections)")
    else:
        print(f"  {filename}: ERROR — could not find </main> tag!")


if __name__ == '__main__':
    for fn, data in SUMMARIES.items():
        insert_summary(fn, data)
    print("Done!")

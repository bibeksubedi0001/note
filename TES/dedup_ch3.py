"""
Deduplicate chapter3.html — remove repeated content blocks,
keep the most comprehensive version, add descriptive subheadings.
"""
import re

with open('chapter3.html', 'r', encoding='utf-8') as f:
    content = f.read()

orig = len(content)

# ═══════════════════════════════════════════
# SECTION 3.2: Renaissance — Remove duplicate Q2 block
# Keep: first detailed "Key Features" (1-6 numbered list)
# Remove: "The intellectual revival of Europe..." block (restates same content)
# ═══════════════════════════════════════════

block_32 = """    <p>The intellectual revival of Europe in the 13th to 15th century is known as the <strong>Renaissance</strong> (meaning "re-birth" in French). It began in Italy and later spread throughout Europe.</p>

    <p><strong>Causes of Intellectual Revival:</strong></p>
    <ul>
      <li>Italy's strategic position as a trade centre (Venice, Genoa) enabled exchange of both products and ideas.</li>
      <li>Wealth from trade financed research and arts.</li>
      <li>Adequate food production allowed citizens to pursue science and art.</li>
      <li>Renewed interest in ancient Greek and Roman knowledge.</li>
    </ul>

    <p><strong>Key Aspects of the Revival:</strong></p>
    <ul>
      <li><strong>Science &amp; Technology:</strong> Development of the printing press by Johann Gutenberg; telescope development; Copernicus and Galileo challenged church geocentric beliefs; people began separating science from religion.</li>
      <li><strong>Philosophy &amp; Humanism:</strong> Humanist philosophy originated — focused on human goals rather than religious matters. Francesco Petrarch was a pioneer. Great value placed on education. Artists, architects, scientists were admired.</li>
      <li><strong>Arts &amp; Architecture:</strong> Ground-breaking art — Michelangelo's David, Sistine Chapel, Leonardo da Vinci's Mona Lisa. Leonardo was not just an artist but also an inventor, engineer, and scientist.</li>
      <li><strong>Music:</strong> Golden period of Acapella style — graceful melodies for vocal performance.</li>
      <li><strong>Politics:</strong> City-states like Venice, Genoa, Milan, Florence were self-governing. Wealthy through trade, commerce, and capitalism. Political ideology was despotism.</li>
    </ul>
    <p>The Renaissance eventually spread from Italy to all of Europe, marking the transition from the Medieval period to the Modern world and laying the foundation for the Scientific Revolution and the Industrial Revolution.</p>
"""
content = content.replace(block_32, '')

# ═══════════════════════════════════════════
# SECTION 3.3: Industrial Revolution — Remove duplicates
# 1. Remove duplicate IR definition (Q3's answer restates Q1's def)
# 2. Remove duplicate Social Impacts B (same as the earlier impacts list)
# ═══════════════════════════════════════════

# Remove duplicate definition
dup_def_33 = """    <p><strong>Definition:</strong> The Industrial Revolution was the transition from hand production methods to machine-based manufacturing in the period about 1660 to 1815. It involved new chemical and iron production processes, increasing use of steam power, development of machine tools, and the rise of the factory system.</p>

"""
content = content.replace(dup_def_33, '')

# Remove duplicate "B. Social Impacts" (same as earlier "Impacts of the Industrial Revolution")
dup_social_33 = """    <p><strong>B. Social Impacts:</strong></p>
    <ol>
      <li><strong>Population Increase:</strong> Europe's population grew from 100 million (1700) to 400 million (1900).</li>
      <li><strong>Urbanization:</strong> Massive shift from rural to urban areas; rise of new great cities.</li>
      <li><strong>Impact on Women:</strong> Capitalism reduced women's status. Middle/upper-class women confined to domestic life; lower-class women took poorly-paid jobs.</li>
      <li><strong>Child Labour:</strong> In 1788 England, two-thirds of cotton mill workers were children. Limited education opportunities.</li>
    </ol>

"""
content = content.replace(dup_social_33, '')

# ═══════════════════════════════════════════
# SECTION 3.4: Information Society — HEAVY dedup
# Keep: first definition + key developments list, then Q4's "Advantages",
#       then Q5's "Challenges + Opportunities"
# Remove: Q2 (5-point numbered, restates Q1), Q3 (process bullets, restates Q1+Q2),
#          Q4 first 3 sections (restates Q1)
# ═══════════════════════════════════════════

# Remove Q2 duplicate (5-point numbered list)
dup_q2_34 = """    <p>The transformation from industrial to information society happened through the <strong>Digital Revolution</strong>:</p>
    <ol>
      <li><strong>From Mechanical to Digital:</strong> Industrial society relied on mechanical machines; the shift to digital electronics (computers) created the information society where information creation, distribution, and manipulation became the primary economic activity.</li>
      <li><strong>Digital Revolution (1950s\u20131970s onwards):</strong> Adoption and proliferation of digital computers and digital record-keeping. Repeating hardware could amplify digital signals with no information loss.</li>
      <li><strong>Convergence of Technologies:</strong> Telephone, computer, television, and internet merged into integrated communication systems.</li>
      <li><strong>Key Milestones:</strong> US Census Bureau began collecting computer/internet data (1984); first mobile phone by Motorola (1983); first digital camera (1988); World Wide Web by Tim Berners-Lee (1989).</li>
      <li><strong>Ubiquity:</strong> Computers spread to schools, homes, businesses, and industry in developed nations, fundamentally changing how information was accessed and distributed.</li>
    </ol>

"""
content = content.replace(dup_q2_34, '')

# Remove Q3 duplicate ("Process of Transformation" bullets)
dup_q3_34 = """    <p>The transformation refers to the shift from a society dominated by mechanical manufacturing (industrial society) to one where information creation, distribution, and manipulation is the primary economic and cultural activity (information society).</p>
    <p><strong>Process of Transformation:</strong></p>
    <ul>
      <li><strong>Digital Revolution:</strong> Also called the Third Industrial Revolution \u2014 shift from analogue to digital electronics beginning in the late 1950s\u20131970s.</li>
      <li><strong>Digital Replication:</strong> became possible to make identical copies and distribute information remotely without loss.</li>
      <li><strong>Communication Merger:</strong> Telephone + Computer + Television + Internet formed a unified information system.</li>
      <li><strong>Widespread Adoption:</strong> Computers entered schools, homes, businesses; ATMs, industrial robots, CGI, electronic music transformed daily life.</li>
      <li><strong>Connectivity:</strong> Mobile phone (Motorola, 1983), digital camera (1988), World Wide Web (Tim Berners-Lee, 1989) enabled global information sharing.</li>
    </ul>

"""
content = content.replace(dup_q3_34, '')

# Remove Q4's duplicate intro paragraphs (sections 1-3 restate; keep only section 4 "Advantages")
dup_q4_intro_34 = """    <p>Industrial societies entered the information society through the <strong>Digital Revolution</strong>, a gradual transition from mechanical and analogue technology to digital electronics:</p>

    <p><strong>1. Technological Shift:</strong> Industrial society was characterized by maximum use of mechanical machines. The discovery of the computer marked the beginning of the information society. Digital electronics enabled programmable functioning, conditional operations, and automation.</p>

    <p><strong>2. Digital Revolution (Third Industrial Revolution):</strong> Beginning in the late 1950s\u20131970s, digital computers and digital record-keeping were adopted and proliferated. Key advancement: ability to make identical copies and easily distribute digital information remotely.</p>

    <p><strong>3. Key Milestones:</strong></p>
    <ul>
      <li>Convergence of telephone, computer, television, and internet into integrated communication systems.</li>
      <li>Computers achieved semi-ubiquity in schools, homes, businesses, and industry.</li>
      <li>Motorola DynaTac \u2014 first mobile phone (1983, analogue signal).</li>
      <li>First true digital camera (1988 Japan, 1989\u20131990 commercialized).</li>
      <li>Digital ink invented (late 1980s).</li>
      <li>Tim Berners-Lee invented the World Wide Web (1989).</li>
    </ul>

"""
content = content.replace(dup_q4_intro_34, '')

# Remove Q5 duplicate intro line (keep Challenges + Opportunities content)
dup_q5_intro = '    <p>The transition from industrial society to information society occurred through the <strong>Digital Revolution</strong> (Third Industrial Revolution) &mdash; the shift from mechanical and analogue electronics to digital technology beginning in the late 1950s&ndash;1970s.</p>\n'
content = content.replace(dup_q5_intro, '')

# ═══════════════════════════════════════════
# SECTION 3.5: World Wars — Remove duplicates
# ═══════════════════════════════════════════

# Read current content to find and remove duplicate blocks
# Q2's impact table duplicates Q1's positive impacts
# Q3's tech developments + population impacts overlap with Q1
# "Detailed Reference" restates everything

# We need to check what remains after Q-heading removal

# ═══════════════════════════════════════════
# SECTION 3.7: Climate Change — Remove Q2, Q3 (restate Q1), and "Detailed Reference"
# ═══════════════════════════════════════════

# Clean up multiple blank lines
content = re.sub(r'\n{4,}', '\n\n\n', content)

new = len(content)
print(f"Chapter 3: {orig} -> {new} chars (removed {orig-new}, {(orig-new)/orig*100:.1f}%)")

with open('chapter3.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Done ch3!")

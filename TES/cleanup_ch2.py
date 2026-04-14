"""Remove duplicate content blocks from chapter2.html"""
import re

with open('chapter2.html', 'r', encoding='utf-8') as f:
    content = f.read()

original_len = len(content)

# ═══════════════════════════════════════════
# SECTION 2.1: LEP — Remove duplicate blocks
# ═══════════════════════════════════════════

# 1. Remove standalone duplicate "LEP stands for..." line before Merits
content = content.replace(
    '    <p><strong>LEP</strong> stands for Labour-based, Environment-friendly, and Participatory development approach.</p>\n    <p><strong>Merits of LEP Approach:</strong></p>',
    '    <p><strong>Merits of LEP Approach:</strong></p>'
)

# 2. Remove duplicate "LEP Approach for Nepal's development combines three strategies" block
# This restates L, E, P + advantages + disadvantages (already covered by lines 96-140)
block_start = '    <p>The LEP Approach for Nepal\'s development combines three strategies:</p>'
block_end = '      <li>Benefits group over individual self-interest.</li>\n    </ol>\n'
idx_start = content.find(block_start)
idx_end = content.find(block_end)
if idx_start != -1 and idx_end != -1:
    content = content[:idx_start] + content[idx_end + len(block_end):]

# 3. Remove duplicate advantages/disadvantages after "Essential Features of Participatory Approach"
# Keep the features list but remove the Advantages and Disadvantages that follow
features_adv_start = '    <p><strong>Advantages:</strong></p>\n    <ol>\n      <li>Cultivates feeling of ownership among participating members'
features_disadv_end = '      <li>Greater chance of clash of ideals and division of ideas.</li>\n    </ol>\n'
idx_fs = content.find(features_adv_start)
idx_fe = content.find(features_disadv_end)
if idx_fs != -1 and idx_fe != -1:
    content = content[:idx_fs] + content[idx_fe + len(features_disadv_end):]

# ═══════════════════════════════════════════
# SECTION 2.2: Community Management — Remove duplicate blocks
# ═══════════════════════════════════════════

# 4. Remove third CM definition + summary (after ladder SVG)
block = '''    <p><strong>Community management</strong> is the management of common pool resources along with the community by the community itself with the help of volunteers and stakeholders.</p>
    <p><strong>Participatory approach for community management:</strong></p>
    <ul>
      <li>Participation is a process through which people influence and share control over planning and decision-making.</li>
      <li>Freedom of thought and expressing views is ensured; opinions and decisions of people count.</li>
      <li>It helps identify weaknesses and strengths, builds self-esteem and capacity.</li>
      <li>Three strategic approaches are used: Learning (analyzing problems, finding solutions), Partnership (developing professional teams), and Empowerment (involving stakeholders at all levels).</li>
      <li>Community development follows three approaches: Top-down (low empowerment), Bottom-up (moderate empowerment), and Partnership/cooperative (high empowerment and sustainable).</li>
    </ul>

'''
content = content.replace(block, '')

# 5. Remove "Part A / Part B" block
part_ab_start = '    <p><strong>Part A — Participatory Approach for Community Management: [4 marks]</strong></p>'
part_ab_end_marker = '      <li><strong>Conflict Resolution:</strong> Solving certain conflicts and interferences.</li>\n    </ol>\n'
idx_pa = content.find(part_ab_start)
idx_pe = content.find(part_ab_end_marker)
if idx_pa != -1 and idx_pe != -1:
    content = content[:idx_pa] + content[idx_pe + len(part_ab_end_marker):]

# 6. Remove fourth CM definition + full duplicate participatory content + engineer's role
block2_start = '    <p><strong>Community Management:</strong></p>\n    <p>Community management is the management of Common Pool Resources (CPR) along with the community as a whole by the community itself with the help of volunteers and stakeholders. It entails all activities around building desired relationships'
block2_end = '    <p><strong>6 C Principles of Community Management:</strong> Content, Cross Promotion, Creating Relationships, Cultivating Relationships, Collaboration, Consistency.</p>\n    <p><strong>Engineer\'s Role as Facilitator:</strong></p>\n    <p>An engineer has technical and management expertise making them an ideal facilitator. Their roles include:</p>\n    <ol>\n      <li>Acting as technical expert and researching</li>\n      <li>Selecting the level, defining borders and work scope for analysis</li>\n      <li>Ensuring all team members understand the process</li>\n      <li>Organizing and directing activities involved</li>\n      <li>Planning, scheduling, and leading meetings</li>\n      <li>Focal point in communication, recognizing training needs and encouraging the team</li>\n      <li>Solving certain conflicts and interferences</li>\n    </ol>\n'
idx_b2s = content.find(block2_start)
idx_b2e = content.find(block2_end)
if idx_b2s != -1 and idx_b2e != -1:
    content = content[:idx_b2s] + content[idx_b2e + len(block2_end):]

# 7. Remove duplicate "engineer in community-led development" block
block3 = '''    <p>An engineer has technical and management expertise making them an ideal facilitator in community-led development projects. Their roles include:</p>
    <ol>
      <li><strong>Technical Expert:</strong> Providing technical knowledge, researching solutions, and ensuring project feasibility.</li>
      <li><strong>Defining Scope:</strong> Selecting the level, defining borders and work scope for analysis.</li>
      <li><strong>Process Facilitation:</strong> Ensuring all team members understand the development process and objectives.</li>
      <li><strong>Organizing Activities:</strong> Directing and coordinating all activities involved in the project.</li>
      <li><strong>Meeting Management:</strong> Planning, scheduling, and leading meetings with community stakeholders.</li>
      <li><strong>Communication Hub:</strong> Serving as the focal point in communication, recognizing training needs, and encouraging the team.</li>
      <li><strong>Conflict Resolution:</strong> Solving conflicts and interferences between stakeholders.</li>
    </ol>
    <p>The engineer must balance technical requirements with community needs, using the partnership approach (high empowerment, sustainable development) rather than a top-down approach.</p>

'''
content = content.replace(block3, '')

# 8. Remove "Community Development" + Engineer's Role (another duplicate)
block4_start = '    <p><strong>Community Development</strong> has two interlinked goals'
block4_end = '    <p>Engineers should adopt the Partnership approach, following the 6 C Principles of Community Management: Content, Cross Promotion, Creating Relationships, Cultivating Relationships, Collaboration, and Consistency.</p>\n'
idx_b4s = content.find(block4_start)
idx_b4e = content.find(block4_end)
if idx_b4s != -1 and idx_b4e != -1:
    content = content[:idx_b4s] + content[idx_b4e + len(block4_end):]

# 9. Remove last CM definition + engineer's role before SVGs
block5 = '''    <p><strong>Community Management</strong> is the management of Common Pool Resources (CPR) by the community itself with the help of volunteers and stakeholders. It entails all activities around building desired relationships, creating value, and connecting organizations to communities.</p>
    <p><strong>Engineer's Role:</strong></p>
    <ol>
      <li>Acting as technical expert and researching appropriate solutions</li>
      <li>Selecting the level, defining borders and work scope for analysis</li>
      <li>Ensuring all team members understand the process</li>
      <li>Organizing and directing activities involved</li>
      <li>Planning, scheduling, and leading meetings</li>
      <li>Focal point in communication, recognizing training needs and encouraging the team</li>
      <li>Solving conflicts and interferences between stakeholder groups</li>
    </ol>

'''
content = content.replace(block5, '')

# ═══════════════════════════════════════════
# SECTION 2.3: Infrastructure Policies — Remove duplicate summary lists
# ═══════════════════════════════════════════

# 10. Remove first duplicate summary list
block6 = '''    <p>Nepal\'s strategic vision for development is based on 3 "I"s: <strong>Inclusion, Investment, and Infrastructure</strong>. Key features of Nepal\'s infrastructure development policies include:</p>
    <ol>
      <li><strong>Periodic Plans:</strong> Nepal has implemented 15 periodic plans since 2013 BS, evolving from basic local infrastructure improvement (1st plan) to ambitious targets like 10.3% economic growth and 90% literacy (15th plan, 2076/77–2080/81).</li>
      <li><strong>Agricultural Perspective Plan (APP, 1997–2017):</strong> Focuses on agricultural technology, road and power infrastructure, irrigation, and chemical fertilizer to reduce poverty.</li>
      <li><strong>20-Year Road Plan (2002–2022):</strong> Strengthening political/administrative linkages, alleviating poverty, developing economic potential, minimizing transportation cost and environmental impacts.</li>
      <li><strong>National Transport Policy (2001):</strong> Develop reliable, cost-effective, safe, and sustainable transportation — district roads, village roads, agricultural roads.</li>
      <li><strong>Priority Investment Plan (1997–2007):</strong> Guidance for road development. Nepal Roads Board Act (2002).</li>
      <li><strong>Local Self Government Act (1999):</strong> Empowering local bodies for infrastructure development.</li>
      <li><strong>Infrastructure Gap:</strong> Nepal needs to invest 10-15% of national income to bridge the infrastructure gap. 1% increase in infrastructure stock associates with 1% increase in GDP.</li>
    </ol>

'''
content = content.replace(block6, '')

# 11. Remove second duplicate summary list
block7 = '''    <p>Key features of Nepal\'s infrastructure development policies:</p>
    <ol>
      <li><strong>Periodic Development Plans:</strong> 15 plans from 2013 BS to present, each focusing on infrastructure improvement, poverty alleviation, and economic growth.</li>
      <li><strong>Sectoral Policies:</strong> APP for agriculture, 20-Year Road Plan for transportation, National Transport Policy for sustainable transport systems.</li>
      <li><strong>LEP Approach:</strong> Labour-based, environment-friendly, and participatory development as guiding principle.</li>
      <li><strong>Investment Target:</strong> 10-15% of national income needed for infrastructure; focus on both economic infrastructure (roads, electricity, telecom) and social infrastructure (education, health).</li>
      <li><strong>Decentralization:</strong> Local Self Government Act (1999) empowering local bodies for development.</li>
    </ol>

'''
content = content.replace(block7, '')

# ═══════════════════════════════════════════
# SECTION 2.4: Ethnographic — Remove duplicate blocks
# ═══════════════════════════════════════════

# 12. Remove "Application in Community Management" duplicate
block8 = '''    <p>The ethnographic approach is valuable for community management because it involves studying people in their own cultural context to understand their needs, behaviors, and social structures.</p>
    <p><strong>Application in Community Management:</strong></p>
    <ul>
      <li><strong>Understanding Culture:</strong> Searching for meaning of cultural norms, views, and reasons for certain behaviors and practices.</li>
      <li><strong>Social Interactions:</strong> Examining social trends, instances, interactions, and encounters within the community.</li>
      <li><strong>Family &amp; Organization Roles:</strong> Understanding the roles of families, relationships, and organizations in community dynamics.</li>
      <li><strong>Data Collection:</strong> Using content, artifacts, and interactions to collect data. Methods include participant observation, case studies, and focus groups.</li>
    </ul>
    <p>The ethnographic approach helps managers and engineers understand community needs from the inside, enabling more effective participatory development rather than imposing top-down solutions.</p>

'''
content = content.replace(block8, '')

# 13. Remove "Detailed Reference" block in 2.4
block9_start = '    <p><strong>Detailed Reference:</strong></p>\n    <p><strong>Definition:</strong></p>\n    <p>Ethnography literally means'
block9_end = '      <li>Focus groups</li>\n    </ul>\n'
idx_b9s = content.find(block9_start)
idx_b9e = content.find(block9_end, idx_b9s) if idx_b9s != -1 else -1
if idx_b9s != -1 and idx_b9e != -1:
    content = content[:idx_b9s] + content[idx_b9e + len(block9_end):]

# ═══════════════════════════════════════════
# SECTION 2.5: Participatory Empowerment — Remove duplicate blocks
# ═══════════════════════════════════════════

# 14. Remove second "participatory approach encourages community empowerment" block
block10 = '''    <p>The participatory approach encourages community empowerment through several mechanisms:</p>
    <p><strong>Importance of Participation:</strong></p>
    <ul>
      <li><strong>Freedom of thought:</strong> Expressing views and participating in community life</li>
      <li><strong>Opinions count:</strong> Acknowledging people as active and competent</li>
      <li><strong>Identify strengths and weaknesses:</strong> Self-assessment and directed guidance</li>
      <li><strong>Build self-esteem and capacity</strong></li>
    </ul>
    <p><strong>Scale of Participation:</strong></p>
    <ul>
      <li><strong>Extractive:</strong> Rapid expert analysis, questionnaires, key informants — opinions shared but not power</li>
      <li><strong>Empowering:</strong> In-depth joint analysis, learning and action, visual diagrams, group discussions, active participation</li>
    </ul>
    <p><strong>Steps to Empowerment:</strong> Manipulation (non-participation) → Information → Consultation (tokenism) → Partnership → Delegated Power (citizen power).</p>
    <p><strong>Community Development Approaches:</strong></p>
    <ul>
      <li>Top-down: Static, passive — low empowerment</li>
      <li>Bottom-up: Active, dynamic — moderate empowerment</li>
      <li>Partnership: Working together — high empowerment and sustainable</li>
    </ul>

'''
content = content.replace(block10, '')

# 15. Remove third empowerment definition ("Empowerment is a process of change...")
block11_start = '    <p><strong>Empowerment</strong> is a process of change enabling individuals or groups'
block11_end = '    <p><strong>Development Approaches:</strong> Top-down (low empowerment), Bottom-up (moderate empowerment), Partnership (high empowerment and sustainable). The goals of community development are: (1) improve quality of life of all members, (2) involve all members in the process.</p>\n'
idx_b11s = content.find(block11_start)
idx_b11e = content.find(block11_end)
if idx_b11s != -1 and idx_b11e != -1:
    content = content[:idx_b11s] + content[idx_b11e + len(block11_end):]

# 16. Remove short summary paragraph
block12 = '    <p>Participatory approach empowers communities by providing people with freedom of thought and expression, acknowledging their competence, helping them identify strengths and weaknesses, and building self-esteem and capacity. It moves from extractive (expert-driven) to empowering (community-driven joint analysis), following the partnership model for high empowerment and sustainability.</p>\n\n'
content = content.replace(block12, '')

# 17. Remove "Yes, participatory approaches empower communities" justification (duplicate of first block's content)
block13_start = '    <p><strong>Yes, participatory approaches empower communities.</strong> Justification:</p>'
block13_end = '      <li><strong>Self-Efficacy:</strong> Communities gain decision-making ability, build self-esteem, and develop skills to manage challenges, moving from dependency to self-reliance.</li>\n    </ol>\n'
idx_b13s = content.find(block13_start)
idx_b13e = content.find(block13_end)
if idx_b13s != -1 and idx_b13e != -1:
    content = content[:idx_b13s] + content[idx_b13e + len(block13_end):]

# 18. Remove "Detailed Reference" section in 2.5
block14_start = '    <p><strong>Detailed Reference:</strong></p>\n    <p><strong>Definition:</strong></p>\n    <p>Participation is a process through which people influence'
block14_end_marker = '      <li><strong>Delegated Power:</strong> Authorization to act as representative through negotiations — Citizen Power</li>\n    </ol>\n'
idx_b14s = content.find(block14_start)
idx_b14e = content.find(block14_end_marker, idx_b14s) if idx_b14s != -1 else -1
if idx_b14s != -1 and idx_b14e != -1:
    content = content[:idx_b14s] + content[idx_b14e + len(block14_end_marker):]

# 19. Remove duplicate "Community Development Approaches" table at end of 2.5 (keep the content leading to SVGs)
block15 = '''    <p><strong>Community Development Approaches:</strong></p>
    <table>
      <thead>
        <tr><th>Approach</th><th>Participation</th><th>Empowerment</th></tr>
      </thead>
      <tbody>
        <tr><td>Top-down</td><td>As a means (static, passive, controllable)</td><td>Low empowerment</td></tr>
        <tr><td>Bottom-up</td><td>As an end (active, dynamic, self-mobilization)</td><td>Moderate empowerment</td></tr>
        <tr><td>Partnership</td><td>Working together</td><td>High empowerment and sustainable</td></tr>
      </tbody>
    </table>

'''
# Only remove if it appears in section 2.5 (not 2.2's table)
idx_25_header = content.find('2.5 Participatory Approach as Community Empowerment')
idx_table = content.find(block15, idx_25_header) if idx_25_header != -1 else -1
if idx_table != -1:
    content = content[:idx_table] + content[idx_table + len(block15):]

# ═══════════════════════════════════════════
# Clean up multiple blank lines
# ═══════════════════════════════════════════
content = re.sub(r'\n{4,}', '\n\n\n', content)

# Report
new_len = len(content)
print(f"Original: {original_len} chars")
print(f"Cleaned:  {new_len} chars")
print(f"Removed:  {original_len - new_len} chars ({(original_len - new_len) / original_len * 100:.1f}%)")

with open('chapter2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done! chapter2.html cleaned.")

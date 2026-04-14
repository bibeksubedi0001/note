"""
Add EPP-style year-tags and subtopic numbering to TES chapter1_updated.html.
Transforms h2/h3/h4 headings to include year-tags and proper numbering.
"""
import re

with open('chapter1_updated.html', 'r', encoding='utf-8') as f:
    content = f.read()

original = content

# ════════════════════════════════════════════════════
# HEADING REPLACEMENTS — h2 get year-tags on section level
# ════════════════════════════════════════════════════

h2_replacements = {
    # 1.1: asked 2081,2080,2079,2078,2074,2072(x2)
    '<h2>1.1 Definition of Technology</h2>':
        '<h2>1.1 Definition of Technology <span class="year-tag">2081</span><span class="year-tag">2080</span><span class="year-tag">2079</span><span class="year-tag">2078</span><span class="year-tag">2074</span><span class="year-tag">2072</span></h2>',

    # 1.2: asked 2079(x2),2078,2073,2072,2071,2070,2069
    '<h2>1.2 Impact of Technology on Environment &amp; Society</h2>':
        '<h2>1.2 Impact of Technology on Environment &amp; Society <span class="year-tag">2079</span><span class="year-tag">2078</span><span class="year-tag">2073</span><span class="year-tag">2072</span><span class="year-tag">2071</span><span class="year-tag">2070</span><span class="year-tag">2069</span></h2>',

    # 1.3: asked 2079,2074,2072
    '<h2>1.3 Benefits of Technology Due to New Inventions</h2>':
        '<h2>1.3 Benefits of Technology Due to New Inventions <span class="year-tag">2079</span><span class="year-tag">2074</span><span class="year-tag">2072</span></h2>',

    # 1.4: asked 2077
    '<h2>1.4 Conflict of Technology &amp; Technology Creates Opportunity for Society to Change</h2>':
        '<h2>1.4 Conflict of Technology &amp; Technology Creates Opportunity for Society to Change <span class="year-tag">2077</span></h2>',

    # 1.5: asked 2079,2077,2075,2074,2073(x2),2071(x2)
    '<h2>1.5 Appropriate Technology</h2>':
        '<h2>1.5 Appropriate Technology <span class="year-tag">2079</span><span class="year-tag">2077</span><span class="year-tag">2075</span><span class="year-tag">2074</span><span class="year-tag">2073</span><span class="year-tag">2071</span></h2>',

    # 1.6: asked 2079,2078
    '<h2>1.6 Intermediate Technology, Labour Based &amp; Labour Intensive Technology</h2>':
        '<h2>1.6 Intermediate Technology, Labour Based &amp; Labour Intensive Technology <span class="year-tag">2079</span><span class="year-tag">2078</span></h2>',

    # 1.7: asked 2073,2069
    '<h2>1.7 Shifts in Employment Due to Technological Advancement</h2>':
        '<h2>1.7 Shifts in Employment Due to Technological Advancement <span class="year-tag">2073</span><span class="year-tag">2069</span></h2>',

    # 1.8: asked 2076,2075,2069
    '<h2>1.8 Role of Technology to Unmask Old Social Problems &amp; Society\'s Control of Technology</h2>':
        '<h2>1.8 Role of Technology to Unmask Old Social Problems &amp; Society\'s Control of Technology <span class="year-tag">2076</span><span class="year-tag">2075</span><span class="year-tag">2069</span></h2>',

    # 1.10: asked 2081,2078
    '<h2>1.10 Technology Is Irreversible</h2>':
        '<h2>1.10 Technology Is Irreversible <span class="year-tag">2081</span><span class="year-tag">2078</span></h2>',

    # 1.11: asked 2076,2070,2069
    '<h2>1.11 Agricultural Age, Industrial Age and Information Age</h2>':
        '<h2>1.11 Agricultural Age, Industrial Age and Information Age <span class="year-tag">2076</span><span class="year-tag">2070</span><span class="year-tag">2069</span></h2>',

    # 1.12: asked 2072,2071,2073,2070
    '<h2>1.12 Characteristics of Information Society</h2>':
        '<h2>1.12 Characteristics of Information Society <span class="year-tag">2073</span><span class="year-tag">2072</span><span class="year-tag">2071</span><span class="year-tag">2070</span></h2>',
}

for old, new in h2_replacements.items():
    content = content.replace(old, new)

# ════════════════════════════════════════════════════
# h3 subtopics → numbered + year-tagged
# ════════════════════════════════════════════════════

h3_replacements = {
    # Section 1.1
    '<h3>Characteristics of Technology</h3>':
        '<h3>1.1.1 Characteristics of Technology <span class="year-tag">2080</span></h3>',

    '<h3>Technology as the Foundation of Civilization</h3>':
        '<h3>1.1.2 Technology as the Foundation of Civilization <span class="year-tag">2072</span></h3>',

    # Section 1.8
    '<h3>Technology Controlling the Price of Basic Commodities</h3>':
        '<h3>1.8.1 Technology Controlling the Price of Basic Commodities <span class="year-tag">2075</span><span class="year-tag">2069</span></h3>',

    # Section 1.10
    '<h3>Definitions: Technology, Environment, and Society</h3>':
        '<h3>1.10.1 Definitions: Technology, Environment, and Society <span class="year-tag">2081</span></h3>',

    # Section 1.12
    '<h3>Impact of Computers and Cybernetics on Creating Information Society</h3>':
        '<h3>1.12.1 Impact of Computers and Cybernetics on Creating Information Society <span class="year-tag">2070</span></h3>',
}

for old, new in h3_replacements.items():
    content = content.replace(old, new)

# ════════════════════════════════════════════════════
# h4 subtopics in section 1.2 → numbered + year-tagged
# ════════════════════════════════════════════════════

h4_replacements_12 = {
    '<h4>Positive Impacts on Society:</h4>':
        '<h3>1.2.1 Positive Impacts on Society <span class="year-tag">2079</span><span class="year-tag">2078</span><span class="year-tag">2073</span><span class="year-tag">2072</span><span class="year-tag">2071</span><span class="year-tag">2070</span></h3>',

    '<h4>Negative Impacts on Society:</h4>':
        '<h3>1.2.2 Negative Impacts on Society <span class="year-tag">2079</span><span class="year-tag">2078</span><span class="year-tag">2073</span><span class="year-tag">2070</span></h3>',

    '<h4>Positive Impacts on Environment:</h4>':
        '<h3>1.2.3 Positive Impacts on Environment <span class="year-tag">2079</span><span class="year-tag">2078</span><span class="year-tag">2073</span></h3>',

    '<h4>Negative Impacts on Environment:</h4>':
        '<h3>1.2.4 Negative Impacts on Environment <span class="year-tag">2079</span><span class="year-tag">2078</span><span class="year-tag">2073</span></h3>',

    '<h4>Impact Summary Table:</h4>':
        '<h3>1.2.5 Impact Summary Table</h3>',

    '<h4>Impact on Nepalese Society:</h4>':
        '<h3>1.2.6 Impact on Nepalese Society <span class="year-tag">2069</span></h3>',
}

for old, new in h4_replacements_12.items():
    content = content.replace(old, new)

# ════════════════════════════════════════════════════
# h4 subtopics in section 1.3 → numbered + year-tagged
# ════════════════════════════════════════════════════

# Need to find actual h4 content in section 1.3
h4_replacements_13 = {
    '<h4>Benefits of Technology in Education:</h4>':
        '<h3>1.3.1 Benefits of Technology in Education <span class="year-tag">2072</span></h3>',

    '<h4>Benefits of Technology for Civil Engineering:</h4>':
        '<h3>1.3.2 Benefits of Technology for Civil Engineering <span class="year-tag">2074</span></h3>',
}

for old, new in h4_replacements_13.items():
    content = content.replace(old, new)

# ════════════════════════════════════════════════════
# h4 subtopics in section 1.5 → numbered + year-tagged
# ════════════════════════════════════════════════════

# Section 1.5 has h4 blocks for LDC relevance, sustainable dev, indigenous tech
# Let me check what h4s exist and convert them

# 1.6 has Advantages and Disadvantages h4
h4_replacements_16 = {
    '<h4>Advantages and Disadvantages:</h4>':
        '<h3>1.6.1 Advantages and Disadvantages <span class="year-tag">2079</span></h3>',
}

for old, new in h4_replacements_16.items():
    content = content.replace(old, new)

# ════════════════════════════════════════════════════
# Report
# ════════════════════════════════════════════════════

count_yt = content.count('year-tag')
print(f"Year-tags added: {count_yt}")
print(f"h2 replacements: {sum(1 for k in h2_replacements if k not in content)}")

# Verify all h2 have year-tags
import re
h2s = re.findall(r'<h2>.*?</h2>', content)
for h in h2s:
    has_yt = 'year-tag' in h
    print(f"  {'✓' if has_yt else '✗'} {h[:80]}...")

with open('chapter1_updated.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("\nDone! chapter1_updated.html updated with year-tags and subtopic numbering.")

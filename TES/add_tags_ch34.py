"""
Add year-tags to h2 headings and convert content blocks to numbered h3 subtopics
for TES chapters 3 and 4. Follows EPP format (like chapters 1 and 2).
"""

def add_tags_ch3():
    with open('chapter3.html', 'r', encoding='utf-8') as f:
        c = f.read()

    def yt(year):
        return f'<span class="year-tag">{year}</span>'

    # === H2 YEAR TAGS ===
    c = c.replace(
        '<h2>3.1 Early Civilization</h2>',
        f'<h2>3.1 Early Civilization {yt(2070)}</h2>')
    c = c.replace(
        '<h2>3.2 Great Renaissance of Europe (1300s\u20131600s)</h2>',
        f'<h2>3.2 Great Renaissance of Europe (1300s\u20131600s) {yt(2077)}{yt(2071)}</h2>')
    c = c.replace(
        '<h2>3.3 Early Part of Industrial Revolution (1660\u20131815)</h2>',
        f'<h2>3.3 Early Part of Industrial Revolution (1660\u20131815) {yt(2080)}{yt(2079)}{yt(2073)}{yt(2070)}</h2>')
    c = c.replace(
        '<h2>3.4 Transformation of Industrial Society into Information Society</h2>',
        f'<h2>3.4 Transformation of Industrial Society into Information Society {yt(2081)}{yt(2078)}{yt(2071)}{yt(2069)}</h2>')
    c = c.replace(
        '<h2>3.5 Impact of World War I and II, Population Explosion</h2>',
        f'<h2>3.5 Impact of World War I and II, Population Explosion {yt(2074)}{yt(2070)}</h2>')
    # 3.6 has no exam questions
    c = c.replace(
        '<h2>3.7 Climate Change as a Threat to Human Civilization</h2>',
        f'<h2>3.7 Climate Change as a Threat to Human Civilization {yt(2079)}</h2>')

    # === SECTION 3.3 SUBTOPICS ===
    c = c.replace(
        '<p><strong>Impacts of the Industrial Revolution:</strong></p>',
        f'<h3>3.3.1 Impacts of the Industrial Revolution {yt(2070)}</h3>')
    c = c.replace(
        '<p><strong>Environmental Consequences:</strong></p>',
        f'<h3>3.3.2 Environmental Consequences {yt(2080)}</h3>')
    c = c.replace(
        '<p><strong>A. Important Technological Developments:</strong></p>',
        f'<h3>3.3.3 Important Technological Developments {yt(2073)}</h3>')
    c = c.replace(
        '<p><strong>C. Industrial Revolution in America:</strong></p>',
        '<h3>3.3.4 Industrial Revolution in America</h3>')
    c = c.replace(
        '<p><strong>D. Impacts in Nepal:</strong></p>',
        '<h3>3.3.5 Impacts in Nepal</h3>')
    c = c.replace(
        '<p><strong>E. Major Early Events Timeline:</strong></p>',
        '<h3>3.3.6 Major Early Events Timeline</h3>')

    # === SECTION 3.4 SUBTOPICS ===
    c = c.replace(
        '<p><strong>Key developments in the transformation:</strong></p>',
        f'<h3>3.4.1 Key Developments in the Transformation {yt(2078)}{yt(2069)}</h3>')
    c = c.replace(
        '<p><strong>4. Advantages of Information Society:</strong></p>',
        f'<h3>3.4.2 Advantages of Information Society {yt(2071)}</h3>')
    c = c.replace(
        '<p><strong>Challenges of the Transition:</strong></p>',
        f'<h3>3.4.3 Challenges of the Transition {yt(2081)}</h3>')
    c = c.replace(
        '<p><strong>Opportunities of the Transition:</strong></p>',
        f'<h3>3.4.4 Opportunities of the Transition {yt(2081)}</h3>')

    # === SECTION 3.5 SUBTOPICS ===
    # WWI heading (keep bold paragraph, wrap in h3)
    c = c.replace(
        '    <p><strong>World War I (1914\u20131919):</strong></p>\n    <p><strong>Causes:</strong> Alliances',
        f'    <h3>3.5.1 World War I (1914\u20131919) {yt(2074)}{yt(2070)}</h3>\n    <p><strong>Causes:</strong> Alliances')
    c = c.replace(
        '    <p><strong>World War II (1939\u20131945):</strong></p>\n    <p><strong>Causes:</strong> Treaty of Versailles',
        f'    <h3>3.5.2 World War II (1939\u20131945) {yt(2074)}{yt(2070)}</h3>\n    <p><strong>Causes:</strong> Treaty of Versailles')
    c = c.replace(
        '<p><strong>Positive Impacts:</strong></p>',
        f'<h3>3.5.3 Positive and Negative Impacts {yt(2074)}{yt(2070)}</h3>\n    <p><strong>Positive Impacts:</strong></p>')
    c = c.replace(
        '<p><strong>Key Technological Developments:</strong></p>',
        f'<h3>3.5.4 Key Technological Developments {yt(2070)}</h3>')
    c = c.replace(
        '<p><strong>Population Explosion:</strong></p>',
        f'<h3>3.5.5 Population Explosion</h3>')

    with open('chapter3.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Chapter 3: year-tags and subtopics added.")


def add_tags_ch4():
    with open('chapter4.html', 'r', encoding='utf-8') as f:
        c = f.read()

    def yt(year):
        return f'<span class="year-tag">{year}</span>'

    # === H2 YEAR TAGS ===
    c = c.replace(
        '<h2>4.1 Definition of Environment</h2>',
        f'<h2>4.1 Definition of Environment {yt(2073)}{yt(2070)}</h2>')
    c = c.replace(
        '<h2>4.2 Importance, Ecology &amp; Ecosystem</h2>',
        f'<h2>4.2 Importance, Ecology &amp; Ecosystem {yt(2074)}{yt(2072)}{yt(2071)}{yt(2070)}{yt(2069)}</h2>')
    # 4.3 has no exam questions
    c = c.replace(
        '<h2>4.4 Optimum Utilization of Natural Resources</h2>',
        f'<h2>4.4 Optimum Utilization of Natural Resources {yt(2081)}{yt(2079)}</h2>')
    c = c.replace(
        '<h2>4.5 Renewable and Non-Renewable Resources</h2>',
        f'<h2>4.5 Renewable and Non-Renewable Resources {yt(2079)}{yt(2071)}</h2>')
    c = c.replace(
        '<h2>4.6 Conflict of Resources</h2>',
        f'<h2>4.6 Conflict of Resources {yt(2081)}{yt(2078)}</h2>')
    c = c.replace(
        '<h2>4.7 Global Environmental Issues</h2>',
        f'<h2>4.7 Global Environmental Issues {yt(2079)}{yt(2077)}</h2>')
    c = c.replace(
        '<h2>4.8 Environmental Issues of Nepal</h2>',
        f'<h2>4.8 Environmental Issues of Nepal {yt(2080)}{yt(2074)}{yt(2072)}{yt(2070)}{yt(2069)}</h2>')

    # === SECTION 4.2 SUBTOPICS ===
    c = c.replace(
        '<p><strong>Ecology:</strong> Ecology is the branch of biology concerned with the relations',
        f'<h3>4.2.1 Ecology and Ecosystem {yt(2071)}{yt(2069)}</h3>\n    <p><strong>Ecology:</strong> Ecology is the branch of biology concerned with the relations')
    c = c.replace(
        '<p><strong>How increasing population disturbs the ecosystem:</strong></p>',
        f'<h3>4.2.2 Population Disturbance to Ecosystem {yt(2070)}</h3>')
    c = c.replace(
        '<p><strong>How to minimize the disturbance:</strong></p>',
        f'<h3>4.2.3 Minimizing the Disturbance {yt(2070)}</h3>')
    c = c.replace(
        '<p>Human interventions in the ecosystem are driven by the following primary reasons:</p>',
        f'<h3>4.2.4 Human Interventions in the Ecosystem {yt(2074)}{yt(2072)}</h3>\n    <p>Human interventions in the ecosystem are driven by the following primary reasons:</p>')
    c = c.replace(
        '<p><strong>How natural resources are converted into wealth:</strong></p>',
        f'<h3>4.2.5 Conversion of Natural Resources into Wealth {yt(2072)}</h3>')

    # === SECTION 4.4 SUBTOPICS ===
    c = c.replace(
        '<p><strong>Objectives of Optimum Utilization:</strong></p>',
        f'<h3>4.4.1 Objectives of Optimum Utilization {yt(2081)}{yt(2079)}</h3>')
    c = c.replace(
        '<p><strong>Types of Resources:</strong></p>',
        f'<h3>4.4.2 Types of Resources {yt(2079)}</h3>')

    # === SECTION 4.6 SUBTOPICS ===
    c = c.replace(
        '<p><strong>Causes of Resource Conflicts:</strong></p>',
        f'<h3>4.6.1 Causes of Resource Conflicts {yt(2078)}</h3>')

    # === SECTION 4.7 SUBTOPICS ===
    c = c.replace(
        '<p><strong>Regional Environmental Issues:</strong>',
        f'<h3>4.7.1 Regional and Global Environmental Issues {yt(2079)}{yt(2077)}</h3>\n    <p><strong>Regional Environmental Issues:</strong>')
    c = c.replace(
        '<p><strong>Factors Contributing to Global Warming:</strong></p>',
        f'<h3>4.7.2 Factors Contributing to Global Warming {yt(2079)}</h3>')

    # === SECTION 4.8 SUBTOPICS ===
    c = c.replace(
        '<p>Nepal faces several major environmental issues:</p>',
        f'<h3>4.8.1 Major Environmental Issues {yt(2074)}{yt(2072)}{yt(2070)}{yt(2069)}</h3>\n    <p>Nepal faces several major environmental issues:</p>')
    c = c.replace(
        '<p><strong>Key Environmental Issues in Kathmandu Valley:</strong></p>',
        f'<h3>4.8.2 Environmental Issues of Kathmandu Valley {yt(2080)}</h3>')
    c = c.replace(
        '<p><strong>Corrective Measures (General):</strong></p>',
        f'<h3>4.8.3 Causes and Mitigation Measures {yt(2074)}</h3>')
    c = c.replace(
        '<p><strong>Causes of Acid Rain:</strong></p>',
        f'<h3>4.8.4 Causes of Acid Rain {yt(2072)}</h3>')

    with open('chapter4.html', 'w', encoding='utf-8') as f:
        f.write(c)
    print("Chapter 4: year-tags and subtopics added.")


if __name__ == '__main__':
    add_tags_ch3()
    add_tags_ch4()
    print("Done!")

"""
Comprehensive deduplication for TES chapters 3 and 4.
Removes duplicate content blocks, adds missing exam-note box to 3.2.
"""
import re

def process_chapter3():
    with open('chapter3.html', 'r', encoding='utf-8') as f:
        content = f.read()
    original = len(content)

    # 1. Add exam-note box to section 3.2 (missing)
    marker = '<h2>3.2 Great Renaissance of Europe (1300s\u20131600s)</h2>'
    exam_box = '''<h2>3.2 Great Renaissance of Europe (1300s\u20131600s)</h2>

    <div class="exam-note">
      <h4>PAST EXAM QUESTIONS:</h4>
      <ol>
        <li>Explain the role played by Renaissance period in the development of science and technology. [3] <em>(2077 Chaitra, Q3a)</em></li>
        <li>Describe important features of Renaissance Period. [4] <em>(2071 Magh, Q4)</em></li>
      </ol>
    </div>'''
    content = content.replace(marker + '\n\n    <p><strong>Renaissance</strong>',
                              exam_box + '\n\n    <p><strong>Renaissance</strong>')

    # 2. Section 3.5: Remove first duplicate table (impacts in table form + death stats)
    block_start = '    <p>The World Wars had profound impacts on society:</p>\n    <table>'
    block_end = '70% industry collapsed after WWII.</p>\n'
    idx_s = content.find(block_start)
    idx_e = content.find(block_end)
    if idx_s != -1 and idx_e != -1:
        content = content[:idx_s] + content[idx_e + len(block_end):]

    # 3. Section 3.5: Remove "Detailed Reference" block (keep Population Explosion)
    dr_start = '    <p><strong>Detailed Reference:</strong></p>\n\n    <p><strong>World War I (1914'
    pop_marker = '    <p><strong>Population Explosion:</strong></p>'
    idx_s = content.find(dr_start)
    idx_e = content.find(pop_marker)
    if idx_s != -1 and idx_e != -1:
        content = content[:idx_s] + content[idx_e:]

    # 4. Section 3.7: Remove second block (7 threats + evidence line)
    block2_start = '    <p>Climate change \u2014 the change in global/regional climate patterns'
    block2_end = 'arctic sea ice loss, vegetation changes, sea level rise.</p>\n'
    idx_s = content.find(block2_start)
    idx_e = content.find(block2_end)
    if idx_s != -1 and idx_e != -1:
        content = content[:idx_s] + content[idx_e + len(block2_end):]

    # 5. Section 3.7: Remove third block (evidences list + threats + philosophical paragraph)
    block3_start = '    <p>Climate change \u2014 driven by increased CO2 from fossil fuel use'
    block3_end = 'all creatures on the planet.</p>\n'
    idx_s = content.find(block3_start)
    idx_e = content.find(block3_end)
    if idx_s != -1 and idx_e != -1:
        content = content[:idx_s] + content[idx_e + len(block3_end):]

    # 6. Section 3.7: Remove "Detailed Reference" block through Effects list
    dr2_start = '    <p><strong>Detailed Reference:</strong></p>\n\n    <p><strong>Definition:</strong> Climate change'
    # Find the end of the Effects ordered list (the </ol> followed by blank lines before SVG)
    dr2_end_marker = '    </ol>\n\n  \n\n    <div class="figure">\n      <figure>\n        <svg'
    idx_s = content.find(dr2_start)
    # Look for the closing </ol> of the Effects list, followed by whitespace then the SVG
    # Find the pattern after the Detailed Reference
    if idx_s != -1:
        # Find the next SVG figure after the Detailed Reference start
        svg_after = content.find('<div class="figure">', idx_s)
        if svg_after != -1:
            # Remove from Detailed Reference start to just before the SVG figure
            # But we need to find the exact boundary - look for </ol> before the SVG
            content = content[:idx_s] + '\n' + content[svg_after:]

    final = len(content)
    print(f"Chapter 3: {original} -> {final} chars (removed {original - final}, {(original-final)/original*100:.1f}%)")

    with open('chapter3.html', 'w', encoding='utf-8') as f:
        f.write(content)


def process_chapter4():
    with open('chapter4.html', 'r', encoding='utf-8') as f:
        content = f.read()
    original = len(content)

    # 1. Section 4.1: Remove second set of Environment/Ecosystem definitions
    dup_start = '    <p><strong>Environment:</strong> Environment refers to all external conditions'
    dup_end = 'all characterized by general structural and functional attributes.</p>\n'
    idx_s = content.find(dup_start)
    idx_e = content.find(dup_end)
    if idx_s != -1 and idx_e != -1:
        content = content[:idx_s] + content[idx_e + len(dup_end):]

    # 2. Section 4.2: Remove "Primary reasons for human interventions (as above)" duplicate
    dup2 = '    <p><strong>Primary reasons for human interventions</strong> (as above): population growth, economic development, energy needs, agricultural expansion, resource extraction, urbanization, technological advancement, and unsustainable consumption patterns.</p>\n'
    content = content.replace(dup2, '')

    # 3. Section 4.2: Remove second Ecology/Ecosystem definition block (with 3 principles)
    block_start = '    <p><strong>Ecology:</strong> The branch of biology concerned with the relations between organisms and their environment. It spans micro-level'
    block_end = 'well-balanced ecosystem.</p>\n'
    idx_s = content.find(block_start)
    idx_e = content.find(block_end)
    if idx_s != -1 and idx_e != -1:
        content = content[:idx_s] + content[idx_e + len(block_end):]

    # 4. Section 4.2: Remove third Ecology/Ecosystem/Characteristics block
    block_start = '    <p><strong>Ecology:</strong> Scientific study of interactions between organisms'
    block_end = 'determine ecosystem development.</li>\n      <li><strong>Variable scale:</strong> Ecosystem area can vary from tiny to vast.</li>\n    </ul>\n'
    idx_s = content.find(block_start)
    idx_e = content.find(block_end)
    if idx_s != -1 and idx_e != -1:
        content = content[:idx_s] + content[idx_e + len(block_end):]

    # 5. Section 4.6: Remove second definition block
    dup_def = '    <p><strong>Definition:</strong> Conflict of resources is the situation where the allocation, management, or use of natural resources results in violence, human rights abuses, or denial of access to resources, significantly diminishing human welfare.</p>\n    <p>About 40% of international conflicts are related to ownership of resources. Resources are the centre of development and therefore a reason for conflicts among and within countries.</p>\n    <p><strong>Causes:</strong> Rapid population growth, social inequality, failure of governing bodies, unsustainable consumption, economic globalization.</p>\n    <p><strong>Examples:</strong></p>\n    <ul>\n      <li><strong>Global:</strong> Diamond conflicts in Africa, oil conflicts in the Middle East, gold mining conflicts in Indonesia and South America.</li>\n      <li><strong>Nepal:</strong> Conflicts related to land (boundary disputes, ownership changes, tenant eviction), forests (ownership, illegal collection, poaching), and water (source disputes, irrigation sharing, compensation for project damage).</li>\n    </ul>\n'
    content = content.replace(dup_def, '')

    # 6. Section 4.6: Remove third block after SVG (conflict + optimum use)
    block_start = '    <p><strong>Conflict of Resources:</strong> A situation where the allocation'
    block_end = 'focus must be on maximizing use of renewable and perpetual resources.</li>\n    </ul>\n'
    idx_s = content.find(block_start)
    idx_e = content.find(block_end)
    if idx_s != -1 and idx_e != -1:
        content = content[:idx_s] + content[idx_e + len(block_end):]

    # 7. Section 4.8: Remove first short list (brief overview is already in the detailed list)
    short_list_start = '    <p>Major environmental issues of Nepal:</p>\n    <ol>\n      <li>Climate change and global warming</li>'
    short_list_end = '      <li>Water-borne diseases</li>\n    </ol>\n'
    idx_s = content.find(short_list_start)
    idx_e = content.find(short_list_end)
    if idx_s != -1 and idx_e != -1:
        content = content[:idx_s] + content[idx_e + len(short_list_end):]

    # 8. Section 4.8: Remove repeated "Major Environmental Issues of Nepal" block
    rep_start = '    <p><strong>Major Environmental Issues of Nepal:</strong></p>\n    <ol>\n      <li><strong>Climate Change &amp; Global Warming:</strong> Melting snow/glaciers'
    rep_end = '      <li><strong>Water-borne Diseases:</strong> Cholera, diarrhea, typhoid, dysentery, jaundice.</li>\n    </ol>\n'
    idx_s = content.find(rep_start)
    idx_e = content.find(rep_end)
    if idx_s != -1 and idx_e != -1:
        content = content[:idx_s] + content[idx_e + len(rep_end):]

    # 9. Section 4.8: Remove last repeated list "The major environmental problems of Nepal are:"
    rep2_start = '    <p>The major environmental problems of Nepal are:</p>\n    <ol>'
    # Find the ending </ol> for this specific list
    idx_s = content.find(rep2_start)
    if idx_s != -1:
        # Find the closing </ol> after this start
        idx_e = content.find('    </ol>\n', idx_s + len(rep2_start))
        if idx_e != -1:
            end_pos = idx_e + len('    </ol>\n')
            content = content[:idx_s] + content[end_pos:]

    final = len(content)
    print(f"Chapter 4: {original} -> {final} chars (removed {original - final}, {(original-final)/original*100:.1f}%)")

    with open('chapter4.html', 'w', encoding='utf-8') as f:
        f.write(content)


if __name__ == '__main__':
    process_chapter3()
    process_chapter4()
    print("Done!")

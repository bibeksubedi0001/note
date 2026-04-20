"""
Script to add year-tags to h3 sub-subtopic headings and 'Asked' badges to figures
based on past exam questions analysis.
"""

import re
import os

BASE_DIR = r"d:\Final Year\Theory\cm\Theory"

# ──────────────────────────────────────────────────────────
# H3 HEADING MAPPINGS: (pattern_to_match, [years])
# Pattern is matched via startswith on stripped heading text
# ──────────────────────────────────────────────────────────
H3_MAPPINGS = {
    "chapter1.html": [
        ("1.3.1 Characteristics of a Construction Project", ["2071"]),
        ("1.6.1 Three-Party System", ["2079", "2078", "2075", "2074", "2072", "2071", "2069"]),
        ("1.6.3 Roles and Responsibilities of the Employer", ["2079", "2074"]),
        ("1.6.4 Roles and Responsibilities of the Contractor", ["2074"]),
        ("1.6.5 Roles and Responsibilities of the Consultant", ["2081", "2070"]),
    ],
    "chapter2.html": [
        ("Planning by the Client", ["2081", "2079", "2077", "2074"]),
        ("Planning by the Contractor", ["2080", "2079", "2071", "2070"]),
        ("Steps Involved in Planning", ["2072", "2070"]),
        ("Stages of Planning", ["2072"]),
    ],
    "chapter3.html": [
        ("ABC Analysis", ["2080", "2079", "2074", "2073", "2072", "2070"]),
        ("Classification of Construction Materials", ["2073"]),
        ("Definition of Material Wastage Standard", ["2081", "2071"]),
        ("Controllable Wastage", ["2079", "2070"]),
        ("Steps in Material Provisioning Process", ["2080", "2078", "2071", "2069"]),
        ("Economic Order Quantity", ["2081", "2078", "2074", "2071"]),
        ("Inventory Cost Terminology", ["2074"]),
        ("Inventory of Repetitive Materials", ["2079", "2077", "2073"]),
        ("VE Job Plan Phases", ["2081", "2072", "2071"]),
    ],
    "chapter4.html": [
        ("Advantages of Using Equipment", ["2079", "2077", "2075", "2074", "2073"]),
        ("Disadvantages of Using Equipment", ["2079", "2077", "2075", "2074", "2073", "2070"]),
        ("a. Excavator", ["2079", "2072", "2071"]),
        ("b. Dozers", ["2079"]),
        ("d. Backhoe Loader", ["2075"]),
        ("e. Dragline", ["2079", "2074"]),
        ("i. Graders", ["2074", "2072"]),
        ("b. Sheep Foot Roller", ["2078", "2079"]),
        ("b. Concrete Batching", ["2079", "2071", "2070"]),
        ("c. Concrete Mixing", ["2079", "2075"]),
        ("Classification of Cranes", ["2076", "2070"]),
        ("A. Conventional Method", ["2078", "2072", "2071", "2070", "2069"]),
        ("B. Tunneling by Tunnel Boring Machine", ["2078", "2076"]),
        ("Planning for Equipment Selection", ["2079", "2078", "2074", "2073", "2072"]),
    ],
    "chapter5.html": [
        ("5.2.1 Definition of Contract", ["2078", "2076"]),
        ("Elements of a Valid Contract", ["2078", "2076"]),
        ("5.2.2 Types of Contract", ["2079", "2078", "2076", "2075", "2074", "2073", "2071", "2070"]),
        ("A. Classification by Method of Payment", ["2076", "2075", "2071"]),
        ("(d) EPC Contract", ["2080", "2079"]),
        ("(e) Turn-Key Contract", ["2079", "2074"]),
        ("(f) BOOT Contract", ["2079", "2074", "2073", "2070"]),
        ("(i) BTO Contract", ["2079"]),
        ("Tender Notice", ["2079", "2075", "2074", "2072"]),
        ("Preparation Before Inviting Tenders", ["2075", "2073"]),
        ("Bidding Document", ["2079", "2074", "2073"]),
        ("Earnest Money", ["2080", "2072"]),
        ("Methods of Procurement", ["2079"]),
    ],
    "chapter6.html": [
        ("Site Surveying", ["2075", "2072"]),
        ("Construction Site Preparation", ["2075", "2073", "2072"]),
        ("Objectives of Layout Decision", ["2081", "2080", "2079", "2078", "2077", "2075", "2073", "2071", "2069"]),
        ("Key Points of Material Handling", ["2074", "2073", "2072"]),
        ("Financial Management", ["2072", "2070"]),
        ("Cash Flow Management", ["2079", "2075", "2074", "2073", "2072", "2070"]),
        ("Cash Flow Forecasting of Contractor", ["2077"]),
        ("Cash Flow Diagram of Contractor", ["2071", "2070"]),
    ],
    "chapter7.html": [
        ("Scope Control Processes", ["2081", "2077", "2073", "2071"]),
        ("Quality Control Measures", ["2072"]),
        ("Factors Affecting Labor Productivity", ["2080", "2079", "2078"]),
        ("Typical Causes of Low Labor Productivity", ["2078"]),
        ("Labor Productivity Improvement Measures", ["2079", "2071"]),
        ("Causes and Remedies for Low Equipment Productivity", ["2079", "2076", "2074"]),
        ("Causes and Remedies to Minimize Wastage", ["2078", "2075", "2073"]),
        ("What is EVA", ["2079", "2076", "2075", "2074", "2072", "2071", "2070"]),
    ],
    "chapter8.html": [
        ("Roles and Responsibilities", ["2081", "2079", "2077", "2074", "2072", "2070", "2069"]),
        ("Types of Documentation", ["2079", "2078", "2069"]),
        ("Steps for Preparing Bills", ["2078", "2071", "2070"]),
        ("MB Sample Format", ["2079", "2073", "2072", "2070"]),
        ("Muster Roll Contents", ["2079", "2078", "2077", "2075", "2074", "2073", "2071"]),
    ],
    "chapter9.html": [
        ("Why Maintenance is Needed", ["2078", "2077", "2073", "2071", "2070"]),
        ("Objectives of Maintenance", ["2078", "2073"]),
        ("1. Planned Maintenance", ["2079", "2078", "2074", "2073", "2071"]),
        ("2. Unplanned Maintenance", ["2079", "2074", "2073"]),
        ("Preventive vs Corrective Maintenance", ["2081", "2079", "2078", "2077", "2076", "2074", "2072", "2070", "2069"]),
        ("Maintenance Planning", ["2079", "2076", "2073", "2072"]),
    ],
    "chapter10.html": [
        ("Fayol", ["2079", "2069"]),
        ("Difference between Administration and Management", ["2071"]),
        ("Centralization", ["2074"]),
        ("Decentralization", ["2080", "2079"]),
        ("Types of Leadership Styles", ["2079", "2075", "2073", "2072", "2071", "2070"]),
        ("What is Motivation", ["2078"]),
        ("A. Content Theories of Motivation", ["2081", "2076", "2069"]),
        ("B. Process Theories of Motivation", ["2076"]),
        ("Recruitment", ["2078", "2077", "2073", "2072"]),
        ("Importance of Communication", ["2079", "2074", "2073", "2072"]),
        ("Barriers to Communication", ["2077"]),
    ],
    "chapter11.html": [
        ("Why Regulatory Requirements are Needed", ["2080", "2073"]),
        ("Causes of Accidents", ["2081", "2078", "2071"]),
        ("Why Safety is Important", ["2079", "2078", "2075"]),
        ("Safety Measures in Construction Areas", ["2073"]),
        ("Safety Control Devices", ["2078"]),
        ("Fire Safety", ["2079"]),
        ("Insurance", ["2079", "2070"]),
        ("National Building Code", ["2081", "2079"]),
        ("Four Levels of NBC", ["2079"]),
        ("How Building Codes Help", ["2080", "2079", "2075", "2073"]),
        ("Building Bye-Laws", ["2077"]),
        ("Quality Control", ["2073", "2072"]),
    ],
    "chapter12.html": [
        ("Purpose of Specification", ["2079", "2072"]),
        ("a. Contract Specification", ["2078", "2074"]),
        ("Principles/Techniques of Specification Writing", ["2079", "2078", "2075", "2072", "2070", "2069"]),
        ("A) Specification for Brick Work", ["2080", "2079", "2072", "2071", "2070", "2069"]),
        ("B) Specification for RCC Works", ["2069"]),
        ("D) Specification for Stone Masonry", ["2073"]),
        ("E) Specification for Plaster Work", ["2077"]),
    ],
    "chapter13.html": [
        ("Purposes of Valuation", ["2078", "2076", "2074", "2073", "2070"]),
        ("Principles of Valuation", ["2073", "2070"]),
        ("Types of Values", ["2076", "2075", "2073", "2071"]),
        ("Methods of Calculating Depreciation", ["2072"]),
        ("1. Cost-based Method", ["2070"]),
        ("2. Plinth Area Method", ["2070"]),
        ("7. Development Method", ["2070"]),
    ],
}

# ──────────────────────────────────────────────────────────
# FIGURE MAPPINGS: (fig_number, optional_caption_keyword)
# If keyword is None, match all instances of that fig number
# ──────────────────────────────────────────────────────────
FIGURE_MAPPINGS = {
    "chapter1.html": [
        ("Fig 1.4", "Phases"),
        ("Fig 1.6", "Three-Party"),
    ],
    "chapter2.html": [
        ("Fig 2.5", None),
    ],
    "chapter3.html": [
        ("Fig 3.1", None),
        ("Fig 3.5", None),
    ],
    "chapter4.html": [
        ("Fig 4.2", None),
        ("Fig 4.3", None),
        ("Fig 4.4", None),
        ("Fig 4.5", None),
        ("Fig 4.6", None),
        ("Fig 4.7", None),
        ("Fig 4.8", None),
        ("Fig 4.9", None),
        ("Fig 4.11", None),
        ("Fig 4.15", None),
    ],
    "chapter6.html": [
        ("Fig 6.1", None),
        ("Fig 6.4", None),
    ],
    "chapter7.html": [
        ("Fig 7.4", None),
    ],
    "chapter8.html": [
        ("Fig 8.3", None),
        ("Fig 8.5", None),
    ],
    "chapter10.html": [
        ("Fig 10.4", None),
    ],
}


def strip_html_entities(text):
    """Remove HTML tags and decode common entities."""
    text = re.sub(r'<[^>]+>', '', text)
    text = text.replace('&rsquo;', "'").replace('&lsquo;', "'")
    text = text.replace('&rdquo;', '"').replace('&ldquo;', '"')
    text = text.replace('&mdash;', '-').replace('&ndash;', '-')
    text = text.replace('&amp;', '&')
    text = re.sub(r'&[a-z]+;', '', text)  # strip remaining entities
    return text.strip()


def heading_matches(plain_text, pattern):
    """Check if the stripped heading text matches the pattern."""
    pt = plain_text.strip()
    pat = pattern.strip()
    # Exact or starts-with match (case-insensitive)
    if pt.lower() == pat.lower():
        return True
    if pt.lower().startswith(pat.lower()):
        return True
    return False


def process_file(filename):
    filepath = os.path.join(BASE_DIR, filename)
    if not os.path.exists(filepath):
        print(f"  [SKIP] File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    h3_count = 0
    fig_count = 0

    # ── Process h3 headings ──────────────────────────────
    if filename in H3_MAPPINGS:
        h3_re = re.compile(r'(<h3[^>]*>)(.*?)(</h3>)', re.DOTALL)
        matches = list(h3_re.finditer(content))

        # Process in reverse to preserve positions
        for m in reversed(matches):
            h3_open = m.group(1)
            h3_inner = m.group(2)
            h3_close = m.group(3)
            plain = strip_html_entities(h3_inner)

            for pattern, years in H3_MAPPINGS[filename]:
                if heading_matches(plain, pattern):
                    # Get existing year tags
                    existing = set(re.findall(r'class="year-tag">(\d{4})', h3_inner))
                    new_years = [y for y in years if y not in existing]
                    if not new_years:
                        break

                    year_html = ''.join(
                        f' <span class="year-tag">{y}</span>' for y in new_years
                    )
                    replacement = h3_open + h3_inner + year_html + h3_close
                    content = content[:m.start()] + replacement + content[m.end():]
                    h3_count += 1
                    break

    # ── Process figures ───────────────────────────────────
    if filename in FIGURE_MAPPINGS and FIGURE_MAPPINGS[filename]:
        fig_re = re.compile(
            r'(<figcaption><strong>)(Fig\s+\d+\.\d+)'
            r'(</strong>\s*(?:&mdash;|—)\s*)(.*?)(</figcaption>)',
            re.DOTALL
        )
        fig_matches = list(fig_re.finditer(content))

        for fm in reversed(fig_matches):
            fig_num = fm.group(2).strip()
            caption_text = fm.group(4).strip()

            for fig_id, keyword in FIGURE_MAPPINGS[filename]:
                if fig_num == fig_id:
                    # Check keyword filter
                    if keyword and keyword.lower() not in caption_text.lower():
                        continue
                    # Check not already tagged
                    if 'asked-tag' in fm.group(0):
                        continue

                    # Insert asked badge before </figcaption>
                    replacement = (
                        fm.group(1) + fm.group(2) + fm.group(3)
                        + fm.group(4)
                        + ' <span class="year-tag asked-tag">📝 Asked</span>'
                        + fm.group(5)
                    )
                    content = content[:fm.start()] + replacement + content[fm.end():]
                    fig_count += 1
                    break

    # ── Write back ────────────────────────────────────────
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  [OK] {filename}: {h3_count} h3 tags, {fig_count} figure tags added")
    else:
        print(f"  [--] {filename}: no changes needed")


def main():
    print("=" * 60)
    print("  Adding year-tags to h3 & asked-badges to figures")
    print("=" * 60)

    all_files = sorted(set(
        list(H3_MAPPINGS.keys()) + list(FIGURE_MAPPINGS.keys())
    ))

    for fn in all_files:
        print(f"\n  Processing {fn}...")
        process_file(fn)

    print("\n" + "=" * 60)
    print("  Done!")
    print("=" * 60)


if __name__ == "__main__":
    main()

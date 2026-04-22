"""
Safe SVG replacement utility for GW_THE chapters.
Finds SVGs by figcaption substring and replaces the enclosing figure-container.
Uses string searching instead of regex to avoid catastrophic backtracking.
"""
import re

def find_and_replace_svg_safe(html, figcaption_substr, new_figure_html):
    """Find a figure-container by its figcaption text and replace it.
    Uses backward scanning from figcaption to find the enclosing figure-container."""
    
    # Find the figcaption containing the target text
    idx = html.find(figcaption_substr)
    if idx == -1:
        print(f"  ✗ NOT FOUND: ...{figcaption_substr[:50]}...")
        return html
    
    # Find the enclosing <div class="figcaption"> tag
    figcap_div_start = html.rfind('<div class="figcaption">', 0, idx)
    if figcap_div_start == -1:
        print(f"  ✗ No figcaption div found for: ...{figcaption_substr[:50]}...")
        return html
    
    # Find the closing </div> of the figcaption
    figcap_div_end = html.find('</div>', idx)
    if figcap_div_end == -1:
        print(f"  ✗ No figcaption closing div for: ...{figcaption_substr[:50]}...")
        return html
    figcap_div_end += len('</div>')
    
    # Now scan backward from figcap_div_start to find <div class="figure-container">
    container_start = html.rfind('<div class="figure-container">', 0, figcap_div_start)
    if container_start == -1:
        print(f"  ✗ No figure-container found for: ...{figcaption_substr[:50]}...")
        return html
    
    # Find the closing </div> after the figcaption (the container's closing tag)
    # After figcap_div_end, skip whitespace and find </div>
    rest = html[figcap_div_end:]
    close_match = re.match(r'\s*</div>', rest)
    if close_match:
        container_end = figcap_div_end + close_match.end()
    else:
        # Just use figcap_div_end + </div>
        next_close = html.find('</div>', figcap_div_end)
        container_end = next_close + len('</div>') if next_close != -1 else figcap_div_end
    
    # Verify there's no CLOSER figure-container between container_start and figcap_div_start
    # (to avoid matching a parent div)
    check_region = html[container_start + 1:figcap_div_start]
    closer = check_region.rfind('<div class="figure-container">')
    if closer != -1:
        container_start = container_start + 1 + closer
    
    old_block = html[container_start:container_end]
    svg_count = old_block.count('<svg')
    
    html = html[:container_start] + new_figure_html + html[container_end:]
    print(f"  ✓ Replaced ({svg_count} SVGs removed): ...{figcaption_substr[:50]}...")
    return html

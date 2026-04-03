"""Bulk replace emojis with text labels/Unicode symbols in all HTML files."""
import re, glob, os

# Emoji → text replacement map
REPLACEMENTS = {
    # Map/Globe
    '🗺️': '',  '🗺': '',  '🌍': '',  '🌎': '',  '🌐': '',
    # Satellite/Signal
    '🛰️': '',  '🛰': '',  '📡': '',
    # Tools/Measurement
    '📐': '',  '📏': '',
    # Keys/Links
    '🔑': 'PK',  '🔗': '',  '🔄': '',
    # Files/Folders
    '📂': '',  '📁': '',  '📄': '',  '📜': '',
    # Labels/Clipboard
    '📋': '',  '📝': '',  '🏷️': '',  '🏷': '',
    # Charts/Data
    '📊': '',  '📅': '',
    # Nature
    '🌿': '',  '🌳': '',  '🌈': '',  '🌊': '',
    # Water
    '💧': '',
    # Buildings/Infrastructure
    '🏢': '',  '🏗️': '',  '🏗': '',  '🏥': '',  '🏖️': '',  '🏖': '',
    '🚧': '',  '🛣️': '',  '🛣': '',  '🌉': '',
    # People/Actions
    '🤝': '',
    # Tech
    '💻': '',  '📱': '',  '🖱️': '',  '🖱': '',  '📷': '',  '🖤': '',
    # Warning/Status
    '💥': '',  '💸': '',  '🗑️': '',  '🗑': '',  '🚫': '—',
    # Targets/Points
    '📍': '',  '🎯': '',  '📖': '',
    # Misc
    '💰': '',  '📦': '',  '🕸️': '',  '🕸': '',  '📥': '',
    '🔦': '',  '🛩️': '',  '🛩': '',  '🔥': '',  '🔴': '',
    '🟢': '●',  '🟡': '●',  '🪨': '',  '🏜️': '',  '🏜': '',
    '★': '',
    # Variation selectors (leftover after emoji removal)
    '\uFE0F': '',
}

files = glob.glob(os.path.join(os.path.dirname(__file__), '*.html'))
total = 0

for fpath in sorted(files):
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for emoji, replacement in REPLACEMENTS.items():
        if emoji in content:
            # If replacement is empty, also clean up leading/trailing spaces
            if replacement == '':
                # "emoji Text" → "Text"  and  "Text emoji" → "Text"
                content = content.replace(emoji + ' ', '')
                content = content.replace(' ' + emoji, '')
                content = content.replace(emoji, '')
            else:
                content = content.replace(emoji, replacement)
    
    if content != original:
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        changes = sum(1 for a, b in zip(original, content) if a != b) + abs(len(original) - len(content))
        fname = os.path.basename(fpath)
        print(f"  Cleaned: {fname}")
        total += 1

print(f"\nDone. Modified {total} files.")

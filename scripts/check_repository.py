"""Static repository checks only; does not run the lab or validate Wazuh semantics."""
from pathlib import Path
import re
import xml.etree.ElementTree as ET

root = Path(__file__).resolve().parents[1]
errors = []
markdown = list(root.rglob('*.md'))
for path in markdown:
    text = path.read_text(encoding='utf-8')
    if len(re.findall(r'^```', text, re.M)) % 2:
        errors.append(f'{path.relative_to(root)}: unbalanced fences')
    # Ignore illustrative snippets and inline code, which may show future image links.
    prose = re.sub(r'```.*?```', '', text, flags=re.S)
    prose = re.sub(r'`[^`\n]*`', '', prose)
    for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)', prose):
        if '://' in target or target.startswith('#'):
            continue
        dest = (path.parent / target.split('#')[0]).resolve()
        if not dest.is_relative_to(root) or not dest.exists():
            errors.append(f'{path.relative_to(root)}: broken local link {target}')
for path in root.glob('configs/*.xml'):
    try:
        ET.parse(path)
    except ET.ParseError as exc:
        errors.append(f'{path.name}: {exc}')
for path in root.rglob('*'):
    if path.is_file() and path.suffix.lower() in {'.png', '.jpg', '.pcap', '.pcapng', '.evtx'}:
        errors.append(f'{path.relative_to(root)}: new evidence requires manual review')
if errors:
    raise SystemExit('\n'.join(errors))
print(f'PASS: {len(markdown)} Markdown files; local links, fences and XML well-formedness.')
print('Runtime telemetry, Wazuh rule behavior, external links and GitHub rendering are not tested.')

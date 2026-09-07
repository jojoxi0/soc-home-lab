# Real screenshot capture checklist

**SCREENSHOT REQUIRED — no image files currently exist.** Capture only after running the relevant exercise.

| Future filename | Screen to open | Required visible details | Future README placement |
| --- | --- | --- | --- |
| 01-wazuh-dashboard.png | Wazuh agent list/dashboard | WIN-LAB Active; time context | Screenshots: environment |
| 02-failed-login-alert.png | Threat Hunting expanded actual failure alert | Event 4625, rule ID, lab account alias, time range | Screenshots: authentication |
| 03-windows-event-viewer.png | Event Viewer → Windows Logs → Security → actual 4625 | Event ID, time and failure details | Screenshots: source evidence |
| 04-sysmon-event.png | Event Viewer → Applications and Services Logs → Microsoft → Windows → Sysmon → Operational | Event 1 with parent/command-line context | Screenshots: process analysis |
| 05-wireshark-capture.png | Windows Wireshark, saved scenario 3 capture | Display filter, TCP flags, several destination ports | Screenshots: network analysis |

Redact personal usernames, emails, real device names, non-lab addresses, tokens, browser profile details and unrelated windows. Keep synthetic lab aliases consistent. Solid opaque redaction is preferable to reversible overlays; reopen the exported flat image to check it. Avoid cropping out the fields needed to support your conclusion.

Save sanitized PNGs here using the exact filenames above. Keep originals outside the repository. Add a dated caption stating exercise, vantage point and redactions. Only after a file exists, add its Markdown image reference under README's Screenshots section, for example `![Verified Wazuh agent](screenshots/01-wazuh-dashboard.png)`. Do not add the reference while the image is absent.

If no SIEM alert appears, troubleshoot and retain the gap; do not fabricate an alert or label a local Event Viewer image as Wazuh evidence.

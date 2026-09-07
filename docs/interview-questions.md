# Interview preparation — 15 questions

Answers describe the design. Replace planned language only after personally completing and understanding the work.

## 1. What is this project, and what have you actually done?

**Beginner answer:** It is a learning lab design. Deployment and evidence collection are still pending.

**Technical answer:** Separate authored documentation and example configurations from executed tests. Update the status only after end-to-end validation.

**Understand:** Integrity; scope; reproducibility.

## 2. What does a SIEM do?

**Beginner answer:** It brings logs together and helps analysts find and investigate important patterns.

**Technical answer:** Collection, parsing, rules and indexed alert search are distinct stages. A missing alert may indicate rule coverage rather than absence of source events.

**Understand:** Telemetry pipeline; alerts versus events.

## 3. Why isolate the network?

**Beginner answer:** So test traffic stays inside the machines I own.

**Technical answer:** The baseline uses an Internal Network with no gateway and no other connected adapters. Temporary provisioning access is removed before testing.

**Understand:** Internal versus host-only versus NAT.

## 4. What is Event 4625?

**Beginner answer:** It records a failed Windows logon.

**Technical answer:** Inspect the Security provider, account, logon type and status/substatus. Local explicit-credential tests may not have a network source address.

**Understand:** Provider; audit policy; authentication context.

## 5. Does a failed logon prove an attack?

**Beginner answer:** No. It can be a mistake or an old saved password.

**Technical answer:** Correlate recurrence, source context, account and related activity; evaluate benign hypotheses and scope conclusions to the evidence window.

**Understand:** False positives; correlation; uncertainty.

## 6. What does Sysmon add?

**Beginner answer:** It records detailed system activity such as process creation.

**Technical answer:** This small configuration focuses on Event 1 and process lineage. It is not a network IDS and is not the source of Security authentication logs.

**Understand:** Process GUID; parent process; collection scope.

## 7. How do you investigate PowerShell?

**Beginner answer:** I read the command and check who launched it and why.

**Technical answer:** Correlate Windows PowerShell script-block telemetry with process metadata and surrounding events. PowerShell itself and -NoProfile are not sufficient malicious indicators.

**Understand:** Script content; parent chain; context.

## 8. What is the difference between PowerShell 4104 and Sysmon 1?

**Beginner answer:** One shows script content; the other shows a process starting.

**Technical answer:** They come from different channels and can have different coverage. Correlate host and time plus identifiers; do not assume a one-to-one event count.

**Understand:** Channels; many-to-one relationships.

## 9. How does the scan appear in Wireshark?

**Beginner answer:** One computer sends connection requests to several ports on another.

**Technical answer:** Measure distinct destination ports, inspect flags and responses, and distinguish retransmissions from separate probes. Interpret results from the capture vantage point.

**Understand:** TCP handshake; filtered versus closed; vantage point.

## 10. Will Wazuh automatically detect that scan?

**Beginner answer:** Not necessarily; it needs suitable input and detection logic.

**Technical answer:** The baseline captures packets separately and does not ingest IDS events. Endpoint process logging alone cannot reliably detect all inbound port probes.

**Understand:** Sensor coverage; ingestion; rule prerequisites.

## 11. What do the custom rules detect?

**Beginner answer:** They find the exercise account or special harmless markers.

**Technical answer:** These are visibility checks, not production threat analytics. They select decoded fields and require positive/negative runtime validation against the installed ruleset.

**Understand:** Marker tests; field names; production validity.

## 12. Why use a negative control?

**Beginner answer:** To check that ordinary activity does not trigger the same marker rule.

**Technical answer:** Run a separate baseline window and keep all conditions except the marker comparable. Check both source telemetry and final rule result to avoid mistaking missing collection for a successful negative test.

**Understand:** Specificity; controlled experiments.

## 13. How do you use MITRE ATT&CK?

**Beginner answer:** It helps describe a behavior when the mapping really fits.

**Technical answer:** Map only the observed behavior and distinguish benign simulation from adversary intent. A technique label is neither attribution nor proof of compromise.

**Understand:** Behavior mapping; intent; attribution.

## 14. How do you preserve evidence?

**Beginner answer:** I keep original files private and share carefully redacted copies.

**Technical answer:** Record source, UTC window, tool/version and hashes for originals and derivatives. Preserve event details needed for reproducibility without exposing secrets.

**Understand:** Provenance; integrity; redaction.

## 15. What would you improve next?

**Beginner answer:** I would run the lab, capture evidence and tune the detections from the results.

**Technical answer:** Prioritize end-to-end coverage and a validated correlation threshold before adding an IDS. Document resource limits and false positives rather than claiming unmeasured accuracy.

**Understand:** Validation; tuning; honest limitations.

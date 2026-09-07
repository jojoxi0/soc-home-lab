# Detection engineering notes

**EXAMPLE rules — XML structure checked locally, Wazuh runtime not tested.**

| Rule | Logic | Why / expected telemetry | False positives and limits | Investigation |
| --- | --- | --- | --- | --- |
| 100510 | 4625 + dedicated account | Select individual lab logon failures | Typos; no frequency correlation | Count in a defined window; inspect status and related successes |
| 100511 | 4104 + exact lab marker | Surface benign script block content | Anyone can print marker; not suspiciousness | Read the complete script and process context |
| 100512 | Sysmon 1 + command marker | Surface parent process for exercise 4 | Literal marker can occur anywhere | Follow process GUID relationships |

These rules trade generality for explainable lab visibility. They are not production security analytics. No custom ATT&CK tag or severity claim is assigned to harmless markers.

## Install without overwriting rules

1. Snapshot the Wazuh VM. Check for existing IDs 100510–100512 under `/var/ossec/etc/rules` and `/var/ossec/ruleset/rules` using `rg` (or `grep -R` if unavailable). If occupied, choose unused IDs in Wazuh's custom range and update all references.
2. On the manager, create `/var/ossec/etc/rules/soc_lab_rules.xml` containing the repository [example](../configs/wazuh-lab-rules.xml). Do not replace `local_rules.xml`. Use the ownership and file mode of adjacent local rule files.
3. Run `sudo /var/ossec/bin/wazuh-analysisd -t`. Resolve errors before restarting; retain existing configuration if validation fails.
4. Run `sudo /var/ossec/bin/wazuh-logtest` interactively with real single-line input in the format the Windows collector sends, following the [testing documentation](https://documentation.wazuh.com/current/user-manual/ruleset/testing.html). Verify decoded field names and the matched rule. Do not paste an entire indexed alert wrapper (`data.win`) as if it were raw collector input (`win`). If input is unavailable, leave this test pending.
5. Only after syntax checks succeed, restart with `sudo systemctl restart wazuh-manager`. Check manager status and `/var/ossec/logs/ossec.log`.
6. Generate a new marker event. Verify the end-to-end indexed result and confirm that a negative control does not match the marker rule. Record actual rule IDs; stock rules can interact with custom rule matching.
7. Remove only the added file to roll back, rerun the syntax check, and restart the manager.

The parent group `windows` and decoded names must match the installed ruleset. The dashboard prefixes event fields with `data.`; rule XML does not. If no match appears, inspect actual Phase 2 decoder output instead of repeatedly changing random IDs. Ensure the configured alert threshold permits levels 3 and 5. See [custom rules](https://documentation.wazuh.com/current/user-manual/ruleset/rules/custom.html) and [syntax](https://documentation.wazuh.com/current/user-manual/ruleset/ruleset-xml-syntax/rules.html).

## Authentication correlation design

Proposed logic, not an implemented Wazuh frequency rule:

```text
Select failures for an owned host and account.
Within a rolling 120-second window, count matching failures.
If count >= 3, create a triage candidate.
Attach failure reasons and any related successful logon.
```

Group by host and account; add source address for a remote-logon hypothesis only when populated. Validate window boundaries, field absence, repeated events and unrelated accounts. A threshold is a starting assumption to tune, not evidence of maliciousness.

## Coverage gaps

No PCAP ingestion, brute-force correlation engine, malware detection test or automatic containment is implemented here. Alerts-only storage can omit benign events. Endpoint loss, clock differences and collection filters can also hide data. Document gaps rather than reporting zero results as a clean bill of health.

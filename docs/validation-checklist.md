# Execution validation checklist

**All runtime checks are PLANNED.** Repository static checks are reported separately in [quality review](quality-review.md).

## Record before starting

| Component | Actual version/build | Installation date | Status |
| --- | --- | --- | --- |
| Host resources | Not measured | — | PLANNED |
| VirtualBox | Not installed by this project | — | PLANNED |
| Windows | Not measured | — | PLANNED |
| Kali / Nmap | Not measured | — | PLANNED |
| Wazuh manager / agent | Not measured | — | PLANNED |
| Sysmon / config schema | Not measured | — | PLANNED |
| Wireshark / capture driver | Not measured | — | PLANNED |

## Gates

- [ ] Confirm resources and lawful Windows media/evaluation eligibility.
- [ ] Verify isolated adapters and no unintended IPv4/IPv6 default route.
- [ ] Take clean snapshots and record clock offset.
- [ ] Verify Security, Sysmon and Windows PowerShell source telemetry.
- [ ] Verify agent enrollment and actual event delivery.
- [ ] Check custom IDs are unused; manager validates rule XML.
- [ ] Positive marker matches intended rule; negative control produces source events without that marker match.
- [ ] Record actual authentication failures and related logons.
- [ ] Compare baseline and four-port scan in the saved capture.
- [ ] Complete one report with observed facts and evidence references.
- [ ] Redact and review five real screenshots.
- [ ] Clean up temporary account and preserve evidence before snapshot rollback.
- [ ] Update README status and LinkedIn claims to match completed work.

## Per-scenario record

| Scenario | UTC interval | Positive result | Negative result | Evidence | Limitations |
| --- | --- | --- | --- | --- | --- |
| Authentication | PLANNED | PLANNED | PLANNED | None | Runtime pending |
| PowerShell | PLANNED | PLANNED | PLANNED | None | Runtime pending |
| Network | PLANNED | PLANNED | PLANNED | None | Runtime pending |
| Process | PLANNED | PLANNED | PLANNED | None | Runtime pending |

A failed check is an investigation task, not permission to mark the project complete. Record failure, diagnosis, change and retest in your own words.

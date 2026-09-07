# Scenario 1 — Multiple failed authentication attempts

**PLANNED simulation.** No observed results are supplied.

## 1. Objective

Recognize clustered authentication failures without equating them with compromise.

## 2. Environment

Owned Windows VM, failure auditing enabled, dedicated disposable standard account `soclab`. Kali is not needed. Complete the isolation checks in the [setup](../docs/setup-guide.md).

## 3. Simulation

In administrator Windows PowerShell create the account using an interactive password prompt; no password is stored in the command:

```powershell
net user soclab * /add
net accounts
```

Inspect the lockout threshold and duration. Keep a separate administrator account. In a terminal run:

```powershell
runas /user:.\soclab cmd.exe
```

Enter an intentionally wrong password manually. Repeat at most three times, stopping before the configured lockout threshold (if lower). Do not weaken the policy to reach a count. Record the actual number and UTC times. `runas` here generates local explicit-credential logons, not a remote Kali attack. A later correct-password test is optional and should be documented separately; do not use `/netonly`.

## 4. Telemetry generated

Look for Security 4625 on the Windows VM. Inspect account, logon type, status/substatus and event timestamp. Source network address may be absent for local attempts. 4624 is a successful logon, but a nearby success is not automatically related. [Microsoft event reference](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4625).

## 5. Detection

Use the [4625 query](../queries/useful-queries.md). An analyst triage hypothesis is three failures for the same host/account within two minutes. This is a proposed investigation threshold, not a deployed correlation rule. If policy permits fewer attempts, use those events and document the lower count. Optional rule 100510 surfaces individual lab-account failures, not an aggregated brute-force alert.

## 6. Investigation

Compare source event time with ingestion time. Group by host/account and, for remote events, source address. Examine failure reasons and nearby successes, check test timestamps, and confirm who initiated the test. Compare a non-lab account's routine event as a negative control: 100510 should not match it. Typos, stale saved passwords and service credentials are benign explanations.

## 7. Evidence

Capture Windows event details and the corresponding SIEM result with the time range visible. Record real event record IDs privately and publish sanitized references per [evidence instructions](../evidence/README.md). Do not fill missing IP addresses with Kali's address.

## 8. Analyst conclusion

Pending execution. After validation, describe controlled failures and observed outcomes. Absence of a success within a searched window does not prove no compromise anywhere.

## 9. Recommended response

For this lab: stop attempts, verify the account is usable and remove it after evidence collection (`net user soclab /delete`). For an unplanned comparable event: check context, related successes and account exposure before recommending lockout tuning or credential reset. Do not enable automatic blocking from this low threshold.

## 10. MITRE ATT&CK

[T1110.001 — Password Guessing](https://attack.mitre.org/techniques/T1110/001/) is a conceptual mapping for deliberate repeated guesses. Manual wrong-password entries exercise related telemetry; they are not proof of an adversary or a complete brute-force campaign.

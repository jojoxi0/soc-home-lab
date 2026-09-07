# Scenario 4 — Unusual process context

**PLANNED simulation.**

## 1. Objective

Follow a parent-child process relationship and separate a lab marker from a threat indicator.

## 2. Environment

Owned Windows VM with Sysmon process collection, standard user session.

## 3. Simulation

In Command Prompt:

```cmd
cmd.exe /d /c "echo SOC-LAB-PROC-001 & whoami.exe"
```

This prints a marker and the current identity, then exits. Do not publish the raw identity. Negative control: run `whoami.exe` alone. No unusual executable is downloaded or masqueraded as a system binary.

## 4. Telemetry generated

Sysmon 1 should show the new command interpreter and child `whoami.exe`. Inspect ProcessGuid and ParentProcessGuid, paths and command line. Metadata depends on the installed configuration. [Sysmon reference](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon).

## 5. Detection

Optional rule 100512 matches the marker-bearing process command line. It does not assert that `whoami.exe` is malicious and may not match the child itself. Use [process queries](../queries/useful-queries.md) to find the child and join its parent GUID to the parent's process GUID.

## 6. Investigation

Check parent chain, user context, execution location and timing. Compare the negative control, which should not match the marker rule. Inventory tools and troubleshooting can legitimately invoke the same commands. A familiar path or valid signature alone does not establish safe behavior.

## 7. Evidence

Capture the parent event and child relationship. Keep full original event XML privately and publish sanitized details. Do not invent process hashes or GUIDs.

## 8. Analyst conclusion

Pending. Expected benign context must be verified against the actual recorded exercise; no malware claim is justified.

## 9. Recommended response

No containment for a verified marker. If unexpected, investigate context and adjacent activity. The commands exit without persistent changes.

## 10. MITRE ATT&CK

No formal technique mapping assigned to the broad label “unusual process.” This runbook focuses on process triage, not claiming a complete adversary technique from a benign command name.

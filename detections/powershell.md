# Scenario 2 — PowerShell activity investigation

**PLANNED simulation.**

## 1. Objective

Distinguish script content from process metadata and investigate context.

## 2. Environment

Isolated Windows VM, Windows PowerShell 5.1 script block logging, Sysmon and optional Wazuh collection.

## 3. Simulation

Open a new ordinary Windows PowerShell session and run:

```powershell
powershell.exe -NoProfile -Command "Write-Output 'SOC-LAB-PS-001'"
```

The child prints a marker and exits. It does not download, persist, disable protection or change files. Negative control: run again with `SOC-LAB-BASELINE` instead of `SOC-LAB-PS-001`.

## 4. Telemetry generated

Windows PowerShell Operational 4104 should contain script text when enabled; Sysmon 1 records process creation. These are different providers. Correlate time, host, process IDs and content; IDs may be reused. The parent session's script block may also contain the marker, so multiple matching events are possible. [PowerShell logging](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging?view=powershell-5.1).

## 5. Detection

Search [queries](../queries/useful-queries.md); optional 100511 is marker visibility only. The baseline should not match that marker rule. A generic PowerShell process is not inherently suspicious.

## 6. Investigation

Inspect executable path, parent, user, command line and script content. Ask whether execution was expected. Check adjacent process events rather than asserting malicious behavior from `-NoProfile`. Administration and monitoring frequently use this flag.

## 7. Evidence

Save a sanitized 4104 view and the related process event with timestamps. Record missing or fragmented script blocks as a gap; reconstruct by script block ID and message sequence if needed.

## 8. Analyst conclusion

Pending. Expected explanation is a benign marker command; conclude only after comparing actual telemetry with the recorded command.

## 9. Recommended response

No containment for a verified lab marker. For unknown scripts, preserve content and investigate origin and effects before remediation. Close the child/session after collection.

## 10. MITRE ATT&CK

[T1059.001 — PowerShell](https://attack.mitre.org/techniques/T1059/001/) describes interpreter use by adversaries. This benign exercise demonstrates visibility of that interpreter, not malicious execution.

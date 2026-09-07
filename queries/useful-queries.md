# Useful investigation queries

**EXAMPLE — validate field names against one expanded event first.** Use Wazuh Threat Hunting / Discover, alerts data view (`wazuh-alerts-*`), DQL search mode, agent filter and an explicit time range. These are search filters, not Wazuh API WQL or deployed correlation rules.

| Question | DQL filter | How to use it |
| --- | --- | --- |
| Which logons failed? | `agent.name: "WIN-LAB" AND data.win.system.eventID: "4625"` | Inspect account, host and failure reason; count in chosen window |
| Which logons succeeded? | `agent.name: "WIN-LAB" AND data.win.system.eventID: "4624"` | Correlate account/time/logon type; do not assume causality |
| Which script blocks exist? | `agent.name: "WIN-LAB" AND data.win.system.eventID: "4104"` | Read scriptBlockText; benign events may not be indexed |
| Which processes started? | `agent.name: "WIN-LAB" AND data.win.system.channel: "Microsoft-Windows-Sysmon/Operational" AND data.win.system.eventID: "1"` | Inspect parent GUID, process GUID, image and command line |
| Did a marker alert index? | `agent.name: "WIN-LAB" AND (rule.id: "100510" OR rule.id: "100511" OR rule.id: "100512")` | Confirm against the actual simulation time and source record |

Use the UI's exact field-value filter on `data.win.eventdata.targetUserName` for `soclab`; inspect the field's actual capitalization in your documents. Build a table grouped by host/account or export a private selection to count failures. The broad 4625 query alone does not implement a rolling window.

## Local Windows verification

In an elevated Windows PowerShell session, inspect recent source records:

```powershell
Get-WinEvent -FilterHashtable @{LogName='Security'; Id=4625; StartTime=(Get-Date).AddMinutes(-10)} -MaxEvents 10
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-PowerShell/Operational'; Id=4104; StartTime=(Get-Date).AddMinutes(-10)} -MaxEvents 10
Get-WinEvent -FilterHashtable @{LogName='Microsoft-Windows-Sysmon/Operational'; Id=1; StartTime=(Get-Date).AddMinutes(-10)} -MaxEvents 10
```

A “no events found” result is a troubleshooting observation. Check channel, policy, session version and time before assuming Wazuh dropped an event.

## Network comparison

Use the [scenario 3 filter](../detections/network-reconnaissance.md). Compare distinct destination ports rather than raw packet count. Examine responses with `ip.addr == 10.77.77.20 && tcp` after capture. Retain the unfiltered private original.

## Validation

For each query record data view, search mode, timezone, absolute start/end, result count and representative record. Run the documented negative control in a separate window so earlier marker events do not contaminate the result.

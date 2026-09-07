# Beginner setup guide

**PLANNED — these commands have not been executed on your machines.** Work through one checkpoint at a time. Record versions and actual results in [validation](validation-checklist.md).

## 0. Choose a feasible path

The [Wazuh quickstart](https://documentation.wazuh.com/current/quickstart.html) recommends 4 vCPU, 8 GiB RAM and 50 GB storage for its smallest all-in-one tier. That excludes your Windows, Kali and host operating system.

Suggested VM allocations, not measured performance: Wazuh 8 GB/4 vCPU/50 GB disk; Windows 4–6 GB/2 vCPU/80 GB disk; Kali 2 GB/2 vCPU/30 GB disk. Leave RAM for the host and disk space for snapshots. Do not allocate more physical resources than available.

**8 GB host:** start with only a Windows VM, Sysmon and Event Viewer. Run scenarios 1, 2 and 4 locally. Keep Wazuh and network correlation PLANNED. Power off other VMs. If even Windows cannot run comfortably, stop at documentation until suitable hardware is available. Do not advertise a full SIEM lab based on endpoint-only work.

Use existing appropriately licensed Windows media or evaluate the [Windows Enterprise evaluation](https://www.microsoft.com/en-us/evalcenter/evaluate-windows-11-enterprise) if eligible under its terms. The published evaluation lasts 90 days; it is not a perpetual free Windows license. Follow its hardware and activation requirements. Do not bypass licensing or system requirements.

## 1. Install VirtualBox

Download the base package from [VirtualBox](https://www.virtualbox.org/). Install on the host, enable hardware virtualization in firmware if required, and reboot if prompted. The Extension Pack is not needed for this project. Store VMs on a disk with enough free space.

## 2. Create Windows

Select New, name `WIN-LAB`, attach the official ISO, allocate the resources above, and follow Windows installation. Configure required EFI/TPM options for your supported guest. Install updates and tools during provisioning. Use only lab accounts; never reuse an important password. Create a snapshot before logging changes.

## 3. Create Kali

Download the VirtualBox image from [Kali](https://www.kali.org/get-kali/), verify its published checksum, extract and open/import the supplied VM. Change any default password before use. During temporary NAT provisioning, install missing tools using `sudo apt update` then `sudo apt install nmap wireshark`. No attack packages or password lists are needed.

## 4. Prepare Wazuh and the isolated network

Import the official [Wazuh OVA](https://documentation.wazuh.com/current/deployment-options/virtual-machine/virtual-machine.html), following its release-specific instructions; it contains the central components. Review its initial-access instructions locally and replace default credentials. Do not paste them into this repository. Provision/download dependencies with temporary NAT if necessary.

Power off all VMs. Settings → Network → Adapter 1 → Internal Network → `soc-lab`; enable Cable connected. Disable adapters 2–4. Disable shared clipboard, drag-and-drop and shared folders during exercises. Boot and assign the [static addresses](architecture.md) through each guest's network settings. In Windows: adapter IPv4 properties → manual address and mask `255.255.255.0`; leave gateway and DNS blank. On Linux use the desktop network editor or the distribution's documented persistent network configuration.

Verify the IP inside each VM with `ipconfig` (Windows) or `ip -br address` (Linux). Check `route print -4` and `ip route`: no default route should exist. Inspect IPv6 routes too; disable any unintended adapter or route before continuing. Confirm all VMs share the exact same internal-network name. Do not treat a failed ping alone as proof of isolation.

## 5. Install Sysmon

Download and extract [Microsoft Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) during provisioning. Review its license and executable signature. Copy `configs/sysmon-lab.xml` from this repository beside `Sysmon64.exe`. Open an administrator PowerShell in that directory:

```powershell
.\Sysmon64.exe -accepteula -i .\sysmon-lab.xml
```

For an existing installation use `-c .\sysmon-lab.xml` instead of `-i`. This deliberately small configuration captures process creation only. Check Event Viewer → Applications and Services Logs → Microsoft → Windows → Sysmon → Operational. Event 1 contains process metadata; Sysmon is not the source of Windows logon failure Event 4625.

## 6. Enable Windows logging

On the Windows VM, open administrator Windows PowerShell **5.1**. Confirm `$PSVersionTable.PSVersion`. Enable Logon success/failure auditing with the locale-independent subcategory GUID:

```powershell
auditpol /set /subcategory:"{0CCE9215-69AE-11D9-BED3-505054503030}" /success:enable /failure:enable
auditpol /get /subcategory:"{0CCE9215-69AE-11D9-BED3-505054503030}"
```

Enable script block logging: run `gpedit.msc` → Computer Configuration → Administrative Templates → Windows Components → Windows PowerShell → Turn on PowerShell Script Block Logging → Enabled. Open a fresh Windows PowerShell session afterward. This guide uses `powershell.exe`; PowerShell 7 uses different logging configuration/channel and is outside this baseline. [Microsoft reference](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_logging?view=powershell-5.1).

Run `Write-Output 'SOC-LAB-BASELINE'`. Check the PowerShell Operational channel for 4104. Keep personal commands and credentials out of logged sessions.

## 7. Verify Wazuh central services

From Windows inside the lab open `https://10.77.77.10`. Verify the expected lab server/certificate identity before accepting a local self-signed certificate warning. Use the official OVA instructions for initial login. On the Wazuh VM inspect:

```bash
sudo systemctl status wazuh-manager wazuh-indexer wazuh-dashboard filebeat
```

If the dashboard is unavailable, check guest addresses, service logs, and the documented OVA firewall configuration. Permit only the lab peers/ports listed in the architecture. Do not expose it through a router.

## 8. Enroll the Windows agent

In the dashboard, use Deploy new agent (label may vary), choose Windows, server `10.77.77.10`, agent name `WIN-LAB`. Obtain the matching official MSI during provisioning; use a manager-compatible agent version. Transfer it via an attached ISO or temporary provisioning folder, then remove the shared folder before simulations.

Run the MSI and set the manager/enrollment address as instructed by the dashboard. Use its generated version-specific install command only after reviewing it. Start the agent service. Verify the dashboard reports this agent Active; enrollment alone is not proof of event ingestion.

Back up `C:\Program Files (x86)\ossec-agent\ossec.conf` privately. Merge the `<localfile>` elements from [the example](../configs/windows-eventchannels.xml) **inside the existing `<ossec_config>`**. Preserve existing client and enrollment settings. Security is commonly already configured; do not duplicate it, and inspect existing filters for excluded events. Then:

```powershell
Restart-Service -Name WazuhSvc
Get-Service -Name WazuhSvc
Test-NetConnection 10.77.77.10 -Port 1514
```

Check `ossec.log` in the agent directory for errors. A TCP test checks reachability, not correct decoding. [Wazuh collection documentation](https://documentation.wazuh.com/current/user-manual/capabilities/log-data-collection/configuration.html).

## 9. Install Wireshark

Install the official Windows package from [Wireshark](https://www.wireshark.org/download.html) with its capture driver during provisioning. Open Capture Options and select the Windows adapter with address `10.77.77.20`. Capture only this isolated interface. Wireshark must be running before scenario 3 starts.

## 10. Verify telemetry and optional marker rules

Run a baseline command and verify it in Event Viewer before searching Wazuh. Open Threat Hunting/Discover with the alerts data view (`wazuh-alerts-*`), correct agent and a recent time range. Use [queries](../queries/useful-queries.md).

**Collected events are not all indexed as alerts.** If the local event exists but no alert appears, inspect the collection filters, agent/manager logs, decoder and rule matching. Use the optional [lab marker rules and deployment instructions](../detections/detection-notes.md) for bounded visibility. This project does not enable indefinite full-event archiving.

## 11. Run one simulation

Follow the four [README runbooks](../README.md). Log the start/end in UTC. Perform a baseline/negative control first. Stop if isolation is uncertain. No external targets or malware are needed.

## 12. Investigate

Record the original event ID, host alias, event time, source and relevant fields. Search adjacent events and test benign explanations. Do not infer compromise from a process name or a failed logon alone. Apply [the methodology](investigation-methodology.md).

## 13. Capture evidence

Follow [screenshots](../screenshots/README.md) and [evidence handling](../evidence/README.md). Keep originals private; publish only reviewed derivatives. A screenshot is a supporting artifact, not a replacement for analysis.

## 14. Complete and clean up

Copy the report template to a new report, fill observed facts, link sanitized evidence, and update the execution checklist. Close only after the evidence supports the result. Remove the temporary lab account, close created processes, stop capture, and restore the pre-exercise snapshot if desired **after exporting evidence privately**. Snapshot rollback loses events and changes VM time; record it. Never silently convert the illustrative report into supposed evidence.

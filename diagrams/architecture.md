# Evidence paths

**PLANNED topology.**

```mermaid
flowchart TD
  K["Kali on soc-lab"] -->|"Four-port probe"| W["Windows on soc-lab"]
  W --> S["Security, PowerShell and Sysmon logs"]
  W --> P["Endpoint Wireshark capture"]
  S --> A["Wazuh agent"]
  A --> M["Wazuh all-in-one on soc-lab"]
  M --> T["Triage and correlation"]
  P --> T
  T --> R["Evidence-backed report"]
```

Authentication and process exercises run locally on Windows. Only the network exercise needs Kali. No internet route is present during simulations. See [address and port plan](../docs/architecture.md).

# Architecture and boundaries

**PLANNED.** These are synthetic lab addresses, not discovered information about the author's network.

| VM | Example address | Purpose |
| --- | --- | --- |
| WAZUH-LAB | 10.77.77.10/24 | Manager, indexer, dashboard |
| WIN-LAB | 10.77.77.20/24 | Monitored endpoint; packet capture; analyst browser |
| KALI-LAB | 10.77.77.30/24 | Bounded scanner |

Use one VirtualBox **Internal Network** named `soc-lab` on all VMs. Disable all other adapters before simulations. Do not configure a gateway or DNS server. Do not enable routing, bridging, Internet Connection Sharing, or NAT forwarding. Internal networking excludes the host; host-only networking includes it. Browse the dashboard from Windows inside the lab. [Oracle networking reference](https://docs.oracle.com/en/virtualization/virtualbox/7.1/user/networkingdetails.html).

| Direction | TCP port | Purpose |
| --- | --- | --- |
| Windows → Wazuh | 1514 | Agent events |
| Windows → Wazuh | 1515 | Enrollment, when required |
| Windows browser → Wazuh | 443 | Dashboard |
| Kali → Windows | 135,139,445,3389 | Scenario 3 probes only; services need not be open |

Keep indexer 9200 and API 55000 restricted to the Wazuh VM unless an explicitly documented deployment requirement exists. Do not disable endpoint firewalls to make a scan look successful.

Download and update on temporary NAT during provisioning, then power off and switch to internal networking. Never run simulations with NAT still attached. Keep the same addresses before and after Wazuh certificate/enrollment configuration, or regenerate/reconfigure using its documented procedure.

Capture at Windows or the scanner: a separate third VM does not automatically see switched unicast traffic. Wireshark evidence does not flow into Wazuh merely because both tools are installed.

[Diagram](../diagrams/architecture.md) · [Setup](setup-guide.md)

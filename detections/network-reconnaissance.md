# Scenario 3 — Bounded network reconnaissance

**PLANNED simulation.**

## 1. Objective

Identify one source probing several destination ports and explain packet responses.

## 2. Environment

Kali `10.77.77.30`, owned Windows `10.77.77.20`, internal network only. These addresses are the synthetic plan. Verify they match your two VMs; otherwise stop and update the plan and command consistently. Keep Windows Firewall enabled.

## 3. Simulation

Start Wireshark on Windows' lab interface with capture filter `host 10.77.77.30`. From Kali run once:

```bash
nmap -sT -Pn -n -p 135,139,445,3389 --max-retries 0 --scan-delay 500ms --host-timeout 15s 10.77.77.20
```

This requests a TCP connect scan of four ports on one owned endpoint. No scripts, exploitation, service-version probing, subnet ranges or public hosts. `-Pn` skips discovery; `-n` avoids DNS lookups. The timeout bounds the attempt and can make results incomplete. [Nmap scan reference](https://nmap.org/book/man-port-scanning-techniques.html).

## 4. Telemetry generated

Wireshark should capture outgoing/incoming traffic visible at that endpoint. SYN requests, SYN/ACK for accepted connections, RST responses or unanswered requests may occur. Filtering can yield no response; do not interpret it as a proven closed port. Record actual behavior, not an expected port list.

## 5. Detection

Display filter:

```text
ip.src == 10.77.77.30 && ip.dst == 10.77.77.20 && tcp.flags.syn == 1 && tcp.flags.ack == 0
```

Count distinct destination ports within the recorded window. Repeated SYNs can be retransmissions. There is **no automatic Wazuh scan alert promised**: this baseline has no network IDS ingestion or Windows firewall auditing rule for scans. Sysmon process collection alone cannot see every rejected inbound connection.

## 6. Investigation

Compare packet times with the Nmap start/end. Inspect Conversations and the selected packets. Negative control: capture 30 seconds of idle lab traffic before the scan and compare port diversity. Approved inventory scanners can produce similar behavior.

## 7. Evidence

Stop capture and save PCAPNG privately; publish a reviewed screenshot showing filters, source/destination aliases and TCP flags. Note that a capture on Kali proves sent traffic; a capture on Windows additionally shows arrival at the target interface. Neither alone proves application compromise.

## 8. Analyst conclusion

Pending. Describe observed port probes, capture vantage point, and response limitations. No exploitation was attempted.

## 9. Recommended response

Stop the scan; no service changes are necessary. For an unexplained real-world pattern, validate scanner ownership and scope before proposing isolation. Do not open ports just to improve the screenshot.

## 10. MITRE ATT&CK

[T1046 — Network Service Discovery](https://attack.mitre.org/techniques/T1046/) fits this controlled port-discovery behavior. Technique similarity does not establish hostile intent.

# SOC-LAB-001 — Repeated Failed Authentication Attempts

> **EXAMPLE ONLY — hypothetical worked report. No events were executed or observed for this report. Every outcome below describes an illustrative case.**

| Field | Illustrative value |
| --- | --- |
| Incident ID | SOC-LAB-001 |
| Severity | Medium — hypothetical triage priority, not measured risk |
| Status | Closed — Simulation (example only; actual execution pending) |
| Affected host | WIN-LAB, synthetic alias |
| Account | soclab, designated example lab account |

## Executive Summary

In this hypothetical case, an operator intentionally submits three incorrect passwords on an isolated endpoint. An analyst checks the resulting authentication records, relates them to the exercise window, and finds the pattern consistent with the authorized test. This is not a claim about completed work or real attackers.

Required declaration for the completed real simulation report:

“This incident was generated intentionally inside an isolated cybersecurity home lab for educational purposes.”

That declaration becomes factual only after the learner actually performs the exercise.

## Detection Source

Proposed source: Security Event 4625 collected by the Windows Wazuh agent; manual grouping of failures. Rule 100510 would surface individual failures if validated and deployed. No aggregated brute-force rule has been deployed by this repository.

## Timeline

The following relative times are fictional; they are not captured timestamps.

| Relative time | Hypothetical event |
| --- | --- |
| T+00 s | Operator records start |
| T+20 s | First failed local attempt |
| T+40 s | Second failed local attempt |
| T+60 s | Third failed local attempt |
| T+120 s | Analyst reviews source events and alert search |

## Indicators

Repeated failures against the same lab account are the illustrative signal. No external IP, attacker domain, malware hash or compromise indicator has been observed. Local `runas` may provide no source network address.

## Evidence

**SCREENSHOT REQUIRED.** No evidence IDs, counts or hashes are supplied as actual results. Capture instructions are in [screenshots](../screenshots/README.md).

## Investigation

A completed investigation would compare host, account, failure reason, logon type and exercise times; search for related successes; and consider typos or saved credentials. The hypothetical attribution to the operator depends on those checks. No claim of a successful or prevented breach follows from failed logons alone.

## MITRE ATT&CK Mapping

Conceptual [T1110.001](https://attack.mitre.org/techniques/T1110/001/) relationship for deliberate guesses; this is a controlled telemetry exercise.

## Root Cause

Illustrative explanation: intentionally incorrect input. Actual root cause remains unassessed until execution and evidence review.

## Containment Recommendation

For the hypothetical known test, stop further attempts. No host isolation or automatic blocking is warranted solely by these three failures.

## Remediation

Verify account state, remove the disposable account after preserving evidence, and restore the intended lab baseline. For unexplained equivalent behavior, investigate related successes before recommending credential actions.

## Analyst Conclusion

Example conclusion: the observed cluster is consistent with a controlled test and no further response is justified by the scoped evidence. **Do not reuse this conclusion as a factual result without doing the investigation.**

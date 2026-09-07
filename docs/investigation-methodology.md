# Investigation methodology

**IMPLEMENTED: procedure. PLANNED: case execution.**

1. **Scope:** record authorized VM aliases, exercise, UTC start/end and expected effects.
2. **Validate:** find the original event before interpreting an alert. Check provider, channel, host, policy and ingest delay.
3. **Correlate:** join by time plus account/logon context or process GUID; do not rely on PID alone. State capture vantage point for network evidence.
4. **Compare hypotheses:** deliberate lab action; user mistake; routine automation; missing telemetry. State which evidence supports or contradicts each.
5. **Assess:** distinguish observed behavior, inferred cause, potential impact and unknowns. Severity is your reasoned case assessment, not a copied rule level.
6. **Respond:** propose only actions justified by scope. For a known harmless test, stopping the test and documenting it is usually sufficient.
7. **Close:** record evidence references, bounded conclusion, confidence, limitations and cleanup.

Example phrasing: “Three failures were observed for the lab account in the selected two-minute window; the operator's recorded exercise is consistent with these events.” Use that sentence only if three failures were actually recorded. Avoid “a hacker was blocked” without evidence of either claim.

## Time and confidence

Record event creation time and SIEM timestamp separately. Keep original timezone offsets; normalize the investigation timeline to UTC. Synchronize clocks during provisioning and check again after snapshots. High confidence in intentional test generation does not imply complete visibility of the host.

## Evidence handling

Use [the evidence register](../evidence/README.md), private originals and public redacted derivatives. Record SHA-256 of originals for your private working record, and hashes of sanitized artifacts separately. Never fabricate missing fields.

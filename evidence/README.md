# Evidence handling

**No evidence has been collected.** Keep raw EVTX, JSON alerts, PCAPNG and screenshots outside the public repository (or under the ignored `evidence/private/` directory). Ignore rules reduce accidents; they do not inspect content or remove already tracked files.

For every real item maintain a private register: evidence ID, incident ID, filename, host alias, collection time UTC, tool/version, source interval, SHA-256, original location, redactions and sanitized output name. On Windows use `Get-FileHash -Algorithm SHA256 -LiteralPath 'actual-file-path'`; substitute a real existing path. Hash originals and derivatives separately.

Only publish reviewed text extracts or flattened screenshots. Inspect command lines, script contents, packet payloads and image metadata for secrets. Synthetic addresses in this project's topology are safe design examples, not evidence of the author's network. Never upload VM disks, installation credentials or private keys.

Collect a UTC timeline and a negative control as well as the positive result. Mark unavailable records as unavailable rather than inventing values.

# Security Controls Overview

## Encryption

- **In transit:** TLS 1.2+ / TLS 1.3; strong cipher suites
- **At rest:** AES-256 (databases/storage); managed cloud storage encryption
- SFTP file transfers: AES with minimum 128-bit key length
- Credentials: not stored/transmitted in clear text; hashing with unique salting
- SHA2 for integrity protection against tampering
- PII masking in UI/API/logs; RBAC-gated unmasked access

## Key management

- Encryption keys managed by Marmin via KMS
- Key rotation enforced every **90 days**
- **Customer-managed keys / BYOK:** **not allowed**. Keys are Marmin-managed via KMS only.

## Application / API security

- Short-lived JWT authentication
- RBAC authorization
- Rate limiting, IP allowlisting, replay protection
- WAF on public-facing apps
- HTTPS FQDN with TLS certificates; EV certs for public sites
- Session controls: terminate on logout; session ID changed each login; session not allowed on multiple systems/devices
- Idle session timeout ≤ 15 minutes
- Maker-checker for critical user admin / transaction processing

## Infrastructure security

- Private VPCs with restricted ingress/egress
- Network policies for service-to-service boundaries
- Secrets via vault (not hardcoded)
- OS hardening, patching, vulnerability assessment
- Endpoint protection / anti-malware on servers
- Principle of least privilege
- Zero Trust network model

## Audit & monitoring

Audit coverage includes: authentication events; admin activities; invoice submissions/processing; API/integration activity; security-relevant events; user administration.

Audit logs protected against unauthorized modification; no credentials/PAN/PII in logs (masked if needed).

Security log retention: **6 months**. Application monitoring logs generally **not** directly downloadable by customers in SaaS model; relevant security log info can be provided on request.

## Incident management

Formal process aligned with ISO 27001 and SOC 2:

- Identification/classification → containment/remediation → RCA → CAPA → customer notification per contract/regulation
- Recent enterprise cloud response claims: no material customer-data confidentiality breach; no ransomware; no regulatory non-compliance; minor ops incidents under standard IR
- 24×7 monitoring; automated alerting; post-incident review

## Vulnerability management

- Continuous vulnerability scanning
- Dependency / third-party component reviews
- Risk-based prioritization
- Scheduled + emergency patching
- Periodic penetration testing / VAPT
- VAPT every **3 months** (implementation questionnaire); periodic VAPT and DR validation (enterprise SaaS annexure)

## Data anonymization / masking

Techniques: irreversible hashing/salting; tokenization; data substitution; minimization.  
Applied for non-prod use of prod-like data. Runtime masking in UI/API; DB views; log redaction pipelines.

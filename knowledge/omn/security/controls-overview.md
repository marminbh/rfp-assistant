# Oman Security Controls — Overview

Platform security for Oman deployments follows Marmin’s managed SaaS / dedicated-cloud security baseline, with enterprise controls for customer-managed infrastructure deployments.

## Confirmed for RFP use

- Authenticated API access via **Kong API Gateway**; RBAC; audit logging
- Peppol / OTA transmission over the configured network path
- Oman PDPL compliance; PCI-DSS controls where card data is in scope
- CBO security-gap certification letter available
- OWASP-aligned secure coding and OWASP API Security Top 10 controls
- Encryption: **AES-256** at rest; **TLS 1.2+** (TLS 1.3 preferred) in transit; HSTS; mTLS for high-assurance service traffic
- Keys/secrets via Vault / HSM / KMS patterns — not hardcoded
- SIEM-integrable audit logging (retain ≥90 days where required)
- Kubernetes container security baselines; separate Dev / QA / Staging / Production
- Backup & DR: **RPO less than 5 minutes**, **RTO less than 1 hour** (see `../operations/business-continuity-dr.md`)
- Integration with SIEM, SCM, DAM, PAM, and IAM controls where required
- Maker-checker; full application audit trail

## Partial / configuration

- LDAP / Active Directory authentication for internal staff
- Customer password-policy configuration (expiry, weak-password detection, periodic change)
- Full OAuth 2.0 / JWT enterprise IdP patterns with customer infrastructure
- API keys as sole authentication factor (treat as identifiers; customize if required)
- Compatibility with a named customer security/backup tool stack
- Full infrastructure-component log shipping to customer SIEM
- Point-in-time production restore (engagement validation with customer backup tooling)

## Not supported

- Native integration with customer OSS monitoring via Email / SMS / SNMP anomaly alerts
- Customer-managed encryption keys / BYOK — not documented; answer **I don't know the answer** unless separately confirmed

## Detailed sections

- `authentication-iam.md` — authentication, sessions, passwords, MFA, LDAP
- `encryption-keys.md` — AES/TLS, key management
- `infrastructure-security.md` — network, DMZ, WAF, logging
- `container-security.md` — Kubernetes / Docker controls
- `platform-component-security.md` — MongoDB, Redis, RabbitMQ, object storage, Peppol AP
- `application-security.md` — OWASP secure coding, crypto, VAPT
- `api-security.md` — API gateway + OWASP API Top 10

Do not copy UAE-only residency matrices (Abu Dhabi / Mumbai / Singapore) into Oman answers unless separately confirmed for Oman.

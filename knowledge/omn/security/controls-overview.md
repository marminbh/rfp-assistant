# Oman Security Controls — Overview

Platform security for Oman deployments follows Marmin’s managed SaaS / dedicated-cloud security baseline.

## Confirmed for RFP use

- Authenticated API access; RBAC; audit logging
- Peppol / OTA transmission over the configured network path
- Oman PDPL compliance
- CBO security-gap certification letter available
- OWASP-aligned secure coding practices supported across application development controls
- OWASP API Security Top 10 (2023) controls supported, with one customization note on API-key-only auth
- TLS 1.2 minimum (TLS 1.3 preferred); HSTS; no insecure TLS fallback
- Integration with SIEM, SCM, DAM, PAM, and IAM controls where required
- Full comprehensive audit trail; maker-checker

## Customization / caveats

- LDAP / AD-only authentication: customization required
- Using API keys as the sole authentication factor: customization required (treat keys as identifiers; rotate and store securely)
- Customer-managed encryption keys / BYOK: not documented for Oman — answer **I don't know the answer** unless separately confirmed

## Detailed sections

- `authentication-iam.md` — authentication, sessions, passwords, MFA, LDAP
- `application-security.md` — OWASP secure coding, crypto, data protection, VAPT
- `api-security.md` — OWASP API Security Top 10 (2023)

Do not copy UAE-only residency matrices (Abu Dhabi / Mumbai / Singapore) into Oman answers unless separately confirmed for Oman.

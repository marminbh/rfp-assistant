# Application Security Controls Checklist (v2.3) — Highlights

Status values from the completed checklist are **Compliant** unless noted.

## Solution design

- Process/data flow diagrams; web/app server separation and network zones; architecture with ports/protocols/auth and WAF in DMZ
- Dev/Test separated from Production
- Sensitive data not in non-prod unless scrambled
- AV/anti-malware on servers; DR/backup servers in place

## User administration

- Unique User IDs; no duplicates
- Default accounts disabled/changed; service accounts documented, complex passwords, no interactive login unless justified
- Maker-checker for user admin / critical processing
- RBAC with approved roles matrix
- Detailed audit logs for user admin; entitlement/activity reports (incl. inactivity 45+ days, failed logins, last login/mod dates)

## Password / session standards

- Admin password expiry 30 days; user 90 days
- History 6; min length 8; complexity enforced
- First-login password change; lockout after 6 failures; 30-min lockout
- Dormant after 90 days inactivity; idle timeout ≤15 min
- MFA for critical/public-facing apps

## Audit logging

- Required security audit attributes present; no sensitive data in logs
- SIEM monitoring integration
- Download accountability (user id on report download)
- Restricted, tamper-protected audit log access

## Data validation

- Maker-checker for critical transactions
- Input validation; buffer overflow protections (validated via IBM AppScan)
- File upload validates size, content type, format
- Autocomplete disabled on password fields

## Auth / session / crypto

- Random access tokens for external system auth
- Full session termination on logout; session ID rotation; no multi-device concurrent session ID reuse
- TLS 1.2+; FQDN certs; EV for public; internal CA for internal; WAF; SFTP AES ≥128-bit; salted credential hashes; SHA2; encryption of sensitive data; PII masking

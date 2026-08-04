# Oman Application Security

OWASP-aligned secure coding and application security practices are supported for Oman deployments. Controls below are organized by theme for RAG.

## Input validation

- Validate all data on a trusted system (server-side); classify trusted vs untrusted sources
- Centralized input validation; specify character sets (e.g. UTF-8); canonicalize before validating
- Validation failures reject input; validate parameters, URLs, headers, cookies, and automated postbacks
- Prefer allow-lists; encode/sanitize hazardous characters
- Discrete checks for null bytes, CRLF, path traversal, double-encoding
- Prevent XFS, CRLF / header splitting, and SSRF (allow-list destinations; block internal/loopback/cloud metadata)

## Output encoding

- Encode on trusted system; contextually encode untrusted outbound data
- Sanitize untrusted data to SQL, XML, LDAP queries, and OS commands

## Access control

- Authorization from trusted server-side objects; site-wide authorization component; fail securely
- Enforce authZ on every request; deny by default; least privilege
- Restrict files, URLs, functions, direct object refs, services, and security config
- Presentation-layer and server-side rules must match
- Rate-limit transactions; Referer header never sole authZ check
- Account auditing; disable unused accounts; terminate sessions when authorization ceases
- Restrictive CORS; no wildcard origins on authenticated endpoints

## Cryptographic practices

- Crypto protecting secrets runs on trusted system; modules fail securely
- Approved CSPRNG for unguessable randoms
- Cryptographic modules validated to **FIPS 140-3** (or equivalent); note FIPS 140-2 retirement
- Documented key-management policy/process
- Keys stored separately from encrypted data; protected in transit and at rest
- Only approved algorithms/key lengths/protocols; crypto-agility including post-quantum readiness
- Customer-managed BYOK is not documented for Oman — do not assert it

## Error handling & logging

- No sensitive data in errors; no stack traces to users; generic custom error pages
- Logging on trusted system for security events; no passwords/session IDs in logs
- Forward to centralized log management / SIEM; NTP clock sync
- Cryptographic hash to validate log-entry integrity
- Log validation failures, auth attempts, access-control failures, tampering, invalid sessions, admin/security-config changes, TLS/crypto failures

## Data protection

- Least privilege; purge temporary/cached sensitive files promptly
- Encrypt highly sensitive stored auth verification data
- No clear-text passwords/connection strings on client; no sensitive data in GET parameters
- Disable client caching on sensitive pages (`Cache-Control: no-store`)
- Encrypt stored PII and confidential data per regulation
- Enforce data-retention policies; encrypt confidential data on portable media, backups, and outside trusted hosting

## Communication security

- Encrypt all sensitive transmission (TLS; may supplement with file encryption)
- Valid TLS certificates; failed TLS must not fall back to insecure connection
- **TLS 1.2 minimum (TLS 1.3 preferred)**; weak protocols/ciphers disabled
- Enforce **HSTS** on all HTTPS endpoints

## System configuration

- Latest approved versions and patches; directory listings off; least privilege service accounts
- Remove unnecessary functionality and non-production test code
- Define supported HTTP methods; disable unnecessary methods
- Remove version info from response headers
- Security headers: CSP, X-Content-Type-Options, X-Frame-Options / CSP frame-ancestors, Referrer-Policy, Permissions-Policy
- Isolate development from production; change-control for code

## Database security

- Strongly typed parameterized queries; least privilege DB access
- Encrypted connection strings in separate config (not hard-coded)
- Close connections promptly; change default admin passwords
- Surface-area reduction; different credentials per trust distinction

## File & memory management

- Authenticate before upload; validate type by file headers; store uploads outside web context
- No execute on upload dirs; malware scan uploads
- Safe memory/resource handling for unmanaged code paths; avoid known vulnerable copy APIs

## Secure SDLC & VAPT

- Formal Secure Development Lifecycle (requirements, threat modeling, secure design, coding, testing, deployment)
- Continuous SCA + SBOM; automated secrets scanning in CI/CD
- Mandatory automated SAST before deploy with severity thresholds
- Independent VAPT covering web, mobile, APIs/web services, microservices, integrations, backends/DBs, network, and infrastructure
- Frameworks: OWASP Top 10, OWASP API Top 10, OWASP Mobile Top 10, SANS Top 25, CSA threats, CWE/SANS, PCI DSS, ISO 27001
- Methods: black/white/gray-box; DAST; SAST; IAST where applicable; SCA
- Remediation: Critical/High fixed before production; Medium planned; Low documented; all fixes retested

## Security control integrations

Supports integration with SIEM, SCM (Security Configuration Management), DAM, PAM, and IAM.

## Central Bank of Oman

Vendor will provide a letter certifying that the supplied application/solution is free from any known security gaps, as required by the **CBO**.

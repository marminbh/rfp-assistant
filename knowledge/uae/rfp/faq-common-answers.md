# RFP FAQ — Common Questionnaire Answers

Use with `conflicts-and-caveats.md` before locking numbers.

## Availability & SLA

- Target availability: **99.9%+** (most docs); some questionnaires state **99.99%**.
- Auto-scaling: Yes.
- Planned downtime: ~1 min/week (implementation questionnaire).

## Data residency

- Production: UAE — **Abu Dhabi** (current matrix).
- Replica: **Mumbai**.
- DR: **Singapore** (residency matrix); BC overview also describes **Mumbai** app DR.
- Hosting provider: **Oracle Cloud**. AWS used for encrypted backup storage.
- Arbitrary customer DC selection: **not** in standard SaaS.

## Tenancy

- Standard: multi-tenant logical isolation.
- Dedicated single-tenant available commercially.
- Multi-entity in one organization instance: Yes.

## RPO / RTO (pick carefully)

Common UAE SaaS answer set:

- RTO ≤ 1 hour; RPO near-zero / no data loss for committed transactions; DR tested quarterly.

Alternate conservative annexure answer:

- RTO ≤ 4 hours; RPO ≤ 1 hour; backup/restore DR.

Questionnaire variant: RPO <15 min; RTO <1 hr.

## Backups

- Continuous multi-region DB replication + automated backups.
- S3 encrypted hourly backups, 15-day retention (residency matrix).
- Backup/restore drills every 3 months; last cited successful restore 4 Apr 2026.
- Backups stored in separate region: Yes (Singapore).

## Encryption & keys

- In transit: TLS 1.2 / 1.3
- At rest: AES-256 / cloud-managed encryption
- Keys: Marmin-managed KMS; rotation every 90 days
- Customer-managed encryption keys (BYOK): **not allowed**

## Security certifications

ISO 27001 / ISO 27001:2022; SOC 2 Type II; GDPR.

## Authentication

- Email/password + MFA (email OTP): Yes.
- Password policy (checklist): admin expiry 30 days; user 90 days; history 6; min length 8; lockout after 6 failures / 30 min; idle timeout ≤15 min.
- Session: terminate on logout; session ID rotated each login; not reusable across multiple devices.
- SSO/SAML/OIDC/Entra ID: conflicting — treat as roadmap/not GA unless Security Overview is the approved source for that bid.
- IP whitelisting: configurable.
- Audit/user activity logs: Yes; SIEM integration for security events.
- Application security checklist v2.3: see `../security/application-security-checklist.md`.

## Integrations

- API (documented), SFTP bulk, WebApp, AI PDF extraction, middleware platforms: Yes.
- Docs: https://docs.ae.marmin.ai/

## Exit

Full extraction (XML, PDF, CSV/XLSX, structured dumps), SFTP delivery, certified purge after confirmation; regulatory retention may block early deletion.

## Implementation / company

- Timeline: 2–6 weeks typical, or up to ~4 months for larger enterprise plans.
- Local team: Dubai; also Bangalore development/support.
- Employees: 100+.
- Support by Principal; portal https://marmin.ai.

## Incidents (recent enterprise cloud response)

No material confidentiality breach; no ransomware; no regulatory non-compliance.

## Audit rights

Customer audit rights, regulatory inspections, evidence sharing, log export, VA/PT coordination — subject to governance, tenant isolation, CSP shared-responsibility limits.

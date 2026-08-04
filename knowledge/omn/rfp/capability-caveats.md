# Oman Capability Caveats

Use these caveats when answering RFPs. Prefer section docs under `product/`, `architecture/`, `deployment/`, `security/`, `compliance/`, and `operations/` for detail.

## Response codes (internal meaning)

| Code | Meaning |
|---|---|
| **SUP** | Supported in base package without further enhancement |
| **CST** | Customization required during implementation (priced in commercial proposal) |
| **FUT** | On product roadmap within ~12 months of go-live; no additional cost |
| **NS** | Not supported and not scheduled within the next calendar year |
| **PC** | Partial — supported with configuration and/or customer-managed infrastructure |

## Customization / partial (CST or PC)

- Full LDAP / Active Directory authentication for internal staff
- AD-only user setup when Windows auth is used (depends on LDAP)
- Customer password-policy configuration (weak-password detection, expiry, periodic change)
- Full OAuth 2.0 / JWT enterprise IdP patterns with customer infrastructure
- API keys as sole authentication factor (treat as identifiers; rotate/store securely)
- Compatibility with a named customer security / backup tool stack
- Full infrastructure log shipping to customer SIEM (app audit logging is standard)
- Point-in-time production restore (validate with customer backup tooling)
- Multi-format security/ops reports beyond CSV/XLSX (PDF/DOC/XML reporting asked in some RFPs is partial)

## Roadmap / future (FUT)

- Full compatibility with Windows Server 2022 and above
- Full compatibility with Windows 11 and above
- Admin activity reports
- Scheduled e-mail report distribution
- SMS/Email with incident details
- Maintaining settlement account with the customer bank

## Not supported (NS)

- JSON import
- Uniform customizable Look & Feel across platforms
- Print and help on all screens
- End-user created/modified/published reports and schedules
- Microsoft Exchange integration
- Bank-specific customization beyond documented options (scope-dependent)
- Blockchain / distributed ledger
- Automation and robotics (RPA)
- Database dictionary for auditors (all tables/variables/interconnections)
- Islamic banking / Shari’ah processing support
- Native customer OSS monitoring via Email / SMS / SNMP anomaly alerts

## Confirmed DR numbers (do use)

- **RPO less than 5 minutes**, **RTO less than 1 hour** — see `../operations/business-continuity-dr.md`

## Partial / nuanced (product)

- Personalization: Arabic language customization supported; broader personalization not supported
- Import/export: Excel/CSV supported; PDF customizable; XML future
- Reports: CSV/XLSX standard; broader formats may be partial depending on report type

## Customer-process items (not product defects)

- Revoking vendor staff physical/logical permissions at project handover is a **customer project-management** responsibility, not a Marmin product feature gap.

## Answering rules

- Do not invent Oman hosting **city/region** or certification **IDs** not documented under `omn/`
- Do not reuse UAE FTA / PINT-AE / Abu Dhabi–Mumbai–Singapore residency facts for Oman
- Do not name specific prior customers (e.g. telecom RFP sources) in answers — keep answers generic
- If unknown: answer exactly **I don't know the answer.**

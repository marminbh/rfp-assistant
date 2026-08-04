# Oman Capability Caveats

Use these caveats when answering RFPs. Prefer section docs under `product/`, `architecture/`, `deployment/`, `security/`, `compliance/`, and `operations/` for detail.

## Response codes (internal meaning)

| Code | Meaning |
|---|---|
| **SUP** | Supported in base package without further enhancement |
| **CST** | Customization required during implementation (priced in commercial proposal) |
| **FUT** | On product roadmap within ~12 months of go-live; no additional cost |
| **NS** | Not supported and not scheduled within the next calendar year |

## Customization required (CST)

- Full LDAP integration for user authentication
- AD-only user setup when Windows auth is used (depends on LDAP)
- API keys as sole authentication factor (treat as identifiers; rotate/store securely)

## Roadmap / future (FUT)

- Full compatibility with Windows Server 2022 and above
- Full compatibility with Windows 11 and above
- Admin activity reports
- Scheduled e-mail report distribution
- SMS/Email with incident details
- Maintaining settlement account with the customer bank

## Not supported (NS)

- JSON import
- Multi-format reporting beyond CSV/XLSX
- Uniform customizable Look & Feel across platforms
- Print and help on all screens
- End-user created/modified/published reports and schedules
- Microsoft Exchange integration
- Bank-specific customization beyond documented options (scope-dependent)
- Blockchain / distributed ledger
- Automation and robotics (RPA)
- Database dictionary for auditors (all tables/variables/interconnections)
- Islamic banking / Shari’ah processing support

## Partial / nuanced

- Personalization: Arabic language customization supported; broader personalization not supported
- Import/export: Excel/CSV supported; PDF customizable; XML future
- Vendor demographics for a specific annexure sheet may be empty — use `shared/rfp/company-demographics.md` for approved Marmin company facts

## Answering rules

- Do not invent Oman hosting regions, RTO/RPO numbers, or certification IDs not documented under `omn/`
- Do not reuse UAE FTA / PINT-AE / Abu Dhabi–Mumbai–Singapore residency facts for Oman
- If unknown: answer exactly **I don't know the answer.**

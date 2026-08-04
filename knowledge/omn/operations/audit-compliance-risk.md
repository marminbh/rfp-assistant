# Oman Audit, Compliance & Risk Controls

## Audit

- Audit log detailing all transactions; changes by authorized users with old value, new value, and dates
- Log all user authorization changes and permission escalations
- Log every manual override, parameter modification, and system rule exception
- Log every failed/success login and access rejection
- Specific user tracking IDs (no shared/generic admin accounts)
- Read-only Audit profile that can read/export reports, dashboards, system settings, and screens
- Application audit logging retainable for at least **90 days** where required by customer baseline
- Logs integrable with enterprise monitoring / SIEM (full infra-component shipping may be partial — see `../security/infrastructure-security.md`)
- Database dictionary listing all tables, variables, and interconnections: **not supported**

## Product security assurance

- Documented Secure Software Development Lifecycle (S-SDLC)
- Regular independent third-party security assessments; vendor responsible for SAST/DAST of customized components
- Warranty for code, components, and configurations developed/customized/deployed
- Written confirmation for third-party/open-source components used in the solution
- Vulnerability remediation with SLA timelines; Threat Advisories for product vulnerabilities
- Documentation of applicable security standards/certifications available for the engagement (do not invent certificate numbers)
- PCI-DSS-aligned controls when systems manage, store, or process card data

## Compliance operations

- Retain records per regulatory retention requirements
- Oman PDPL compliance; data privacy framework aligned with industry best practices (e.g. GDPR-style controls where relevant)
- Regulatory reporting obligations supported
- Prompt invoice retrieval for regulatory inspections and investigations
- Exception detection (duplicates, unusual amendments, cancellations) for fraud support
- Data classification, labelling, and handling per industry/customer information security policies
- Personal data processed per applicable retention and deletion rules
- Data Loss Prevention (DLP) technologies/rules per risk assessment where required
- On-premise / hybrid deployments: sensitive customer data not shared outside the approved customer network or cloud without exception approval
- NDA and vendor-staff monitoring for project personnel

## Risk & governance support

- Support bank/enterprise governance: arrangement ownership, audit support, segregation of duties, conflict checks, regulatory/board approval evidence where applicable
- Provide information for materiality/criticality assessment (service scope, dependency, substitutability, concentration risk, cloud/offshore elements, subcontractors)
- Operational risk controls: process resilience, maker-checker, input validation, exception handling, audit trails; fraud controls and change management; UAT, training, post-implementation support
- Third-party due diligence materials: legal entity details, ownership/UBO, financial viability, sanctions/adverse media, litigation/regulatory history, references, certifications, security assurance reports, support model, roadmap, end-of-life policy
- Disclose subcontractors and critical supply-chain dependencies
- Contractual commitments: scope/SLAs, audit rights, **CBO** and control-function access, confidentiality and banking secrecy, data ownership, data location controls, sub-outsourcing consent, termination, exit assistance, liability/indemnity, insurance, compliance with **Omani law**, reporting obligations
- Cloud and hosting controls: hosting model, data centre locations, tenant isolation, shared responsibility, portability/exit, backup, resilience
- Regulatory approvals and records for CBO approval/no objection, outsourcing register updates, record retention, material incident reporting
- Monitoring and ongoing assurance: SLAs, service reviews, annual DD refresh, updated certifications/reports, incident/breach reporting, remediation tracking
- Exit, portability and transition: exit strategy, data export formats, transition assistance, knowledge transfer, return/destruction of bank data
- Public disclosure: do not use customer name, logo, or officer references without written consent
- Ethics / reputation: no history/involvement in unethical practices impacting customer reputation

## Business continuity & DR

See `business-continuity-dr.md` for recovery targets (**RPO less than 5 minutes**, **RTO less than 1 hour**), backup types, HA, and environment segregation.

## Islamic banking / Shari’ah

Islamic banking processing support (profit calculation, AAOIFI-compatible accounting outputs, Shari’a review support) is **not supported** in the current Oman e-invoicing offering.

## Commercial caveat

Maintaining a settlement / account-maintenance arrangement with the customer bank for payments is on the **future** roadmap, not base package today.

# Oman RFP FAQ — Common Answers

## Product

- Marmin supports Oman e-invoicing with Peppol / **PINT OM** document exchange, B2B/B2G/B2C issuance, invoice receipt, and OTA tax reporting.
- Taxpayer onboarding with Peppol **SML/SMP** registration and status tracking.
- B2C: compliant QR codes and PDF invoices with QR.
- Integrations: REST APIs (Kong gateway), webhooks, WebApp, bulk upload, SFTP, MQ; XVAT / FA / core banking / ERP / ESB.
- API docs: **https://docs.om.marmin.ai**
- Arabic UI, maker-checker, role-based dashboards; report export Excel/CSV/PDF.

## Compliance

- 5-Corner Model, XVAT / OTA Data Dictionary, OTA-approved ASP, PINT OM enrichment.
- Oman PDPL compliance supported; S-SDLC and independent security assessments supported.
- PCI-DSS-aligned controls when card data is in scope.
- History purge: only data older than **10 years** (regulation).
- Decimal rules: quantity and unit rate max **8** decimals; other amount fields **2**.
- Mandate applicability and legal tax advice are customer responsibilities.

## Technical / infrastructure

- SaaS / PaaS / IaaS / on-prem; cloud-agnostic microservices on Kubernetes.
- Stack: MongoDB, PostgreSQL, RabbitMQ, Redis; Ubuntu **26.04 LTS**; Kong API Gateway.
- Environments: Production (OTA-connected) and Sandbox/Test; also Dev/QA/Staging as needed.
- Sizing is engagement-specific (reference proposals: **7/5** compact or **11/9** bank-scale).
- LDAP / AD auth and customer password-policy tuning: configuration / customization.
- Windows Server 2022+ / Windows 11+: roadmap / future.

## Delivery & support

- Typical implementation: **6–8 weeks** (scope-dependent).
- Major releases about every **3–6 months**.
- 24×7 enterprise support under SLA (MENA-capable).

## Security & DR

- OWASP secure-coding, web, and API Top 10 controls supported.
- Encryption: AES-256 at rest; TLS 1.2+ (TLS 1.3 preferred) in transit; secrets via Vault/HSM/KMS patterns.
- Backup & DR: **RPO less than 5 minutes**, **RTO less than 1 hour**; secondary geographic DR site.
- API keys as sole authentication factor: customization required.
- OSS Email/SMS/SNMP monitoring integration: not supported.
- CBO security-gap certification letter: supported.
- Do **not** answer Oman questions using UAE-only residency, FTA, or PINT-AE details — use **PINT OM**.
- If Oman-specific hosting **city/region** or certification **IDs** are not documented: **I don't know the answer.**

## Company

- Company demographics live under `shared/rfp/company-demographics.md`.
- Do not invent vendor staffing or reference counts without shared demographics or approved bid materials.
- Do not name specific prior bank customers in answers.

## Caveats index

See `capability-caveats.md` for SUP / CST / PC / FUT / NS summaries.

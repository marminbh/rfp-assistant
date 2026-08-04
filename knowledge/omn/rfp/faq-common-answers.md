# Oman RFP FAQ — Common Answers

## Product

- Marmin supports Oman e-invoicing with Peppol-oriented document exchange, sale/purchase APIs, and party management.
- OTA alignment: 5-Corner Model, XVAT / OTA Data Dictionary, OTA-approved ASP for validated tax invoices.
- Integrations: REST APIs, webhooks, WebApp, bulk upload, SFTP, MQ/web services.
- Arabic UI, maker-checker, role-based dashboards, configurable logo.

## Compliance

- Technical enablement for Peppol / Oman e-invoicing workflows is in scope.
- Oman PDPL compliance supported.
- History purge: only data older than **10 years** (regulation).
- Decimal rules: quantity and unit rate max **8** decimals; other amount fields **2**.
- Mandate applicability and legal tax advice are customer responsibilities.

## Technical / infrastructure

- N-tier microservices on Kubernetes; VMware supported.
- Stack: MongoDB, PostgreSQL, RabbitMQ, Redis; proposed OS Ubuntu **26.04 LTS**.
- Proposed sizing: **7** production servers, **5** test servers.
- LDAP / AD-only auth: customization required.
- Windows Server 2022+ / Windows 11+: roadmap / future.

## Security

- OWASP secure-coding and API Top 10 controls supported.
- API keys as sole authentication factor: customization required.
- CBO security-gap certification letter: supported.
- Do **not** answer Oman questions using UAE-only residency, FTA, or PINT-AE details.
- If Oman-specific hosting regions, RTO/RPO numbers, or certifications are not documented: **I don't know the answer.**

## Company

- Company demographics live under `shared/rfp/company-demographics.md`.
- Do not invent vendor staffing or reference counts without shared demographics or approved bid materials.

## Caveats index

See `capability-caveats.md` for SUP / CST / FUT / NS summaries.

# Oman RFP FAQ — Common Answers

## Product

- Marmin supports Oman e-invoicing with Peppol-oriented document exchange, sale/purchase APIs, and party management.
- OTA alignment: 5-Corner Model, XVAT / OTA Data Dictionary, OTA-approved ASP for validated tax invoices.
- Integrations: REST APIs (Kong gateway), webhooks, WebApp, bulk upload, SFTP, MQ/web services.
- Arabic UI, maker-checker, role-based dashboards, configurable logo.

## Compliance

- Technical enablement for Peppol / Oman e-invoicing workflows is in scope.
- Oman PDPL compliance supported; S-SDLC and independent security assessments supported.
- PCI-DSS-aligned controls when card data is in scope.
- History purge: only data older than **10 years** (regulation).
- Decimal rules: quantity and unit rate max **8** decimals; other amount fields **2**.
- Mandate applicability and legal tax advice are customer responsibilities.

## Technical / infrastructure

- N-tier microservices on Kubernetes with Kong API Gateway; VMware supported.
- Stack: MongoDB, PostgreSQL, RabbitMQ, Redis; proposed OS Ubuntu **26.04 LTS**.
- Environments: Development, QA, Staging, Production.
- Proposed sizing: **7** production servers, **5** test servers.
- LDAP / AD auth and customer password-policy tuning: configuration / customization.
- Windows Server 2022+ / Windows 11+: roadmap / future.

## Security & DR

- OWASP secure-coding, web, and API Top 10 controls supported.
- Encryption: AES-256 at rest; TLS 1.2+ (TLS 1.3 preferred) in transit; secrets via Vault/HSM/KMS patterns.
- Backup & DR: **RPO less than 5 minutes**, **RTO less than 1 hour**; secondary geographic DR site.
- API keys as sole authentication factor: customization required.
- OSS Email/SMS/SNMP monitoring integration: not supported.
- CBO security-gap certification letter: supported.
- Do **not** answer Oman questions using UAE-only residency, FTA, or PINT-AE details.
- If Oman-specific hosting **city/region** or certification **IDs** are not documented: **I don't know the answer.**

## Company

- Company demographics live under `shared/rfp/company-demographics.md`.
- Do not invent vendor staffing or reference counts without shared demographics or approved bid materials.

## Caveats index

See `capability-caveats.md` for SUP / CST / PC / FUT / NS summaries.

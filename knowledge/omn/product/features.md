# Oman Product Features & Capabilities

## Core e-invoicing

- Multimodal invoice creation: Web App, bulk upload, and API integration
- Sales and purchase invoice lifecycle (create, list, retrieve, resubmit where allowed)
- Credit/debit note support aligned with Oman document models
- Peppol transmission and retrieval of e-documents
- PDF and XML artifact download
- Oman 5-Corner Model / OTA / XVAT / ASP alignment (see `overview.md` and `../compliance/oman-e-invoicing.md`)

## Document tracking

- Peppol status and status-log retrieval for submitted documents
- Message-level transparency for troubleshooting
- Comprehensive audit logs for document actions and user authorization changes
- Support for detecting/reporting duplicate invoices, unusual amendments, cancellations, and configurable exception scenarios

## Entity & master data

- Organization and party/profile management
- Multi-entity / multi-TIN style operational separation where configured
- Codelists including Oman subdivisions and electronic address schemes
- Single unified data model without unnecessary data duplication

## UX & localization

- Web-enabled console; supports Microsoft Edge and Chrome
- Thin-client open standards; no proprietary client software required
- Arabic language interface
- Personalization limited to Arabic language customization (date/time/amount format personalization beyond that is not supported)
- Configurable customer logo
- Uniform customizable Look & Feel across platforms: not supported
- Print and help on all screens: not supported
- Easy learning curve for business users

## Reporting & analytics

- Standard reports for platform functions
- Reports available in CSV / XLSX
- Rich graphical display (pie, bar, and similar charts)
- Role-based dashboards with user-driven parameterization
- End-user authored report builder / publish/schedule own reports: not supported
- Report distribution via e-mail (on the fly or scheduled): on roadmap (future)
- Admin view/manage/generate activity reports: on roadmap (future)

## Controls & administration

- Maker-checker for transactions and admin setup
- Admin facility to manage/control setup with maker-checker
- Limit screen access by access rights (RBAC)
- Full comprehensive audit trail
- Limit DBA from accessing sensitive data
- Backup processing of historical data
- Decimal rules per regulation: quantity and unit rate max **8** decimal points; all other amount fields **2** decimal points
- History purge: only data older than **10 years** (as per regulation)

## Emerging capabilities

- AI and machine learning features: supported
- Blockchain / distributed ledger: not supported
- Automation and robotics (RPA): not supported

## Developer ecosystem

- REST APIs for documents, parties, auth, and status
- Webhooks for status/events
- Sandbox environments for integration testing
- Self-service credential patterns via the auth/developer flows

## Explicit non-capabilities (confirm before RFP use)

- Do not invent Oman-specific regulatory timelines or tax-authority outcomes not documented here.
- Bank-specific UI customization beyond documented options depends on scope and is generally not supported without commercial agreement.
- If a capability is not covered in this OMN knowledge base, answer that it is unknown until documented.

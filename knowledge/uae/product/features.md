# Product Features & Capabilities

## Core e-invoicing & compliance

- **Universal scenario support:** Full compatibility with FTA-mandated invoicing scenarios and transaction types, including B2B and B2G.
- **Multimodal invoice creation:** Web App, bulk upload, or direct API integration.
- **Flexible bulk upload:** Marmin-standard Excel templates or customized user templates (mandatory data points mapped).
- **Non-e-invoice registry:** Upload and manage historical or non-e-invoiced transactions for holistic tax reporting.
- **VAT return automation:** Automated VAT returns from e-invoiced data, or combination of non-e-invoice and e-invoiced records.
- **Regulatory archiving:** Secure, tamper-proof storage of e-documents for the legally required period.
  - Feature list states **6-year** archiving.
  - Retention matrix / questionnaires state **5 years** for tax invoices / processing metadata / audit trail (see `rfp/conflicts-and-caveats.md`).

## Document lifecycle & tracking

- Real-time transmission tracking for FTA and Buyer status.
- Message-level transparency: unique Message IDs and raw responses via Web App or API.
- Peppol network integration for transmission and retrieval of e-documents.
- Buyer-side retrieval: automated retrieval and storage of incoming PDFs and data files from vendors/sellers.
- Dynamic PDF engine: customizable PDF generation based on end-user branding/design.
- Comprehensive audit logs: timestamped logs of every document action; viewable or API-downloadable.

## Entity & master data management

- Group organizational hierarchy: single Organization view across legal entities.
- Multi-TIN management under a single consolidated login.
- Master data bulk ingestion: Customers (AR), Vendors (AP), Product/Service catalogs.
- Intra-group flagging: automated identification of internal subsidiary transactions.
- Multiple entities in a single organization instance with operational separation.

## Developer ecosystem & integration

- Self-service developer portal for Client ID / Secret credential management.
- Webhooks configurable at TIN or Event level; granular endpoint triggers.
- Webhook monitoring & recovery: payload/failure visibility; manual resend of failed events.
- API documentation with mandatory vs optional field definitions; samples in Python, Curl, Go, and more.
- Full-scale sandbox mirroring production for end-to-end integration testing.
- Public API docs: https://docs.ae.marmin.ai/

## Analytics, reporting & access

- Executive MIS dashboards (role-based) for compliance rates, VAT exposure, system health.
- Detailed document reports: exportable Excel with full line-item details for Sales and Purchase.
- RBAC with multiple sub-users and restricted access to specific data/entities.
- Arabic localization (I18n) for Web Application UI and PDF templates.
- Proactive exception intelligence: spike alerts (high rejection rates) and latency alerts (transmission delays).

## Invoice processing integrity

- Idempotency via uniqueness constraint on **Invoice Number + TIN**.
- Duplicate submissions rejected with **HTTP 409 Conflict**.
- Database operations described as transactional / ACID compliant.
- Asynchronous, event-driven processing aligned with UAE 5-corner framework.
- Horizontal scalability, retries with backoff, dead-letter queues for failed processing.

## UI configuration

UI-based configuration for organization details, user roles, document templates/settings, and operational parameters without code changes.

## Explicit non-capabilities (standard SaaS)

- Mobile app is **not** part of the standard offering (web browser access only).
- Social login (Google/Facebook/LinkedIn) **not** supported.
- No dedicated low-code middleware / predefined ERP connectors in standard offering (integrations via REST APIs, webhooks, SFTP/file exchange, customer middleware).

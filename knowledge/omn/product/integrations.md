# Oman Integrations

## Integration mechanisms

| Method | Support |
|---|---|
| REST APIs / Web Services over HTTPS | Yes (OpenAPI / Swagger documented) |
| OAuth 2.0 / JWT authentication | Yes |
| Mutual TLS (mTLS) | Yes where required |
| Webhooks (delivery notifications / status callbacks) | Yes |
| Synchronous and asynchronous integration | Yes |
| WebApp (individual + bulk) | Yes |
| File-based / bulk upload | Yes |
| SFTP | Yes |
| MQ / APIs for interfacing systems | Yes |
| Customer ESB or API Gateway | Yes (without significant customization for standard REST patterns) |
| Consume / expose web services | Yes |
| Batch and online integration with external feeds | Yes |
| Microsoft Exchange | Not supported (depends on intended use; not in base package) |

There is no hard maximum on the number of applications that can be integrated.

## Out-of-the-box API catalog

| API group | Functionality | Style |
|---|---|---|
| Authentication | OAuth2/JWT authentication, token management | RESTful |
| Invoice | Create, validate, submit, query invoices; credit/debit notes | RESTful |
| Onboarding | Taxpayer onboarding, participant registration, profile management | RESTful |
| Webhooks | Delivery notifications and status callbacks | RESTful |

Documentation: **https://docs.om.marmin.ai**

## Upstream / domain systems

- **XVAT** — VAT-determined transaction data
- **FA / input-side systems** — import-of-service and related AP feeds where e-invoice is mandatory
- **Core banking** and related bank subsystems via standard APIs / middleware
- **ERP / procurement** — route validated received invoices; notify receipt status
- **Oman Tax Authority** e-invoicing platform (and future designated government platforms) via Peppol / ASP path
- Future OTA specification changes accommodated through configuration or minor enhancement where possible

## Integration quality attributes

- Detailed interface specs: request/response formats, data mapping, validation rules (OpenAPI)
- HTTPS / TLS 1.2 or above for all APIs
- Configurable retry, error handling, logging, and monitoring for failed integration transactions
- End-to-end integration testing support: test environments, test data, mock services where applicable
- API versioning strategy; backward compatibility during upgrades or documented migration approach
- Audit logging and transaction traceability for integration activities
- Performance characteristics (response times, throughput, limits) provided per engagement
- Identify third-party dependencies, connectors, middleware, and licenses required for integrations
- Post-go-live integration support and knowledge transfer to the customer technical team

## Data import / export

| Format | Support |
|---|---|
| Excel / CSV | Supported |
| PDF (artifacts / report export) | Supported |
| Peppol / invoice XML | Supported for e-invoice exchange and schema validation |
| General XML file import/export outside Peppol flows | Future / engagement-specific |
| JSON import (generic bulk) | Not supported |

## Typical data flow

1. Core banking, XVAT, FA, ERP, or middleware submits or feeds invoice data via API, SFTP, or file upload.
2. Platform validates, enriches to PINT OM, and prepares the Peppol / OTA payload.
3. Document is transmitted through the configured Peppol / ASP path (buyer AP and/or OTA AP as applicable).
4. Status, acknowledgements, and webhooks are stored and exposed via APIs/UI.
5. PDF/XML artifacts remain available for download and audit; received invoices can be routed to ERP/procurement.

## Security for APIs

- TLS 1.2+ (TLS 1.3 preferred); OAuth 2.0 / mTLS as configured
- Authenticated API access via Kong API Gateway
- Rate limiting and validation controls as configured
- Treat API keys as identifiers, not the sole authentication factor — customization required for key-only auth models (see `../security/api-security.md`)

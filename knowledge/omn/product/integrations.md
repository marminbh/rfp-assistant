# Oman Integrations

## Integration mechanisms

| Method | Support |
|---|---|
| REST APIs / Web Services over HTTPS | Yes |
| Webhooks (status/events) | Yes |
| WebApp (individual + bulk) | Yes |
| File-based / bulk upload | Yes |
| SFTP | Yes |
| MQ / APIs for interfacing systems | Yes |
| Consume web services exposed by other applications | Yes |
| Expose web services for use by other applications | Yes |
| Batch and online integration with external feeds | Yes |
| Microsoft Exchange | Not supported (depends on intended use; not in base package) |

There is no hard maximum on the number of applications that can be integrated.

## Integration approaches

- Seamless integration with legacy/core applications and other open-standard systems (including Islamic banking cores and related subsystems where in scope).
- N-tier, open, scalable architecture with microservice deployment patterns.
- Portable / migratable across environments; DevOps and Agile delivery supported.

## API surface (high level)

- Sale documents (invoices and related notes)
- Purchase documents
- Party / profile management
- Peppol status and status logs
- Supporting resources / codelists (countries, OMN subdivisions, electronic address schemes)

## Data import / export

| Format | Support |
|---|---|
| Excel / CSV | Supported |
| PDF | Customizable |
| XML | Future |
| JSON import | Not supported |

## Typical data flow

1. ERP or middleware submits invoice data via API, SFTP, or file upload.
2. Platform validates and prepares the Peppol / OTA regulatory payload.
3. Document is transmitted through the configured Peppol / ASP path.
4. Status and acknowledgements are stored and exposed via APIs/UI.
5. PDF/XML artifacts remain available for download and audit.

## Security for APIs

- TLS for transit (TLS 1.2 minimum; TLS 1.3 preferred)
- Authenticated API access (token/API credentials per environment)
- Rate limiting and validation controls as configured for the deployment
- Treat API keys as identifiers, not the sole authentication factor — customization required for key-only auth models (see `../security/api-security.md`)

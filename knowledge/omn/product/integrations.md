# Oman Integrations

## Integration mechanisms

| Method | Support |
|---|---|
| REST APIs over HTTPS | Yes |
| Webhooks (status/events) | Yes |
| File-based / bulk upload | Yes |
| WebApp individual + bulk upload | Yes |
| Enterprise middleware via standard web protocols | Yes |

## API surface (high level)

- Sale documents (invoices and related notes)
- Purchase documents
- Party / profile management
- Peppol status and status logs
- Supporting resources / codelists (countries, OMN subdivisions, electronic address schemes)

## Typical data flow

1. ERP or middleware submits invoice data via API or file upload.
2. Platform validates and prepares the Peppol / regulatory payload.
3. Document is transmitted through the configured Peppol path.
4. Status and acknowledgements are stored and exposed via APIs/UI.
5. PDF/XML artifacts remain available for download and audit.

## Security for APIs

- TLS for transit
- Authenticated API access (token/API credentials per environment)
- Rate limiting and validation controls as configured for the deployment

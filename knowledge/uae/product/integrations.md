# Integrations

## Integration mechanisms

| Method | Support |
|---|---|
| REST APIs over HTTPS | Yes |
| Webhooks (status/events) | Yes — validation results, clearance status, processing failures |
| File-based batch (CSV, XLSX) | Yes |
| SFTP-based bulk upload / secure file exchange | Yes |
| WebApp individual + bulk upload | Yes |
| AI-based data extraction and upload for PDF documents | Yes (implementation questionnaire) |
| Enterprise middleware (SAP PiPo, SAP BTP Integration Suite, MuleSoft, OIC, Dell Boomi) | Yes — via standard web protocols |

## API surface

Exposed major entities include: organizations, invoices, customers, vendors, document/transaction statuses.

API authentication options cited across sources:

- API keys
- JWT tokens
- OAuth 2.0 / secure API keys (also listed as under development in some sources — see `rfp/conflicts-and-caveats.md`)

API security:

- TLS 1.2+ / TLS 1.3
- Rate limiting / API throttling
- IP allowlisting
- Replay-attack protection
- WAF, payload/schema validation, threat detection, transaction tracing
- Kong Gateway as API gateway

## Webhook capabilities

- Configure at TIN or Event level
- Real-time visibility into payloads and failure reasons
- Manual resend of failed events

## Typical data flow

1. Source ERP / business application submits invoice data.
2. Platform validates and transforms into required tax authority format.
3. Invoice submitted to relevant tax authority / Peppol participants.
4. Responses, acknowledgements, and status updates captured and stored.
5. Audit records and compliance logs maintained for traceability.

Data types processed: invoice data; tax/compliance information; customer and supplier master data; integration metadata and audit records.

## Connectivity options

- Standard: public internet HTTPS.
- Enterprise / dedicated: Site-to-Site IPSec VPN; private endpoints; VPN-only access possible for isolated deployments.
- Internet connectivity still required for FTA / Peppol / buyer-supplier exchange.
- VPN / private connectivity may involve additional commercial arrangements outside standard SaaS.

## Message formats

- JSON for API integrations
- XLSX for file-based exchange / bulk import-export / historical load
- PINT XML validation referenced in release/sandbox testing
- Cryptographically signed XML payloads referenced in exit/handover process
- EDI / SWIFT / flat-file native middleware formats: **not** part of the standard SaaS integration layer (use customer middleware if needed)

## Inbound / outbound patterns

- **Inbound:** API invoice submission, document uploads, data synchronization, webhook callbacks
- **Outbound:** API retrieval, webhooks, file-based exports (XLSX / SFTP where configured)
- Standard API integrations included in SaaS; complex/custom integrations may need additional implementation services
- Customers can build their own services/workflows on exposed APIs; custom APIs beyond the standard set may be PaaS/custom development
- Reasonable API rate limits / throttling applied for stability; higher throughput by arrangement
- **Not standard SaaS:** direct database-format dumps or automated SFTP database exports

## Production-to-test (P2T)

Controlled P2T data copies via database export/import or backup restore into non-production, managed by the Service Provider. Masking/anonymization can be applied when production-like data is used in test (may involve separate commercials).

## Commercial extras (typically outside standard SaaS)

Separate commercials often apply for: IPSec VPN setup/subscription; dedicated private connectivity / partner links; storage/compute beyond normal usage; customer encryption-key management services; production-data encryption/masking for test; OAuth identity-service enablement beyond native JWT/API keys. User authentication/authorization and social-ID arrangements: no separate charge for social ID (social login is not offered).

## SIEM / PAM (enterprise proposals)

- SIEM integration can include access logs, audit logs, network events (firewall/WAF anomalies).
- PAM capabilities described internally: JIT privileged access, credential vaulting, automatic password rotation, MFA, RBAC, audit logging, bastion access; enterprise PAM integration described as discussable.

# Encryption & Key Management

## Standard posture

- Transit: TLS 1.2 / 1.3
- Rest: AES-256 / cloud-managed encryption
- Marmin-managed KMS keys
- Rotation: every 90 days
- AWS S3 DR backups: AES-256 SSE-KMS with Marmin-managed KMS keys

## BYOK / customer-managed keys

- **Enterprise cloud architecture response:** BYOK **not supported**; Marmin manages KMS for seamless DR/BCP.
- **Enterprise SaaS annexure:** Customer-managed encryption key management **can be supported** through OCI KMS; may involve additional infrastructure costs.

Treat BYOK as non-standard / commercially exceptional unless a dedicated design is agreed. See `rfp/conflicts-and-caveats.md`.

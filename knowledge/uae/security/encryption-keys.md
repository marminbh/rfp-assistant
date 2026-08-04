# Encryption & Key Management

## Standard posture

- Transit: TLS 1.2 / 1.3 (HTTPS enforced for sensitive data, internal and external)
- Rest: AES-256 / cloud-managed encryption for sensitive data including PII and card data where applicable
- Marmin-managed KMS keys
- Rotation: every 90 days
- AWS S3 DR backups: AES-256 SSE-KMS with Marmin-managed KMS keys
- FQDN-bound TLS certificates; **EV certificates** for public-facing sites from a reputable external CA
- Internal production certs issued/revoked via internal CA where applicable
- **WAF** on public-facing applications
- **SFTP** file transfers with AES (≥128-bit key length)
- Credentials: salted hashing; never clear text in transit or at rest
- Integrity: SHA2 (or equivalent secure hash) for tamper protection
- PII masking/truncation in UI and print; unmasked access only for authorized users

## Customer-managed keys / BYOK

Customer-managed encryption keys (BYOK) are **not allowed**.

- Encryption keys are managed exclusively by Marmin via KMS.
- Customers cannot bring, own, or administer encryption keys for the platform.
- This applies across SaaS and standard cloud deployments so DR/BCP and key lifecycle remain under Marmin control.

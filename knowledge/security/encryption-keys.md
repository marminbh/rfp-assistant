# Encryption & Key Management

## Standard posture

- Transit: TLS 1.2 / 1.3
- Rest: AES-256 / cloud-managed encryption
- Marmin-managed KMS keys
- Rotation: every 90 days
- AWS S3 DR backups: AES-256 SSE-KMS with Marmin-managed KMS keys

## Customer-managed keys / BYOK

Customer-managed encryption keys (BYOK) are **not allowed**.

- Encryption keys are managed exclusively by Marmin via KMS.
- Customers cannot bring, own, or administer encryption keys for the platform.
- This applies across SaaS and standard cloud deployments so DR/BCP and key lifecycle remain under Marmin control.

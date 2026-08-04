# Oman Encryption & Key Management

## Data in transit

- All sensitive client↔server and service↔service traffic encrypted with **TLS 1.2 or higher** (**TLS 1.3** preferred)
- HTTPS for web and API traffic; TLS for application-to-database connections where applicable
- Weak/legacy protocols disabled: SSLv1/v2/v3, TLS 1.0 (and similarly obsolete ciphers)
- Cipher strength must not be below **128 bits**
- Mutual TLS (**mTLS**) supported for high-assurance internal microservice / API communication
- HSTS on HTTPS endpoints

## Data at rest

- Industry-standard encryption for sensitive stored data (e.g. **AES-256**, AES-256-GCM)
- Backups encrypted at rest with AES-256 or equivalent
- PII, credentials, and financial data protected with encryption and access controls per regulation (including Oman PDPL where applicable)
- Data masking / tokenization for sensitive elements in UI, logs, and non-production views where required

## Algorithms

Approved patterns include:

- Symmetric: AES-256 (GCM mode)
- Asymmetric: ECC (e.g. ECDSA, ECDH) and other proven standard algorithms
- Password hashing: bcrypt, Argon2, or PBKDF2 (never plaintext)

## Key management

- Encryption keys stored and managed via a secure key management approach (e.g. HashiCorp Vault, HSM, or cloud KMS)
- Data encryption keys (DEK) encrypted by a key encryption key (KEK); keys stored separately from ciphertext
- Keys protected at rest and in transit; rotated periodically per policy; revoked immediately if compromised
- Secrets, API keys, and tokens never hardcoded or exposed in URLs
- Database and service credentials stored in a secrets manager — not in source code

## Customer-managed keys / BYOK

Customer-managed encryption keys / BYOK are **not** documented as a standard Oman capability. Unless separately confirmed for a bid, answer **I don't know the answer.**

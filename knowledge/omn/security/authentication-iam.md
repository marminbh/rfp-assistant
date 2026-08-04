# Oman Authentication & IAM

## Supported

- Authenticate all non-public pages/resources; enforce on server; centralized auth; fail securely
- Username/password with adaptive memory-hard password hashing (Argon2id, scrypt, bcrypt, or PBKDF2); salted one-way hashes; no MD5/SHA-1/plain SHA-256
- Screen new/changed passwords against known-compromised lists
- Generic failure messages; credentials over encrypted channels; HTTP POST for credential submission
- Obscure password entry; disable “remember me”
- Password reset/change at same control level as create/auth; email resets only to pre-registered address
- MFA per approved authentication standard; prefer phishing-resistant factors (e.g. FIDO2/WebAuthn); OTP generation/validation with secure format and expiry controls
- Support for additional authentication mechanisms (hard tokens, biometrics, digital certificates) where engagement scope includes them
- Re-authenticate before critical/sensitive operations
- No Basic or Digest authentication (application or API)
- Unique non-descriptive usernames/IDs; server-side authentication state
- RBAC; limit screen access by access rights
- Separate RBAC roles for account-admin vs system-admin/ops
- Local identity management for non-directory users (e.g. external/dealer-style users) where configured
- Strong API auth via established protocols (OAuth 2.0, OpenID Connect); prefer central IdP over APIs handling credentials directly
- JWT signature verification every request; reject `none`/unexpected algs; validate exp/nbf/iss/aud; short lifetimes; rotate signing keys
- Prefer RS256 (asymmetric) or HS256 with strong secrets; secrets in Vault/KMS/HSM — never hardcoded
- Access tokens short-lived; refresh tokens stored securely; token blacklist/denylist for immediate revocation
- Refresh-token rotation and server-side revocation
- Authorization Code Flow with PKCE for browser/mobile apps; Client Credentials for server-to-server; Implicit Flow must not be used
- For third-party-exposed APIs: opaque tokens preferred over JWT to reduce information exposure (via API gateway)

## Session management

- Server/framework session management; strong random session IDs (not based on user info or timestamps)
- Secure, HttpOnly, SameSite cookies; restricted domain/path
- Do not store JWTs in localStorage/sessionStorage when cookie-based delivery is used
- Logout terminates session; short inactivity timeout; no persistent logins
- Periodic session termination even if active (with user notice)
- New session after login; new ID on re-auth; periodic ID rotation
- Session IDs only in cookie headers — never in URLs, logs, or error messages
- CSRF tokens for sensitive operations
- Prefer consistent HTTPS; new session ID when upgrading HTTP→HTTPS
- Server-side session data protected with access control and encryption where needed

## Configuration / partial (customer policy alignment)

These require configuration and/or customer-managed identity infrastructure:

- Microsoft Active Directory / LDAP authentication for internal staff
- AD-only user setup when Windows auth is used (depends on LDAP)
- Password policy configured to customer standards (complexity, weak/predictable password detection, expiry periods, periodic forced change)
- Full OAuth 2.0 / JWT enterprise patterns end-to-end with customer IdP — supported with configuration alongside customer infrastructure

## API key note

Treat API keys as identifiers, not the sole authentication factor. Rotation and secure storage are required. Key-only auth models need customization.

## Explicit non-support / caution

- Do not assert SSO/SAML/OIDC as generally available for Oman beyond what is documented here without confirming current release status for the bid.

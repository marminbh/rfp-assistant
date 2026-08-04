# Oman Authentication & IAM

## Supported

- Authenticate all non-public pages/resources; enforce on server; centralized auth; fail securely
- Username/password with adaptive memory-hard password hashing (Argon2id, scrypt, bcrypt, or PBKDF2); salted one-way hashes; no MD5/SHA-1/plain SHA-256
- Screen new/changed passwords against known-compromised lists
- Generic failure messages; credentials over encrypted channels; HTTP POST for credential submission
- Password complexity, length, lockout/throttling, history/reuse, and expiry per bank/customer standard where configured
- Obscure password entry; disable “remember me”
- Password reset/change at same control level as create/auth; email resets only to pre-registered address
- MFA per approved authentication standard; prefer phishing-resistant factors (e.g. FIDO2/WebAuthn)
- Re-authenticate before critical/sensitive operations
- No Basic or Digest authentication
- Unique non-descriptive usernames/IDs; server-side authentication state
- RBAC; limit screen access by access rights
- Separate RBAC roles for account-admin vs system-admin/ops
- Strong API auth via established protocols (OAuth 2.0, OpenID Connect); prefer central IdP over APIs handling credentials directly
- JWT signature verification every request; reject `none`/unexpected algs; validate exp/nbf/iss/aud; short lifetimes; rotate signing keys
- Refresh-token rotation and server-side revocation

## Session management

- Server/framework session management; strong random session IDs
- Secure, HttpOnly, SameSite cookies; restricted domain/path
- Logout terminates session; short inactivity timeout; no persistent logins
- Periodic session termination even if active (with user notice)
- New session after login; new ID on re-auth; periodic ID rotation
- Session IDs only in cookie headers — never in URLs, logs, or error messages
- CSRF tokens for sensitive operations
- Prefer consistent HTTPS; new session ID when upgrading HTTP→HTTPS

## Customization required

- Full LDAP integration for user authentication
- Where Windows auth is used, user setup only at Active Directory (not duplicated in the app) — depends on LDAP integration

## API key note

Treat API keys as identifiers, not the sole authentication factor. Rotation and secure storage are required. Key-only auth models need customization.

## Explicit non-support / caution

- Do not assert SSO/SAML/OIDC as generally available for Oman beyond what is documented here without confirming current release status for the bid.

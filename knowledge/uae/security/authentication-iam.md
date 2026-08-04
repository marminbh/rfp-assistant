# Authentication & IAM

## Currently supported

- Username / password (native email + password)
- MFA / 2FA — email-based OTP (can be enforced for all user and admin accounts)
- API auth: API keys and/or JWT; OAuth 2.0 also listed in some sources
- RBAC with least privilege; granular functional permissions (invoice creation, tax return generation, approvals, API key management)
- Unique user IDs (email/employee ID primary key); prevent duplicates
- Admin password expiry 30 days; user password expiry 90 days
- Password history: cannot reuse previous 6 (checklist); hybrid materials also cite 10–12
- Min length 8 (checklist); hybrid materials example 12–16
- Complexity: upper, lower, numeric, special
- Lockout after 6 failed attempts; 30-minute lockout for normal users
- Inactive accounts dormant/disabled after 90 days
- Force password change on first login (local auth)
- MFA OTP parameters: ≥5 digits; expiry 5 minutes or resend; separate verified medium SMS or Email
- Idle session timeout ≤ 15 minutes
- Session ID changed on each login; session not allowed across multiple systems/devices with the same session ID
- Full session termination on logout / browser close; no resume via back-button / cached authenticated pages
- Maker-checker for user administration and critical transaction processing
- Entitlement reports include inactivity 45+ days, failed logins, last login/modification (see `application-security-checklist.md`)
- Autocomplete disabled on password and other sensitive input fields
- External integrations authenticate with randomly generated access tokens (not by forwarding end-user credentials)

## Not applicable (checklist)

- Biometric authentication (stored biometrics) — not used
- Customer LAM-only application administration handover — SaaS platform admin model
- Dual-control split-knowledge for interactive system IDs — not applicable to current posture

## SSO / federation — conflicting statements

| Source | Claim |
|---|---|
| Security, Compliance & BC Overview | SSO **fully implemented** with **SAML 2.0** and **OIDC**; IdPs e.g. Azure AD, Okta |
| Auth response notes | Entra ID **under development**; OAuth 2.0 **under development**; does not currently support SAML 2.0 or OIDC |
| Enterprise SaaS annexure | Native auth only; **SAML not supported**; AD/Azure AD/SCIM **not implemented** |
| Implementation questionnaire | M365 user authentication: **“Yes, this can be built.”** |

**RFP guidance:** Do not assert SSO/SAML/OIDC as generally available without confirming current release status. Prefer “native email/password + email OTP MFA; enterprise IdP federation on roadmap / can be built” unless using the Security Overview wording intentionally for a specific bid.

## User provisioning

- Accounts created by organization administrators or via platform registration with **email verification**
- Customer admins manage users/roles within their tenant; platform identity store is application-native (no sync down to on-prem AD)

## Explicit non-support (standard SaaS)

- Social ID login (Google/Facebook/etc.)
- Active Directory / ADFS / Azure AD / SCIM provisioning (enterprise SaaS annexure: **N**)
- SAML 2.0 federation (enterprise SaaS annexure: **N**)
- On-prem IDP sync components in customer DMZ (not required — IdP integration not implemented)
- Third-party MFA providers (email OTP included; third-party MFA = separate commercials if required)

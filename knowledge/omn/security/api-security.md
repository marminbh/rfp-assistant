# Oman API Security

Aligned to **OWASP API Security Top 10 (2023)**. Complements application security controls in `application-security.md`.

Unless noted, controls below are supported in the base package.

## API1 — Broken Object Level Authorization (BOLA)

- Enforce object-level authorization on every request that accesses an object by identifier
- Centralized, reusable object-level authorization component
- Validate object ownership/tenancy in multi-tenant data (no cross-tenant access)
- Prefer random, unpredictable resource IDs (e.g. UUIDs) as defense-in-depth
- Log and alert on repeated authorization failures

## API2 — Broken Authentication

- Strong auth via OAuth 2.0 / OpenID Connect; prefer central IdP
- JWT: verify signature every request; reject `none`/unexpected algs; validate exp/nbf/iss/aud; short lifetimes; rotate signing keys
- Refresh-token rotation + server-side revocation; invalidate on logout, password change, privilege change
- Password storage and MFA align with approved authentication standard
- Protect auth endpoints against brute force / credential stuffing
- Do not expose tokens/credentials in URLs, logs, or error messages
- **Customization required:** treat API keys as identifiers, not the sole authentication factor; rotate and store securely

## API3 — Broken Object Property Level Authorization

- Prevent mass assignment via explicit property allow-lists
- Server-side DTO / response schema filtering (no excessive data exposure)
- Property-level authorization for sensitive fields
- Validate request/response payloads against schema (OpenAPI / JSON Schema)

## API4 — Unrestricted Resource Consumption

- Rate limiting / throttling per client (API key, token, user, and/or IP)
- Maximum request payload size; pagination and max record-count
- Request timeouts and concurrent connection limits
- Limit/monitor costly downstream ops; container/process resource limits

## API5 — Broken Function Level Authorization (BFLA)

- Role-based or claims-based access control validated server-side
- Function-level authorization on every endpoint including admin; deny by default
- Separate admin API functions from regular user functions
- Do not rely on client UI or HTTP method alone to enforce function access

## API6 — Unrestricted Access to Sensitive Business Flows

- Identify sensitive flows and protect against automated abuse
- Anti-automation controls proportionate to risk
- Per-flow velocity/rate limits beyond generic API limits

## API7 — Server-Side Request Forgery (SSRF)

- Validate and allow-list destinations for client-driven server-side requests
- Block internal/loopback and cloud metadata; disable unsafe URL schemes and automatic redirect following

## API8 — Security Misconfiguration

- HTTPS/TLS for all API traffic: TLS 1.2 minimum (TLS 1.3 preferred)
- HSTS on all API endpoints
- Restrictive CORS; disable unnecessary HTTP methods
- Generic client errors; structured status codes; secrets outside code
- Harden API servers/gateways; patch dependencies; remove version/banner info

## API9 — Improper Inventory Management

- Complete inventory of API endpoints (version, environment, auth, data sensitivity)
- Up-to-date OpenAPI documentation for exposed endpoints
- Retire/restrict deprecated versions; segregate prod / non-prod / debug

## API10 — Unsafe Consumption of APIs

- Validate/sanitize data from third-party/upstream APIs as rigorously as user input
- TLS with certificate validation; do not blindly follow redirects
- Timeouts and secure error handling; assess third-party API security posture before integration

## Logging, monitoring & testing

- Comprehensive security event logging; integrate with IDS/IPS and SIEM
- Do not log credentials, tokens, full PII, or card data
- Security testing through SDLC; automated SAST and DAST
- Independent third-party VAPT covering OWASP API Security Top 10
- API-specific tests for BOLA, BFLA, mass assignment, and excessive data exposure

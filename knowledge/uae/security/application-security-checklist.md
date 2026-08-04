# UAE Application Security Controls Checklist (v2.3)

Completed checklist responses for Marmin UAE e-invoicing. Status is **Compliant** unless noted **Not Applicable**.

## Solution design — Compliant

- Application process flow and data flow diagrams available
- Web server and application server on separate machines; different network zones for public-facing apps
- Architecture diagrams show component connection points, network-zone placement, ports/protocols/services, authentication between components, and **WAF** in DMZ where applicable
- Dev and Test environments separated from Production
- Sensitive data not stored/used in non-production; if production-like data is required, it is scrambled / follows infrastructure data-refresh standards
- Advanced antivirus / anti-malware installed on servers
- Backup servers / DR arrangement in place

## User administration

### Compliant

- Unique User IDs enforced for accountability; primary key such as Email ID or Employee ID; prevent duplicate ID creation
- Default application/DB accounts identified and disabled where possible; otherwise default passwords changed, whitelisted, ownership defined
- Service/functional accounts documented and approved with defined ownership; credentials protected in storage and transmission; complex passwords; no interactive login unless justified
- Maker-checker for application user administration, operational maintenance (parameter/limit), and critical transaction processing
- RBAC with approved user roles and rights matrix
- Detailed audit logs for user creation, deletion, and modification
- Entitlement / activity monitoring reports covering at minimum: User ID, name, department, current/previous profile and entitlements, account status (Active/Disabled), creation date, last login, last modification, LAM/admin modifier ID where applicable, login history, failed login attempts, inactivity **45+ days**

### Not Applicable

- Dual-control / split-knowledge / escrow or privileged-ID management for interactive system IDs that cannot be disabled — **Not Applicable** to current UAE SaaS posture
- Handing application administration of critical apps to customer **LAM** with access-management-only rights — **Not Applicable** (customer-org process; Marmin retains platform admin model for SaaS)

## Password standards

### Compliant

- Password expiry **30 days** for administrators / privileged accounts
- Password expiry **90 days** for all user accounts
- Cannot reuse any of the previous **6** passwords
- Minimum length **8** characters
- Complexity: upper case, lower case, numeric, and special characters
- Force password change on first login for local authentication
- Lockout after **6** successive failed login attempts
- Lockout duration **30 minutes** for normal users (or unlock via LAM/admin process)
- Administrator / privileged unlock via LAM/admin contact process
- Inactive accounts not used for **90 days** marked dormant or disabled
- Idle session timeout **≤ 15 minutes**
- MFA for critical / public-facing / regulatory apps: password + OTP/token; OTP length ≥ **5** digits; expiry **5 minutes** or resend; separate verified medium SMS or Email

### Not Applicable

- Changing default passwords following installation of system/software — **Not Applicable** where no customer-installable default credentials apply (managed SaaS / Marmin-operated stack)

## Audit logging and monitoring

### Compliant

- Security audit logs exclude sensitive data and include: user ID, destination ID, source IP, destination IP, event type, event information (e.g. permission changes), process impacted, date/time, success/failure, affected resource identity
- Security events monitored via **SIEM**; critical-component audit logs integrated with SIEM (DB views for app logs in DB where applicable)
- Report downloads record the user ID of the person who downloaded for accountability
- Access to audit logs (including admin activities) restricted; logs protected against tampering; credentials, PAN, PII must not appear in logs (mask if business-required)

### Not Applicable

- Dedicated audit log whenever a user *views* critical financial/non-financial detail (e.g. customer balance, account statement, SI/PII) — **Not Applicable** as a separate control in current product framing (core security/admin audit logging still Compliant)

## Data validation — Compliant

- Maker-checker for critical transaction processing
- Input validation: reject out-of-range values, invalid characters/types, incomplete data, and volume limit violations (validated via automated vulnerability scanning, e.g. IBM AppScan)
- Buffer overrun/overflow protections (validated via automated vulnerability scanning)
- Detailed logs of activities in the data output validation process
- Autocomplete disabled on forms/fields that accept passwords or other sensitive user data
- File upload validates file size, content type, and file format

## Authentication and session management

### Compliant

- External-system communication uses randomly generated access tokens (client requests authenticated without sending the user’s credentials)
- Forceful termination of all existing sessions on logout and/or when the browser is closed without logout
- After logout: remove client- and server-side session parameters; no resume via manual redirect to previous page; no cached authenticated pages
- Session ID not allowed to log in on multiple systems/devices
- Authentication session ID changed on each login

### Not Applicable

- Biometric authentication based on stored user biometrics (non event-bound true/false API) — **Not Applicable** (biometrics not used)

## Control over application source code

### Compliant

- Access to application source code restricted and controlled
- Access to design, architecture, source code, and functional specifications restricted and controlled
- Audit log maintained for accesses to program source libraries and associated items
- Source code ownership defined and documented; escrow agreement established where source is maintained with a vendor and contractually required
- Source code reviewed before production deployment to detect malicious/Trojan code (validated via automated scanning, e.g. IBM AppScan Source)

### Not Applicable

- Third-party-developed/maintained applications providing source-code assessment and/or independent VAPT reports *as a customer-facing artifact for this control row* — **Not Applicable** in that framing; Marmin still performs periodic VAPT / vulnerability management as a platform practice (see `controls-overview.md`)

## Cryptography — Compliant

- HTTPS with **TLS 1.2 or later** enforced for sensitive data in transit (internal and external)
- FQDN used so TLS certificates match the domain
- Public-facing HTTPS sites use **Extended Validation (EV)** certificates from a reputable external CA
- Internal production systems may use certificates issued/revoked by an **internal CA** (including internal self-signed patterns under that CA)
- **WAF** implemented for external / public-facing applications
- **SFTP** for file-based transfers; encryption **AES** with minimum **128-bit** key length
- User credentials never transmitted or stored in clear text; hashing with unique salting for credential storage
- Secure Hash Algorithm (e.g. **SHA2**) for integrity protection in storage and transmission
- Sensitive data (card data, PII) encrypted in storage (database, config, etc.) and in transmission
- Customer sensitive data / PII masked or truncated in display and printing wherever possible; unmasked access only for authorized users

## RFP answering notes

- Prefer this file for checklist-style application security questions for **UAE**
- BYOK remains **not allowed** — see `encryption-keys.md`
- Do not invent LAM/customer-org process compliance for Not Applicable rows
- Cross-check password/session numbers with `authentication-iam.md` (hybrid materials may cite longer password lengths or histories)

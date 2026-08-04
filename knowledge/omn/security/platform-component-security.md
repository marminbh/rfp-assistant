# Oman Platform Component Security

Security baselines for stack components used in Oman e-invoicing deployments. All items below are supported as standard platform practices unless noted.

## MongoDB

- Authentication enabled; anonymous access prohibited
- RBAC with least privilege
- TLS for client-to-server and inter-node communication
- Encryption at rest (native or underlying disk encryption)
- Access restricted to authorized app servers/admins via firewall/security groups; no public internet access unless explicitly approved
- Credentials in secrets manager (not hardcoded)
- Audit logging for auth, authorization, and admin activity
- Automated encrypted backups with periodic restore tests
- Patched supported releases; monitor failed logins and suspicious activity
- Disable unused features, sample DBs, and insecure defaults

## Redis

- Authentication with strong passwords or ACLs; least-privilege ACLs
- Bind to private interfaces only; firewall-restricted
- TLS for client and replication traffic
- Disable dangerous commands (e.g. FLUSHALL, CONFIG, DEBUG) for non-admin users where applicable
- Credentials in secrets manager
- Secure persistence files / encrypted backups when persistence enabled
- Secure replication and failover with auth + TLS
- Monitor memory, connections, and auth failures

## RabbitMQ

- Authentication for all users; default guest disabled for remote access
- Least-privilege permissions via vhosts and roles
- TLS for client and cluster communication
- Management console and AMQP ports restricted to trusted networks
- Credentials in secrets manager
- Audit/operational logs for admin actions
- Secure clustering, mirrored/quorum queues, and DR mechanisms
- Management UI protected with HTTPS, MFA where supported, and IP restrictions

## Object storage (S3-compatible)

Where object storage is used:

- Block public access unless explicitly approved
- IAM roles / least privilege (avoid long-lived access keys)
- Server-side encryption (SSE-KMS or SSE-S3); HTTPS/TLS required for access
- Versioning; access/audit logging
- Cross-region or cross-account replication for critical data where required
- Object lock / immutable storage for regulated data where applicable
- Lifecycle policies for retention and secure deletion
- Do not store secrets in buckets unless encrypted and tightly access-controlled

## Peppol / Access Point

- Authenticate participants with valid Peppol digital certificates from an approved CA
- Only authorized apps, users, and Access Points send/receive documents
- Maintain Peppol Participant IDs and SMP registration
- TLS 1.2+ for communications; AS4 messages digitally signed
- Certificate lifecycle: secure storage, renewal, rotation, revocation
- Network controls: firewalls, IP filtering, segmentation for Access Point connectivity
- RBAC for admin, certificate management, and message processing
- Private keys/certificates in secrets manager or HSM where applicable
- Log inbound/outbound exchanges, auth events, admin and security events
- Preserve signed message evidence for non-repudiation
- Validate Peppol BIS / XML schemas and business rules before send and on receive
- Protect invoice/business data per data-protection rules (including Oman PDPL)
- HA Access Point deployment; encrypted backups of configs, certs, logs, metadata
- Monitor delivery failures, certificate expiry, and security events
- Incident procedures for failed transmissions, cert compromise, unauthorized access
- Keep Access Point / AS4 / OS components patched
- Comply with OpenPeppol / Peppol BIS and applicable tax-authority requirements
- Retain invoices, transmission evidence, and audit logs per legal retention
- BC/DR for uninterrupted e-invoice exchange
- Third-party Access Point providers must meet equivalent security and contractual controls

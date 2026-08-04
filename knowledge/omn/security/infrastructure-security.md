# Oman Infrastructure Security

Applies to Oman e-invoicing deployments. Many network-zone and perimeter controls are implemented as part of the deployment architecture when hosted on **customer-managed** or enterprise infrastructure; Marmin collaborates on design documentation and security reviews.

## Security by design

- Security by design for web, API, and supporting infrastructure covering confidentiality, integrity, and availability at application, data, infrastructure, and network layers
- Network and application architecture subject to customer security architecture review before implementation
- Multi-tier architecture: presentation (web), application (API), and data tiers logically separated (native microservices)
- Admin/management interfaces segregated from published servers and restricted to internal networks
- Public DMZ hosts only necessary publishing web servers; app/DB remain in internal zones behind firewalls
- Distinct non-production environments (Development, QA, Staging) before Production go-live

## Network security

- Network segmentation across environments (dev / staging / production)
- No implicit trust between components; authenticated/authorized interactions
- mTLS where applicable for microservices and APIs
- Unnecessary default services removed; unused ports closed
- Client↔server: HTTPS
- North/south-bound server traffic: HTTPS, SFTP, LDAPS, or other TLS-enabled protocols
- TLS 1.2+ only; insecure SSL/TLS versions disabled
- Internet-published web traffic may terminate/offload TLS on a customer **WAF**; WAF tuning supported as part of deployment on customer infrastructure
- Vulnerability assessment and penetration testing with remediation before production data / go-live

## Logging & monitoring

- Application and platform audit logging enabled; retain security/audit trails (at least **90 days** where required by customer baseline)
- Logs can integrate with enterprise monitoring / **SIEM**
- Forwarding all infrastructure-component logs (OS, K8s, Docker, Redis, etc.) to a customer SIEM: **partial** — application audit logging is standard; full infra log shipping depends on customer-managed infrastructure integration
- Tamper-resistant storage of key security events (auth, privilege changes, data access, config changes)

## High availability

- Failover management with integrity during failover
- HA infrastructure design; DR at a secondary geographic site (see `../operations/business-continuity-dr.md`)

## Compatibility caveat

Compatibility with a specific customer’s existing security tool stack (named backup products, golden images, corporate proxies, etc.) is **partial / configuration** — supported when deployed on customer-managed infrastructure with joint design, not as a universal out-of-the-box guarantee for every tool brand.

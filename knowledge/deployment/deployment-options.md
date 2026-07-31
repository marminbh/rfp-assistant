# Deployment Options

Marmin offers three primary strategic models, plus hybrid variants for regulated enterprises.

## Option 1 — Cloud multi-tenant (logical separation)

**Recommended for:** SMB  
**Model:** Shared cloud; strict logical isolation  
**Isolation:** Tenant-aware data models + RBAC; no cross-tenant access  
**Encryption:** TLS 1.3 in transit; AES-256 at rest  
**Marmin owns:** Infra, deployment/upgrades/patching, monitoring/incident mgmt, backup/DR, Peppol + FTA integration  
**Customer owns:** User/role management within tenant; operational usage  
**Pros:** Cost-efficient; fast onboarding; fully managed  
**Cons:** Logical (not physical) isolation; standard compliance posture

## Option 2 — Isolated cloud (single-tenant)

**Recommended for:** Enterprises with sensitive data / compliance needs  
**Model:** Dedicated VPC/VCN, compute, storage; single-tenant K8s + DB; VPN private access; Marmin-managed  
**Isolation:** Physical + network-level; dedicated DBs and storage volumes  
**Encryption:** TLS 1.3; AES-256  
**Access:** Site-to-site VPN or private endpoints  
**Marmin owns:** End-to-end infra, maintenance, monitoring, backup/DR/failover, Peppol + FTA  
**Customer owns:** Secure VPN access; internal user/ops management  
**Pros:** Strong isolation; audit readiness; predictable performance  
**Cons:** Higher cost; slightly longer provisioning

## Option 3 — Fully on-premise

**Recommended for:** Strict data residency / regulatory constraints  
**Model:** Entire stack in customer DC  
**Encryption:** TLS in transit; AES-256 at rest; customer firewalls/IDS/IPS/zero-trust  
**Customer owns:** Infra; FTA + Peppol connectivity; monitoring; backup/DR; security/compliance; **Peppol Access Point accreditation**  
**Marmin owns:** Application stack + deployment guidance; implementation/upgrade support; assist accreditation  
**Pros:** Maximum sovereignty/control/customization  
**Cons:** Highest ops overhead; customer owns Peppol accreditation and external connectivity

## Comparison

| Criteria | Multi-tenant cloud | Isolated cloud | Fully on-prem |
|---|---|---|---|
| Infra | Shared | Dedicated | Customer-owned |
| Isolation | Logical (RBAC) | Physical + logical | Physical |
| Cost | Low | Medium | High |
| Ops ownership | Marmin | Marmin | Business |
| Scalability | High | High | Limited by infra |
| Compliance effort | Low | Low | High |
| Time to onboard | Fast | Moderate | Slow |

## Questionnaire summary

Supports cloud SaaS, completely on-prem, and hybrid. Hosting provider: Oracle Cloud. DC: Abu Dhabi. DR: Singapore (see conflicts file for alternate DR wording).

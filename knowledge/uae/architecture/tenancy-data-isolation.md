# Tenancy & Data Isolation

## Supported tenancy models

1. **Shared / multi-tenant SaaS** — shared application + shared DB with logical isolation (organization/tenant ID).
2. **Shared application + dedicated schema**
3. **Shared application + dedicated database**
4. **Dedicated / single-tenant** — dedicated VPC/VCN, compute, storage, Kubernetes cluster, database, encryption keys, VPN, monitoring workspace (recommended for regulated enterprises / sensitive data).

## Logical isolation mechanisms (multi-tenant)

- Every record scoped with mandatory `organization_id`.
- Tenant filtering enforced at data access layer / ORM / service-layer guards.
- JWT authentication with embedded tenant context; gateway validates tenant boundaries.
- Users scoped to a specific organization; cross-organization access not configurable via UI/API.
- Automated tests / static checks enforce tenant filters.
- Comprehensive per-tenant audit logging.
- Backup data follows same tenant isolation principles.
- No direct DB access for customers/external systems — API-only with validation and throttling.

## Environment isolation

Dev / UAT / Production isolated at infrastructure level:

- Separate Kubernetes clusters / namespaces
- Independent databases and storage
- Separate credentials, secrets, access policies
- No production data in Dev/UAT unless anonymized

## Dedicated deployment isolation

- Isolated compute and storage
- Separate databases
- Network-level isolation
- Optional VPN-only access / elimination of public exposure
- IP allowlisting and private access endpoints supported for SaaS as well

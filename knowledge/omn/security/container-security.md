# Oman Container & Kubernetes Security

Marmin’s Oman e-invoicing platform deploys as containerized microservices on **Kubernetes**, following container security best practices.

## Design & segregation

- Equivalent security controls across enterprise DC, physical, and virtual platforms
- Micro-segmentation / network policies between services and tiers
- Tenant segregation on shared infrastructure (control-plane isolation, no cross-tenant access)
- Environment segregation: Development, QA, Staging, Production
- Tier segregation (web / app / data)
- RBAC for tenants and operators; defined incident-response roles

## Communication

- Service-to-service communication over authenticated, authorized, encrypted channels
- Kubernetes / Docker control-plane APIs not exposed to the public internet
- External exposure only via approved ingress / API gateway paths

## Images & supply chain

- Block insecure/external registries; only approved registries and roles
- Remove insecure image versions; maintain known-secure versions
- Image scanning and remediation as part of deployment/release security testing
- No clear-text embedded secrets; centralized secrets management
- SCA / dependency scanning for vulnerable libraries

## Runtime & orchestration

- Least-privilege containers; reduced attack surface
- Orchestration admin access via jump host / PAM patterns with MFA where required — no direct public SSH to nodes
- Integration with enterprise AD/LDAP/SAML/IdP for platform access where customer infrastructure provides it
- Monitor and alert on administrative activities
- Host OS RBAC, logging, and hardening
- Application-layer security logs persisted for SIEM/monitoring integration
- WAF protection for published web entry points on customer infrastructure
- High availability / site redundancy for mission-critical container infrastructure

## CI/CD

- Secured CI/CD access (including cloud CI credentials when used)
- Security testing as part of deployment and release process

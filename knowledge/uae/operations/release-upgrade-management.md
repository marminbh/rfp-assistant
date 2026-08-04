# Hardware, Software Updates & Upgrade Management

Marmin follows a structured Release and Upgrade Management process so infrastructure, platform, security, and application updates are thoroughly validated before production deployment.

All updates are first deployed and validated within Marmin's internal environments before promotion to any white-labelled environment.

## Scope of the release lifecycle

- Application enhancements and bug fixes
- Kubernetes platform upgrades
- Operating system patches
- Database upgrades
- Security patches
- Container image updates
- Third-party library updates
- PINT specification upgrades
- Peppol specification updates
- UAE regulatory compliance updates
- Infrastructure and configuration changes

## Promotion path

1. Marmin Development
2. Marmin Sandbox (prod-like)
3. White-labelled Sandbox (partner UAT)
4. Marmin Production
5. White-labelled Production

Single version-controlled release artifact; partner behavior via configuration (no partner-specific code forks during promotion). White-label production only after partner sandbox approval.

## Dev validation gates

Unit, integration, functional, E2E, regression, performance, load, security testing; SAST; dependency/container image scanning; DB migration validation; infra validation.

## Sandbox validation

Deployment verification, smoke/sanity, API compatibility, PINT XML validation, Peppol interoperability, upgrade + rollback verification, infra health.

## Types of updates managed

### Application
New features, enhancements, bug fixes, performance optimizations, API improvements, configuration updates.

### Kubernetes
Version upgrades, control plane, worker nodes, ingress controller, CSI, CNI, Helm charts.

### Operating system
Linux security patches, kernel updates, package updates, critical vulnerability remediation.

### Database
PostgreSQL upgrades, MongoDB upgrades, security patches, performance improvements, schema migrations.

### Security
OpenSSL updates, base container image refresh, third-party dependency updates, vulnerability remediation, certificate rotation, secret rotation.

### Standards and regulatory
PINT upgrades, Peppol BIS updates, UAE e-Invoicing framework updates, XML Schema revisions, validation rule updates, code list updates.

## Governance & rollback

Approvals: Engineering, QA, DevOps, Release Manager, Partner UAT (white-label).  
No production deployment without mandatory quality gates.

Rollback: health assessment → prior validated release → DB rollback if applicable → RCA/CAPA.

## Maintenance windows

Routine upgrades during scheduled windows. Emergency security updates may run outside windows after internal validation and risk assessment.

## Traceability

Release version, notes, changelog, tested components, impact assessment, approvals, deployment history, rollback package, timestamps.

## Service level commitments

- Releases validated internally before white-label deployment
- White-labelled deployments use the same validated artifacts as Marmin
- Partner production only after white-labelled sandbox validation and formal partner approval
- Post-release monitoring for service stability

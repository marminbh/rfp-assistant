# Support, Maintenance & SLAs

## Support scope

Platform, white-label, prod + sandbox, APIs, web apps/portals, Kubernetes, databases, messaging, monitoring, security, backup/DR, regulatory updates, releases.

## Tiers

- **L1:** intake, ticket logging, initial troubleshooting, user assistance, categorization, communication, escalation
- **L2:** functional/app troubleshooting, config, integration, logs, performance, environment validation
- **L3:** code defects, hotfixes, infra/DB/security, RCA, engineering
- **Platform Engineering:** K8s, infra, monitoring, CI/CD, DBA, capacity, backup, DR readiness

## Channels

Service Desk Portal (Confluence), Email, Telephone, Customer Success Manager, Emergency channel for criticals. Unique ticket per request.

## Incident priorities

| Priority | Examples |
|---|---|
| P1 Critical | Prod unavailable; full outage; security breach; data corruption; invoice processing down |
| P2 High | Major function down; integration failures; multi-customer impact; significant degradation |
| P3 Medium | Functional/single-customer/config/non-critical API issues |
| P4 Low | Cosmetic; docs; enquiries; feature requests |

## Service level targets (Ongoing Support Plan)

| Priority | Initial response | Target resolution |
|---|---|---|
| Critical | 30 minutes | 4 hours (or workaround) |
| High | 1 hour | 8 business hours |
| Medium | 4 business hours | 3 business days |
| Low | 1 business day | Next planned release |

Targets may vary with third-party / regulatory authority dependencies.

## Escalation matrix (alternate enterprise cloud response)

| Severity | Response time | Escalation |
|---|---|---|
| Critical (P0) | 15 minutes | Operations Head + CTO |
| High (P1) | 30 minutes | Engineering Manager |
| Medium (P2) | 4 hours | Support Lead |
| Low (P3) | 1 business day | Support Team |

24×7 operational support for production incidents (enterprise cloud response).

## Maintenance

- Planned windows communicated in advance; rolling deployments where possible
- Planned downtime ~**1 min / week** (implementation questionnaire)
- Emergency security updates may run outside windows after internal validation/risk assessment

## Communication & reporting

Customers/partners informed of: incident ack/progress/workarounds/resolution; planned maintenance; releases; security advisories; regulatory updates; RCA for major incidents.  
Operational reporting may include incident stats, SLA achievement, availability, capacity, security/maintenance/release summaries.

# Shared Responsibility Model

## SaaS

| Area | Marmin | Client |
|---|---|---|
| Cloud infrastructure | Fully responsible | — |
| Network security | Design/implement/monitor/maintain | — |
| Platform security (OS harden/patch/vuln) | ✔ | — |
| Application security (SSDLC, pentest, secure coding) | ✔ | — |
| IAM (Marmin platform admin access) | ✔ | — |
| API availability | ✔ | — |
| Encryption in transit/at rest | ✔ | — |
| Backup & DR | ✔ | — |
| Security monitoring / IR | ✔ | — |
| API credential issuance/lifecycle | ✔ | Secure storage & usage ✔ |
| Client ERP/apps integrating to Marmin | — | ✔ |
| Accuracy/legality/authorization of submitted data | — | ✔ |
| Endpoint security of client devices/networks | — | ✔ |
| User auth within client systems | — | ✔ |

Clients do **not** provision/manage VMs in Marmin SaaS.

## Client monitoring of SaaS

Via: API response codes/errors; client-side request/response logging; API health; webhook delivery status; integration logs; support notifications for maintenance/incidents. Infra-level monitoring remains Marmin-owned; operational reports available where required.

- Application monitoring logs are **not** directly downloadable by customers in SaaS
- Security logs retained **6 months**; relevant excerpts can be provided on request
- Planned maintenance: Service Provider notifies customers in advance when downtime is expected

## Disaster recovery roles

| Party | Responsibility |
|---|---|
| Marmin | Infrastructure recovery, system/data restore, platform bring-up |
| Customer | Validate application functionality, verify internal integrations, confirm business process continuity after restore |

Customers do **not** directly configure SaaS backup schedules or download raw backup images; they may request data exports.

## Configuration management roles

- Marmin: infrastructure, OS, DB, security baselines, patching, change control, unauthorized-change monitoring/alerts
- Customer: application-level config only (users, org settings, document/operational parameters)
- Changes validated in non-production before production; formal change review/prioritization

## White-label support split

- Partner: L1 customer support and all customer communications
- Marmin: L2/L3, product, security patching, regulatory updates, infra/K8s/DB, monitoring, backup/DR, releases, availability

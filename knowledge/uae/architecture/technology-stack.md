# Technology Stack

## Core stack

| Layer | Technology |
|---|---|
| API Gateway | Kong Gateway |
| Frontend | React |
| Backend | Golang, Java, Python; Node.js also listed |
| Databases | MongoDB and PostgreSQL (transactional data) |
| Cache | Redis |
| Messaging | RabbitMQ |
| Orchestration | Kubernetes |
| CI/CD | Jenkins (referenced in DR/exit materials) |
| Secrets | Secure vault / HashiCorp Vault (on-prem recommended stack) |
| Monitoring | Prometheus, Grafana; Thanos; Loki/Promtail; OpenTelemetry; Alertmanager; ELK/OpenSearch also referenced |

## Version details (hybrid/on-prem sizing materials)

| Technology | Version |
|---|---|
| Python | 3.13 |
| Java | 25 |
| Go | 1.25.5 |
| Node.js | 21.6 |
| Kubernetes | v1.35+ |
| OS | Ubuntu Server 24.04.4 LTS |
| Observability | Prometheus, Grafana, VictoriaLogs |

Also cited: Golang 1.25 and Java 25 LTS; TLS 1.2 or higher.

## SaaS hardware sketch (OCI)

**Production**

- Application nodes: auto-scaled; AMD EPYC 7J13; 8 vCPU / 32GB / 128GB; Linux; OCI Block Storage; containerized microservices
- DB cluster (MongoDB/PostgreSQL): 3 nodes; 8–16 vCPU; 32–64 GB; 256 GB; HA cluster
- Load balancer: OCI Managed LB
- Object/backup storage: OCI Object Storage

**TDL / test**

- App test env: 2 × 4 vCPU / 16 GB
- Test DB: 1 × 4–8 vCPU / 16–32 GB

Licenses for Linux, Kubernetes, runtimes, MongoDB, PostgreSQL: managed/included by Service Provider in SaaS model.

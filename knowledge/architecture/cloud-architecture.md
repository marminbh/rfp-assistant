# Cloud Architecture

## Architectural style

- Microservices architecture: modularity, scalability, independent service lifecycle.
- Core components: API gateway, domain services, messaging systems, data stores.
- Push-based deployment model: vendor-controlled releases, version control, rollback, auditability.
- Asynchronous event-driven invoice processing.
- Horizontally scalable; Kubernetes-orchestrated containers.

## Layered deployment view

1. Network Layer
2. Security Layer
3. Application Layer
4. Data Layer
5. Monitoring & Governance Layer

## High-level SaaS flow

```text
Enterprise Users / Enterprise Systems
→ Secure HTTPS / API Integration
→ Cloud Load Balancer
→ Kubernetes Application Services
→ Database Layer (MongoDB / PostgreSQL)
→ Encrypted Storage and Backups
```

External regulatory / trading-partner exchange handled through the application service layer / Peppol Access Point.

## UAE production hosting (primary SaaS design)

| Component | Operator | Region (primary design) | Role |
|---|---|---|---|
| Application platform | Marmin Technologies (Data Processor) | Abu Dhabi (Primary) | Application services |
| Production database | Marmin | Abu Dhabi (Primary) | Invoice metadata & processing records |
| Database replica | Marmin | Mumbai | Real-time replication / BC |
| Disaster recovery DB | Marmin | Singapore | Warm standby / DR |
| Monitoring & logs | Marmin | Abu Dhabi | Operational logs |

**Conflict:** Some enterprise SaaS annexure responses state hosting in **Oracle Cloud Dubai Region** (and “Dubai and Abu Dhabi Region”), with multi-AD HA inside the region. Prefer current UAE production matrix (Abu Dhabi / Mumbai / Singapore) unless a bid-specific annexure wording is approved. See `rfp/conflicts-and-caveats.md`.

## Infrastructure components (DR Plan — Oracle Cloud Abu Dhabi)

- Oracle Kubernetes Engine (OKE)
- Node pools for HA
- OCI Load Balancers for ingress
- OCI Block Storage for persistent workloads
- MongoDB 3-member replica set on Kubernetes
- RabbitMQ (async workflows, durable messages, persistent volumes)
- Redis (cache, OTP/session, rate limiting)
- Peppol Access Point as microservice on same OKE cluster
- AWS S3 for encrypted cross-cloud backups
- Observability: kube-prometheus; Fluentd logging; Loki/Promtail/Grafana/Thanos/OpenTelemetry

## Network segmentation

- Segregated VCNs; public/private segmentation
- Dedicated subnets for application, database, management
- NSGs / security lists; least-privilege tier communication
- Firewalls between external / app / DB tiers
- WAF, DDoS protection, IDS capabilities via OCI + application controls
- Administrative access via secure channels / bastion / least privilege

## CSP options

| CSP | Status |
|---|---|
| Oracle Cloud Infrastructure (OCI) | Highly recommended |
| Amazon Web Services (AWS) | Recommended |
| Microsoft Azure | Supported |
| Google Cloud Platform (GCP) | Supported |

## Portability

Containerized, Kubernetes-based, cloud-agnostic enough to redeploy to public cloud, private/community cloud, or on-prem Kubernetes (Helm charts / container images / controlled data migration).

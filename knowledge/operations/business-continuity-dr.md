# Business Continuity & Disaster Recovery

## Canonical UAE SaaS BC narrative

- **Primary production:** Abu Dhabi; multi-AZ distribution
- **DR:** Mumbai active-passive application DR site in BC overview; residency matrix cites Singapore warm standby DR DB + Mumbai real-time replica
- **DB topology:** three-region continuous replication — Abu Dhabi primary, Mumbai secondary, Singapore secondary/DR
- **Availability target:** 99.9%+ (some questionnaires state 99.99% — see conflicts)
- **DR testing:** every **3 months**; BCP training last dated 25 Mar 2026; backup restore drill 4 Apr 2026 successful (Security overview)

### Failover steps (BC overview)

detect → approve DR activation → DB failover/validate → activate DR app services → redirect traffic → communicate/monitor → controlled failback

### Recovery claims (residency / recovery matrix)

- RPO: no data loss for committed transactions; replication lag <1 second; self-managing leader election
- RTO: within 1 hour; internal validation expected **within 15 minutes** under normal conditions

## Detailed Oracle DR Plan (component RTOs)

| Component | RTO | RPO |
|---|---|---|
| MongoDB | 30–90 min | ~1 minute |
| API & microservices | <15 min | Zero (stateless) |
| Peppol AP | <15 min | Zero |
| Kubernetes cluster | 30–60 min | N/A |
| RabbitMQ | <15 min | Zero |
| Redis | Zero hard dependency | Zero (rebuild) |
| Full platform | 45–60 min | ~1 minute |

Backup notes: realtime multi-region replication; snapshot every 1 hour; full backup daily; S3 encrypted + versioning; daily integrity verification.

**Annual DR test success criteria in same plan:** restore full platform **<6 hours**; no data loss beyond RPO of **4 hours** — conflicts with near-zero RPO claims elsewhere.

Communication: notify customers if downtime may exceed 1 hour; hourly updates until recovery; RCA within 48 hours. DRP review every 6 months.

## Security overview alternate RTO/RPO

| Scope | RTO | RPO |
|---|---|---|
| Platform-level | 15 minutes | 1 hour |
| System/service-level | 1 hour | 15 minutes |

## Enterprise SaaS annexure (more conservative)

- DR methodology: **Backup & Restore** with in-region redundancy; pilot-light/warm/hot/cross-cloud **not** part of standard offering in that response
- RTO up to **4 hours**; RPO up to **1 hour**
- Uptime **99.9%** excluding maintenance
- Security logs 6 months / 180 days

## Hybrid always-on

RTO under **20 minutes**; RPO near-zero sub-minute (see `deployment/hybrid-onprem.md`).

## Disaster types covered

OCI region outage; K8s control plane/node failure; MongoDB corruption; microservices/ingress failure; RabbitMQ/Redis failure; network/DNS/LB outage; security breach/ransomware; Peppol AP outage.

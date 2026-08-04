# Business Continuity & Disaster Recovery

## Canonical UAE SaaS recovery targets

| Metric | Target |
|---|---|
| **RPO** | **0** (no data loss) |
| **RTO** | **1 hour** |

Use these as the default UAE SaaS RFP answers. Older annexure variants (e.g. RTO ≤4h / RPO ≤1h) are superseded for standard answering.

## Canonical UAE SaaS BC narrative

- **Primary production:** Abu Dhabi; multi-AZ distribution
- **DR:** Mumbai active-passive application DR site in BC overview; residency matrix cites Singapore warm standby DR DB + Mumbai real-time replica
- **DB topology:** three-region continuous replication — Abu Dhabi primary, Mumbai secondary, Singapore secondary/DR
- **Availability target:** 99.9%+ (some questionnaires state 99.99% — see conflicts)
- **DR testing:** every **3 months**; BCP training last dated 25 Mar 2026; backup restore drill 4 Apr 2026 successful (Security overview)

### Failover steps (BC overview)

detect → approve DR activation → DB failover/validate → activate DR app services → redirect traffic → communicate/monitor → controlled failback

### Recovery design notes

- RPO **0** / no data loss for committed transactions; replication lag typically under 1 second; self-managing leader election
- RTO **1 hour**; internal validation often expected within **15 minutes** under normal conditions

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

**Annual DR test success criteria in same plan:** restore full platform under **6 hours**; no data loss beyond RPO of **4 hours** — historical plan wording; do **not** use these as the default RFP answer (use RPO 0 / RTO 1 hour).

Communication: notify customers if downtime may exceed 1 hour; hourly updates until recovery; RCA within 48 hours. DRP review every 6 months.

## Security overview alternate RTO/RPO

| Scope | RTO | RPO |
|---|---|---|
| Platform-level | 15 minutes | 1 hour |
| System/service-level | 1 hour | 15 minutes |

## Enterprise SaaS annexure (historical / superseded for RTO–RPO)

- DR methodology: **Backup & Restore** with in-region / cloud-infrastructure redundancy; **pilot-light, warm standby, hot standby, and cross-cloud DR are not** part of the standard SaaS offering in that response
- Separate DR/TDL licenses: **not applicable** in SaaS (DR resources managed by Service Provider)
- That annexure once stated RTO up to **4 hours** and RPO up to **1 hour** — **superseded**; answer **RPO 0** and **RTO 1 hour** for UAE SaaS
- Uptime **99.9%** excluding scheduled maintenance
- Service credits for missed contractual SLAs: definable in the commercial agreement
- Security logs 6 months / 180 days
- Failover DNS propagation within standard DNS timelines after recovery environment is ready
- Temporary latency increase possible when failing over to a secondary site

## Hybrid always-on

RTO under **20 minutes**; RPO near-zero sub-minute (see `deployment/hybrid-onprem.md`).

## Disaster types covered

OCI region outage; K8s control plane/node failure; MongoDB corruption; microservices/ingress failure; RabbitMQ/Redis failure; network/DNS/LB outage; security breach/ransomware; Peppol AP outage.

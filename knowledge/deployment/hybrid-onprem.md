# Hybrid / On-Premise Models (Enterprise Materials)

## Option A — Core on-premises with Marmin as ASP (recommended)

- Core services + primary operational DB hosted in the customer datacenter.
- Marmin acts as Authorized Service Provider (ASP) and Peppol Access Point.
- Marmin handles mandated XML generation, secure transmission to FTA, and Peppol routing.
- Cloud AP stores **only transmission metadata** (sender, receiver, timestamp, status). **No customer financial/transactional data stored in cloud AP.**
- DR site: secondary UAE datacenter — mirrored standby.
- Dedicated isolated sandbox (replica of live) across DCs for release/patch testing and annual BCP/DR drills.
- Monitoring: Grafana + Prometheus.
- Marmin infra team remote access via VPN + MFA for monitoring/maintenance/releases (including schema/data migrations).

## Option B — Fully decentralized on-premise (not recommended by Marmin)

- Entire Marmin stack including Peppol AP hosted locally.
- Customer must independently obtain **Peppol Access Point accreditation** and **MOF ASP approval**.
- Requires additional dedicated machine for Peppol AP.
- Marmin provides software stack, implementation support, and accreditation assistance; ongoing accreditation ownership remains with customer.

## Always-on hot standby sizing (Options A/B)

- Primary: customer primary DC — Active K8s + 3 DB nodes
- DR: secondary UAE DC — Always-On K8s + 2 DB nodes
- Topology: 3+2 distributed DB; app compute fully scaled in DR
- Expected RTO: **under 20 minutes**; RPO: **near-zero (sub-minute)**

### Live primary per-machine sketch

| Tier | Qty | Config | Storage |
|---|---|---|---|
| K8s control plane | 3 | 4 vCPU, 8 GB | 256 GB SSD |
| K8s workers | 2 | 16 vCPU, 32 GB | 512 GB NVMe |
| Database | 3 | 32 vCPU, 128 GB | 4 TB NVMe |
| Cache & messaging | 2 | 16 vCPU, 32 GB | 256 GB SSD |
| Observability | 2 | 8 vCPU, 32 GB | 2 TB SSD (1 year app logs) |

### MongoDB growth projection

- 10,000 documents/day × 50 KB ≈ 500 MB/day
- ~182.5 GB raw/year (~365 GB with indexes/oplog/WiredTiger)
- 5-year ≈ 1.8 TB; nodes over-provisioned with ~5 TB NVMe

### Failover workflow

1. Force DR DB nodes to form new Primary (~5 min)
2. DNS/LB cutover to DR Ingress (~5–15 min)
3. Redis/RabbitMQ rebuild locally (not WAN-replicated)

### On-prem backup recommendation

- Separate 2–4 TB network storage
- Full weekly; incremental daily; transaction logs every 15 min
- Retention: daily 7 days; weekly 4 weeks; monthly 6–12 months

### Multi-layer data protection

1. Network/perimeter: zero-trust private network; K8s Ingress; customer firewalls/IDS for full on-prem
2. Transit: TLS 1.3 pod-to-pod and external; Peppol via accredited AP
3. Rest: AES-256 volume encryption for MongoDB/PostgreSQL; encrypted backups
4. Use/privacy: cloud AP metadata-only; sanitized sandbox; audit logs up to 1 year in observability tier

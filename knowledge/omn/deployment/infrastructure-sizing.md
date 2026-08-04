# Oman Infrastructure Sizing

Proposed sizing for dedicated / VMware-style or customer-cloud compute deployments. Customer-specific volume statistics are not stored in this knowledge base. **Exact BOQ is engagement-specific** — two reference proposals are documented below.

## Environments

| Environment | Purpose |
|---|---|
| Production | Live connectivity to OTA / Peppol |
| Sandbox / Test | Integration testing and UAT |

Architecture diagrams (network and hardware, including DR) can be provided once an NDA is signed / as part of the technical proposal.

## Reference proposal A — compact (7 / 5)

| Environment | Servers |
|---|---|
| Production | **7** |
| Test | **5** |

### Production (proposal A)

OS: **Ubuntu 26.04 LTS**.

| # Servers | Applications / Module | CPU | Cores | RAM (GB) | Disk (GB) | Notes |
|---|---|---|---|---|---|---|
| **2** | Microservices | 1 | 4 | 16 | 256 | |
| **3** | MongoDB, PostgreSQL, RabbitMQ, Redis | 1 | 4 | 16 | 256 + 512 | Additional **512 GB SSD** for database storage; 256 GB for OS |
| **2** | Kubernetes platform | 1 | 4 | 16 | 256 | |

### Test (proposal A)

| # Servers | Applications | CPU | Cores | RAM (GB) | Disk (GB) | Notes |
|---|---|---|---|---|---|---|
| **3** | Microservices + MongoDB + PostgreSQL + RabbitMQ + Redis | 1 | 4 | 16 | 256 + 512 | Additional **512 GB SSD** for DB storage |
| **2** | Kubernetes platform | 1 | 4 | 16 | 256 | |

## Reference proposal B — bank-scale (11 / 9)

| Environment | Servers |
|---|---|
| Production | **11** |
| Test | **9** |

### Production (proposal B)

| # Servers | Applications / Module | OS | Cores | RAM (GB) | Disk (GB) |
|---|---|---|---|---|---|
| **3** | PostgreSQL compute | Ubuntu 26.04 | 2 | 12 | 512 |
| **3** | MongoDB compute | Ubuntu 26.04 | 2 | 12 | 512 |
| **5** | Application servers | Ubuntu 26.04 | 2 | 12 | 256 |

### Test (proposal B)

| # Servers | Applications / Module | OS | Cores | RAM (GB) | Disk (GB) |
|---|---|---|---|---|---|
| **3** | PostgreSQL compute | Ubuntu 26.04 | 2 | 8 | 512 |
| **3** | MongoDB compute | Ubuntu 26.04 | 2 | 8 | 512 |
| **3** | Application servers | Ubuntu 26.04 | 2 | 8 | 256 |

Additional networking requirements apply. Choose or blend proposals based on HA, volume, and customer standards.

## Platform signals

- Containerized microservices on **Kubernetes**
- Data/services: **MongoDB**, **PostgreSQL** (RabbitMQ / Redis in compact K8s-oriented proposals)
- Virtualization: **VMware** supported (including SQL on VMware)
- Linux OS baseline: **Ubuntu 26.04 LTS**
- Cloud-agnostic; SaaS / PaaS / IaaS / on-prem (see `deployment-options.md`)

## Gaps / unknowns

- Detailed per-server hardware SKUs / vendor makes are not documented here
- Do not invent Oman DC city names; do not reuse UAE Mumbai/Singapore DR cities for Oman

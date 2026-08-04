# Oman Infrastructure Sizing

Proposed sizing for dedicated / VMware-style deployments. Customer-specific volume statistics are not stored in this knowledge base.

## Server counts

| Environment | Servers |
|---|---|
| Production | **7** |
| Test | **5** |

Architecture diagrams based on stated business capacity can be provided once an NDA is signed.

## Production environment

OS: **Ubuntu 26.04 LTS**.

| # Servers | Applications / Module | CPU | Cores | RAM (GB) | Disk (GB) | Notes |
|---|---|---|---|---|---|---|
| **2** | Microservices | 1 | 4 | 16 | 256 | |
| **3** | MongoDB, PostgreSQL, RabbitMQ, Redis | 1 | 4 | 16 | 256 + 512 | Additional **512 GB SSD** for database storage; 256 GB for OS |
| **2** | Kubernetes platform | 1 | 4 | 16 | 256 | |

## Test environment

| # Servers | Applications | CPU | Cores | RAM (GB) | Disk (GB) | Notes |
|---|---|---|---|---|---|---|
| **3** | Microservices + MongoDB + PostgreSQL + RabbitMQ + Redis | 1 | 4 | 16 | 256 + 512 | Additional **512 GB SSD** for DB storage |
| **2** | Kubernetes platform | 1 | 4 | 16 | 256 | |

## Platform signals

- Containerized microservices on **Kubernetes**
- Data/services: **MongoDB**, **PostgreSQL**, **RabbitMQ**, **Redis**
- Virtualization: **VMware** supported (including SQL on VMware)
- Linux OS baseline in proposal: **Ubuntu 26.04 LTS**

## Gaps / unknowns

- Detailed per-server hardware SKUs are not documented here
- Physical-server BOM alternatives are not documented (VMware path is the answered path)
- Do not reuse UAE OCI SaaS node sizes for Oman unless separately confirmed

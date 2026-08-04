# Exit Strategy, Data Portability & Migration

## Data ownership

- Customer business data, invoices, audit records, logs, and metadata remain sole property of the customer.
- Marmin acts as data processor / service provider.
- No retention beyond agreed contractual timelines after termination (subject to regulatory retention holds).

## Portability / redeployment

Platform is containerized and Kubernetes-based; supports redeployment to:

- Customer private datacenter
- VMware
- OpenShift
- Other Kubernetes on-prem / private / community cloud

On-prem recommended stack includes: Kubernetes, PostgreSQL & MongoDB, RabbitMQ, Prometheus + Grafana, ELK, Jenkins, HashiCorp Vault, object storage, load balancer, container registry.

## Exit / handover deliverables

- 100% extraction of historical transaction records, compliance logs, customer master data
- Cryptographically signed XML payloads with official tax authority hashes
- Audit-ready PDF archives of cleared e-invoices (network timestamps / approval markers)
- Tabular ledger exports (.xlsx / .csv)
- Tenant-isolated DB exports as structured text/JSON (**no raw physical multi-tenant DB snapshots**)
- Secure SFTP transfer; certified wipe after client confirms receipt

## Other export statements

- CSV / XLSX export of invoice data + status/processing metadata
- Full DB export, audit log export, object storage export, API extraction, migration assistance, knowledge transfer
- Defined transition period after SaaS termination for customer data export

## Deletion constraints

Where deletion is requested during an active regulatory retention period, Marmin cannot permanently erase regulated invoice records until the legal retention period elapses or contractual obligation ends.

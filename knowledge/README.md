# UAE E-Invoicing Knowledge Base

Structured markdown for the RFP Assistant, enriched from Marmin RFP/security/ops source documents.

## Layout

| Folder | Contents |
|--------|----------|
| `product/` | Overview, features, integrations |
| `architecture/` | Cloud architecture, stack, tenancy |
| `deployment/` | Deployment options, hybrid/on-prem, exit |
| `security/` | Controls, IAM, encryption, app checklist |
| `compliance/` | Certifications, residency/retention, shared responsibility |
| `operations/` | Support/SLA, releases, monitoring, BC/DR |
| `rfp/` | FAQ, conflicts/caveats, company demographics |

After edits, re-index: `python -m app.ingest` or use **Re-index** in the UI.

**Important:** Before locking RFP numbers, read `rfp/conflicts-and-caveats.md`.

# Data Residency, Subprocessors & Retention

## Current UAE production design

| Component | Hosting | Retention | Deletion |
|---|---|---|---|
| Application platform | Abu Dhabi primary | Life of contract | After offboarding unless regulatory retention applies |
| Production DB | Abu Dhabi | 5 years (regulatory) | Not before statutory retention |
| DB replica | Mumbai | Same as primary | Same |
| DR DB | Singapore | Same as primary | Same |
| Monitoring & logs | Abu Dhabi | 6 months | Automatic retention policy |

## DPA clarification

Earlier DPA Annex 2 referenced AWS US and OCI Saudi Arabia as **legacy/generic template** entries — **not** current UAE e-invoicing production. Updated design reflects Abu Dhabi / Mumbai / Singapore.

## AWS S3 backup controls

- Purpose: encrypted DR backups only
- Encryption: AES-256 SSE-KMS; Marmin-managed keys
- Frequency: hourly
- Retention: **15 days**; automated lifecycle deletion
- Access: least-privilege infra admins

## Retention datasets

| Dataset | Retention | Basis |
|---|---|---|
| Tax invoices | 5 years | UAE tax/accounting requirements |
| Invoice processing metadata | 5 years | Auditability/traceability |
| Audit trail | 5 years | Regulatory evidence |
| Application logs | 6 months | Operational |
| Database backups (extreme all-replica loss) | 15 days | DR |

**Clarification:** Prior “10-year” wording = statutory 5 years after financial year **plus** up to 4 additional years for audits/disputes (maximum posture), not the standard operating retention.

**Conflict:** Feature list “6-year regulatory archiving” vs 5-year matrix above — see `rfp/conflicts-and-caveats.md`.

## Data center selection

Standard SaaS: customers cannot arbitrarily select DCs. UAE production in UAE region; backup/DR per Marmin BCP/DR policy. Specific residency can be discussed contractually where required.

# Oman Security Controls — Starter

Platform security for Oman deployments follows Marmin’s managed SaaS / dedicated-cloud security baseline (TLS in transit, encryption at rest, RBAC, audit logging, vulnerability management).

## Confirmed for RFP use (OMN KB)

- Authenticated API access
- Role-based access control
- Audit logging of document and admin actions
- Peppol transmission over the configured network path

## Not yet documented for Oman in this KB

- Exact production data residency region(s)
- Oman-specific DR topology and RTO/RPO numbers
- Customer-managed encryption keys / BYOK policy for Oman bids

Until those are added under `omn/`, do not invent values and do not copy UAE-only residency matrices.

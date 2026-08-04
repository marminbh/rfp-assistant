# Oman Business Continuity & Disaster Recovery

## Recovery targets

Marmin’s Oman e-invoicing backup and DR architecture supports:

| Metric | Target |
|---|---|
| **RPO** | **Less than 5 minutes** |
| **RTO** | **Less than 1 hour** |

These targets meet or exceed common enterprise SLA asks such as RTO 2 hours / RPO 4 hours. Confirm engagement-specific contractual SLAs in the commercial proposal.

## Backup & restore

- Secure, automated, regularly tested backup, restore, and archiving for critical data and configurations
- Backup of persistent system logs and configuration on a regular, configurable basis
- Full (hot/cold), incremental, differential, and snapshot backup types
- Hot (live) database backup support
- Database journaling / roll-forward recovery where the database engine supports it
- Point-in-time restoration of production to a previous state: **partial** — available as a platform capability but may need engagement-specific validation with customer backup tooling
- Non-interruption of services during backup/restore procedures where designed
- Backups encrypted at rest (**AES-256** or equivalent) and transmitted over TLS
- Immutable / access-controlled archive storage where required
- Automated integrity checks for backup completeness; alerts on failed or missed jobs
- Compatibility with customer centralized backup infrastructure when deployed on customer-managed environments

## High availability & DR topology

- Failover management with data/system integrity during failover
- High-availability infrastructure design
- Disaster recovery at a secondary geographic site
- DR/BCP processes aligned to the customer’s organization plans for the engagement

## Environments

Separate **Development**, **QA**, **Staging**, and **Production** environments are supported before go-live.

## Notes

- Numeric DR **location** (city/region) for Oman is not documented here — if asked for a specific Oman DR city without a documented answer: **I don't know the answer.**
- Do not reuse UAE Mumbai/Singapore DR facts for Oman.

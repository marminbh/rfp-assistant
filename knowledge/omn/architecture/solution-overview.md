# Oman Solution Architecture Overview

## High-level components

- **API gateway:** Kong Gateway for authenticated/authorized API access and policy enforcement
- **API layer:** REST services for documents, parties, auth, and Peppol status
- **UI:** Business-user console for invoice operations (Edge / Chrome)
- **Document services:** Create, validate, store, and transform invoice payloads
- **Network connector:** Peppol Access Point / OTA-approved ASP path for submit and receive
- **Supporting services:** Auth, audit, codelists (including OMN subdivisions), partner management, messaging, cache, secrets management

## Architecture principles

- N-tier, open, and scalable architecture
- Microservice architecture on Kubernetes
- Cluster architecture with failover
- Single unified data model without unnecessary data duplication
- Thin-client open standards; no proprietary client software
- Scalable for growing users and large data volumes
- Portable / migratable across environments
- Does not rely on undisclosed third-party technology for core operations; open-source components include Kubernetes and Docker
- DevOps support and Agile delivery processes

## Typical deployment pattern

1. Customer systems call Marmin APIs (or submit via WebApp / bulk / SFTP) with authenticated credentials
2. Marmin validates invoice and party data against OTA / platform rules
3. Document is submitted through the configured Oman Peppol / ASP path (5-Corner Model)
4. Status is retrieved via Peppol status APIs
5. Artifacts remain available for download and audit; retention/purge rules apply

## Platform compatibility notes

- Web UI: Microsoft Edge and Chrome supported
- VMware virtualization: supported (including SQL Server on VMware)
- Kubernetes containerization (e.g. OCI OKE): supported
- Windows Server 2022+ compatibility: on roadmap (future)
- Windows 11+ client compatibility: on roadmap (future)

## Notes

- Prefer market-specific hosting/residency facts only when documented under `omn/` (do not reuse UAE Abu Dhabi/Mumbai/Singapore facts for Oman unless confirmed).
- See `technology-stack.md` for runtime/data components and `../deployment/infrastructure-sizing.md` for proposed server counts.

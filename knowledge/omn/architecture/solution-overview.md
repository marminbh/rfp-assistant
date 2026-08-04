# Oman Solution Architecture Overview

## High-level components

- **API layer:** REST services for documents, parties, auth, and Peppol status
- **UI:** Business-user console for invoice operations
- **Document services:** Create, validate, store, and transform invoice payloads
- **Network connector:** Peppol Access Point / ASP path for submit and receive
- **Supporting services:** Auth, codelists (including OMN subdivisions), partner management

## Typical deployment pattern

1. Customer systems call Marmin APIs with authenticated credentials
2. Marmin validates invoice and party data
3. Document is submitted through the configured Oman Peppol path
4. Status is retrieved via Peppol status APIs
5. Artifacts remain available for download and audit

## Notes

- Prefer market-specific hosting/residency facts only when documented under `omn/` (do not reuse UAE Abu Dhabi/Mumbai/Singapore facts for Oman unless confirmed).

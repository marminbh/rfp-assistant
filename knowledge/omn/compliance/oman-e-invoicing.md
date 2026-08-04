# Oman E-Invoicing Compliance

## Scope

Marmin Oman e-invoicing supports electronic invoice exchange using Peppol-oriented flows and Oman-relevant document/party data (including Oman subdivision and address-scheme codelists), aligned with Oman Tax Authority (OTA) requirements.

## OTA / tax mandate alignment

- Oman electronic invoicing using the **5-Corner Model** for secure, standardized invoice exchange between businesses, service providers, and the **OTA**
- Align / integrate with **XVAT** using the OTA **Data Dictionary**
- Issue VAT invoices electronically in OTA-approved format via an **OTA-approved ASP**
- E-invoicing solution integrated with XVAT to issue **validated tax invoices**

## Solution alignment

- Structured electronic invoice payloads suitable for Oman Peppol / OTA exchange
- Party identification and validation required for submission/receipt
- Peppol status tracking and status logs for operational follow-up
- Retention of document artifacts (XML/PDF) for audit support
- Retrieve invoices promptly for regulatory inspections and investigations
- Detect/report duplicate invoices, unusual amendments, cancellations, and other configurable exception scenarios

## Privacy & regulatory compliance

- Compliance with **Oman Personal Data Protection Law (PDPL)**
- Retain records per regulatory retention requirements
- Regulatory reporting obligations supported
- Support for **CBO** outsourcing / regulatory documentation needs (approvals, registers, incident reporting)
- Data protection posture also references **PCI-DSS** and banking secrecy obligations where applicable to the engagement

## Data rules

- Quantity and unit rate: max **8** decimal points; all other amount fields: **2** decimal points
- History purge: only data older than **10 years** (as per regulation)

## RFP notes

- Exact regulatory timelines and mandate phases are defined by Oman authorities; confirm the latest official guidance for the prospect’s sector and size.
- The platform provides technical enablement (APIs, validation, network submission). Legal determination of mandate applicability remains with the customer’s tax advisors.
- Do not reuse UAE FTA / PINT-AE / Abu Dhabi residency facts for Oman.

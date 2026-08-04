# Oman Product Features & Capabilities

## Taxpayer onboarding

- Authorized administrators initiate taxpayer onboarding
- Capture and validate taxpayer registration details
- Register Peppol participant information in the **Service Metadata Locator (SML)**
- Publish service metadata in the **Service Metadata Publisher (SMP)**
- Validate successful Peppol network registration
- Maintain onboarding status and provide status updates to authorized users
- Onboarding APIs for taxpayer/participant registration and profile management

## Data extraction & upstream feeds

- Integrate with **XVAT** to receive VAT-determined transaction data
- Integrate with FA / input-side systems where e-invoice is mandatory for import-of-service transactions
- Extract all mandatory invoice attributes required for e-invoicing
- Validate completeness and integrity of extracted data
- Log extraction failures and notify support users

## B2B / B2G invoice issuance

- Receive VAT-determined invoice and credit-note transactions from upstream systems
- Validate incoming data against mandatory business rules
- Enrich invoice data to comply with **PINT Oman (PINT OM)** (hardcoded and logically derived fields)
- Validate invoice XML against applicable Peppol BIS schema
- Digitally prepare invoice payloads for secure transmission
- Transmit invoices and credit notes to the buyer’s Peppol Access Point
- Receive and record Peppol delivery acknowledgements
- Update invoice processing status throughout the lifecycle
- Straight-through processing (STP) across modules where configured

## Tax reporting to OTA

- Report invoice issuance (Accounts Receivable) to the OTA Access Point via Peppol
- Report invoice receipt (Accounts Payable) to the OTA Access Point
- Validate successful submission of reported transactions
- Maintain reporting acknowledgements and submission history

## B2C invoice issuance

- Receive B2C invoice and credit-note transaction data
- Validate and enrich to PINT OM requirements
- Generate a compliant **QR code** for each applicable B2C invoice
- Generate a PDF invoice containing the QR code
- Report B2C invoice data to the OTA Access Point via Peppol
- Maintain reporting acknowledgements for B2C transactions

## PDF generation

- Generate PDF invoices for invoice types mandated by Oman e-invoicing regulations
- Generate PDF credit notes where applicable
- Apply prescribed invoice layout and mandatory fields
- Download or share generated PDFs through configured channels

## Invoice receipt (AP)

- Receive supplier invoices through the Peppol network
- Validate received invoice XML against Peppol schema standards
- Validate mandatory business rules for incoming invoices
- Route validated invoices to the customer ERP or procurement system
- Notify the target system of invoice receipt status
- Maintain receipt acknowledgements and processing history

## Document tracking & error handling

- Peppol status and status-log retrieval for submitted documents
- Message-level transparency for troubleshooting
- Identify and classify processing errors
- Notifications for failed transactions with failure reason
- Automatically retry configurable transient failures
- Authorized users can manually reprocess failed transactions
- Detect/report duplicates, unusual amendments, cancellations, and configurable exception scenarios

## Dashboards & reports

- Dashboards showing invoice processing statistics
- Reports on issued, received, reported, failed, and pending invoices
- Search and filter invoice records
- Report export in **Excel, CSV, and PDF**
- Restrict dashboard access based on user roles
- Rich graphical display (pie, bar, and similar charts)
- End-user authored report builder / publish/schedule own reports: not supported
- Scheduled e-mail report distribution: on roadmap (future)

## Entity & master data

- Organization and party/profile management
- Multi-entity / multi-TIN style operational separation where configured
- Codelists including Oman subdivisions and electronic address schemes
- Single unified data model without unnecessary data duplication
- Parameterization of platform behaviour where configured

## UX & localization

- Web-enabled console; Edge and Chrome mandatory; Safari supported; Firefox/Opera optional
- Thin-client open standards; no proprietary client software required
- Arabic language interface
- Personalization limited to Arabic language customization (broader personalization not supported)
- Configurable customer logo
- Uniform customizable Look & Feel across platforms: not supported
- Print and help on all screens: not supported

## Controls & administration

- Role-based access control (RBAC); create/modify/activate/deactivate users
- Assign users to predefined roles and permissions
- Authenticate users before granting access; password management and lockout per customer security standards
- Maker-checker for transactions and admin/static-data changes; multi-level authorization by amount ranges where configured
- Web-based administration module
- Full audit trail for user activities, system events, and invoice lifecycle (create, validate, report, transmit, receive)
- Retain audit records per regulatory retention requirements
- Decimal rules: quantity and unit rate max **8** decimals; other amount fields **2**
- History purge: only data older than **10 years** (as per regulation)

## Emerging capabilities

- AI and machine learning features: supported
- Blockchain / distributed ledger: not supported
- Automation and robotics (RPA): not supported

## Developer ecosystem

- REST APIs for authentication, invoices, onboarding, and webhooks (see `integrations.md`)
- Sandbox environments for integration testing
- Docs: **https://docs.om.marmin.ai**

## Explicit non-capabilities (confirm before RFP use)

- Do not invent Oman-specific regulatory timelines or tax-authority outcomes not documented here.
- Customer-specific UI customization beyond documented options depends on scope and commercial agreement.
- If a capability is not covered in this OMN knowledge base, answer that it is unknown until documented.

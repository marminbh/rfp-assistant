# Oman Technology Stack

## Core stack

| Layer | Technology |
|---|---|
| API Gateway | Kong Gateway |
| Orchestration | Kubernetes |
| Containers | Docker |
| Microservices | Containerized application services |
| Databases | MongoDB, PostgreSQL |
| Cache | Redis |
| Messaging | RabbitMQ |
| Object storage | S3-compatible (where used) |
| Secrets | Secure vault / HashiCorp Vault / HSM / KMS patterns |
| Virtualization | VMware (supported, including SQL Server on VMware) |
| OS (proposed sizing) | Ubuntu 26.04 LTS |
| Browsers | Microsoft Edge and Google Chrome (mandatory); Apple Safari supported; Firefox / Opera optional |
| API docs | https://docs.om.marmin.ai |

## Environments

Separate **Development**, **QA**, **Staging**, and **Production** environments.

## Open-source components

Kubernetes and Docker are explicitly used. Other stack components follow Marmin’s managed platform standards for the chosen deployment model. Third-party/open-source components are covered by security testing and warranty obligations as part of product security assurance.

## Delivery practices

- DevOps support and Agile delivery
- Secure Software Development Lifecycle (S-SDLC)
- Proof of load tests available for anticipated UAT/production volumes
- Monitoring and early-warning alerts for high availability
- Debugging and logging of errors
- Database tables properly indexed
- Security testing (SAST/DAST/VAPT) as part of deployment and release

## Protocols & session controls

- TLS / HTTPS for application traffic (TLS 1.2+; TLS 1.3 preferred)
- mTLS for high-assurance service-to-service communication
- SMTP / SMPP where messaging channels are configured
- Session timeouts enforced
- Maker-checker for sensitive operational and admin actions

## Compatibility caveats

- Full Windows Server 2022+ compatibility: future / roadmap
- Full Windows 11+ compatibility: future / roadmap
- LDAP authentication and AD-only user provisioning: configuration / customization (see `../security/authentication-iam.md`)

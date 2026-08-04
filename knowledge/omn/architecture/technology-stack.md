# Oman Technology Stack

## Core stack

| Layer | Technology |
|---|---|
| Orchestration | Kubernetes |
| Containers | Docker |
| Microservices | Containerized application services |
| Databases | MongoDB, PostgreSQL |
| Cache | Redis |
| Messaging | RabbitMQ |
| Virtualization | VMware (supported, including SQL Server on VMware) |
| OS (proposed sizing) | Ubuntu 26.04 LTS |
| Browsers | Microsoft Edge, Google Chrome |

## Open-source components

Kubernetes and Docker are explicitly used. Other stack components follow Marmin’s managed platform standards for the chosen deployment model.

## Delivery practices

- DevOps support
- Agile methodology and related processes
- Proof of load tests available for anticipated UAT/production volumes
- Monitoring and early-warning alerts for high availability
- Debugging and logging of errors
- Database tables properly indexed

## Protocols & session controls

- SSL / HTTPS for application traffic
- SMTP / SMPP where messaging channels are configured
- Session timeouts enforced
- Maker-checker for sensitive operational and admin actions

## Compatibility caveats

- Full Windows Server 2022+ compatibility: future / roadmap
- Full Windows 11+ compatibility: future / roadmap
- LDAP authentication and AD-only user provisioning: customization required (see `../security/authentication-iam.md`)

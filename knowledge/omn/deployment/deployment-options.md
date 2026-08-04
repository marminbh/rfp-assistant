# Oman Deployment Options

## Supported models

| Model | Support |
|---|---|
| SaaS | Yes |
| PaaS | Yes |
| IaaS | Yes |
| On-premises | Yes |
| Cloud-native / cloud-agnostic | Yes |
| Container / Kubernetes | Yes |
| Hardware-agnostic (x86 and equivalent) | Yes |

The platform is built as cloud-native microservices and can run on customer cloud or on-prem infrastructure. Regional cloud hosting experience includes **OCI** deployments in GCC markets (e.g. Saudi Arabia and UAE stacks); Oman residency city/region must still be confirmed per engagement.

## Environments

Typical bank / enterprise proposals include at least:

- **Production** — live connectivity to OTA / Peppol
- **Sandbox / Test** — integration and UAT

Broader environment sets (Development, QA, Staging, Production) are also supported — see `../security/infrastructure-security.md` and `../operations/business-continuity-dr.md`.

## Integration posture

- Integrates with core banking and related systems via REST APIs and middleware
- Modular platform with STP, parameterization, and horizontal/vertical scalability
- Real-time processing and data synchronisation supported where configured
- Minimum-downtime design; continuous upgrade of the platform

## Sizing

Server counts and BOQ vary by engagement volume and HA requirements — see `infrastructure-sizing.md`.

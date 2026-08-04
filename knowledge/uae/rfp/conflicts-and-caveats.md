# Source Conflicts & Answering Caveats

Resolve with product/security ownership before RFP submission. Sources below are anonymized internal response sets (not customer-specific).

## 1. Primary region

- Abu Dhabi (data residency matrix, implementation questionnaire, BC/DR, DR Plan)
- Dubai Region / Dubai+Abu Dhabi (enterprise SaaS annexure)
- On-prem customer Dubai DC + secondary UAE DR DC (hybrid enterprise design)

## 2. DR location & model

- Mumbai passive app DR + 3-region DB (BC/DR overview)
- Singapore DR / warm standby (data residency matrix, implementation questionnaire)
- Backup & restore in-region only; no warm/hot/cross-cloud as standard (enterprise SaaS annexure)
- Always-on hot standby at secondary UAE DC (hybrid enterprise design)

## 3. RTO / RPO

**Resolved for UAE SaaS:** **RPO 0** (no data loss); **RTO 1 hour**.

Historical variants (do not use as default):

| Source | RTO | RPO |
|---|---|---|
| Enterprise SaaS annexure | ≤4 hr | ≤1 hr |
| Security overview platform | 15 min | 1 hr |
| Security overview system | 1 hr | 15 min |
| Implementation questionnaire | <1 hr | <15 min |
| DR Plan full platform | 45–60 min | ~1 min |
| DR Plan annual success criteria | <6 hr | ≤4 hr |
| Hybrid hot standby design | <20 min | Near-zero |

## 4. Availability

99.9%+ vs implementation questionnaire 99.99%.

## 5. Retention / archiving

5 years (data residency matrix / questionnaire) vs 6-year archiving (Feature list) vs clarified max 10-year posture (5+4).

## 6. SSO / SAML / OIDC / Entra ID

Fully implemented (Security Overview) vs not available / under development (auth response notes, enterprise SaaS annexure) vs “can be built” (implementation questionnaire).

## 7. BYOK / customer-managed keys

**Resolved:** Customer-managed encryption keys (BYOK) are **not allowed**. Keys are Marmin-managed via KMS only. Earlier annexure wording that suggested OCI customer-managed keys (or “can be supported through cloud KMS”) is superseded — do not offer BYOK.

## 8. Implementation timeline

2–6 weeks (implementation questionnaire) vs ~4 months (enterprise demographics annexure).

## 9. OAuth 2.0

Listed as supported for APIs in places; also “under development” in auth response notes; enterprise SaaS annexure says OAuth identity services not part of current auth model (native + JWT/API keys).

## 10. DPA geography

Legacy AWS US / OCI KSA template language superseded by Abu Dhabi / Mumbai / Singapore production design.

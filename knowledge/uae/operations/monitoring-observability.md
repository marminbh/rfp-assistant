# Monitoring & Observability

## Stack

| Function | Tools |
|---|---|
| Metrics | Prometheus (kube-prometheus-stack), Thanos |
| Visualization | Grafana |
| Logging | Loki + Promtail |
| Tracing | OpenTelemetry |
| Alerting | Alertmanager |

Also referenced: Fluentd; ELK/OpenSearch; VictoriaLogs (hybrid sizing); CSP-native monitoring; APM; SIEM.

## Monitored signals

App/API availability; K8s/container health; CPU/memory/disk; MongoDB & PostgreSQL replication; RabbitMQ; Redis; SSL expiry; backup status; storage; network latency; app logs; security alerts; audit events.

## KRIs

Security (failed logins, privilege escalations); Availability (uptime, node failures); Performance (API latency, queue lag); Capacity (CPU/mem/storage); Compliance (patch compliance, audit failures); DR (backup validation success).

## Customer visibility

SaaS customers generally do not get direct infra monitoring dashboards; notified on service-impacting incidents. Can monitor via APIs/webhooks and their own integration logs.

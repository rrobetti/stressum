# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T11:32:01Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 3 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260715-122016` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.67 RPS (per instance) |
| **Total throughput** | 26.68 RPS (all instances) |
| **p50 latency** | 29967.31 ms |
| **p95 latency** | 46811.06 ms |
| **p99 latency** | 77131.88 ms |
| **p999 latency** | 104455.62 ms |
| **Error rate** | 44.00% (0.44) |
| **Total requests** | 44518 |
| **Failed requests** | 19576 |
| **Total successful** | 24942 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 59 |
| observed_postgres_backends_avg_numbackends | 55.81 |
| observed_postgres_backends_median_numbackends | 56 |
| observed_client_backends_active_median | 40501 |
| observed_client_backends_active_max | 61214 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | pgbouncer-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.9% / 4.9% / 9.8% |
| OJP proxy-tier host_cpu (avg / peak) | 11.4% / 69.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 21.50% |
| OJP proxy-tier RSS (avg / peak, summed) | 35.20 MiB / 35.20 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.9% / 4.9% / 9.8% |
| PgBouncer tier RSS (avg / peak, summed) | 35.20 MiB / 35.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 3.9% / 4.9% / 8.8% |
| HAProxy RSS (avg / peak, summed) | 23.20 MiB / 23.40 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.9% / 1.0% / 5.9% / 9.7% / 17.6% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.0% / 104.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 30.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 58.40 MiB / 58.60 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 27 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (46811.06 ms) |
| Error rate | < 0.1% | ❌ FAIL (44.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.22 RPS (all instances) |
| **Achieved throughput** | 26.68 RPS (all instances) |
| **Attempted − achieved gap** | 19.54 RPS (42.28%) |
| **Total attempted ops** | 43215 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29884.415 | 47579.135 | 69468.159 | 1.6235155207228174 | 45.43% | 0.025025025025025023 | 1 |
| 10 | 30228.479 | 47841.279 | 73203.711 | 1.5860843822559618 | 46.92% | 0.025025025025025023 | 2 |
| 11 | 30523.391 | 46891.007 | 75366.399 | 1.6053338581060268 | 45.66% | 0.02502815667626079 | 1 |
| 12 | 30097.407 | 47513.599 | 90439.679 | 1.7219140839737928 | 42.07% | 0.025025025025025023 | 1 |
| 13 | 29835.263 | 44859.391 | 74121.215 | 1.609611896368801 | 45.31% | 0.025025025025025023 | 2 |
| 14 | 29818.879 | 46399.487 | 92209.151 | 1.6556025783764186 | 44.22% | 0.025025025025025023 | 2 |
| 15 | 30343.167 | 45514.751 | 78053.375 | 1.5625534754782846 | 47.50% | 0.02502815667626079 | 2 |
| 1 | 29671.423 | 48824.319 | 72941.567 | 1.732607349463694 | 41.77% | 0.02502815667626079 | 2 |
| 2 | 29605.887 | 49446.911 | 74842.111 | 1.6994543350523954 | 43.03% | 0.025025025025025023 | 2 |
| 3 | 29720.575 | 45580.287 | 71237.631 | 1.7015933587591952 | 42.87% | 0.025025025025025023 | 2 |
| 4 | 29753.343 | 48431.103 | 73269.247 | 1.7475786303432697 | 41.37% | 0.025021894157387717 | 1 |
| 5 | 30654.463 | 48332.799 | 94175.231 | 1.653461788562237 | 44.67% | 0.025025025025025023 | 2 |
| 6 | 29474.815 | 47480.831 | 70451.199 | 1.766835471468067 | 40.77% | 0.025025025025025023 | 2 |
| 7 | 29409.279 | 43646.975 | 67698.687 | 1.734744515554947 | 41.93% | 0.02502815667626079 | 2 |
| 8 | 30719.999 | 46432.255 | 76939.263 | 1.5176356968450504 | 49.21% | 0.025025025025025023 | 1 |
| 9 | 29736.959 | 44204.031 | 79691.775 | 1.7572060957832403 | 40.86% | 0.025025025025025023 | 2 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 1264 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=82) |
| 10 | SQLTransientConnectionException | 1311 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=90) |
| 11 | SQLTransientConnectionException | 1261 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=75) |
| 12 | SQLTransientConnectionException | 1169 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=73) |
| 13 | SQLTransientConnectionException | 1247 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=80) |
| 14 | SQLTransientConnectionException | 1227 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=73) |
| 15 | SQLTransientConnectionException | 1322 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=12, active=12, idle=0, waiting=73) |
| 1 | SQLTransientConnectionException | 1162 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=88) |
| 2 | SQLTransientConnectionException | 1200 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=85) |
| 3 | SQLTransientConnectionException | 1194 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=90) |
| 4 | SQLTransientConnectionException | 1153 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=83) |
| 5 | SQLTransientConnectionException | 1248 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=89) |
| 6 | SQLTransientConnectionException | 1137 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=82) |
| 7 | SQLTransientConnectionException | 1171 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=88) |
| 8 | SQLTransientConnectionException | 1375 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=90) |
| 9 | SQLTransientConnectionException | 1135 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=73) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T11:32:01Z → 2026-07-15T11:47:01Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 56 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 40501 / 61214 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2840554392 | Cumulative since stats reset |
| Transactions rolled back | 1184 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5857 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 417212 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T11:32:01Z → 2026-07-15T11:47:01Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 2.0 | 2.9 | 3.9 | 4.8 | 2.9 | 23.5 | 34.3 | 62.8 | 11.8 | 11.8 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.9 | 2.9 | 7.8 | 3.4 | 2.9 | 4.9 | 32.3 | 34.2 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.9 | 2.0 | 9.8 | 3.6 | 2.9 | 5.8 | 32.3 | 37.1 | 11.7 | 11.7 |
| PostgreSQL | db | 1427.8 | 1433.2 | 1520.9 | 1562.2 | 1567.4 | 1599.5 | 1599.5 | 1600.0 | 1600.0 | 1600.0 | 146230.8 | 153992.0 |
| HAProxy | lb | 1.0 | 1.0 | 3.9 | 4.9 | 8.8 | 4.7 | 3.9 | 7.8 | 34.1 | 39.2 | 23.2 | 23.4 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T11:50:58Z*

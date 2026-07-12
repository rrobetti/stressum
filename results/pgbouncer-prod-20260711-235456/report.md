# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T23:06:47Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260711-235456` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.82 RPS (per instance) |
| **Total throughput** | 15.28 RPS (all instances) |
| **p50 latency** | 9775.10 ms |
| **p95 latency** | 25170.00 ms |
| **p99 latency** | 32940.00 ms |
| **p999 latency** | 49545.25 ms |
| **Error rate** | 2.00% (0.02) |
| **Total requests** | 14441 |
| **Failed requests** | 247 |
| **Total successful** | 14194 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.14 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 21872 |
| observed_client_backends_active_max | 33107 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | pgbouncer-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 2.9% / 4.9% |
| OJP proxy-tier host_cpu (avg / peak) | 8.4% / 54.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 9.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.20 MiB / 34.00 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 2.9% / 4.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.20 MiB / 34.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 1.9% / 2.9% / 3.9% |
| HAProxy RSS (avg / peak, summed) | 22.10 MiB / 22.10 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.1% / 1.0% / 3.9% / 5.8% / 6.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 28.0% / 141.1% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 13.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.30 MiB / 56.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.13% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 26 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (25170.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (2.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.50 RPS (all instances) |
| **Achieved throughput** | 15.28 RPS (all instances) |
| **Attempted − achieved gap** | 0.23 RPS (1.46%) |
| **Total attempted ops** | 14404 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 7606.271 | 23592.959 | 31621.119 | 3.836237524714429 | 1.00% | 0.1002004008016032 | 6 |
| 1 | 7294.975 | 19677.183 | 28508.159 | 3.862149324258232 | 0.44% | 0.15022533800701052 | 7 |
| 2 | 9838.591 | 27557.887 | 35586.047 | 3.8117578067732008 | 2.02% | 0.1002004008016032 | 7 |
| 3 | 14360.575 | 29851.647 | 36044.799 | 3.7650504954638206 | 3.38% | 0.15022533800701052 | 6 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 36 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=76) |
| 1 | SQLTransientConnectionException | 16 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=9, active=9, idle=0, waiting=71) |
| 2 | SQLTransientConnectionException | 73 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=10, active=10, idle=0, waiting=38) |
| 3 | SQLTransientConnectionException | 122 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=63) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T23:06:47Z → 2026-07-11T23:21:47Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21872 / 33107 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 428246272 | Cumulative since stats reset |
| Transactions rolled back | 4464 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5474 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 405951 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T23:06:47Z → 2026-07-11T23:21:47Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.4 | 2.0 | 4.8 | 32.4 | 52.2 | 11.4 | 11.3 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 2.6 | 2.0 | 3.9 | 5.9 | 34.3 | 11.4 | 11.3 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 2.6 | 2.0 | 3.9 | 4.9 | 35.0 | 11.4 | 11.4 |
| PostgreSQL | db | 229.2 | 239.5 | 298.0 | 304.7 | 317.7 | 385.6 | 400.0 | 400.0 | 400.0 | 400.0 | 15084.1 | 16985.3 |
| HAProxy | lb | 0.5 | 0.0 | 1.9 | 2.9 | 3.9 | 20.3 | 8.7 | 61.2 | 91.0 | 104.8 | 22.1 | 22.1 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T23:24:55Z*

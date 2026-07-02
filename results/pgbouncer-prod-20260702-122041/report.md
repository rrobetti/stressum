# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T11:32:26Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260702-122041` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.03 RPS (per instance) |
| **Total throughput** | 16.10 RPS (all instances) |
| **p50 latency** | 29921.25 ms |
| **p95 latency** | 39379.00 ms |
| **p99 latency** | 46383.25 ms |
| **p999 latency** | 63332.25 ms |
| **Error rate** | 62.00% (0.62) |
| **Total requests** | 44696 |
| **Failed requests** | 27714 |
| **Total successful** | 16982 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.65 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 25584 |
| observed_client_backends_active_max | 37097 |
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
| OJP proxy-tier host_cpu (avg / peak) | 13.4% / 72.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 12.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 2.9% / 4.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 5.8% |
| HAProxy RSS (avg / peak, summed) | 21.90 MiB / 21.90 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.1% / 1.0% / 3.9% / 5.9% / 10.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.4% / 77.1% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 18.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.20 MiB / 56.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 48 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (39379.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (62.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 40.96 RPS (all instances) |
| **Achieved throughput** | 16.10 RPS (all instances) |
| **Attempted − achieved gap** | 24.86 RPS (60.69%) |
| **Total attempted ops** | 43204 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29917.183 | 39714.815 | 46759.935 | 3.862529952379508 | 63.52% | 0.15037593984962408 | 11 |
| 1 | 29949.951 | 39649.279 | 46727.167 | 3.939302887463519 | 62.81% | 0.15045135406218657 | 11 |
| 2 | 29868.031 | 38699.007 | 45252.607 | 4.35636012450538 | 58.90% | 0.15037593984962408 | 15 |
| 3 | 29949.951 | 39452.671 | 46792.703 | 3.942142728504943 | 62.79% | 0.15030060120240482 | 11 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7095 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=360) |
| 1 | SQLTransientConnectionException | 7018 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=13, active=13, idle=0, waiting=360) |
| 2 | SQLTransientConnectionException | 6582 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=13, active=13, idle=0, waiting=360) |
| 3 | SQLTransientConnectionException | 7019 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=17, active=17, idle=0, waiting=360) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T11:32:26Z → 2026-07-02T11:47:26Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 25584 / 37097 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 521266972 | Cumulative since stats reset |
| Transactions rolled back | 4997 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7849 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 726251 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T11:32:26Z → 2026-07-02T11:47:26Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 5.4 | 2.9 | 32.2 | 33.5 | 35.5 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 5.3 | 2.9 | 32.5 | 34.3 | 41.2 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.9 | 4.9 | 3.0 | 2.0 | 4.9 | 26.3 | 36.6 | 11.4 | 11.4 |
| PostgreSQL | db | 276.5 | 277.7 | 330.8 | 342.0 | 344.9 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 15651.8 | 17574.6 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 2.9 | 5.8 | 5.2 | 3.9 | 14.5 | 35.0 | 36.3 | 21.9 | 21.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T11:50:29Z*

# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T17:51:51Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260711-184013` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.46 RPS (per instance) |
| **Total throughput** | 13.84 RPS (all instances) |
| **p50 latency** | 11483.62 ms |
| **p95 latency** | 38867.00 ms |
| **p99 latency** | 113606.75 ms |
| **p999 latency** | 231080.00 ms |
| **Error rate** | 10.00% (0.10) |
| **Total requests** | 14348 |
| **Failed requests** | 1405 |
| **Total successful** | 12943 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 80 |
| observed_postgres_backends_max_numbackends | 90 |
| observed_postgres_backends_avg_numbackends | 86.06 |
| observed_postgres_backends_median_numbackends | 88 |
| observed_client_backends_active_median | 19456 |
| observed_client_backends_active_max | 28402 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | hikari-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| OJP proxy-tier host_cpu (avg / peak) | N/A% / N/A% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 0% |
| OJP proxy-tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| PgBouncer tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | N/A% / N/A% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 0.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | N/A MiB / 0.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 65 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (38867.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (10.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.41 RPS (all instances) |
| **Achieved throughput** | 13.84 RPS (all instances) |
| **Attempted − achieved gap** | 1.56 RPS (10.14%) |
| **Total attempted ops** | 14402 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 3622.911 | 31899.647 | 106758.143 | 3.49836578938362 | 8.78% | 0.15015015015015015 | 17 |
| 1 | 11952.127 | 44924.927 | 106037.247 | 3.4748402953132973 | 9.45% | 0.15015015015015015 | 16 |
| 2 | 13901.823 | 36143.103 | 104136.703 | 3.505859855444778 | 8.61% | 0.15015015015015015 | 16 |
| 3 | 16457.727 | 42500.095 | 137494.527 | 3.3636111815205663 | 12.32% | 0.1502253380070105 | 16 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 315 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=20, active=20, idle=0, waiting=93) |
| 1 | SQLTransientConnectionException | 339 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=20, active=20, idle=0, waiting=82) |
| 2 | SQLTransientConnectionException | 309 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=20, active=20, idle=0, waiting=65) |
| 3 | SQLTransientConnectionException | 442 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=20, active=20, idle=0, waiting=69) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T17:51:51Z → 2026-07-11T18:06:51Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 88 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 19456 / 28402 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 378029869 | Cumulative since stats reset |
| Transactions rolled back | 4063 | Non-zero → contention or application errors |
| Temp file bytes written | 63 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -27 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4717 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 357053 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T17:51:51Z → 2026-07-11T18:06:51Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 213.1 | 210.9 | 244.0 | 256.3 | 256.3 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 32396.0 | 39468.4 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T18:09:51Z*

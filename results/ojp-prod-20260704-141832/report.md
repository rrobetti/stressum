# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-04T13:30:23Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260704-141832` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.00 RPS (per instance) |
| **Total throughput** | 4.00 RPS (all instances) |
| **p50 latency** | 6.49 ms |
| **p95 latency** | 1591.55 ms |
| **p99 latency** | 5884.43 ms |
| **p999 latency** | 10071.02 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 3604 |
| **Failed requests** | 2 |
| **Total successful** | 3602 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 13.71 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 11087 |
| observed_client_backends_active_max | 16542 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 12 |
| OJP servers | 3 |
| Real DB connections per OJP server | 4 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.4% / 2.0% / 9.8% / 20.5% / 34.3% |
| OJP proxy-tier host_cpu (avg / peak) | 15.0% / 89.1% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 69.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 634.10 MiB / 646.60 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.4% / 2.0% / 9.8% / 20.5% / 34.3% |
| PgBouncer tier RSS (avg / peak, summed) | 634.10 MiB / 646.60 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.4% / 2.0% / 9.8% / 20.5% / 34.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.0% / 89.1% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 69.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 634.10 MiB / 646.60 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.20% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 190 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (1591.55 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 4.00 RPS (all instances) |
| **Achieved throughput** | 4.00 RPS (all instances) |
| **Attempted − achieved gap** | 0.00 RPS (0.06%) |
| **Total attempted ops** | 3603 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 7.619 | 1587.199 | 3774.463 | 1.0003730580993577 | 0.00% | 0.20015012511260633 | 46 |
| 1 | 7.075 | 1684.479 | 6021.119 | 1.0002986463217098 | 0.00% | 0.20020020020020018 | 45 |
| 2 | 5.859 | 1610.751 | 6447.103 | 1.0004330398285606 | 0.00% | 0.2001000500250125 | 48 |
| 3 | 5.415 | 1483.775 | 7294.975 | 0.9982311654654211 | 0.22% | 0.20020020020020018 | 51 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 3 | SQLTransientConnectionException | 1 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLException | 1 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-04T13:30:23Z → 2026-07-04T13:45:23Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 24.3 | 40.0 | 0.060 | 22 | 0 |
| ojp-2 | 25.3 | 40.0 | 0.039 | 19 | 0 |
| ojp-3 | 23.8 | 40.0 | 0.058 | 27 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-04T13:30:23Z → 2026-07-04T13:45:23Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 11087 / 16542 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 91061333 | Cumulative since stats reset |
| Transactions rolled back | 1299 | Non-zero → contention or application errors |
| Temp file bytes written | -2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1381 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 138292 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-04T13:30:23Z → 2026-07-04T13:45:23Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.2 | 1.0 | 3.9 | 13.7 | 30.8 | 5.5 | 3.9 | 17.6 | 35.3 | 64.4 | 211.4 | 214.1 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.1 | 1.0 | 3.9 | 7.8 | 16.6 | 4.4 | 3.9 | 6.9 | 33.5 | 43.1 | 211.5 | 213.3 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.2 | 1.0 | 3.9 | 15.4 | 21.6 | 5.4 | 3.9 | 18.7 | 34.5 | 50.7 | 211.2 | 219.2 |
| PostgreSQL | db | 28.9 | 0.7 | 170.9 | 263.3 | 316.3 | 128.0 | 85.0 | 396.9 | 400.0 | 400.0 | 3810.8 | 8983.4 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-04T13:47:50Z*

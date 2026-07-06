# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-04T16:35:05Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260704-172311` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.00 RPS (per instance) |
| **Total throughput** | 4.00 RPS (all instances) |
| **p50 latency** | 6.30 ms |
| **p95 latency** | 1383.42 ms |
| **p99 latency** | 5170.68 ms |
| **p999 latency** | 9706.50 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 3604 |
| **Failed requests** | 1 |
| **Total successful** | 3603 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 13.57 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 11127 |
| observed_client_backends_active_max | 16571 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.3% / 2.0% / 9.8% / 17.6% / 24.5% |
| OJP proxy-tier host_cpu (avg / peak) | 13.8% / 71.8% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 55.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 651.20 MiB / 665.70 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.3% / 2.0% / 9.8% / 17.6% / 24.5% |
| PgBouncer tier RSS (avg / peak, summed) | 651.20 MiB / 665.70 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.3% / 2.0% / 9.8% / 17.6% / 24.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 13.8% / 71.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 55.90% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 651.20 MiB / 665.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.20% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 185 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (1383.42 ms) |
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
| **Attempted − achieved gap** | 0.00 RPS (0.03%) |
| **Total attempted ops** | 3603 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 7.699 | 1449.983 | 3733.503 | 1.000404158838865 | 0.00% | 0.20020020020020018 | 48 |
| 1 | 6.435 | 1502.207 | 5021.695 | 1.0003586191276117 | 0.00% | 0.2001000500250125 | 45 |
| 2 | 5.935 | 1409.023 | 6017.023 | 1.000440815764549 | 0.00% | 0.2001000500250125 | 45 |
| 3 | 5.147 | 1172.479 | 5910.527 | 0.9993859328656948 | 0.11% | 0.2001000500250125 | 47 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 3 | SQLException | 1 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-04T16:35:05Z → 2026-07-04T16:50:05Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 28.0 | 48.0 | 0.054 | 16 | 0 |
| ojp-2 | 28.2 | 46.0 | 0.041 | 14 | 0 |
| ojp-3 | 27.2 | 48.0 | 0.059 | 19 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-04T16:35:05Z → 2026-07-04T16:50:05Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 11127 / 16571 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 89007237 | Cumulative since stats reset |
| Transactions rolled back | 1301 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1374 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 137587 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-04T16:35:05Z → 2026-07-04T16:50:05Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.2 | 1.0 | 3.9 | 11.8 | 19.6 | 4.5 | 3.9 | 7.8 | 33.3 | 34.3 | 218.4 | 220.4 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.1 | 1.0 | 3.9 | 9.8 | 15.7 | 3.9 | 3.9 | 6.8 | 12.8 | 19.6 | 215.4 | 217.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.1 | 1.0 | 3.9 | 10.8 | 20.6 | 5.7 | 3.9 | 23.5 | 35.3 | 65.4 | 217.4 | 228.2 |
| PostgreSQL | db | 27.7 | 0.7 | 158.5 | 262.9 | 302.5 | 122.7 | 83.8 | 396.9 | 400.0 | 400.0 | 3793.2 | 8960.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-04T16:52:37Z*

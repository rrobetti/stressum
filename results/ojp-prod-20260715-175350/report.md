# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T17:06:02Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 3 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260715-175350` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 2.39 RPS (per instance) |
| **Total throughput** | 38.27 RPS (all instances) |
| **p50 latency** | 4.71 ms |
| **p95 latency** | 39.32 ms |
| **p99 latency** | 35758.00 ms |
| **p999 latency** | 46639.06 ms |
| **Error rate** | 18.00% (0.18) |
| **Total requests** | 43301 |
| **Failed requests** | 7653 |
| **Total successful** | 35648 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 56 |
| observed_postgres_backends_avg_numbackends | 53.09 |
| observed_postgres_backends_median_numbackends | 53 |
| observed_client_backends_active_median | 54218 |
| observed_client_backends_active_max | 81756 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 48 |
| OJP servers | 3 |
| Real DB connections per OJP server | 16 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 9.8% / 8.8% / 16.6% / 20.6% / 30.3% |
| OJP proxy-tier host_cpu (avg / peak) | 33.9% / 120.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 58.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 1186.00 MiB / 1196.20 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 9.8% / 8.8% / 16.6% / 20.6% / 30.3% |
| PgBouncer tier RSS (avg / peak, summed) | 1186.00 MiB / 1196.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 9.8% / 8.8% / 16.6% / 20.6% / 30.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 33.9% / 120.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 58.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1186.00 MiB / 1196.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.07% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1286 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (39.32 ms) |
| Error rate | < 0.1% | ❌ FAIL (18.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.40 RPS (all instances) |
| **Achieved throughput** | 38.27 RPS (all instances) |
| **Attempted − achieved gap** | 8.13 RPS (17.51%) |
| **Total attempted ops** | 43209 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.803 | 52.479 | 35356.671 | 2.363802145142392 | 18.69% | 0.06259780932197094 | 73 |
| 10 | 4.303 | 34.335 | 34865.151 | 2.5148136902852447 | 13.41% | 0.06260172780768748 | 74 |
| 11 | 4.775 | 37.983 | 35880.959 | 2.4333615151216037 | 16.22% | 0.06881962328353358 | 87 |
| 12 | 4.503 | 31.455 | 34635.775 | 2.338262149461974 | 19.51% | 0.06258997333150809 | 73 |
| 13 | 4.591 | 36.927 | 35749.887 | 2.4920385755975634 | 14.23% | 0.06881024124817983 | 90 |
| 14 | 4.435 | 32.223 | 35946.495 | 2.2839618002536297 | 21.73% | 0.06257822277847308 | 68 |
| 15 | 5.635 | 37.087 | 38273.023 | 2.4341803411060976 | 15.89% | 0.07505629221916436 | 91 |
| 1 | 4.919 | 57.407 | 35815.423 | 2.400831601723707 | 17.33% | 0.06257039169065198 | 84 |
| 2 | 4.523 | 39.839 | 35323.903 | 2.4101296617407284 | 17.47% | 0.06258605582676179 | 76 |
| 3 | 4.731 | 37.151 | 35454.975 | 2.4207297016654876 | 16.78% | 0.07505629221916438 | 91 |
| 4 | 4.579 | 36.351 | 34439.167 | 2.4351258059055816 | 15.97% | 0.06258605582676179 | 76 |
| 5 | 4.847 | 36.383 | 35422.207 | 2.4241456989206727 | 16.93% | 0.07505629221916436 | 91 |
| 6 | 4.479 | 37.343 | 36241.407 | 2.2080213342022503 | 23.90% | 0.06258605582676179 | 68 |
| 7 | 4.975 | 38.751 | 36667.391 | 2.340896697353662 | 19.22% | 0.06258605582676179 | 87 |
| 8 | 4.603 | 44.095 | 36077.567 | 2.437388838919506 | 15.81% | 0.06257822277847308 | 70 |
| 9 | 4.699 | 39.263 | 35979.263 | 2.336554163520064 | 19.70% | 0.06259389083625437 | 87 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 506 | Client throttle limit reached; request rejected to avoid overloading the database |
| 10 | SQLTransientConnectionException | 363 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 11 | SQLTransientConnectionException | 439 | Client throttle limit reached; request rejected to avoid overloading the database |
| 12 | SQLTransientConnectionException | 528 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 13 | SQLTransientConnectionException | 385 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 14 | SQLTransientConnectionException | 588 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 15 | SQLTransientConnectionException | 430 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 1 | SQLTransientConnectionException | 469 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLTransientConnectionException | 473 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLTransientConnectionException | 454 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 4 | SQLTransientConnectionException | 432 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 5 | SQLTransientConnectionException | 458 | Client throttle limit reached; request rejected to avoid overloading the database |
| 6 | SQLTransientConnectionException | 647 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 7 | SQLTransientConnectionException | 520 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 8 | SQLTransientConnectionException | 428 | Client throttle limit reached; request rejected to avoid overloading the database |
| 9 | SQLTransientConnectionException | 533 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-15T17:06:02Z → 2026-07-15T17:21:02Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 32.4 | 54.0 | 0.374 | 157 | 0 |
| ojp-2 | 31.2 | 54.0 | 0.371 | 152 | 0 |
| ojp-3 | 30.9 | 52.0 | 0.471 | 165 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T17:06:02Z → 2026-07-15T17:21:02Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 53 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 54218 / 81756 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2394984614 | Cumulative since stats reset |
| Transactions rolled back | 1344 | Non-zero → contention or application errors |
| Temp file bytes written | 4 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -4 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4889 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 490215 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T17:06:02Z → 2026-07-15T17:21:02Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 3.1 | 2.9 | 7.8 | 9.8 | 19.6 | 6.1 | 4.9 | 10.8 | 33.4 | 39.1 | 387.7 | 391.6 |
| Proxy (OJP / pgBouncer) | ojp-2 | 3.4 | 2.9 | 7.8 | 10.8 | 13.7 | 13.5 | 6.9 | 37.2 | 44.1 | 77.2 | 405.7 | 409.4 |
| Proxy (OJP / pgBouncer) | ojp-3 | 3.4 | 2.9 | 8.8 | 12.7 | 25.4 | 15.0 | 6.8 | 38.1 | 46.0 | 84.1 | 392.6 | 395.2 |
| PostgreSQL | db | 767.3 | 767.4 | 973.9 | 1115.1 | 1275.0 | 1425.6 | 1480.6 | 1597.8 | 1598.7 | 1599.3 | 20054.4 | 30294.6 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T17:25:06Z*

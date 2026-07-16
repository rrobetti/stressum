# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T18:45:29Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260715-193326` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.02 RPS (per instance) |
| **Total throughput** | 48.31 RPS (all instances) |
| **p50 latency** | 4.27 ms |
| **p95 latency** | 31.71 ms |
| **p99 latency** | 35411.94 ms |
| **p999 latency** | 46110.75 ms |
| **Error rate** | 22.00% (0.22) |
| **Total requests** | 57719 |
| **Failed requests** | 12725 |
| **Total successful** | 44994 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 53.56 |
| observed_postgres_backends_median_numbackends | 53 |
| observed_client_backends_active_median | 63956 |
| observed_client_backends_active_max | 94832 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 11.3% / 10.8% / 18.6% / 23.5% / 34.2% |
| OJP proxy-tier host_cpu (avg / peak) | 35.3% / 138.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 50.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 1209.90 MiB / 1213.30 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 11.3% / 10.8% / 18.6% / 23.5% / 34.2% |
| PgBouncer tier RSS (avg / peak, summed) | 1209.90 MiB / 1213.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 11.3% / 10.8% / 18.6% / 23.5% / 34.2% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 35.3% / 138.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 50.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1209.90 MiB / 1213.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.07% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1615 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (31.71 ms) |
| Error rate | < 0.1% | ❌ FAIL (22.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 61.86 RPS (all instances) |
| **Achieved throughput** | 48.31 RPS (all instances) |
| **Attempted − achieved gap** | 13.55 RPS (21.91%) |
| **Total attempted ops** | 57613 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.299 | 34.559 | 35028.991 | 2.9411261411569427 | 23.72% | 0.07505629221916438 | 93 |
| 10 | 4.231 | 29.935 | 36208.639 | 2.905934846107786 | 24.92% | 0.07505629221916438 | 91 |
| 11 | 4.447 | 27.759 | 35389.439 | 2.980614701997733 | 23.28% | 0.075122073369225 | 107 |
| 12 | 4.039 | 29.807 | 35356.671 | 3.0936390948145482 | 20.32% | 0.07505629221916436 | 97 |
| 13 | 4.551 | 31.407 | 35258.367 | 2.963973354265591 | 23.35% | 0.07514088916718847 | 111 |
| 14 | 4.323 | 30.895 | 35291.135 | 3.038741532589238 | 21.74% | 0.07507507507507508 | 91 |
| 15 | 4.411 | 28.511 | 37191.679 | 2.893663487169605 | 25.06% | 0.07515500985545592 | 109 |
| 1 | 4.359 | 36.639 | 35258.367 | 3.106904135952025 | 19.79% | 0.075122073369225 | 109 |
| 2 | 4.243 | 35.263 | 35880.959 | 3.154536925345128 | 18.46% | 0.07508447002878238 | 100 |
| 3 | 4.179 | 33.791 | 35258.367 | 2.9194663697037644 | 24.76% | 0.07511266900350526 | 104 |
| 4 | 3.863 | 29.055 | 34766.847 | 3.0678049478849907 | 21.01% | 0.06258605582676179 | 87 |
| 5 | 4.119 | 32.895 | 34635.775 | 3.1592805738468464 | 18.10% | 0.07513148009015778 | 112 |
| 6 | 4.043 | 31.279 | 35389.439 | 3.077492752983575 | 20.76% | 0.07507507507507508 | 95 |
| 7 | 4.723 | 30.799 | 35520.511 | 2.9944801321169776 | 22.48% | 0.08140586963436267 | 115 |
| 8 | 4.079 | 31.855 | 34996.223 | 3.0013627925443447 | 22.48% | 0.07505159826718069 | 86 |
| 9 | 4.363 | 32.927 | 35160.063 | 3.0096748776108604 | 22.51% | 0.07513148009015778 | 108 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 855 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 10 | SQLTransientConnectionException | 899 | Client throttle limit reached; request rejected to avoid overloading the database |
| 11 | SQLTransientConnectionException | 840 | Client throttle limit reached; request rejected to avoid overloading the database |
| 12 | SQLTransientConnectionException | 733 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 13 | SQLTransientConnectionException | 842 | Client throttle limit reached; request rejected to avoid overloading the database |
| 14 | SQLTransientConnectionException | 784 | Client throttle limit reached; request rejected to avoid overloading the database |
| 15 | SQLTransientConnectionException | 904 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 1 | SQLTransientConnectionException | 714 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 2 | SQLTransientConnectionException | 666 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 3 | SQLTransientConnectionException | 894 | Client throttle limit reached; request rejected to avoid overloading the database |
| 4 | SQLTransientConnectionException | 758 | Client throttle limit reached; request rejected to avoid overloading the database |
| 5 | SQLTransientConnectionException | 653 | Client throttle limit reached; request rejected to avoid overloading the database |
| 6 | SQLTransientConnectionException | 749 | Client throttle limit reached; request rejected to avoid overloading the database |
| 7 | SQLTransientConnectionException | 811 | Client throttle limit reached; request rejected to avoid overloading the database |
| 8 | SQLTransientConnectionException | 811 | Client throttle limit reached; request rejected to avoid overloading the database |
| 9 | SQLTransientConnectionException | 812 | Client throttle limit reached; request rejected to avoid overloading the database |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-15T18:45:29Z → 2026-07-15T19:00:29Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 32.7 | 56.0 | 0.405 | 169 | 0 |
| ojp-2 | 32.5 | 56.0 | 0.522 | 208 | 0 |
| ojp-3 | 32.4 | 56.0 | 0.519 | 182 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T18:45:29Z → 2026-07-15T19:00:29Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 53 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 63956 / 94832 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2062268668 | Cumulative since stats reset |
| Transactions rolled back | 1657 | Non-zero → contention or application errors |
| Temp file bytes written | 2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6277 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 440826 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T18:45:29Z → 2026-07-15T19:00:29Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 3.6 | 2.9 | 7.8 | 10.8 | 15.7 | 7.3 | 5.9 | 15.7 | 36.3 | 52.0 | 376.7 | 377.8 |
| Proxy (OJP / pgBouncer) | ojp-2 | 3.9 | 2.9 | 8.8 | 11.7 | 15.7 | 13.5 | 6.9 | 37.2 | 51.0 | 77.4 | 400.9 | 402.3 |
| Proxy (OJP / pgBouncer) | ojp-3 | 4.0 | 2.9 | 8.8 | 13.7 | 18.6 | 15.4 | 7.8 | 39.2 | 45.9 | 68.6 | 432.3 | 433.2 |
| PostgreSQL | db | 726.7 | 712.5 | 944.6 | 1012.3 | 1120.6 | 1420.0 | 1462.3 | 1596.6 | 1597.6 | 1597.9 | 24914.3 | 35527.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T19:04:34Z*

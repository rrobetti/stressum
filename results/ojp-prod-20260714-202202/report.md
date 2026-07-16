# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-14T19:34:04Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260714-202202` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.95 RPS (per instance) |
| **Total throughput** | 15.21 RPS (all instances) |
| **p50 latency** | 6.55 ms |
| **p95 latency** | 6555.12 ms |
| **p99 latency** | 29653.94 ms |
| **p999 latency** | 49338.38 ms |
| **Error rate** | 2.00% (0.02) |
| **Total requests** | 14452 |
| **Failed requests** | 285 |
| **Total successful** | 14167 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 51.83 |
| observed_postgres_backends_median_numbackends | 50 |
| observed_client_backends_active_median | 31037 |
| observed_client_backends_active_max | 47135 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.9% / 5.9% / 14.7% / 24.4% / 46.8% |
| OJP proxy-tier host_cpu (avg / peak) | 18.7% / 88.1% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 103.50% |
| OJP proxy-tier RSS (avg / peak, summed) | 1124.10 MiB / 1146.50 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.9% / 5.9% / 14.7% / 24.4% / 46.8% |
| PgBouncer tier RSS (avg / peak, summed) | 1124.10 MiB / 1146.50 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.9% / 5.9% / 14.7% / 24.4% / 46.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.7% / 88.1% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 103.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1124.10 MiB / 1146.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.05% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 649 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (6555.12 ms) |
| Error rate | < 0.1% | ❌ FAIL (2.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.47 RPS (all instances) |
| **Achieved throughput** | 15.21 RPS (all instances) |
| **Attempted − achieved gap** | 0.27 RPS (1.73%) |
| **Total attempted ops** | 14408 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.075 | 5464.063 | 21463.039 | 0.9543049997423698 | 1.55% | 0.050043788314775434 | 35 |
| 10 | 10.223 | 7487.487 | 34930.687 | 0.9526331425914205 | 2.10% | 0.050031269543464665 | 34 |
| 11 | 6.079 | 2408.447 | 31801.343 | 0.9450981911810928 | 2.88% | 0.050050050050050046 | 44 |
| 12 | 5.423 | 2633.727 | 32636.927 | 0.9436727227051522 | 2.77% | 0.03754458434073752 | 34 |
| 13 | 6.695 | 7770.111 | 32342.015 | 0.950619242162482 | 1.88% | 0.050050050050050046 | 51 |
| 14 | 6.203 | 5808.127 | 28852.223 | 0.9463255316911761 | 2.33% | 0.05004065823044251 | 39 |
| 15 | 6.263 | 4083.711 | 32735.231 | 0.9494038777012801 | 2.43% | 0.050043788314775434 | 42 |
| 1 | 6.687 | 7585.791 | 21528.575 | 0.9533543472099355 | 1.66% | 0.050050050050050046 | 41 |
| 2 | 6.743 | 6746.111 | 25149.439 | 0.9548331724063941 | 1.44% | 0.05003439884478712 | 35 |
| 3 | 6.475 | 8503.295 | 28393.471 | 0.952674192935835 | 1.66% | 0.050050050050050046 | 44 |
| 4 | 6.799 | 8306.687 | 29999.103 | 0.9520109218299218 | 1.77% | 0.050031269543464665 | 39 |
| 5 | 6.175 | 5431.295 | 25870.335 | 0.9465038181001476 | 1.88% | 0.050043788314775434 | 46 |
| 6 | 6.035 | 9322.495 | 31358.975 | 0.9507848520401233 | 1.44% | 0.050043788314775434 | 36 |
| 7 | 6.567 | 8871.935 | 30162.943 | 0.9547849581003331 | 1.77% | 0.050050050050050046 | 48 |
| 8 | 6.363 | 7266.303 | 33062.911 | 0.9526341680274444 | 2.10% | 0.03754693366708385 | 37 |
| 9 | 6.071 | 7192.575 | 34177.023 | 0.9475652066034386 | 1.88% | 0.050043788314775434 | 44 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 14 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 10 | SQLTransientConnectionException | 19 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 11 | SQLTransientConnectionException | 26 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 12 | SQLTransientConnectionException | 25 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 13 | SQLTransientConnectionException | 17 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 14 | SQLTransientConnectionException | 21 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
| 15 | SQLTransientConnectionException | 22 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 1 | SQLTransientConnectionException | 15 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 2 | SQLTransientConnectionException | 13 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 3 | SQLTransientConnectionException | 15 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 4 | SQLTransientConnectionException | 16 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 5 | SQLTransientConnectionException | 17 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 6 | SQLTransientConnectionException | 13 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 7 | SQLTransientConnectionException | 16 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 8 | SQLTransientConnectionException | 19 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 9 | SQLTransientConnectionException | 17 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-14T19:34:04Z → 2026-07-14T19:49:04Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 32.0 | 52.0 | 0.113 | 71 | 0 |
| ojp-2 | 31.8 | 50.0 | 0.122 | 77 | 0 |
| ojp-3 | 31.2 | 52.0 | 0.189 | 90 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-14T19:34:04Z → 2026-07-14T19:49:04Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 50 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 31037 / 47135 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1263623207 | Cumulative since stats reset |
| Transactions rolled back | 585 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1874 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 189122 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-14T19:34:04Z → 2026-07-14T19:49:04Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.4 | 1.9 | 5.9 | 12.7 | 31.3 | 5.9 | 4.9 | 8.8 | 19.6 | 34.3 | 353.2 | 359.8 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.1 | 2.0 | 4.9 | 13.7 | 28.4 | 7.4 | 4.9 | 33.3 | 38.1 | 77.4 | 378.9 | 384.2 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.5 | 1.9 | 5.9 | 15.6 | 43.8 | 5.9 | 4.9 | 9.8 | 20.5 | 48.7 | 392.0 | 402.5 |
| PostgreSQL | db | 390.0 | 389.2 | 931.3 | 1111.9 | 1160.0 | 1095.7 | 1123.8 | 1595.9 | 1597.3 | 1598.0 | 19653.4 | 62764.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-14T19:53:06Z*

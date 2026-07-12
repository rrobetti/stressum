# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T04:21:06Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260712-050916` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.44 RPS (per instance) |
| **Total throughput** | 17.76 RPS (all instances) |
| **p50 latency** | 7.23 ms |
| **p95 latency** | 4833.27 ms |
| **p99 latency** | 22331.38 ms |
| **p999 latency** | 34713.50 ms |
| **Error rate** | 44.00% (0.44) |
| **Total requests** | 28869 |
| **Failed requests** | 12677 |
| **Total successful** | 16192 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 16.72 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 26464 |
| observed_client_backends_active_max | 39525 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.4% / 4.9% / 12.7% / 24.5% / 32.3% |
| OJP proxy-tier host_cpu (avg / peak) | 14.9% / 60.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 71.40% |
| OJP proxy-tier RSS (avg / peak, summed) | 673.10 MiB / 675.80 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.4% / 4.9% / 12.7% / 24.5% / 32.3% |
| PgBouncer tier RSS (avg / peak, summed) | 673.10 MiB / 675.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.4% / 4.9% / 12.7% / 24.5% / 32.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.9% / 60.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 71.40% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 673.10 MiB / 675.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.35% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 869 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4833.27 ms) |
| Error rate | < 0.1% | ❌ FAIL (44.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 31.60 RPS (all instances) |
| **Achieved throughput** | 17.76 RPS (all instances) |
| **Attempted − achieved gap** | 13.83 RPS (43.78%) |
| **Total attempted ops** | 28803 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 7.447 | 4251.647 | 21315.583 | 4.447446754758845 | 43.90% | 0.35035035035035034 | 220 |
| 1 | 7.183 | 4866.047 | 22478.847 | 4.655730470128278 | 40.99% | 0.35017508754377186 | 232 |
| 2 | 6.583 | 4939.775 | 21905.407 | 4.507121273700765 | 43.39% | 0.3498250874562719 | 204 |
| 3 | 7.699 | 5275.647 | 23625.727 | 4.152038924272273 | 47.37% | 0.35052578868302453 | 213 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 3169 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLTransientConnectionException | 2960 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLTransientConnectionException | 3128 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 3 | SQLTransientConnectionException | 3420 | Client throttle limit reached; request rejected to avoid overloading the database |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-12T04:21:06Z → 2026-07-12T04:36:06Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 24.2 | 40.0 | 0.544 | 93 | 0 |
| ojp-2 | 25.3 | 40.0 | 0.480 | 105 | 0 |
| ojp-3 | 29.3 | 48.0 | 0.140 | 60 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T04:21:06Z → 2026-07-12T04:36:06Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 26464 / 39525 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 470877310 | Cumulative since stats reset |
| Transactions rolled back | 5345 | Non-zero → contention or application errors |
| Temp file bytes written | 2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7228 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 539414 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T04:21:06Z → 2026-07-12T04:36:06Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.9 | 1.0 | 5.9 | 9.8 | 22.5 | 4.6 | 3.9 | 7.9 | 14.7 | 36.3 | 221.1 | 221.7 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.0 | 1.0 | 6.8 | 11.8 | 27.4 | 6.1 | 4.0 | 15.7 | 35.3 | 51.5 | 222.5 | 223.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 4.9 | 10.8 | 21.5 | 4.5 | 3.9 | 7.8 | 20.5 | 37.1 | 229.5 | 231.0 |
| PostgreSQL | db | 170.2 | 164.0 | 273.0 | 295.2 | 301.0 | 381.1 | 399.6 | 400.0 | 400.0 | 400.0 | 6729.9 | 9908.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T04:38:57Z*

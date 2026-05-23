# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-23T03:49:55Z |
| **Duration** | 1800 s |
| **Instances**| 4 |
| **Target RPS**| 5 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260523-043757` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.26 RPS (per instance) |
| **Total throughput** | 1.02 RPS (all instances) |
| **p50 latency** | 12.32 ms |
| **p95 latency** | 29773.75 ms |
| **p99 latency** | 59555.75 ms |
| **p999 latency** | 63799.50 ms |
| **Error rate** | 94.00% (0.94) |
| **Total requests** | 36021 |
| **Failed requests** | 33716 |
| **Total successful** | 2305 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 23 |
| observed_postgres_backends_avg_numbackends | 16.58 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 16738 |
| observed_client_backends_active_max | 23943 |
| observed_client_backends_idle_median | 135 |
| observed_client_backends_idle_max | 270 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 15 |
| OJP servers | 3 |
| Real DB connections per OJP server | 5 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 13.5% / 1.0% / 137.0% / 196.5% / 391.4% |
| OJP proxy-tier host_cpu (avg / peak) | 22.8% / 399.1% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 589.30% |
| OJP proxy-tier RSS (avg / peak, summed) | 3419.50 MiB / 3622.90 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 13.5% / 1.0% / 137.0% / 196.5% / 391.4% |
| PgBouncer tier RSS (avg / peak, summed) | 3419.50 MiB / 3622.90 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 13.5% / 1.0% / 137.0% / 196.5% / 391.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 22.8% / 399.1% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 589.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 3419.50 MiB / 3622.90 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.19% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1203 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 150 ms | ❌ FAIL (29773.75 ms) |
| Error rate | < 0.1% | ❌ FAIL (94.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.97 RPS (all instances) |
| **Achieved throughput** | 1.02 RPS (all instances) |
| **Attempted − achieved gap** | 14.94 RPS (93.60%) |
| **Total attempted ops** | 42004 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.66 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 12.127 | 29720.575 | 58884.095 | 0.2807069202459755 | 92.97% | 0.20020020020020018 | 232 |
| 1 | 13.063 | 29720.575 | 59277.311 | 0.24345584912655224 | 93.90% | 0.20020020020020018 | 314 |
| 2 | 12.871 | 29835.263 | 60030.975 | 0.22261374254055494 | 94.43% | 0.20020020020020018 | 344 |
| 3 | 11.215 | 29818.879 | 60030.975 | 0.27538546204226033 | 93.10% | 0.1503006012024048 | 313 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 1214 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 0 | SQLTransientException | 6450 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 706 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: 19ddf4bbc5b8c770 |
| 1 | SQLException | 1232 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 1 | SQLTransientException | 5825 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 1398 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: 1895a7989b63b646 |
| 2 | SQLException | 1283 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 2 | SQLTransientException | 6369 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 854 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: 784b8f8017db5c2a |
| 3 | SQLException | 1224 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 3 | SQLTransientException | 6192 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 969 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-23T03:49:55Z → 2026-05-23T04:19:55Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 906.1 | 980.0 | 2.045 | 156 | 1 |
| ojp-2 | 529.0 | 980.0 | 5.749 | 276 | 2 |
| ojp-3 | 571.5 | 980.0 | 11.595 | 599 | 2 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-23T03:49:55Z → 2026-05-23T04:19:55Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 16738 / 23943 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 135 / 270 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 108766311 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | -3 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -3 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7494 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 752514 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-23T03:49:55Z → 2026-05-23T04:19:55Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.7 | 0.0 | 2.0 | 9.8 | 195.6 | 4.8 | 3.0 | 5.9 | 34.0 | 200.0 | 1179.7 | 1184.6 |
| Proxy (OJP / pgBouncer) | ojp-2 | 4.1 | 0.0 | 3.9 | 189.2 | 196.6 | 7.0 | 2.9 | 7.9 | 193.3 | 200.0 | 1167.9 | 1187.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 8.0 | 0.0 | 43.3 | 192.8 | 197.1 | 11.4 | 3.9 | 38.2 | 198.1 | 200.0 | 1071.9 | 1251.2 |
| PostgreSQL | db | 37.7 | 0.7 | 288.5 | 317.1 | 331.6 | 137.8 | 92.0 | 399.5 | 400.0 | 400.0 | 11849.4 | 32386.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-23T04:23:01Z*

# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-23T04:50:46Z |
| **Duration** | 1800 s |
| **Instances**| 4 |
| **Target RPS**| 5 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-sqs-prod-20260523-053856` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.31 RPS (per instance) |
| **Total throughput** | 5.24 RPS (all instances) |
| **p50 latency** | 11.70 ms |
| **p95 latency** | 950.18 ms |
| **p99 latency** | 15175.70 ms |
| **p999 latency** | 35307.50 ms |
| **Error rate** | 68.00% (0.68) |
| **Total requests** | 36008 |
| **Failed requests** | 24358 |
| **Total successful** | 11650 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 18.48 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 24178 |
| observed_client_backends_active_max | 39816 |
| observed_client_backends_idle_median | 44 |
| observed_client_backends_idle_max | 44 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-sqs-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 15 |
| OJP servers | 3 |
| Real DB connections per OJP server | 5 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 44.0% / 3.9% / 207.7% / 337.7% / 482.3% |
| OJP proxy-tier host_cpu (avg / peak) | 54.7% / 503.8% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 585.50% |
| OJP proxy-tier RSS (avg / peak, summed) | 2749.50 MiB / 3605.90 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 44.0% / 3.9% / 207.7% / 337.7% / 482.3% |
| PgBouncer tier RSS (avg / peak, summed) | 2749.50 MiB / 3605.90 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 44.0% / 3.9% / 207.7% / 337.7% / 482.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 54.7% / 503.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 585.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 2749.50 MiB / 3605.90 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.24% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 3745 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 150 ms | ❌ FAIL (950.18 ms) |
| Error rate | < 0.1% | ❌ FAIL (68.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 16.20 RPS (all instances) |
| **Achieved throughput** | 5.24 RPS (all instances) |
| **Attempted − achieved gap** | 10.96 RPS (67.64%) |
| **Total attempted ops** | 42004 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.62 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 11.599 | 3538.943 | 16121.855 | 1.2846926555931761 | 68.24% | 0.25419420437214035 | 937 |
| 1 | 11.727 | 107.391 | 16711.679 | 1.3092966820341256 | 67.71% | 0.20030045067601399 | 962 |
| 2 | 11.599 | 61.343 | 14434.303 | 1.3335044108742287 | 67.10% | 0.2508780732563974 | 837 |
| 3 | 11.871 | 93.055 | 13434.879 | 1.3152659069753208 | 67.54% | 0.25012506253126565 | 1009 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 36 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 0 | SQLTransientException | 6086 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 21 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 1895a7989b63b646 |
| 1 | SQLException | 28 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 1 | SQLTransientException | 6037 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 30 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 784b8f8017db5c2a |
| 2 | SQLException | 19 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 2 | SQLTransientException | 5986 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 35 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 784b8f8017db5c2a |
| 3 | SQLException | 36 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 3 | SQLTransientException | 6002 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 42 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-23T04:50:46Z → 2026-05-23T05:20:46Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 432.8 | 641.0 | 17.713 | 904 | 3 |
| ojp-2 | 443.9 | 728.0 | 23.849 | 1299 | 4 |
| ojp-3 | 482.4 | 719.0 | 16.064 | 835 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-23T04:50:46Z → 2026-05-23T05:20:46Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 24178 / 39816 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 44 / 44 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 502670866 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 13174 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 1324755 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-23T04:50:46Z → 2026-05-23T05:20:46Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 13.1 | 1.0 | 131.3 | 188.7 | 195.4 | 16.8 | 3.9 | 143.0 | 194.1 | 199.1 | 907.1 | 1214.3 |
| Proxy (OJP / pgBouncer) | ojp-2 | 18.0 | 1.0 | 154.3 | 192.3 | 195.2 | 21.7 | 3.9 | 163.0 | 197.1 | 199.1 | 933.1 | 1182.5 |
| Proxy (OJP / pgBouncer) | ojp-3 | 13.9 | 1.0 | 127.5 | 171.3 | 194.9 | 17.5 | 3.9 | 136.6 | 180.1 | 199.1 | 909.3 | 1209.1 |
| PostgreSQL | db | 201.1 | 206.2 | 319.9 | 338.2 | 357.2 | 329.9 | 378.8 | 400.0 | 400.0 | 400.0 | 16046.3 | 34720.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-23T05:23:25Z*

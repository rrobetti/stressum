# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-22T16:38:17Z |
| **Duration** | 1800 s |
| **Instances**| 4 |
| **Target RPS**| 5 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-sqs-prod-20260522-172624` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.27 RPS (per instance) |
| **Total throughput** | 5.06 RPS (all instances) |
| **p50 latency** | 11.75 ms |
| **p95 latency** | 682.85 ms |
| **p99 latency** | 16351.23 ms |
| **p999 latency** | 33652.75 ms |
| **Error rate** | 69.00% (0.69) |
| **Total requests** | 36017 |
| **Failed requests** | 24763 |
| **Total successful** | 11254 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 18.77 |
| observed_postgres_backends_median_numbackends | 19 |
| observed_client_backends_active_median | 23347 |
| observed_client_backends_active_max | 39505 |
| observed_client_backends_idle_median | 136 |
| observed_client_backends_idle_max | 139 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-sqs-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 15 |
| OJP servers | 3 |
| Real DB connections per OJP server | 5 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 38.7% / 3.9% / 177.8% / 319.2% / 502.8% |
| OJP proxy-tier host_cpu (avg / peak) | 49.1% / 519.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 587.30% |
| OJP proxy-tier RSS (avg / peak, summed) | 2860.40 MiB / 3617.70 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 38.7% / 3.9% / 177.8% / 319.2% / 502.8% |
| PgBouncer tier RSS (avg / peak, summed) | 2860.40 MiB / 3617.70 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 38.7% / 3.9% / 177.8% / 319.2% / 502.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 49.1% / 519.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 587.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 2860.40 MiB / 3617.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.25% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 3517 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 150 ms | ❌ FAIL (682.85 ms) |
| Error rate | < 0.1% | ❌ FAIL (69.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 16.20 RPS (all instances) |
| **Achieved throughput** | 5.06 RPS (all instances) |
| **Attempted − achieved gap** | 11.13 RPS (68.74%) |
| **Total attempted ops** | 42004 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.60 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 11.623 | 221.439 | 15859.711 | 1.3224000525719286 | 67.37% | 0.250501002004008 | 958 |
| 1 | 11.127 | 101.759 | 18481.151 | 1.277031666873051 | 68.51% | 0.2044468362466006 | 900 |
| 2 | 12.343 | 2306.047 | 16359.423 | 1.1992243429521212 | 70.34% | 0.3003003003003003 | 915 |
| 3 | 11.895 | 102.143 | 14704.639 | 1.2646135117808495 | 68.80% | 0.2500625312656328 | 744 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 60 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 0 | SQLTransientException | 5927 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 79 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 1895a7989b63b646 |
| 1 | SQLException | 94 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 1 | SQLTransientException | 6005 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 71 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLException | 78 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 2 | SQLTransientException | 6175 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 81 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 784b8f8017db5c2a |
| 3 | SQLException | 77 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 3 | SQLTransientException | 6022 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 94 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 784b8f8017db5c2a |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-22T16:38:17Z → 2026-05-22T17:08:17Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 490.6 | 643.0 | 17.556 | 838 | 1 |
| ojp-2 | 457.6 | 794.0 | 13.865 | 581 | 1 |
| ojp-3 | 452.3 | 829.0 | 17.549 | 727 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-22T16:38:17Z → 2026-05-22T17:08:17Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 19 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 23347 / 39505 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 136 / 139 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 490428575 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 13729 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 1134482 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-22T16:38:17Z → 2026-05-22T17:08:17Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 14.3 | 1.0 | 135.4 | 173.5 | 196.8 | 17.7 | 3.9 | 145.3 | 179.4 | 200.0 | 911.1 | 1207.4 |
| Proxy (OJP / pgBouncer) | ojp-2 | 11.3 | 1.0 | 107.1 | 171.4 | 196.5 | 14.7 | 3.9 | 118.8 | 179.2 | 199.1 | 969.5 | 1197.2 |
| Proxy (OJP / pgBouncer) | ojp-3 | 14.0 | 1.0 | 134.5 | 169.7 | 194.0 | 17.9 | 3.9 | 140.8 | 177.3 | 200.0 | 979.8 | 1213.1 |
| PostgreSQL | db | 198.0 | 209.1 | 314.7 | 326.9 | 357.9 | 334.6 | 391.6 | 400.0 | 400.0 | 400.0 | 16024.1 | 31790.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-22T17:10:51Z*

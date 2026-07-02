# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-01T23:34:35Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260702-002242` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.20 RPS (per instance) |
| **Total throughput** | 12.79 RPS (all instances) |
| **p50 latency** | 6.03 ms |
| **p95 latency** | 4696.57 ms |
| **p99 latency** | 11974.65 ms |
| **p999 latency** | 44789.75 ms |
| **Error rate** | 9.00% (0.09) |
| **Total requests** | 14442 |
| **Failed requests** | 1289 |
| **Total successful** | 13153 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 16.14 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 21498 |
| observed_client_backends_active_max | 32289 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.4% / 3.9% / 10.8% / 21.5% / 34.3% |
| OJP proxy-tier host_cpu (avg / peak) | 22.5% / 140.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 70.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 677.90 MiB / 682.80 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.4% / 3.9% / 10.8% / 21.5% / 34.3% |
| PgBouncer tier RSS (avg / peak, summed) | 677.90 MiB / 682.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.4% / 3.9% / 10.8% / 21.5% / 34.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 22.5% / 140.6% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 70.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 677.90 MiB / 682.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.36% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 671 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4696.57 ms) |
| Error rate | < 0.1% | ❌ FAIL (9.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 14.01 RPS (all instances) |
| **Achieved throughput** | 12.79 RPS (all instances) |
| **Attempted − achieved gap** | 1.22 RPS (8.68%) |
| **Total attempted ops** | 14401 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5.875 | 3926.015 | 10780.671 | 3.243275933039276 | 7.89% | 0.35035035035035034 | 161 |
| 1 | 6.079 | 4833.279 | 13369.343 | 3.1493672068733285 | 10.38% | 0.3508771929824561 | 170 |
| 2 | 5.971 | 4784.127 | 11272.191 | 3.2513805503561084 | 7.31% | 0.35052578868302453 | 160 |
| 3 | 6.199 | 5242.879 | 12476.415 | 3.1498556194764618 | 10.12% | 0.40060090135202797 | 180 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 43 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 0 | SQLTransientException | 62 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 180 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 63 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 1 | SQLTransientException | 108 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 204 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e98e4f987f09ed4e |
| 2 | SQLException | 39 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 2 | SQLTransientException | 112 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 113 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e98e4f987f09ed4e |
| 3 | SQLException | 55 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 3 | SQLTransientException | 98 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 212 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-01T23:34:35Z → 2026-07-01T23:49:35Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 29.4 | 45.0 | 0.169 | 80 | 0 |
| ojp-2 | 28.7 | 45.0 | 0.146 | 62 | 0 |
| ojp-3 | 28.2 | 45.0 | 0.131 | 61 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-01T23:34:35Z → 2026-07-01T23:49:35Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21498 / 32289 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 410871428 | Cumulative since stats reset |
| Transactions rolled back | 3936 | Non-zero → contention or application errors |
| Temp file bytes written | -3 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 3 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4694 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 325174 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-01T23:34:35Z → 2026-07-01T23:49:35Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.6 | 1.0 | 4.9 | 13.7 | 29.4 | 8.5 | 3.9 | 33.7 | 36.5 | 86.3 | 226.2 | 227.8 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.5 | 1.0 | 4.9 | 9.8 | 21.6 | 9.4 | 4.9 | 35.6 | 40.0 | 67.3 | 226.6 | 228.2 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.5 | 1.0 | 3.9 | 9.8 | 19.6 | 5.0 | 3.9 | 9.8 | 34.1 | 37.2 | 225.1 | 226.8 |
| PostgreSQL | db | 153.1 | 159.3 | 303.7 | 329.9 | 358.4 | 314.0 | 393.7 | 400.0 | 400.0 | 400.0 | 6441.6 | 10666.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-01T23:52:15Z*

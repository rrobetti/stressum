# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T02:41:51Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260702-033001` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.82 RPS (per instance) |
| **Total throughput** | 7.30 RPS (all instances) |
| **p50 latency** | 8.26 ms |
| **p95 latency** | 1667.07 ms |
| **p99 latency** | 7849.98 ms |
| **p999 latency** | 115818.50 ms |
| **Error rate** | 74.00% (0.74) |
| **Total requests** | 29327 |
| **Failed requests** | 21781 |
| **Total successful** | 7546 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 14.41 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 21463 |
| observed_client_backends_active_max | 28447 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.5% / 2.9% / 16.6% / 34.3% / 51.7% |
| OJP proxy-tier host_cpu (avg / peak) | 22.2% / 111.7% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 118.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 670.00 MiB / 675.50 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.5% / 2.9% / 16.6% / 34.3% / 51.7% |
| PgBouncer tier RSS (avg / peak, summed) | 670.00 MiB / 675.50 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.5% / 2.9% / 16.6% / 34.3% / 51.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 22.2% / 111.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 118.90% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 670.00 MiB / 675.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.30% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 708 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (1667.07 ms) |
| Error rate | < 0.1% | ❌ FAIL (74.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 27.83 RPS (all instances) |
| **Achieved throughput** | 7.30 RPS (all instances) |
| **Attempted − achieved gap** | 20.53 RPS (73.78%) |
| **Total attempted ops** | 28803 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 8.807 | 1563.647 | 6131.711 | 1.5533010983649362 | 77.77% | 0.30060120240480964 | 174 |
| 1 | 8.527 | 1951.743 | 10731.519 | 1.8651623187575763 | 73.29% | 0.3009027081243731 | 165 |
| 2 | 8.199 | 1476.607 | 7192.575 | 1.680478619058639 | 76.54% | 0.300450676014021 | 196 |
| 3 | 7.523 | 1676.287 | 7344.127 | 2.196987744514148 | 69.48% | 0.30075187969924816 | 173 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 518 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 0 | SQLTransientException | 3861 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 1323 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 461 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 1 | SQLTransientException | 3630 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 1271 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 2 | SQLException | 519 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 2 | SQLTransientException | 3707 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 1389 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 5719e1e7b8f36461 |
| 3 | SQLException | 475 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 3 | SQLTransientException | 3275 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 1352 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-02T02:41:51Z → 2026-07-02T02:56:51Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.8 | 43.0 | 0.012 | 4 | 0 |
| ojp-2 | 28.0 | 43.0 | 0.135 | 62 | 0 |
| ojp-3 | 24.9 | 40.0 | 0.522 | 89 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T02:41:51Z → 2026-07-02T02:56:51Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21463 / 28447 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 197152710 | Cumulative since stats reset |
| Transactions rolled back | 4222 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5636 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 556154 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T02:41:51Z → 2026-07-02T02:56:51Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 0.4 | 0.0 | 1.0 | 6.9 | 29.4 | 7.7 | 3.0 | 33.3 | 35.1 | 74.4 | 220.6 | 223.2 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.9 | 1.0 | 6.8 | 19.6 | 41.9 | 7.5 | 3.9 | 34.5 | 39.0 | 57.8 | 226.4 | 228.6 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.2 | 1.0 | 8.8 | 21.5 | 47.6 | 7.4 | 3.9 | 33.5 | 38.4 | 53.9 | 223.0 | 223.7 |
| PostgreSQL | db | 48.2 | 10.2 | 204.0 | 274.2 | 322.1 | 176.3 | 108.4 | 399.6 | 400.0 | 400.0 | 4942.8 | 9288.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T02:59:47Z*

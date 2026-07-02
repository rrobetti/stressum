# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T07:22:45Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260702-081055` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.33 RPS (per instance) |
| **Total throughput** | 17.31 RPS (all instances) |
| **p50 latency** | 6.21 ms |
| **p95 latency** | 4945.93 ms |
| **p99 latency** | 21778.42 ms |
| **p999 latency** | 34582.75 ms |
| **Error rate** | 38.00% (0.38) |
| **Total requests** | 28881 |
| **Failed requests** | 11079 |
| **Total successful** | 17802 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.78 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 25860 |
| observed_client_backends_active_max | 39025 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.3% / 4.9% / 11.7% / 21.6% / 42.1% |
| OJP proxy-tier host_cpu (avg / peak) | 17.1% / 78.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 103.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 671.60 MiB / 674.80 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.3% / 4.9% / 11.7% / 21.6% / 42.1% |
| PgBouncer tier RSS (avg / peak, summed) | 671.60 MiB / 674.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.3% / 4.9% / 11.7% / 21.6% / 42.1% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.1% / 78.3% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 103.90% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 671.60 MiB / 674.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.44% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1101 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4945.93 ms) |
| Error rate | < 0.1% | ❌ FAIL (38.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 28.01 RPS (all instances) |
| **Achieved throughput** | 17.31 RPS (all instances) |
| **Attempted − achieved gap** | 10.70 RPS (38.20%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.343 | 5152.767 | 19890.175 | 4.073080692775857 | 42.34% | 0.40090205473603846 | 289 |
| 1 | 5.939 | 5177.343 | 23019.519 | 4.416902701693227 | 37.01% | 0.4518072289156626 | 262 |
| 2 | 5.959 | 4816.895 | 20758.527 | 4.363014449876777 | 37.69% | 0.4506760140210316 | 289 |
| 3 | 6.611 | 4636.671 | 23445.503 | 4.458278476745166 | 36.40% | 0.4518072289156626 | 261 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 152 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 0 | SQLTransientException | 2705 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 201 | RESOURCE_EXHAUSTED: Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 1 | SQLException | 112 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 1 | SQLTransientException | 2386 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 170 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLException | 109 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 2 | SQLTransientException | 2480 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 130 | RESOURCE_EXHAUSTED: Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 3 | SQLException | 144 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 3 | SQLTransientException | 2226 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 264 | RESOURCE_EXHAUSTED: Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-02T07:22:45Z → 2026-07-02T07:37:45Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 29.1 | 45.0 | 0.390 | 108 | 0 |
| ojp-2 | 28.9 | 45.0 | 0.184 | 82 | 0 |
| ojp-3 | 28.4 | 43.0 | 0.263 | 90 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T07:22:45Z → 2026-07-02T07:37:45Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 25860 / 39025 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 524368201 | Cumulative since stats reset |
| Transactions rolled back | 5477 | Non-zero → contention or application errors |
| Temp file bytes written | 3 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -3 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7683 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 736716 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T07:22:45Z → 2026-07-02T07:37:45Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.9 | 1.0 | 5.9 | 12.7 | 31.4 | 4.7 | 3.9 | 8.9 | 33.5 | 38.0 | 224.5 | 225.4 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.8 | 1.0 | 5.9 | 10.8 | 33.3 | 7.9 | 3.9 | 34.6 | 38.0 | 46.6 | 225.3 | 226.8 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 3.9 | 8.8 | 39.2 | 4.9 | 3.9 | 8.8 | 33.7 | 44.9 | 221.8 | 222.6 |
| PostgreSQL | db | 191.0 | 193.3 | 313.3 | 333.2 | 345.0 | 371.5 | 399.5 | 400.0 | 400.0 | 400.0 | 7119.6 | 10148.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T07:40:27Z*

# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T10:30:21Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260702-111830` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 5.05 RPS (per instance) |
| **Total throughput** | 20.21 RPS (all instances) |
| **p50 latency** | 7.04 ms |
| **p95 latency** | 3974.15 ms |
| **p99 latency** | 20144.12 ms |
| **p999 latency** | 37462.00 ms |
| **Error rate** | 52.00% (0.52) |
| **Total requests** | 43228 |
| **Failed requests** | 22426 |
| **Total successful** | 20802 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.67 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 29660 |
| observed_client_backends_active_max | 44045 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.7% / 4.9% / 11.8% / 19.6% / 29.4% |
| OJP proxy-tier host_cpu (avg / peak) | 18.1% / 84.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 68.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 738.10 MiB / 740.20 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.7% / 4.9% / 11.8% / 19.6% / 29.4% |
| PgBouncer tier RSS (avg / peak, summed) | 738.10 MiB / 740.20 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.7% / 4.9% / 11.8% / 19.6% / 29.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.1% / 84.3% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 68.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 738.10 MiB / 740.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.49% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1370 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (3974.15 ms) |
| Error rate | < 0.1% | ❌ FAIL (52.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 41.98 RPS (all instances) |
| **Achieved throughput** | 20.21 RPS (all instances) |
| **Attempted − achieved gap** | 21.77 RPS (51.86%) |
| **Total attempted ops** | 43203 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 7.727 | 4370.431 | 21463.039 | 4.800472421237055 | 54.57% | 0.450563232235741 | 298 |
| 1 | 6.727 | 4276.223 | 19578.879 | 5.224705934762356 | 50.09% | 0.5017561465127948 | 347 |
| 2 | 6.475 | 3573.759 | 20676.607 | 5.206263065465575 | 50.43% | 0.5002501250625313 | 326 |
| 3 | 7.219 | 3676.159 | 18857.983 | 4.978174482110048 | 52.43% | 0.5017561465127948 | 399 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 289 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 0 | SQLTransientException | 5431 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 177 | RESOURCE_EXHAUSTED: Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 1 | SQLException | 254 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 1 | SQLTransientException | 5005 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 155 | RESOURCE_EXHAUSTED: Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 2 | SQLException | 219 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 2 | SQLTransientException | 5072 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 158 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLException | 274 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 3 | SQLTransientException | 5188 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 204 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-02T10:30:21Z → 2026-07-02T10:45:21Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.2 | 45.0 | 0.318 | 96 | 0 |
| ojp-2 | 28.1 | 45.0 | 0.467 | 121 | 0 |
| ojp-3 | 27.1 | 45.0 | 0.427 | 89 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T10:30:21Z → 2026-07-02T10:45:21Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 29660 / 44045 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 565537989 | Cumulative since stats reset |
| Transactions rolled back | 6328 | Non-zero → contention or application errors |
| Temp file bytes written | -5 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 5 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 10782 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 783765 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T10:30:21Z → 2026-07-02T10:45:21Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.7 | 1.0 | 4.9 | 8.8 | 24.5 | 5.1 | 3.9 | 9.9 | 35.1 | 39.4 | 243.0 | 243.9 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.4 | 2.0 | 6.8 | 8.8 | 23.5 | 7.8 | 4.9 | 34.5 | 38.0 | 60.1 | 246.4 | 247.0 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.8 | 1.0 | 4.9 | 8.8 | 20.6 | 5.6 | 3.9 | 12.8 | 34.3 | 53.9 | 248.7 | 249.3 |
| PostgreSQL | db | 188.3 | 193.9 | 314.1 | 333.6 | 350.1 | 366.6 | 399.5 | 400.0 | 400.0 | 400.0 | 7107.6 | 10226.4 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T10:48:04Z*

# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T16:47:40Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260702-173546` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.80 RPS (per instance) |
| **Total throughput** | 19.18 RPS (all instances) |
| **p50 latency** | 7.76 ms |
| **p95 latency** | 4627.45 ms |
| **p99 latency** | 22786.05 ms |
| **p999 latency** | 34635.75 ms |
| **Error rate** | 54.00% (0.54) |
| **Total requests** | 43276 |
| **Failed requests** | 23469 |
| **Total successful** | 19807 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.98 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 28780 |
| observed_client_backends_active_max | 42449 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.2% / 4.9% / 13.7% / 22.5% / 50.0% |
| OJP proxy-tier host_cpu (avg / peak) | 18.6% / 144.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 108.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 718.20 MiB / 723.50 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.2% / 4.9% / 13.7% / 22.5% / 50.0% |
| PgBouncer tier RSS (avg / peak, summed) | 718.20 MiB / 723.50 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.2% / 4.9% / 13.7% / 22.5% / 50.0% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.6% / 144.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 108.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 718.20 MiB / 723.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.53% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1358 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4627.45 ms) |
| Error rate | < 0.1% | ❌ FAIL (54.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 41.83 RPS (all instances) |
| **Achieved throughput** | 19.18 RPS (all instances) |
| **Attempted − achieved gap** | 22.65 RPS (54.15%) |
| **Total attempted ops** | 43202 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 7.927 | 4980.735 | 23838.719 | 4.696141668550146 | 55.03% | 0.5505505505505506 | 304 |
| 1 | 7.275 | 4513.791 | 21217.279 | 5.209558830678644 | 50.43% | 0.501002004008016 | 357 |
| 2 | 7.659 | 4390.911 | 22429.695 | 4.679556924436298 | 55.32% | 0.5511022044088176 | 311 |
| 3 | 8.199 | 4624.383 | 23658.495 | 4.594972094020644 | 56.13% | 0.500751126690035 | 386 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 279 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 0 | SQLTransientException | 5479 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 191 | RESOURCE_EXHAUSTED: Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 1 | SQLException | 266 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 1 | SQLTransientException | 5031 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 155 | RESOURCE_EXHAUSTED: Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 2 | SQLException | 299 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 2 | SQLTransientException | 5482 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 200 | RESOURCE_EXHAUSTED: Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 3 | SQLException | 283 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 3 | SQLTransientException | 5622 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 182 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-02T16:47:40Z → 2026-07-02T17:02:40Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 25.1 | 40.0 | 0.712 | 135 | 0 |
| ojp-2 | 25.3 | 40.0 | 0.720 | 120 | 0 |
| ojp-3 | 28.5 | 48.0 | 0.131 | 62 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T16:47:40Z → 2026-07-02T17:02:40Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 28780 / 42449 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 525736805 | Cumulative since stats reset |
| Transactions rolled back | 6348 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 3 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 10976 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 776798 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T16:47:40Z → 2026-07-02T17:02:40Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.4 | 2.0 | 7.8 | 14.7 | 41.1 | 5.3 | 3.9 | 10.8 | 20.7 | 43.4 | 226.9 | 230.4 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.3 | 2.0 | 7.8 | 11.7 | 48.0 | 8.4 | 4.9 | 35.3 | 43.6 | 108.7 | 240.3 | 240.8 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 3.9 | 7.8 | 19.6 | 5.2 | 3.9 | 8.8 | 35.6 | 99.0 | 251.0 | 252.3 |
| PostgreSQL | db | 189.4 | 187.6 | 304.2 | 322.0 | 334.3 | 373.3 | 399.5 | 400.0 | 400.0 | 400.0 | 7216.1 | 10951.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T17:05:25Z*

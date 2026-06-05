# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-31T01:56:08Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260531-024349` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.99 RPS (per instance) |
| **Total throughput** | 3.98 RPS (all instances) |
| **p50 latency** | 16.98 ms |
| **p95 latency** | 16588.80 ms |
| **p99 latency** | 46792.70 ms |
| **p999 latency** | 63258.50 ms |
| **Error rate** | 63.00% (0.63) |
| **Total requests** | 14422 |
| **Failed requests** | 9084 |
| **Total successful** | 5338 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 20.28 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 18571 |
| observed_client_backends_active_max | 27718 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 2 |
| Configured client pool size (per replica) | 15 |
| OJP servers | 3 |
| Real DB connections per OJP server | 5 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.3% / 2.0% / 10.8% / 17.6% / 20.6% |
| OJP proxy-tier host_cpu (avg / peak) | 18.3% / 73.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 52.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 680.80 MiB / 685.40 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.3% / 2.0% / 10.8% / 17.6% / 20.6% |
| PgBouncer tier RSS (avg / peak, summed) | 680.80 MiB / 685.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.3% / 2.0% / 10.8% / 17.6% / 20.6% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.3% / 73.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 52.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 680.80 MiB / 685.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.38% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 362 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (16588.80 ms) |
| Error rate | < 0.1% | ❌ FAIL (63.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 10.74 RPS (all instances) |
| **Achieved throughput** | 3.98 RPS (all instances) |
| **Attempted − achieved gap** | 6.76 RPS (62.94%) |
| **Total attempted ops** | 19202 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.32 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 17.039 | 19628.031 | 46465.023 | 2.004467140843294 | 62.75% | 0.40060090135202797 | 179 |
| 1 | 16.927 | 13549.567 | 47120.383 | 1.9774369375079222 | 63.22% | 0.35043806951668743 | 183 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 137 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 0 | SQLTransientException | 4273 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 115 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 128 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 1 | SQLTransientException | 4293 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 138 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-31T01:56:08Z → 2026-05-31T02:11:08Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 29.1 | 48.0 | 0.056 | 23 | 0 |
| ojp-2 | 25.8 | 43.0 | 0.053 | 24 | 0 |
| ojp-3 | 29.8 | 50.0 | 0.046 | 19 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-31T01:56:08Z → 2026-05-31T02:11:08Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 18571 / 27718 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 378579314 | Cumulative since stats reset |
| Transactions rolled back | 3144 | Non-zero → contention or application errors |
| Temp file bytes written | -7 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 7 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 8826 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 539896 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-31T01:56:08Z → 2026-05-31T02:11:08Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.2 | 1.0 | 3.9 | 10.8 | 17.6 | 4.8 | 3.9 | 9.8 | 33.5 | 35.5 | 227.2 | 228.8 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.0 | 1.0 | 2.9 | 9.8 | 16.6 | 3.9 | 3.0 | 5.9 | 14.8 | 34.3 | 223.3 | 224.7 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.1 | 1.0 | 3.9 | 10.8 | 18.6 | 10.0 | 4.8 | 33.3 | 39.0 | 52.2 | 230.3 | 231.9 |
| PostgreSQL | db | 170.5 | 183.1 | 221.2 | 236.0 | 240.2 | 399.2 | 400.0 | 400.0 | 400.0 | 400.0 | 14396.5 | 24948.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T02:13:57Z*

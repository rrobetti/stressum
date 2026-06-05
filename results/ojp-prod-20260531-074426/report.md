# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-31T06:56:43Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260531-074426` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.96 RPS (per instance) |
| **Total throughput** | 3.92 RPS (all instances) |
| **p50 latency** | 18.61 ms |
| **p95 latency** | 14397.45 ms |
| **p99 latency** | 48431.10 ms |
| **p999 latency** | 62193.50 ms |
| **Error rate** | 64.00% (0.64) |
| **Total requests** | 14419 |
| **Failed requests** | 9169 |
| **Total successful** | 5250 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 20.41 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 18509 |
| observed_client_backends_active_max | 27585 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.4% / 2.9% / 10.8% / 18.6% / 24.4% |
| OJP proxy-tier host_cpu (avg / peak) | 19.8% / 136.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 53.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 678.90 MiB / 684.00 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.4% / 2.9% / 10.8% / 18.6% / 24.4% |
| PgBouncer tier RSS (avg / peak, summed) | 678.90 MiB / 684.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.4% / 2.9% / 10.8% / 18.6% / 24.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 19.8% / 136.3% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 53.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 678.90 MiB / 684.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.43% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 408 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (14397.45 ms) |
| Error rate | < 0.1% | ❌ FAIL (64.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 10.76 RPS (all instances) |
| **Achieved throughput** | 3.92 RPS (all instances) |
| **Attempted − achieved gap** | 6.84 RPS (63.55%) |
| **Total attempted ops** | 19202 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.35 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 19.807 | 16195.583 | 48234.495 | 1.925191489935036 | 64.32% | 0.4506760140210316 | 203 |
| 1 | 17.407 | 12599.295 | 48627.711 | 1.9982435155953282 | 62.86% | 0.4008016032064128 | 205 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 155 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 0 | SQLTransientException | 4381 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 100 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 1 | SQLException | 135 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 1 | SQLTransientException | 4255 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 143 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-31T06:56:43Z → 2026-05-31T07:11:43Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.1 | 45.0 | 0.052 | 27 | 0 |
| ojp-2 | 26.0 | 45.0 | 0.051 | 25 | 0 |
| ojp-3 | 27.7 | 45.0 | 0.043 | 20 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-31T06:56:43Z → 2026-05-31T07:11:43Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 18509 / 27585 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 344446145 | Cumulative since stats reset |
| Transactions rolled back | 3106 | Non-zero → contention or application errors |
| Temp file bytes written | -7 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 7 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 8488 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 539504 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-31T06:56:43Z → 2026-05-31T07:11:43Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.2 | 1.0 | 2.9 | 11.7 | 19.6 | 4.2 | 3.9 | 6.9 | 21.7 | 36.3 | 223.4 | 225.6 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.1 | 1.0 | 3.9 | 9.8 | 15.7 | 4.5 | 3.9 | 8.9 | 33.3 | 34.3 | 229.0 | 230.3 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.1 | 1.0 | 3.9 | 10.8 | 18.5 | 11.4 | 3.9 | 48.3 | 54.9 | 114.7 | 226.5 | 228.1 |
| PostgreSQL | db | 172.8 | 179.4 | 218.2 | 240.9 | 256.9 | 399.8 | 400.0 | 400.0 | 400.0 | 400.0 | 13822.0 | 22197.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T07:14:34Z*

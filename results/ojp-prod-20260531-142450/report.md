# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-31T13:37:10Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260531-142450` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 2.28 RPS (per instance) |
| **Total throughput** | 4.56 RPS (all instances) |
| **p50 latency** | 21.29 ms |
| **p95 latency** | 15204.35 ms |
| **p99 latency** | 54280.00 ms |
| **p999 latency** | 64160.00 ms |
| **Error rate** | 72.00% (0.72) |
| **Total requests** | 21624 |
| **Failed requests** | 15489 |
| **Total successful** | 6135 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 20.50 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 19348 |
| observed_client_backends_active_max | 28767 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.5% / 2.9% / 8.8% / 18.6% / 27.4% |
| OJP proxy-tier host_cpu (avg / peak) | 12.8% / 61.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 56.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 686.10 MiB / 690.60 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.5% / 2.9% / 8.8% / 18.6% / 27.4% |
| PgBouncer tier RSS (avg / peak, summed) | 686.10 MiB / 690.60 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.5% / 2.9% / 8.8% / 18.6% / 27.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 12.8% / 61.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 56.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 686.10 MiB / 690.60 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.45% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 459 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (15204.35 ms) |
| Error rate | < 0.1% | ❌ FAIL (72.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 16.04 RPS (all instances) |
| **Achieved throughput** | 4.56 RPS (all instances) |
| **Attempted − achieved gap** | 11.49 RPS (71.60%) |
| **Total attempted ops** | 28802 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.32 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 21.631 | 15990.783 | 52232.191 | 2.3059419661353826 | 71.33% | 0.501002004008016 | 229 |
| 1 | 20.943 | 14417.919 | 56328.191 | 2.2505537400347184 | 71.93% | 0.40040040040040037 | 230 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 339 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 0 | SQLTransientException | 7182 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 191 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 314 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 1 | SQLTransientException | 7264 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 199 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: f891f847dfafb38c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-31T13:37:10Z → 2026-05-31T13:52:10Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 28.6 | 45.0 | 0.050 | 24 | 0 |
| ojp-2 | 26.6 | 45.0 | 0.053 | 25 | 0 |
| ojp-3 | 28.8 | 45.0 | 0.053 | 26 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-31T13:37:10Z → 2026-05-31T13:52:10Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 19348 / 28767 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 352208783 | Cumulative since stats reset |
| Transactions rolled back | 4391 | Non-zero → contention or application errors |
| Temp file bytes written | -8 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 8 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 12202 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 539308 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-31T13:37:10Z → 2026-05-31T13:52:10Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.1 | 1.0 | 3.9 | 8.8 | 15.7 | 4.3 | 3.9 | 7.8 | 22.6 | 35.3 | 226.0 | 227.7 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.1 | 1.0 | 2.9 | 9.8 | 22.5 | 4.2 | 3.9 | 6.9 | 32.5 | 53.7 | 236.3 | 237.7 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.3 | 1.0 | 3.9 | 11.8 | 18.6 | 4.6 | 3.9 | 7.8 | 33.3 | 36.5 | 223.8 | 225.2 |
| PostgreSQL | db | 180.7 | 189.5 | 222.7 | 234.8 | 236.0 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 15658.9 | 24588.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T13:55:03Z*

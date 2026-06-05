# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-31T05:16:01Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260531-060338` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.96 RPS (per instance) |
| **Total throughput** | 3.92 RPS (all instances) |
| **p50 latency** | 16.31 ms |
| **p95 latency** | 19456.00 ms |
| **p99 latency** | 45137.95 ms |
| **p999 latency** | 61800.50 ms |
| **Error rate** | 63.00% (0.63) |
| **Total requests** | 14420 |
| **Failed requests** | 9151 |
| **Total successful** | 5269 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 20.20 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 17978 |
| observed_client_backends_active_max | 27080 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.4% / 2.9% / 9.8% / 18.6% / 23.5% |
| OJP proxy-tier host_cpu (avg / peak) | 26.8% / 132.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 59.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 674.60 MiB / 679.70 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.4% / 2.9% / 9.8% / 18.6% / 23.5% |
| PgBouncer tier RSS (avg / peak, summed) | 674.60 MiB / 679.70 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.4% / 2.9% / 9.8% / 18.6% / 23.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 26.8% / 132.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 59.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 674.60 MiB / 679.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.40% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 358 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (19456.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (63.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 10.73 RPS (all instances) |
| **Achieved throughput** | 3.92 RPS (all instances) |
| **Attempted − achieved gap** | 6.80 RPS (63.41%) |
| **Total attempted ops** | 19202 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.34 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 16.463 | 19169.279 | 44171.263 | 1.9865215261264924 | 63.11% | 0.45045045045045046 | 177 |
| 1 | 16.151 | 19742.719 | 46104.575 | 1.9379916938968489 | 63.81% | 0.35035035035035034 | 181 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 184 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 0 | SQLTransientException | 4224 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 142 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 189 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 1 | SQLTransientException | 4260 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 152 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-31T05:16:01Z → 2026-05-31T05:31:01Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 27.6 | 45.0 | 0.045 | 21 | 0 |
| ojp-2 | 27.3 | 45.0 | 0.058 | 24 | 0 |
| ojp-3 | 25.8 | 43.0 | 0.062 | 27 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-31T05:16:01Z → 2026-05-31T05:31:01Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 17978 / 27080 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 370806150 | Cumulative since stats reset |
| Transactions rolled back | 3101 | Non-zero → contention or application errors |
| Temp file bytes written | -5 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 5 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 8603 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 539681 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-31T05:16:01Z → 2026-05-31T05:31:01Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.1 | 1.0 | 3.9 | 8.8 | 19.6 | 4.1 | 3.9 | 6.9 | 11.8 | 23.4 | 225.4 | 227.0 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.1 | 1.0 | 3.9 | 12.7 | 22.4 | 4.5 | 3.9 | 8.8 | 33.3 | 37.4 | 228.0 | 229.6 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.2 | 1.0 | 3.9 | 10.8 | 17.6 | 18.7 | 5.9 | 62.8 | 99.0 | 125.5 | 221.2 | 223.1 |
| PostgreSQL | db | 170.1 | 182.2 | 222.7 | 237.1 | 249.5 | 399.6 | 400.0 | 400.0 | 400.0 | 400.0 | 12913.8 | 22468.6 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T05:33:54Z*

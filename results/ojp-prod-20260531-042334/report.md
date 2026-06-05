# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-31T03:35:59Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260531-042334` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.88 RPS (per instance) |
| **Total throughput** | 3.76 RPS (all instances) |
| **p50 latency** | 18.07 ms |
| **p95 latency** | 20111.40 ms |
| **p99 latency** | 58114.00 ms |
| **p999 latency** | 63537.00 ms |
| **Error rate** | 65.00% (0.65) |
| **Total requests** | 14430 |
| **Failed requests** | 9370 |
| **Total successful** | 5060 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 25 |
| observed_postgres_backends_avg_numbackends | 20.42 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 17182 |
| observed_client_backends_active_max | 26165 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.3% / 2.9% / 9.8% / 18.6% / 27.4% |
| OJP proxy-tier host_cpu (avg / peak) | 18.6% / 89.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 66.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 671.40 MiB / 682.00 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.3% / 2.9% / 9.8% / 18.6% / 27.4% |
| PgBouncer tier RSS (avg / peak, summed) | 671.40 MiB / 682.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.3% / 2.9% / 9.8% / 18.6% / 27.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.6% / 89.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 66.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 671.40 MiB / 682.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.38% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 368 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (20111.40 ms) |
| Error rate | < 0.1% | ❌ FAIL (65.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 10.69 RPS (all instances) |
| **Achieved throughput** | 3.76 RPS (all instances) |
| **Attempted − achieved gap** | 6.93 RPS (64.86%) |
| **Total attempted ops** | 19202 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.29 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 18.095 | 20824.063 | 56197.119 | 1.8371549412954238 | 65.59% | 0.40090205473603846 | 176 |
| 1 | 18.047 | 19398.655 | 60030.975 | 1.919130034087263 | 64.27% | 0.3502627189470611 | 192 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 251 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 0 | SQLTransientException | 4249 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 232 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 1 | SQLException | 233 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 1 | SQLTransientException | 4114 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 291 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-31T03:35:59Z → 2026-05-31T03:50:59Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 29.2 | 45.0 | 0.060 | 25 | 0 |
| ojp-2 | 26.7 | 45.0 | 0.045 | 21 | 0 |
| ojp-3 | 27.4 | 46.0 | 0.064 | 24 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-31T03:35:59Z → 2026-05-31T03:50:59Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 17182 / 26165 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 377814374 | Cumulative since stats reset |
| Transactions rolled back | 3036 | Non-zero → contention or application errors |
| Temp file bytes written | -9 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 8 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 8283 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 539450 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-31T03:35:59Z → 2026-05-31T03:50:59Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.2 | 1.0 | 3.9 | 10.8 | 24.5 | 4.6 | 3.9 | 8.9 | 33.5 | 83.3 | 223.7 | 230.8 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.1 | 1.0 | 2.9 | 7.8 | 21.6 | 3.9 | 3.0 | 5.9 | 18.7 | 33.3 | 224.4 | 226.0 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.2 | 1.0 | 3.9 | 10.8 | 20.6 | 10.5 | 3.9 | 36.3 | 49.0 | 51.0 | 223.3 | 225.2 |
| PostgreSQL | db | 170.5 | 185.3 | 218.5 | 228.9 | 239.1 | 399.6 | 400.0 | 400.0 | 400.0 | 400.0 | 15739.4 | 26157.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T03:53:57Z*

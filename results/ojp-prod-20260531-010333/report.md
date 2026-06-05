# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-31T00:15:54Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260531-010333` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.90 RPS (per instance) |
| **Total throughput** | 3.80 RPS (all instances) |
| **p50 latency** | 17.02 ms |
| **p95 latency** | 16314.35 ms |
| **p99 latency** | 51642.50 ms |
| **p999 latency** | 63455.00 ms |
| **Error rate** | 65.00% (0.65) |
| **Total requests** | 14430 |
| **Failed requests** | 9372 |
| **Total successful** | 5058 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 19.99 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 18069 |
| observed_client_backends_active_max | 27101 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.3% / 2.0% / 9.8% / 16.6% / 28.4% |
| OJP proxy-tier host_cpu (avg / peak) | 18.2% / 72.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 55.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 673.60 MiB / 678.80 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.3% / 2.0% / 9.8% / 16.6% / 28.4% |
| PgBouncer tier RSS (avg / peak, summed) | 673.60 MiB / 678.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.3% / 2.0% / 9.8% / 16.6% / 28.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.2% / 72.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 55.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 673.60 MiB / 678.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.38% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 364 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (16314.35 ms) |
| Error rate | < 0.1% | ❌ FAIL (65.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 10.81 RPS (all instances) |
| **Achieved throughput** | 3.80 RPS (all instances) |
| **Attempted − achieved gap** | 7.01 RPS (64.88%) |
| **Total attempted ops** | 19202 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.25 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 17.983 | 15310.847 | 46596.095 | 1.9011278220923231 | 64.95% | 0.40090205473603846 | 169 |
| 1 | 16.047 | 17317.887 | 56688.639 | 1.8954426184539215 | 64.95% | 0.35070140280561124 | 195 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 169 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 0 | SQLTransientException | 4395 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 122 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 1 | SQLException | 174 | Connection admission timeout for hash: Bz-CW6Nt9M8dsxNzyFjXgT2cmBvRoyETe7hUbLGOfMM after 30000ms (phase=admission) |
| 1 | SQLTransientException | 4401 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 111 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-31T00:15:54Z → 2026-05-31T00:30:54Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 28.3 | 46.0 | 0.058 | 23 | 0 |
| ojp-2 | 29.1 | 45.0 | 0.045 | 20 | 0 |
| ojp-3 | 30.2 | 50.0 | 0.039 | 16 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-31T00:15:54Z → 2026-05-31T00:30:54Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 18069 / 27101 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 390683316 | Cumulative since stats reset |
| Transactions rolled back | 3063 | Non-zero → contention or application errors |
| Temp file bytes written | -7 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 7 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 8589 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 539418 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-31T00:15:54Z → 2026-05-31T00:30:54Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.1 | 1.0 | 3.9 | 9.8 | 19.6 | 4.2 | 3.9 | 7.8 | 22.7 | 41.2 | 221.8 | 223.5 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.1 | 1.0 | 3.9 | 9.8 | 17.6 | 4.2 | 3.0 | 7.8 | 31.4 | 34.5 | 224.5 | 226.2 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.2 | 1.0 | 3.9 | 9.8 | 18.6 | 10.2 | 4.0 | 34.5 | 36.5 | 65.0 | 227.3 | 229.1 |
| PostgreSQL | db | 172.7 | 185.3 | 218.2 | 227.5 | 265.8 | 399.2 | 400.0 | 400.0 | 400.0 | 400.0 | 14005.3 | 24214.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T00:33:34Z*

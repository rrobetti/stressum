# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T05:55:15Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260712-064323` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.96 RPS (per instance) |
| **Total throughput** | 15.84 RPS (all instances) |
| **p50 latency** | 5.21 ms |
| **p95 latency** | 4932.60 ms |
| **p99 latency** | 39858.00 ms |
| **p999 latency** | 127352.75 ms |
| **Error rate** | 51.00% (0.51) |
| **Total requests** | 29052 |
| **Failed requests** | 14759 |
| **Total successful** | 14293 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.26 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 24152 |
| observed_client_backends_active_max | 35689 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 13.7% / 20.6% / 46.9% |
| OJP proxy-tier host_cpu (avg / peak) | 29.2% / 168.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 96.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 664.40 MiB / 667.60 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 13.7% / 20.6% / 46.9% |
| PgBouncer tier RSS (avg / peak, summed) | 664.40 MiB / 667.60 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.8% / 3.9% / 13.7% / 20.6% / 46.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 29.2% / 168.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 96.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 664.40 MiB / 667.60 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.36% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 973 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4932.60 ms) |
| Error rate | < 0.1% | ❌ FAIL (51.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 31.93 RPS (all instances) |
| **Achieved throughput** | 15.84 RPS (all instances) |
| **Attempted − achieved gap** | 16.09 RPS (50.38%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.903 | 4612.095 | 33128.447 | 4.531230635766514 | 43.24% | 0.35070140280561124 | 252 |
| 1 | 5.327 | 5361.663 | 39878.655 | 4.019974421372365 | 50.33% | 0.37581485147967836 | 245 |
| 2 | 5.099 | 4444.159 | 32522.239 | 3.864392149485135 | 52.10% | 0.35070140280561124 | 261 |
| 3 | 5.499 | 5312.511 | 53903.359 | 3.427671139120116 | 57.50% | 0.35052578868302453 | 215 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 3119 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLTransientConnectionException | 3669 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLTransientConnectionException | 3798 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLTransientConnectionException | 4173 | Client throttle limit reached; request rejected to avoid overloading the database |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-12T05:55:15Z → 2026-07-12T06:10:15Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.1 | 41.0 | 0.372 | 73 | 0 |
| ojp-2 | 24.4 | 41.0 | 0.210 | 55 | 0 |
| ojp-3 | 26.6 | 41.0 | 0.632 | 120 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T05:55:15Z → 2026-07-12T06:10:15Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 24152 / 35689 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 406303825 | Cumulative since stats reset |
| Transactions rolled back | 4873 | Non-zero → contention or application errors |
| Temp file bytes written | -2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 4 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6366 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 649989 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T05:55:15Z → 2026-07-12T06:10:15Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.4 | 0.0 | 6.9 | 13.7 | 41.1 | 19.6 | 3.9 | 105.4 | 125.0 | 147.1 | 220.4 | 221.7 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.4 | 0.0 | 6.9 | 18.6 | 24.5 | 5.4 | 3.0 | 18.7 | 35.1 | 61.8 | 221.0 | 222.4 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.1 | 1.0 | 6.9 | 10.8 | 30.4 | 4.9 | 3.9 | 9.8 | 15.7 | 37.1 | 223.0 | 223.5 |
| PostgreSQL | db | 127.2 | 124.9 | 259.6 | 288.9 | 305.6 | 337.8 | 394.6 | 400.0 | 400.0 | 400.0 | 6944.3 | 9770.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T06:12:59Z*

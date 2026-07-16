# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T03:50:33Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 2 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260715-043836` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.74 RPS (per instance) |
| **Total throughput** | 27.79 RPS (all instances) |
| **p50 latency** | 5.99 ms |
| **p95 latency** | 46.92 ms |
| **p99 latency** | 36657.12 ms |
| **p999 latency** | 48261.12 ms |
| **Error rate** | 12.00% (0.12) |
| **Total requests** | 28837 |
| **Failed requests** | 3531 |
| **Total successful** | 25306 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 53.53 |
| observed_postgres_backends_median_numbackends | 54 |
| observed_client_backends_active_median | 42744 |
| observed_client_backends_active_max | 64816 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 48 |
| OJP servers | 3 |
| Real DB connections per OJP server | 16 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 7.9% / 6.8% / 14.7% / 20.6% / 32.3% |
| OJP proxy-tier host_cpu (avg / peak) | 17.5% / 58.8% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 61.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 1164.80 MiB / 1174.40 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 7.9% / 6.8% / 14.7% / 20.6% / 32.3% |
| PgBouncer tier RSS (avg / peak, summed) | 1164.80 MiB / 1174.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 7.9% / 6.8% / 14.7% / 20.6% / 32.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.5% / 58.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 61.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1164.80 MiB / 1174.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.06% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 958 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (46.92 ms) |
| Error rate | < 0.1% | ❌ FAIL (12.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 31.64 RPS (all instances) |
| **Achieved throughput** | 27.79 RPS (all instances) |
| **Attempted − achieved gap** | 3.86 RPS (12.18%) |
| **Total attempted ops** | 28809 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.047 | 54.655 | 34471.935 | 1.7664680587643566 | 11.27% | 0.06256256256256257 | 53 |
| 10 | 6.323 | 43.935 | 37257.215 | 1.652323731913232 | 16.87% | 0.06254691018263697 | 53 |
| 11 | 6.111 | 45.727 | 39124.991 | 1.8197694228339978 | 7.88% | 0.06256256256256257 | 67 |
| 12 | 5.335 | 37.855 | 36339.711 | 1.752454262597005 | 11.76% | 0.06257039169065198 | 54 |
| 13 | 5.891 | 51.807 | 39124.991 | 1.7336457576473654 | 12.92% | 0.06256256256256257 | 64 |
| 14 | 5.723 | 36.895 | 36110.335 | 1.673988997306918 | 15.36% | 0.06257039169065198 | 51 |
| 15 | 6.019 | 34.111 | 37453.823 | 1.630643409674276 | 17.30% | 0.06256256256256257 | 68 |
| 1 | 6.727 | 68.863 | 35946.495 | 1.7581730086610818 | 12.04% | 0.0625782227784731 | 64 |
| 2 | 6.951 | 64.927 | 35979.263 | 1.8433289977945302 | 5.89% | 0.06257039169065198 | 60 |
| 3 | 5.659 | 48.543 | 35323.903 | 1.7945217178164508 | 10.21% | 0.06255864897801593 | 67 |
| 4 | 5.963 | 44.639 | 35913.727 | 1.82263664599995 | 7.21% | 0.06257039169065198 | 58 |
| 5 | 6.107 | 49.119 | 38174.719 | 1.725420687542397 | 12.53% | 0.06256647712660728 | 63 |
| 6 | 5.499 | 45.919 | 36241.407 | 1.7237676162992417 | 13.20% | 0.06257039169065198 | 54 |
| 7 | 5.863 | 47.519 | 37322.751 | 1.6679380498914855 | 15.43% | 0.06255473539346929 | 62 |
| 8 | 5.451 | 37.471 | 36241.407 | 1.7385576864162735 | 11.82% | 0.06257039169065198 | 54 |
| 9 | 6.187 | 38.687 | 35487.743 | 1.6817125185331028 | 14.21% | 0.06255473539346929 | 66 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 203 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 10 | SQLTransientConnectionException | 304 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 11 | SQLTransientConnectionException | 142 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 12 | SQLTransientConnectionException | 212 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 13 | SQLTransientConnectionException | 233 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 14 | SQLTransientConnectionException | 277 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 15 | SQLTransientConnectionException | 312 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 1 | SQLTransientConnectionException | 217 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 2 | SQLTransientConnectionException | 106 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 3 | SQLTransientConnectionException | 184 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 4 | SQLTransientConnectionException | 130 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 5 | SQLTransientConnectionException | 226 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 6 | SQLTransientConnectionException | 238 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 7 | SQLTransientConnectionException | 278 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 8 | SQLTransientConnectionException | 213 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 9 | SQLTransientConnectionException | 256 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-15T03:50:33Z → 2026-07-15T04:05:33Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 32.0 | 52.0 | 0.299 | 133 | 0 |
| ojp-2 | 30.0 | 50.0 | 0.267 | 122 | 0 |
| ojp-3 | 32.0 | 52.0 | 0.316 | 124 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T03:50:33Z → 2026-07-15T04:05:33Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 54 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 42744 / 64816 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1926765203 | Cumulative since stats reset |
| Transactions rolled back | 1003 | Non-zero → contention or application errors |
| Temp file bytes written | -11 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 11 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3371 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 339235 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T03:50:33Z → 2026-07-15T04:05:33Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.6 | 2.0 | 6.9 | 10.8 | 17.6 | 5.6 | 4.9 | 10.8 | 28.5 | 39.2 | 384.5 | 387.8 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.7 | 2.0 | 6.8 | 10.8 | 25.4 | 6.1 | 4.9 | 11.8 | 35.2 | 38.2 | 392.8 | 395.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.7 | 2.0 | 5.9 | 11.7 | 18.6 | 6.1 | 4.9 | 10.8 | 33.3 | 37.2 | 387.5 | 391.5 |
| PostgreSQL | db | 646.6 | 649.2 | 876.7 | 972.8 | 999.5 | 1523.4 | 1563.3 | 1596.8 | 1598.2 | 1598.5 | 23333.6 | 39135.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T04:09:21Z*

# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T02:11:36Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 2 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260715-025938` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.73 RPS (per instance) |
| **Total throughput** | 27.62 RPS (all instances) |
| **p50 latency** | 5.94 ms |
| **p95 latency** | 48.30 ms |
| **p99 latency** | 36136.88 ms |
| **p999 latency** | 48246.75 ms |
| **Error rate** | 13.00% (0.13) |
| **Total requests** | 28838 |
| **Failed requests** | 3754 |
| **Total successful** | 25084 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 58 |
| observed_postgres_backends_avg_numbackends | 53.46 |
| observed_postgres_backends_median_numbackends | 53 |
| observed_client_backends_active_median | 43578 |
| observed_client_backends_active_max | 65291 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 7.8% / 6.8% / 14.7% / 19.6% / 28.4% |
| OJP proxy-tier host_cpu (avg / peak) | 18.5% / 84.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 66.50% |
| OJP proxy-tier RSS (avg / peak, summed) | 1112.00 MiB / 1124.40 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 7.8% / 6.8% / 14.7% / 19.6% / 28.4% |
| PgBouncer tier RSS (avg / peak, summed) | 1112.00 MiB / 1124.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 7.8% / 6.8% / 14.7% / 19.6% / 28.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.5% / 84.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 66.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1112.00 MiB / 1124.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.06% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 939 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (48.30 ms) |
| Error rate | < 0.1% | ❌ FAIL (13.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 31.72 RPS (all instances) |
| **Achieved throughput** | 27.62 RPS (all instances) |
| **Attempted − achieved gap** | 4.11 RPS (12.94%) |
| **Total attempted ops** | 28808 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5.947 | 65.407 | 35487.743 | 1.6880835459774057 | 13.98% | 0.06256256256256257 | 52 |
| 10 | 5.375 | 41.055 | 38338.559 | 1.6713061213240359 | 15.87% | 0.06254691018263697 | 55 |
| 11 | 6.019 | 49.919 | 37355.519 | 1.6938480014027177 | 14.81% | 0.0625782227784731 | 63 |
| 12 | 5.619 | 40.223 | 37093.375 | 1.6463791092784132 | 16.09% | 0.06257039169065198 | 52 |
| 13 | 5.467 | 38.815 | 37421.055 | 1.8296666431245143 | 8.04% | 0.06257039169065198 | 67 |
| 14 | 5.859 | 37.311 | 36339.711 | 1.7249213638789997 | 13.26% | 0.06254691018263699 | 51 |
| 15 | 6.299 | 36.415 | 36274.175 | 1.7520264701631436 | 11.88% | 0.06256256256256257 | 63 |
| 1 | 5.987 | 72.191 | 35618.815 | 1.7727777673590466 | 10.82% | 0.06256256256256257 | 61 |
| 2 | 7.515 | 58.655 | 34177.023 | 1.7662071584376133 | 11.21% | 0.06254691018263697 | 53 |
| 3 | 5.367 | 49.695 | 33587.199 | 1.7493008897363624 | 12.49% | 0.06256256256256257 | 59 |
| 4 | 5.703 | 46.175 | 35946.495 | 1.7431898720778691 | 12.26% | 0.06256256256256257 | 53 |
| 5 | 5.899 | 51.231 | 35258.367 | 1.7158999069323888 | 12.98% | 0.06252735596258802 | 58 |
| 6 | 5.699 | 47.583 | 36700.159 | 1.6945118968397024 | 14.70% | 0.06256256256256257 | 56 |
| 7 | 6.075 | 48.671 | 36732.927 | 1.709399824207528 | 13.98% | 0.06257039169065198 | 66 |
| 8 | 6.075 | 49.727 | 36700.159 | 1.6726904090267984 | 15.76% | 0.06256256256256257 | 56 |
| 9 | 6.151 | 39.711 | 35160.063 | 1.788073549425333 | 10.15% | 0.06258605582676179 | 74 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 252 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 10 | SQLTransientConnectionException | 286 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 11 | SQLTransientConnectionException | 267 | Client throttle limit reached; request rejected to avoid overloading the database |
| 12 | SQLTransientConnectionException | 290 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 13 | SQLTransientConnectionException | 145 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 14 | SQLTransientConnectionException | 239 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 15 | SQLTransientConnectionException | 214 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 1 | SQLTransientConnectionException | 195 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 2 | SQLTransientConnectionException | 202 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 3 | SQLTransientConnectionException | 225 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 4 | SQLTransientConnectionException | 221 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 5 | SQLTransientConnectionException | 234 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 6 | SQLTransientConnectionException | 265 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 7 | SQLTransientConnectionException | 252 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 8 | SQLTransientConnectionException | 284 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 9 | SQLTransientConnectionException | 183 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-15T02:11:36Z → 2026-07-15T02:26:36Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 30.6 | 54.0 | 0.245 | 123 | 0 |
| ojp-2 | 31.0 | 50.0 | 0.279 | 119 | 0 |
| ojp-3 | 31.8 | 54.0 | 0.310 | 123 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T02:11:36Z → 2026-07-15T02:26:36Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 53 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 43578 / 65291 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1894865213 | Cumulative since stats reset |
| Transactions rolled back | 1013 | Non-zero → contention or application errors |
| Temp file bytes written | -7 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 7 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3440 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 346395 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T02:11:36Z → 2026-07-15T02:26:36Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.5 | 2.0 | 5.9 | 9.8 | 21.6 | 6.3 | 4.9 | 12.8 | 36.2 | 65.6 | 379.2 | 381.6 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.7 | 2.0 | 6.8 | 9.8 | 22.5 | 6.1 | 4.9 | 10.7 | 34.4 | 37.2 | 371.4 | 377.7 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.8 | 2.0 | 6.8 | 11.7 | 22.4 | 6.5 | 4.9 | 12.7 | 35.2 | 39.2 | 361.4 | 365.1 |
| PostgreSQL | db | 654.6 | 646.9 | 880.1 | 1025.5 | 1080.5 | 1519.9 | 1561.5 | 1597.2 | 1598.0 | 1598.0 | 23591.8 | 40530.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T02:30:19Z*

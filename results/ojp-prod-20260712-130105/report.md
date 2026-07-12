# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T12:12:59Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260712-130105` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.82 RPS (per instance) |
| **Total throughput** | 15.28 RPS (all instances) |
| **p50 latency** | 21.51 ms |
| **p95 latency** | 3782.65 ms |
| **p99 latency** | 6514.70 ms |
| **p999 latency** | 14350.35 ms |
| **Error rate** | 68.00% (0.68) |
| **Total requests** | 43691 |
| **Failed requests** | 29553 |
| **Total successful** | 14138 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 26 |
| observed_postgres_backends_avg_numbackends | 17.58 |
| observed_postgres_backends_median_numbackends | 18 |
| observed_client_backends_active_median | 40676 |
| observed_client_backends_active_max | 64591 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 9.0% / 6.8% / 22.5% / 37.2% / 91.8% |
| OJP proxy-tier host_cpu (avg / peak) | 18.7% / 99.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 139.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 742.30 MiB / 746.70 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 9.0% / 6.8% / 22.5% / 37.2% / 91.8% |
| PgBouncer tier RSS (avg / peak, summed) | 742.30 MiB / 746.70 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 9.0% / 6.8% / 22.5% / 37.2% / 91.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.7% / 99.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 139.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 742.30 MiB / 746.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.39% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1538 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (3782.65 ms) |
| Error rate | < 0.1% | ❌ FAIL (68.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.89 RPS (all instances) |
| **Achieved throughput** | 15.28 RPS (all instances) |
| **Attempted − achieved gap** | 31.61 RPS (67.42%) |
| **Total attempted ops** | 43202 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 23.167 | 4122.623 | 7602.175 | 3.6180893566690466 | 69.35% | 0.3512293025589563 | 389 |
| 1 | 18.623 | 3516.415 | 5550.079 | 4.584958086189084 | 59.58% | 0.4014049172102358 | 407 |
| 2 | 19.119 | 4057.087 | 7225.343 | 3.7707332833197347 | 69.70% | 0.4012036108324975 | 380 |
| 3 | 25.119 | 3434.495 | 5681.151 | 3.3036867818304714 | 71.64% | 0.4006009013520281 | 362 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7508 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLTransientConnectionException | 6319 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 2 | SQLTransientConnectionException | 7921 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLTransientConnectionException | 7805 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-12T12:12:59Z → 2026-07-12T12:27:59Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 30.1 | 48.0 | 0.010 | 3 | 0 |
| ojp-2 | 29.0 | 48.0 | 0.132 | 63 | 0 |
| ojp-3 | 25.4 | 40.0 | 2.279 | 379 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T12:12:59Z → 2026-07-12T12:27:59Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 18 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 40676 / 64591 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 464514045 | Cumulative since stats reset |
| Transactions rolled back | 5038 | Non-zero → contention or application errors |
| Temp file bytes written | 2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7423 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 724704 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T12:12:59Z → 2026-07-12T12:27:59Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 0.5 | 0.0 | 2.0 | 7.8 | 26.4 | 3.7 | 2.9 | 4.9 | 32.5 | 50.7 | 245.6 | 246.0 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.3 | 1.0 | 9.8 | 15.7 | 32.3 | 5.8 | 3.9 | 15.8 | 33.5 | 38.4 | 256.2 | 259.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 6.4 | 4.9 | 15.7 | 30.4 | 81.0 | 9.6 | 7.9 | 20.8 | 43.1 | 82.8 | 240.5 | 241.6 |
| PostgreSQL | db | 90.4 | 70.5 | 250.7 | 296.8 | 329.6 | 354.1 | 395.9 | 400.0 | 400.0 | 400.0 | 4996.0 | 9124.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T12:31:12Z*

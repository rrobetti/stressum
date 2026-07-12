# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T01:12:35Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260712-020043` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.66 RPS (per instance) |
| **Total throughput** | 14.62 RPS (all instances) |
| **p50 latency** | 6.45 ms |
| **p95 latency** | 5654.52 ms |
| **p99 latency** | 16832.53 ms |
| **p999 latency** | 31977.50 ms |
| **Error rate** | 8.00% (0.08) |
| **Total requests** | 14452 |
| **Failed requests** | 1151 |
| **Total successful** | 13301 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 16.40 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 23734 |
| observed_client_backends_active_max | 35158 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.9% / 3.9% / 11.8% / 19.6% / 28.4% |
| OJP proxy-tier host_cpu (avg / peak) | 15.5% / 70.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 63.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 662.80 MiB / 666.00 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.9% / 3.9% / 11.8% / 19.6% / 28.4% |
| PgBouncer tier RSS (avg / peak, summed) | 662.80 MiB / 666.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.9% / 3.9% / 11.8% / 19.6% / 28.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.5% / 70.6% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 63.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 662.80 MiB / 666.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.29% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 614 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (5654.52 ms) |
| Error rate | < 0.1% | ❌ FAIL (8.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.84 RPS (all instances) |
| **Achieved throughput** | 14.62 RPS (all instances) |
| **Attempted − achieved gap** | 1.21 RPS (7.66%) |
| **Total attempted ops** | 14401 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.199 | 4825.087 | 15818.751 | 3.6895196892106656 | 7.42% | 0.30060120240480964 | 148 |
| 1 | 7.263 | 5881.855 | 16023.551 | 3.6547344427214896 | 7.69% | 0.30060120240480964 | 163 |
| 2 | 6.407 | 5881.855 | 17268.735 | 3.654812096178343 | 7.72% | 0.3006012024048096 | 157 |
| 3 | 5.931 | 6029.311 | 18219.007 | 3.623519716728674 | 9.02% | 0.250501002004008 | 146 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 268 | Connection admission timeout for hash: _R1oo6-0VGP4VoeSd7fpBbwrG_FsZi1RdIyq5wGF_58 after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 278 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLTransientConnectionException | 279 | Timeout waiting for fast operation slot for operation: f891f847dfafb38c |
| 3 | SQLTransientConnectionException | 326 | Connection admission timeout for hash: _R1oo6-0VGP4VoeSd7fpBbwrG_FsZi1RdIyq5wGF_58 after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-12T01:12:35Z → 2026-07-12T01:27:35Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 25.3 | 40.0 | 0.434 | 92 | 0 |
| ojp-2 | 26.6 | 41.0 | 0.383 | 71 | 0 |
| ojp-3 | 26.5 | 40.0 | 0.337 | 80 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T01:12:35Z → 2026-07-12T01:27:35Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 23734 / 35158 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 409894272 | Cumulative since stats reset |
| Transactions rolled back | 3889 | Non-zero → contention or application errors |
| Temp file bytes written | -7 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 7 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4697 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 326053 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T01:12:35Z → 2026-07-12T01:27:35Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.8 | 1.0 | 6.8 | 10.8 | 22.5 | 4.9 | 3.9 | 8.9 | 33.5 | 38.2 | 220.0 | 220.7 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.6 | 1.0 | 4.9 | 10.8 | 21.6 | 5.9 | 3.9 | 16.8 | 37.1 | 52.9 | 223.0 | 224.2 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.5 | 1.0 | 4.9 | 10.8 | 19.6 | 5.0 | 3.9 | 9.8 | 34.3 | 38.2 | 219.8 | 221.1 |
| PostgreSQL | db | 148.9 | 143.4 | 280.2 | 297.4 | 306.3 | 355.9 | 399.3 | 400.0 | 400.0 | 400.0 | 6304.5 | 10318.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T01:30:29Z*

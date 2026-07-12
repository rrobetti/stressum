# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T18:55:14Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260711-194324` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.63 RPS (per instance) |
| **Total throughput** | 14.52 RPS (all instances) |
| **p50 latency** | 6.66 ms |
| **p95 latency** | 5472.23 ms |
| **p99 latency** | 17780.72 ms |
| **p999 latency** | 31338.50 ms |
| **Error rate** | 8.00% (0.08) |
| **Total requests** | 14455 |
| **Failed requests** | 1200 |
| **Total successful** | 13255 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.38 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 22768 |
| observed_client_backends_active_max | 33836 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.9% / 3.9% / 11.8% / 18.6% / 24.5% |
| OJP proxy-tier host_cpu (avg / peak) | 15.4% / 87.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 55.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 672.40 MiB / 675.50 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.9% / 3.9% / 11.8% / 18.6% / 24.5% |
| PgBouncer tier RSS (avg / peak, summed) | 672.40 MiB / 675.50 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.9% / 3.9% / 11.8% / 18.6% / 24.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.4% / 87.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 55.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 672.40 MiB / 675.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.33% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 615 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (5472.23 ms) |
| Error rate | < 0.1% | ❌ FAIL (8.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.78 RPS (all instances) |
| **Achieved throughput** | 14.52 RPS (all instances) |
| **Attempted − achieved gap** | 1.26 RPS (7.98%) |
| **Total attempted ops** | 14402 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.471 | 4956.159 | 18317.311 | 3.6698998041696727 | 7.31% | 0.3006012024048096 | 148 |
| 1 | 6.975 | 5746.687 | 16465.919 | 3.6650449491819193 | 7.68% | 0.3507892978940337 | 161 |
| 2 | 6.463 | 5398.527 | 15925.247 | 3.6200342098701164 | 8.41% | 0.30045067601402103 | 151 |
| 3 | 6.747 | 5787.647 | 20414.463 | 3.567669053510654 | 9.80% | 0.35052578868302453 | 155 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 264 | Connection admission timeout for hash: _R1oo6-0VGP4VoeSd7fpBbwrG_FsZi1RdIyq5wGF_58 after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 278 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLTransientConnectionException | 304 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLTransientConnectionException | 354 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-11T18:55:14Z → 2026-07-11T19:10:14Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 27.4 | 48.0 | 0.136 | 57 | 0 |
| ojp-2 | 25.7 | 40.0 | 0.377 | 91 | 0 |
| ojp-3 | 26.6 | 40.0 | 0.325 | 72 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T18:55:14Z → 2026-07-11T19:10:14Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 22768 / 33836 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 410373222 | Cumulative since stats reset |
| Transactions rolled back | 3830 | Non-zero → contention or application errors |
| Temp file bytes written | -7 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 7 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4612 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 319878 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T18:55:14Z → 2026-07-11T19:10:14Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.6 | 1.0 | 3.9 | 13.7 | 18.6 | 5.0 | 3.9 | 9.8 | 34.3 | 52.2 | 229.3 | 230.8 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.7 | 1.0 | 4.9 | 9.8 | 19.6 | 6.0 | 3.9 | 16.7 | 36.5 | 63.4 | 225.0 | 225.9 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 5.9 | 12.7 | 17.6 | 4.7 | 3.9 | 8.9 | 25.5 | 41.2 | 218.1 | 218.8 |
| PostgreSQL | db | 154.9 | 152.9 | 281.7 | 303.7 | 315.6 | 361.1 | 399.5 | 400.0 | 400.0 | 400.0 | 6263.5 | 10273.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T19:13:07Z*

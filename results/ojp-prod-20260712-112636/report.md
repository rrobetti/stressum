# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T10:38:29Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260712-112636` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.47 RPS (per instance) |
| **Total throughput** | 13.86 RPS (all instances) |
| **p50 latency** | 7.50 ms |
| **p95 latency** | 1557.50 ms |
| **p99 latency** | 4527.10 ms |
| **p999 latency** | 7444.48 ms |
| **Error rate** | 70.00% (0.70) |
| **Total requests** | 43222 |
| **Failed requests** | 30363 |
| **Total successful** | 12859 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 14.70 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 25265 |
| observed_client_backends_active_max | 35717 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.6% / 3.9% / 9.8% / 16.7% / 24.5% |
| OJP proxy-tier host_cpu (avg / peak) | 14.2% / 62.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 58.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 718.10 MiB / 720.00 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.6% / 3.9% / 9.8% / 16.7% / 24.5% |
| PgBouncer tier RSS (avg / peak, summed) | 718.10 MiB / 720.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.6% / 3.9% / 9.8% / 16.7% / 24.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.2% / 62.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 58.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 718.10 MiB / 720.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.34% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 984 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (1557.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (70.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.58 RPS (all instances) |
| **Achieved throughput** | 13.86 RPS (all instances) |
| **Attempted − achieved gap** | 32.72 RPS (70.24%) |
| **Total attempted ops** | 43204 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 7.387 | 1646.591 | 4362.239 | 3.5442209388955637 | 69.52% | 0.3510531594784353 | 235 |
| 1 | 8.067 | 1351.679 | 4243.455 | 3.2393833094117888 | 72.20% | 0.3508771929824561 | 237 |
| 2 | 6.939 | 1625.087 | 4857.855 | 3.6009628450518307 | 69.11% | 0.3012048192771084 | 238 |
| 3 | 7.611 | 1606.655 | 4644.863 | 3.4794395771142668 | 70.17% | 0.3508771929824561 | 274 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7510 | Connection admission timeout for hash: _R1oo6-0VGP4VoeSd7fpBbwrG_FsZi1RdIyq5wGF_58 after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 7801 | Connection admission timeout for hash: _R1oo6-0VGP4VoeSd7fpBbwrG_FsZi1RdIyq5wGF_58 after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 7469 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 3 | SQLTransientConnectionException | 7583 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-12T10:38:29Z → 2026-07-12T10:53:29Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.1 | 40.0 | 0.035 | 6 | 0 |
| ojp-2 | 25.2 | 41.0 | 0.491 | 95 | 0 |
| ojp-3 | 28.5 | 48.0 | 0.176 | 77 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T10:38:29Z → 2026-07-12T10:53:29Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 25265 / 35717 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 299979894 | Cumulative since stats reset |
| Transactions rolled back | 5523 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 10298 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 720751 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T10:38:29Z → 2026-07-12T10:53:29Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 0.6 | 0.0 | 2.0 | 7.8 | 21.5 | 4.0 | 3.0 | 4.9 | 32.5 | 47.8 | 236.9 | 237.1 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.2 | 2.0 | 5.9 | 8.8 | 16.6 | 5.5 | 4.0 | 9.8 | 34.3 | 41.2 | 235.7 | 236.3 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.0 | 2.0 | 4.9 | 9.8 | 20.6 | 5.0 | 3.9 | 7.8 | 34.3 | 51.0 | 245.5 | 246.6 |
| PostgreSQL | db | 93.2 | 73.2 | 276.4 | 330.5 | 351.6 | 212.2 | 205.4 | 400.0 | 400.0 | 400.0 | 5519.6 | 9353.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T10:56:35Z*

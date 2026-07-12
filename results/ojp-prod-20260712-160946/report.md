# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T15:21:41Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260712-160946` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.67 RPS (per instance) |
| **Total throughput** | 14.66 RPS (all instances) |
| **p50 latency** | 18.67 ms |
| **p95 latency** | 3620.88 ms |
| **p99 latency** | 6300.65 ms |
| **p999 latency** | 11259.88 ms |
| **Error rate** | 69.00% (0.69) |
| **Total requests** | 43697 |
| **Failed requests** | 30274 |
| **Total successful** | 13423 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 28 |
| observed_postgres_backends_avg_numbackends | 18.47 |
| observed_postgres_backends_median_numbackends | 19 |
| observed_client_backends_active_median | 36108 |
| observed_client_backends_active_max | 58407 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.0% / 6.8% / 18.6% / 32.2% / 69.4% |
| OJP proxy-tier host_cpu (avg / peak) | 17.2% / 78.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 111.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 733.50 MiB / 736.10 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.0% / 6.8% / 18.6% / 32.2% / 69.4% |
| PgBouncer tier RSS (avg / peak, summed) | 733.50 MiB / 736.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.0% / 6.8% / 18.6% / 32.2% / 69.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.2% / 78.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 111.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 733.50 MiB / 736.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.40% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1495 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (3620.88 ms) |
| Error rate | < 0.1% | ❌ FAIL (69.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 47.09 RPS (all instances) |
| **Achieved throughput** | 14.66 RPS (all instances) |
| **Attempted − achieved gap** | 32.43 RPS (68.86%) |
| **Total attempted ops** | 43203 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 15.847 | 3837.951 | 6873.087 | 3.468404683576254 | 70.35% | 0.40060090135202797 | 394 |
| 1 | 21.839 | 3530.751 | 5914.623 | 3.9625160199813867 | 67.27% | 0.4506760140210316 | 385 |
| 2 | 23.551 | 3837.951 | 6606.847 | 2.896216416242341 | 75.28% | 0.30105368790767684 | 321 |
| 3 | 13.431 | 3276.799 | 5808.127 | 4.335937413231274 | 64.21% | 0.4506760140210316 | 395 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7693 | Connection admission timeout for hash: _R1oo6-0VGP4VoeSd7fpBbwrG_FsZi1RdIyq5wGF_58 after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 7332 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLTransientConnectionException | 8245 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLTransientConnectionException | 7003 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-12T15:21:41Z → 2026-07-12T15:36:41Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.3 | 40.0 | 0.035 | 10 | 0 |
| ojp-2 | 27.4 | 40.0 | 0.064 | 8 | 0 |
| ojp-3 | 25.5 | 41.0 | 2.469 | 398 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T15:21:41Z → 2026-07-12T15:36:41Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 19 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 36108 / 58407 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 439557562 | Cumulative since stats reset |
| Transactions rolled back | 4784 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 4 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7665 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 767838 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T15:21:41Z → 2026-07-12T15:36:41Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 0.6 | 0.0 | 2.0 | 7.8 | 25.5 | 3.7 | 2.9 | 5.0 | 18.6 | 43.9 | 237.7 | 238.8 |
| Proxy (OJP / pgBouncer) | ojp-2 | 0.5 | 0.0 | 2.0 | 6.9 | 17.6 | 4.2 | 2.9 | 7.8 | 33.3 | 36.1 | 250.0 | 250.3 |
| Proxy (OJP / pgBouncer) | ojp-3 | 7.1 | 5.9 | 16.6 | 31.3 | 68.5 | 9.8 | 7.9 | 19.8 | 35.5 | 71.3 | 245.8 | 247.0 |
| PostgreSQL | db | 63.5 | 46.5 | 200.4 | 267.0 | 298.4 | 334.1 | 385.2 | 400.0 | 400.0 | 400.0 | 5931.5 | 9767.6 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T15:39:51Z*

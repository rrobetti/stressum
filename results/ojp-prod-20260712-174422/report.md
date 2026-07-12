# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T16:56:18Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260712-174422` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 5.62 RPS (per instance) |
| **Total throughput** | 22.46 RPS (all instances) |
| **p50 latency** | 7.11 ms |
| **p95 latency** | 4335.10 ms |
| **p99 latency** | 21020.67 ms |
| **p999 latency** | 38342.50 ms |
| **Error rate** | 53.00% (0.53) |
| **Total requests** | 43266 |
| **Failed requests** | 22845 |
| **Total successful** | 20421 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.69 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 30703 |
| observed_client_backends_active_max | 45950 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.0% / 4.9% / 12.7% / 17.6% / 26.4% |
| OJP proxy-tier host_cpu (avg / peak) | 15.4% / 57.9% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 63.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 727.70 MiB / 729.50 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.0% / 4.9% / 12.7% / 17.6% / 26.4% |
| PgBouncer tier RSS (avg / peak, summed) | 727.70 MiB / 729.50 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.0% / 4.9% / 12.7% / 17.6% / 26.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.4% / 57.9% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 63.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 727.70 MiB / 729.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.43% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1242 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4335.10 ms) |
| Error rate | < 0.1% | ❌ FAIL (53.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 47.53 RPS (all instances) |
| **Achieved throughput** | 22.46 RPS (all instances) |
| **Attempted − achieved gap** | 25.06 RPS (52.73%) |
| **Total attempted ops** | 43204 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 7.655 | 4179.967 | 21217.279 | 5.771275249329215 | 51.52% | 0.45090180360721444 | 337 |
| 1 | 6.447 | 4179.967 | 17367.039 | 5.971412139814776 | 49.88% | 0.45090180360721444 | 329 |
| 2 | 7.423 | 4964.351 | 24182.783 | 5.2649454654970205 | 55.74% | 0.4012036108324975 | 294 |
| 3 | 6.911 | 4016.127 | 21315.583 | 5.457192298184415 | 54.07% | 0.400200100050025 | 282 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 5572 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLTransientConnectionException | 5393 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLTransientConnectionException | 6032 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLTransientConnectionException | 5848 | Client throttle limit reached; request rejected to avoid overloading the database |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-12T16:56:18Z → 2026-07-12T17:11:18Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 24.2 | 40.0 | 0.665 | 127 | 0 |
| ojp-2 | 24.7 | 41.0 | 0.557 | 104 | 0 |
| ojp-3 | 30.3 | 48.0 | 0.156 | 67 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T16:56:18Z → 2026-07-12T17:11:18Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 30703 / 45950 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 559953703 | Cumulative since stats reset |
| Transactions rolled back | 6387 | Non-zero → contention or application errors |
| Temp file bytes written | 2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 10985 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 751719 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T16:56:18Z → 2026-07-12T17:11:18Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.5 | 2.0 | 6.9 | 11.8 | 21.5 | 5.7 | 4.9 | 10.8 | 35.5 | 40.0 | 240.8 | 241.1 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.0 | 2.0 | 5.9 | 9.8 | 18.6 | 5.4 | 3.9 | 10.8 | 34.5 | 39.2 | 238.6 | 238.9 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 3.9 | 8.8 | 23.5 | 4.7 | 3.9 | 6.9 | 34.1 | 35.5 | 248.3 | 249.5 |
| PostgreSQL | db | 217.2 | 220.6 | 339.5 | 356.8 | 396.4 | 371.1 | 399.5 | 400.0 | 400.0 | 400.0 | 6610.3 | 11357.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T17:14:07Z*

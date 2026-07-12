# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T07:30:05Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260712-081810` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.96 RPS (per instance) |
| **Total throughput** | 19.86 RPS (all instances) |
| **p50 latency** | 6.12 ms |
| **p95 latency** | 4856.82 ms |
| **p99 latency** | 17719.30 ms |
| **p999 latency** | 31641.50 ms |
| **Error rate** | 38.00% (0.38) |
| **Total requests** | 28834 |
| **Failed requests** | 10845 |
| **Total successful** | 17989 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.80 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 28804 |
| observed_client_backends_active_max | 42626 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.8% / 4.9% / 13.7% / 23.5% / 50.9% |
| OJP proxy-tier host_cpu (avg / peak) | 14.6% / 75.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 87.20% |
| OJP proxy-tier RSS (avg / peak, summed) | 659.50 MiB / 660.50 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.8% / 4.9% / 13.7% / 23.5% / 50.9% |
| PgBouncer tier RSS (avg / peak, summed) | 659.50 MiB / 660.50 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.8% / 4.9% / 13.7% / 23.5% / 50.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.6% / 75.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 87.20% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 659.50 MiB / 660.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.36% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 998 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4856.82 ms) |
| Error rate | < 0.1% | ❌ FAIL (38.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 31.80 RPS (all instances) |
| **Achieved throughput** | 19.86 RPS (all instances) |
| **Attempted − achieved gap** | 11.94 RPS (37.55%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.027 | 4607.999 | 16596.991 | 5.130200262444692 | 35.22% | 0.3510531594784353 | 247 |
| 1 | 6.023 | 4980.735 | 17383.423 | 5.085794418797185 | 36.25% | 0.40050065087621417 | 242 |
| 2 | 5.959 | 4907.007 | 18038.783 | 4.962401201748761 | 37.62% | 0.3508771929824561 | 275 |
| 3 | 6.467 | 4931.583 | 18857.983 | 4.679866175741698 | 41.35% | 0.35070140280561124 | 234 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2538 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLTransientConnectionException | 2613 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLTransientConnectionException | 2712 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLTransientConnectionException | 2982 | Client throttle limit reached; request rejected to avoid overloading the database |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-12T07:30:05Z → 2026-07-12T07:45:05Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 25.5 | 40.0 | 0.643 | 120 | 0 |
| ojp-2 | 25.8 | 40.0 | 0.583 | 109 | 0 |
| ojp-3 | 25.7 | 41.0 | 0.434 | 81 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T07:30:05Z → 2026-07-12T07:45:05Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 28804 / 42626 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 570448901 | Cumulative since stats reset |
| Transactions rolled back | 5667 | Non-zero → contention or application errors |
| Temp file bytes written | 6 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -6 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7294 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 734033 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T07:30:05Z → 2026-07-12T07:45:05Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.3 | 2.0 | 6.8 | 14.7 | 46.0 | 5.7 | 3.9 | 10.9 | 34.3 | 68.6 | 216.5 | 216.9 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.9 | 1.0 | 5.9 | 8.8 | 15.7 | 4.6 | 3.9 | 8.9 | 12.7 | 42.2 | 219.2 | 219.5 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.8 | 1.0 | 4.9 | 9.8 | 25.5 | 4.6 | 3.9 | 7.8 | 13.7 | 35.6 | 223.8 | 224.1 |
| PostgreSQL | db | 207.5 | 206.1 | 335.2 | 349.9 | 362.8 | 367.3 | 399.5 | 400.0 | 400.0 | 400.0 | 5556.2 | 9242.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T07:47:54Z*

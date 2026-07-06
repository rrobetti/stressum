# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-04T18:07:23Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260704-185535` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.00 RPS (per instance) |
| **Total throughput** | 4.00 RPS (all instances) |
| **p50 latency** | 6.49 ms |
| **p95 latency** | 1236.48 ms |
| **p99 latency** | 5496.85 ms |
| **p999 latency** | 8951.80 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 3604 |
| **Failed requests** | 0 |
| **Total successful** | 3604 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 13.60 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 10982 |
| observed_client_backends_active_max | 16123 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.1% / 2.0% / 7.8% / 17.6% / 30.4% |
| OJP proxy-tier host_cpu (avg / peak) | 12.9% / 69.8% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 57.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 635.20 MiB / 640.00 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.1% / 2.0% / 7.8% / 17.6% / 30.4% |
| PgBouncer tier RSS (avg / peak, summed) | 635.20 MiB / 640.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.1% / 2.0% / 7.8% / 17.6% / 30.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 12.9% / 69.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 57.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 635.20 MiB / 640.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.20% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 181 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (1236.48 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 4.00 RPS (all instances) |
| **Achieved throughput** | 4.00 RPS (all instances) |
| **Attempted − achieved gap** | 0.00 RPS (0.00%) |
| **Total attempted ops** | 3602 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.599 | 1388.543 | 3551.231 | 1.0005363585584726 | 0.00% | 0.20020020020020018 | 47 |
| 1 | 6.371 | 1315.839 | 4943.871 | 1.0004230423741893 | 0.00% | 0.20015012511260633 | 47 |
| 2 | 6.491 | 1094.655 | 6488.063 | 1.0003908297137172 | 0.00% | 0.2001000500250125 | 42 |
| 3 | 6.499 | 1146.879 | 7004.159 | 1.000337516764813 | 0.00% | 0.20020020020020018 | 45 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-04T18:07:23Z → 2026-07-04T18:22:23Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.9 | 46.0 | 0.050 | 15 | 0 |
| ojp-2 | 26.1 | 40.0 | 0.041 | 21 | 0 |
| ojp-3 | 24.9 | 40.0 | 0.054 | 26 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-04T18:07:23Z → 2026-07-04T18:22:23Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 10982 / 16123 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 90847308 | Cumulative since stats reset |
| Transactions rolled back | 1300 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1375 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 137939 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-04T18:07:23Z → 2026-07-04T18:22:23Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.1 | 1.0 | 3.9 | 10.8 | 18.6 | 4.9 | 3.9 | 10.7 | 34.3 | 39.2 | 212.0 | 213.7 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.1 | 1.0 | 3.9 | 8.8 | 24.5 | 3.9 | 3.0 | 6.8 | 12.7 | 28.3 | 213.1 | 214.7 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.0 | 1.0 | 2.9 | 8.8 | 14.7 | 4.4 | 3.9 | 7.8 | 33.3 | 37.6 | 210.1 | 211.6 |
| PostgreSQL | db | 28.8 | 0.7 | 184.8 | 262.4 | 312.7 | 124.5 | 83.9 | 397.9 | 400.0 | 400.0 | 3740.2 | 8268.4 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-04T18:24:55Z*

# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-01T15:47:33Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260701-163521` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.88 RPS (per instance) |
| **Total throughput** | 3.53 RPS (all instances) |
| **p50 latency** | 6.34 ms |
| **p95 latency** | 1490.17 ms |
| **p99 latency** | 5306.90 ms |
| **p999 latency** | 9183.23 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 3604 |
| **Failed requests** | 0 |
| **Total successful** | 3604 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 13.55 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 11103 |
| observed_client_backends_active_max | 16915 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.2% / 2.0% / 9.8% / 19.6% / 26.4% |
| OJP proxy-tier host_cpu (avg / peak) | 16.3% / 108.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 63.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 653.40 MiB / 658.70 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.2% / 2.0% / 9.8% / 19.6% / 26.4% |
| PgBouncer tier RSS (avg / peak, summed) | 653.40 MiB / 658.70 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.2% / 2.0% / 9.8% / 19.6% / 26.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.3% / 108.3% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 63.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 653.40 MiB / 658.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.20% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 177 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (1490.17 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 3.53 RPS (all instances) |
| **Achieved throughput** | 3.53 RPS (all instances) |
| **Attempted − achieved gap** | 0.00 RPS (0.00%) |
| **Total attempted ops** | 3602 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 7.459 | 1510.399 | 3909.631 | 0.8828218159870115 | 0.00% | 0.2004008016032064 | 45 |
| 1 | 6.567 | 1548.287 | 5197.823 | 0.8827197565613706 | 0.00% | 0.2001000500250125 | 45 |
| 2 | 5.851 | 1545.215 | 5931.007 | 0.8826185853416743 | 0.00% | 0.20030045067601399 | 42 |
| 3 | 5.471 | 1356.799 | 6189.055 | 0.8827405124989591 | 0.00% | 0.20020020020020018 | 45 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-01T15:47:33Z → 2026-07-01T16:02:33Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 24.8 | 45.0 | 0.054 | 17 | 0 |
| ojp-2 | 26.1 | 45.0 | 0.045 | 15 | 0 |
| ojp-3 | 29.5 | 48.0 | 0.047 | 19 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-01T15:47:33Z → 2026-07-01T16:02:33Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 11103 / 16915 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 88876527 | Cumulative since stats reset |
| Transactions rolled back | 1298 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1487 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 149027 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-01T15:47:33Z → 2026-07-01T16:02:33Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.1 | 1.0 | 3.9 | 12.7 | 25.5 | 7.1 | 3.9 | 33.3 | 35.1 | 100.5 | 215.7 | 217.6 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.1 | 1.0 | 3.9 | 11.8 | 20.6 | 5.1 | 3.9 | 12.8 | 35.0 | 54.4 | 215.7 | 217.6 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.0 | 1.0 | 2.9 | 9.8 | 17.6 | 4.4 | 3.0 | 7.8 | 33.3 | 47.3 | 222.0 | 223.5 |
| PostgreSQL | db | 27.6 | 0.7 | 156.9 | 260.6 | 326.4 | 125.2 | 83.7 | 394.3 | 400.0 | 400.0 | 3793.2 | 8264.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-01T16:05:05Z*

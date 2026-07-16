# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-14T16:46:00Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260714-173408` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.96 RPS (per instance) |
| **Total throughput** | 15.44 RPS (all instances) |
| **p50 latency** | 5.37 ms |
| **p95 latency** | 6981.38 ms |
| **p99 latency** | 50098.12 ms |
| **p999 latency** | 80515.00 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 14432 |
| **Failed requests** | 0 |
| **Total successful** | 14432 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 214 |
| observed_postgres_backends_avg_numbackends | 170.10 |
| observed_postgres_backends_median_numbackends | 167 |
| observed_client_backends_active_median | 43392 |
| observed_client_backends_active_max | 66883 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | hikari-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 19 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| OJP proxy-tier host_cpu (avg / peak) | N/A% / N/A% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 0% |
| OJP proxy-tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| PgBouncer tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | N/A% / N/A% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 0.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | N/A MiB / 0.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 0 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (6981.38 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.42 RPS (all instances) |
| **Achieved throughput** | 15.44 RPS (all instances) |
| **Attempted − achieved gap** | -0.02 RPS (-0.11%) |
| **Total attempted ops** | 14416 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5.047 | 4526.079 | 28737.535 | 0.964698660010032 | 0.00% | 0.025021894157387717 | 0 |
| 10 | 5.015 | 6516.735 | 51675.135 | 0.963630179913284 | 0.00% | 0.025021894157387717 | 0 |
| 11 | 5.319 | 6217.727 | 54460.415 | 0.964697628255587 | 0.00% | 0.025025025025025023 | 0 |
| 12 | 4.987 | 7163.903 | 54034.431 | 0.964698660010032 | 0.00% | 0.025021894157387717 | 0 |
| 13 | 5.775 | 6627.327 | 53051.391 | 0.964697628255587 | 0.00% | 0.025025025025025023 | 0 |
| 14 | 5.419 | 8314.879 | 51740.671 | 0.9657681707195775 | 0.00% | 0.025025025025025023 | 0 |
| 15 | 5.227 | 6995.967 | 52953.087 | 0.964698660010032 | 0.00% | 0.025025025025025023 | 0 |
| 1 | 5.947 | 3395.583 | 33751.039 | 0.964698660010032 | 0.00% | 0.03753284123608157 | 0 |
| 2 | 5.563 | 6303.743 | 51249.151 | 0.964698660010032 | 0.00% | 0.025021894157387717 | 0 |
| 3 | 5.227 | 10067.967 | 54001.663 | 0.964698660010032 | 0.00% | 0.02502815667626079 | 0 |
| 4 | 5.099 | 10510.335 | 55214.079 | 0.9657671378212807 | 0.00% | 0.025021894157387717 | 0 |
| 5 | 5.635 | 2719.743 | 52461.567 | 0.9636291493004866 | 0.00% | 0.02502815667626079 | 0 |
| 6 | 5.627 | 6680.575 | 52527.103 | 0.964698660010032 | 0.00% | 0.03751875937968984 | 0 |
| 7 | 5.351 | 10239.999 | 53903.359 | 0.9646996917666839 | 0.00% | 0.025025025025025023 | 0 |
| 8 | 5.495 | 9928.703 | 53379.071 | 0.9657681707195775 | 0.00% | 0.025025025025025023 | 0 |
| 9 | 5.119 | 5492.735 | 48431.103 | 0.963630179913284 | 0.00% | 0.02502815667626079 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-14T16:46:00Z → 2026-07-14T17:01:00Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 167 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 43392 / 66883 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1402284101 | Cumulative since stats reset |
| Transactions rolled back | 834 | Non-zero → contention or application errors |
| Temp file bytes written | 32 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -38 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1841 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 186682 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-14T16:46:00Z → 2026-07-14T17:01:00Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 448.4 | 536.0 | 993.7 | 1075.6 | 1075.6 | 1259.9 | 1538.2 | 1598.5 | 1598.6 | 1598.6 | 36751.7 | 97294.6 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-14T17:04:44Z*

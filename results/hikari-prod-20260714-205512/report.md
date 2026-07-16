# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-14T20:07:05Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260714-205512` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.96 RPS (per instance) |
| **Total throughput** | 15.43 RPS (all instances) |
| **p50 latency** | 4.98 ms |
| **p95 latency** | 6669.81 ms |
| **p99 latency** | 47553.56 ms |
| **p999 latency** | 80265.62 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 14431 |
| **Failed requests** | 0 |
| **Total successful** | 14431 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 211 |
| observed_postgres_backends_avg_numbackends | 169.13 |
| observed_postgres_backends_median_numbackends | 165 |
| observed_client_backends_active_median | 43430 |
| observed_client_backends_active_max | 66857 |
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
| p95 latency | < 1500 ms | ❌ FAIL (6669.81 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.42 RPS (all instances) |
| **Achieved throughput** | 15.43 RPS (all instances) |
| **Attempted − achieved gap** | -0.02 RPS (-0.11%) |
| **Total attempted ops** | 14411 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.951 | 4476.927 | 29261.823 | 0.964698660010032 | 0.00% | 0.02502815667626079 | 0 |
| 10 | 4.763 | 9633.791 | 50331.647 | 0.9657671378212807 | 0.00% | 0.02502815667626079 | 0 |
| 11 | 5.379 | 3303.423 | 49020.927 | 0.9636291493004866 | 0.00% | 0.03751875937968985 | 0 |
| 12 | 4.779 | 5844.991 | 52559.871 | 0.964698660010032 | 0.00% | 0.03751875937968985 | 0 |
| 13 | 4.791 | 8060.927 | 49283.071 | 0.964697628255587 | 0.00% | 0.025025025025025023 | 0 |
| 14 | 5.015 | 4102.143 | 47448.063 | 0.964698660010032 | 0.00% | 0.025031289111389236 | 0 |
| 15 | 5.083 | 6873.087 | 47972.351 | 0.964698660010032 | 0.00% | 0.0375234521575985 | 0 |
| 1 | 5.127 | 5783.551 | 31834.111 | 0.964698660010032 | 0.00% | 0.02502815667626079 | 0 |
| 2 | 4.755 | 6500.351 | 52035.583 | 0.964697628255587 | 0.00% | 0.02502815667626079 | 0 |
| 3 | 5.027 | 6361.087 | 51871.743 | 0.964698660010032 | 0.00% | 0.0375234521575985 | 0 |
| 4 | 4.775 | 9854.975 | 51150.847 | 0.964698660010032 | 0.00% | 0.02505951635133442 | 0 |
| 5 | 5.239 | 7307.263 | 42106.879 | 0.9636291493004866 | 0.00% | 0.025025025025025023 | 0 |
| 6 | 4.827 | 6234.111 | 53149.695 | 0.964697628255587 | 0.00% | 0.02502815667626079 | 0 |
| 7 | 5.087 | 6119.423 | 49938.431 | 0.964698660010032 | 0.00% | 0.025043826696719257 | 0 |
| 8 | 4.935 | 9887.743 | 51838.975 | 0.964697628255587 | 0.00% | 0.025025025025025023 | 0 |
| 9 | 5.143 | 6373.375 | 51052.543 | 0.964698660010032 | 0.00% | 0.0375234521575985 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-14T20:07:05Z → 2026-07-14T20:22:05Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 165 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 43430 / 66857 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1396965177 | Cumulative since stats reset |
| Transactions rolled back | 834 | Non-zero → contention or application errors |
| Temp file bytes written | 30 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -36 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1820 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 184183 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-14T20:07:05Z → 2026-07-14T20:22:05Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 414.2 | 452.5 | 930.3 | 991.5 | 991.5 | 1233.2 | 1456.2 | 1598.4 | 1598.7 | 1598.7 | 35312.9 | 94387.6 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-14T20:25:56Z*

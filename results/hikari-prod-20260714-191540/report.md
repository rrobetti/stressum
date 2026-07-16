# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-14T18:27:27Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260714-191540` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.96 RPS (per instance) |
| **Total throughput** | 15.44 RPS (all instances) |
| **p50 latency** | 5.16 ms |
| **p95 latency** | 6509.06 ms |
| **p99 latency** | 48108.50 ms |
| **p999 latency** | 80045.62 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 14435 |
| **Failed requests** | 0 |
| **Total successful** | 14435 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 221 |
| observed_postgres_backends_avg_numbackends | 169.77 |
| observed_postgres_backends_median_numbackends | 166 |
| observed_client_backends_active_median | 43426 |
| observed_client_backends_active_max | 66909 |
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
| p95 latency | < 1500 ms | ❌ FAIL (6509.06 ms) |
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
| **Attempted − achieved gap** | -0.02 RPS (-0.13%) |
| **Total attempted ops** | 14414 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.007 | 4587.519 | 28508.159 | 0.964697628255587 | 0.00% | 0.025034422330704718 | 0 |
| 10 | 4.775 | 6590.463 | 52494.335 | 0.9646965965033492 | 0.00% | 0.02502815667626079 | 0 |
| 11 | 5.131 | 5005.311 | 51838.975 | 0.964698660010032 | 0.00% | 0.02502815667626079 | 0 |
| 12 | 5.135 | 6172.671 | 52035.583 | 0.964698660010032 | 0.00% | 0.02502815667626079 | 0 |
| 13 | 5.039 | 6828.031 | 48889.855 | 0.9657671378212807 | 0.00% | 0.0375234521575985 | 0 |
| 14 | 5.131 | 6135.807 | 47939.583 | 0.9675102771210576 | 0.00% | 0.02502815667626079 | 0 |
| 15 | 5.079 | 7770.111 | 50561.023 | 0.9657671378212807 | 0.00% | 0.03753284123608157 | 0 |
| 1 | 5.259 | 3442.687 | 32358.399 | 0.964698660010032 | 0.00% | 0.025034422330704718 | 0 |
| 2 | 5.231 | 6864.895 | 51150.847 | 0.964697628255587 | 0.00% | 0.025025025025025023 | 0 |
| 3 | 5.119 | 6610.943 | 52920.319 | 0.9646965965033492 | 0.00% | 0.025031289111389236 | 0 |
| 4 | 5.287 | 9150.463 | 50921.471 | 0.964698660010032 | 0.00% | 0.025031289111389236 | 0 |
| 5 | 5.367 | 3831.807 | 51609.599 | 0.9636281186898935 | 0.00% | 0.03752814610958219 | 0 |
| 6 | 4.911 | 3776.511 | 51052.543 | 0.9646996917666839 | 0.00% | 0.025025025025025023 | 0 |
| 7 | 4.655 | 9101.311 | 48529.407 | 0.9646996917666839 | 0.00% | 0.02502815667626079 | 0 |
| 8 | 5.151 | 9281.535 | 49676.287 | 0.964697628255587 | 0.00% | 0.02502815667626079 | 0 |
| 9 | 5.263 | 8994.815 | 49250.303 | 0.964698660010032 | 0.00% | 0.0375234521575985 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-14T18:27:27Z → 2026-07-14T18:42:27Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 166 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 43426 / 66909 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1398517528 | Cumulative since stats reset |
| Transactions rolled back | 834 | Non-zero → contention or application errors |
| Temp file bytes written | 27 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -34 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1834 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 185155 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-14T18:27:27Z → 2026-07-14T18:42:27Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 450.5 | 449.1 | 1052.9 | 1120.2 | 1120.2 | 1247.9 | 1512.2 | 1597.5 | 1598.5 | 1598.5 | 35855.6 | 92770.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-14T18:46:17Z*

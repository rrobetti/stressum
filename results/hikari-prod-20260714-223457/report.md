# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-14T21:46:46Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260714-223457` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.96 RPS (per instance) |
| **Total throughput** | 15.44 RPS (all instances) |
| **p50 latency** | 5.12 ms |
| **p95 latency** | 6350.06 ms |
| **p99 latency** | 48206.81 ms |
| **p999 latency** | 80664.38 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 14432 |
| **Failed requests** | 0 |
| **Total successful** | 14432 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 214 |
| observed_postgres_backends_avg_numbackends | 169.37 |
| observed_postgres_backends_median_numbackends | 164 |
| observed_client_backends_active_median | 43312 |
| observed_client_backends_active_max | 66850 |
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
| p95 latency | < 1500 ms | ❌ FAIL (6350.06 ms) |
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
| **Total attempted ops** | 14413 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.867 | 4505.599 | 27983.871 | 0.964697628255587 | 0.00% | 0.025021894157387717 | 0 |
| 10 | 4.927 | 3829.759 | 46825.471 | 0.9636291493004866 | 0.00% | 0.0375234521575985 | 0 |
| 11 | 4.951 | 6017.023 | 48234.495 | 0.9646965965033492 | 0.00% | 0.03752814610958219 | 0 |
| 12 | 4.867 | 8749.055 | 52264.959 | 0.964698660010032 | 0.00% | 0.025025025025025023 | 0 |
| 13 | 5.075 | 5922.815 | 46694.399 | 0.964697628255587 | 0.00% | 0.02502815667626079 | 0 |
| 14 | 5.111 | 7487.487 | 49414.143 | 0.9657671378212807 | 0.00% | 0.025025025025025023 | 0 |
| 15 | 4.875 | 5386.239 | 51445.759 | 0.964698660010032 | 0.00% | 0.0375234521575985 | 0 |
| 1 | 5.323 | 3102.719 | 30523.391 | 0.964698660010032 | 0.00% | 0.02502815667626079 | 0 |
| 2 | 5.011 | 9551.871 | 50659.327 | 0.9646996917666839 | 0.00% | 0.025025025025025023 | 0 |
| 3 | 5.695 | 3139.583 | 54984.703 | 0.964698660010032 | 0.00% | 0.025031289111389236 | 0 |
| 4 | 5.003 | 9715.711 | 51380.223 | 0.964698660010032 | 0.00% | 0.025031289111389236 | 0 |
| 5 | 5.675 | 3489.791 | 51871.743 | 0.9636281186898935 | 0.00% | 0.03752814610958219 | 0 |
| 6 | 5.543 | 7446.527 | 50855.935 | 0.964697628255587 | 0.00% | 0.025025025025025023 | 0 |
| 7 | 4.699 | 6696.959 | 53116.927 | 0.964697628255587 | 0.00% | 0.025031289111389236 | 0 |
| 8 | 5.299 | 6942.719 | 52363.263 | 0.9646996917666839 | 0.00% | 0.02502815667626079 | 0 |
| 9 | 4.987 | 9617.407 | 52690.943 | 0.9657671378212807 | 0.00% | 0.025025025025025023 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-14T21:46:46Z → 2026-07-14T22:01:46Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 164 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 43312 / 66850 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1395536718 | Cumulative since stats reset |
| Transactions rolled back | 834 | Non-zero → contention or application errors |
| Temp file bytes written | 30 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -45 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1848 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 187106 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-14T21:46:46Z → 2026-07-14T22:01:46Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 432.0 | 523.0 | 951.1 | 1065.4 | 1065.4 | 1252.6 | 1524.8 | 1598.3 | 1598.6 | 1598.6 | 36572.6 | 95710.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-14T22:05:33Z*

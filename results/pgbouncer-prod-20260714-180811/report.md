# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-14T17:20:15Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260714-180811` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.97 RPS (per instance) |
| **Total throughput** | 15.45 RPS (all instances) |
| **p50 latency** | 4.28 ms |
| **p95 latency** | 14034.94 ms |
| **p99 latency** | 38064.06 ms |
| **p999 latency** | 62971.88 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 14446 |
| **Failed requests** | 1 |
| **Total successful** | 14445 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 51.78 |
| observed_postgres_backends_median_numbackends | 49 |
| observed_client_backends_active_median | 43196 |
| observed_client_backends_active_max | 67110 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | pgbouncer-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.0% / 2.9% / 4.9% |
| OJP proxy-tier host_cpu (avg / peak) | 9.3% / 61.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 6.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.80 MiB / 34.90 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.0% / 2.9% / 4.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.80 MiB / 34.90 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 2.9% / 3.9% / 4.9% |
| HAProxy RSS (avg / peak, summed) | 23.20 MiB / 23.40 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.8% / 1.9% / 4.9% / 5.9% / 9.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.3% / 64.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 11.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 58.00 MiB / 58.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 26 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (14034.94 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.42 RPS (all instances) |
| **Achieved throughput** | 15.45 RPS (all instances) |
| **Attempted − achieved gap** | -0.03 RPS (-0.20%) |
| **Total attempted ops** | 14416 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.607 | 11501.567 | 24657.919 | 0.964697628255587 | 0.00% | 0.02501876407305479 | 1 |
| 10 | 3.833 | 14188.543 | 42827.775 | 0.9657671378212807 | 0.00% | 0.02501876407305479 | 2 |
| 11 | 4.099 | 12861.439 | 39190.527 | 0.9668366473869742 | 0.00% | 0.02501876407305479 | 2 |
| 12 | 3.943 | 14368.767 | 40927.231 | 0.9657681707195775 | 0.00% | 0.02501876407305479 | 2 |
| 13 | 4.403 | 15572.991 | 39976.959 | 0.9668376814291231 | 0.00% | 0.02501876407305479 | 1 |
| 14 | 4.057 | 18972.671 | 42663.935 | 0.969588524181388 | 0.00% | 0.02501876407305479 | 1 |
| 15 | 4.547 | 15507.455 | 41222.143 | 0.9679071921386685 | 0.00% | 0.025021894157387717 | 2 |
| 1 | 4.085 | 11722.751 | 25378.815 | 0.964697628255587 | 0.00% | 0.025021894157387717 | 2 |
| 2 | 4.567 | 14131.199 | 39878.655 | 0.9636291493004866 | 0.11% | 0.02501876407305479 | 1 |
| 3 | 4.275 | 14516.223 | 37126.143 | 0.964698660010032 | 0.00% | 0.025021894157387717 | 2 |
| 4 | 4.523 | 14098.431 | 41058.303 | 0.9646996917666839 | 0.00% | 0.02501876407305479 | 1 |
| 5 | 4.331 | 12779.519 | 38109.183 | 0.9646996917666839 | 0.00% | 0.02501876407305479 | 2 |
| 6 | 4.431 | 13041.663 | 39387.135 | 0.964697628255587 | 0.00% | 0.02501876407305479 | 1 |
| 7 | 4.427 | 13508.607 | 37355.519 | 0.9679898720173745 | 0.00% | 0.025021894157387717 | 2 |
| 8 | 4.439 | 12689.407 | 41189.375 | 0.964698660010032 | 0.00% | 0.02501876407305479 | 2 |
| 9 | 3.941 | 15097.855 | 38076.415 | 0.964698660010032 | 0.00% | 0.025021894157387717 | 2 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 2 | SQLTransientConnectionException | 1 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=4, active=4, idle=0, waiting=1) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-14T17:20:15Z → 2026-07-14T17:35:15Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 49 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 43196 / 67110 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1397809748 | Cumulative since stats reset |
| Transactions rolled back | 813 | Non-zero → contention or application errors |
| Temp file bytes written | 18 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -18 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 2207 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 222542 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-14T17:20:15Z → 2026-07-14T17:35:15Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 1.0 | 2.0 | 2.0 | 3.0 | 2.9 | 3.9 | 16.7 | 33.3 | 11.6 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.0 | 1.9 | 2.0 | 3.2 | 2.9 | 3.9 | 32.3 | 34.2 | 11.6 | 11.6 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.0 | 1.9 | 2.9 | 3.3 | 2.9 | 4.9 | 25.4 | 33.2 | 11.6 | 11.6 |
| PostgreSQL | db | 658.4 | 878.1 | 1225.8 | 1238.1 | 1252.8 | 1153.0 | 1473.9 | 1597.9 | 1598.3 | 1598.4 | 137415.7 | 152666.0 |
| HAProxy | lb | 1.0 | 1.0 | 2.9 | 3.9 | 4.9 | 5.1 | 3.9 | 7.8 | 35.0 | 49.5 | 23.2 | 23.4 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-14T17:39:14Z*

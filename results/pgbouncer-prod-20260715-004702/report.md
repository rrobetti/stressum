# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-14T23:59:05Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260715-004702` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.97 RPS (per instance) |
| **Total throughput** | 15.47 RPS (all instances) |
| **p50 latency** | 4.15 ms |
| **p95 latency** | 13474.31 ms |
| **p99 latency** | 37849.06 ms |
| **p999 latency** | 64092.50 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 14449 |
| **Failed requests** | 0 |
| **Total successful** | 14449 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 58 |
| observed_postgres_backends_avg_numbackends | 51.83 |
| observed_postgres_backends_median_numbackends | 50 |
| observed_client_backends_active_median | 43133 |
| observed_client_backends_active_max | 67207 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.9% / 2.9% / 4.9% |
| OJP proxy-tier host_cpu (avg / peak) | 10.1% / 68.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 7.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.70 MiB / 34.80 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.9% / 2.9% / 4.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.70 MiB / 34.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 1.9% / 4.9% / 6.8% |
| HAProxy RSS (avg / peak, summed) | 23.20 MiB / 23.30 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.8% / 1.9% / 3.9% / 7.8% / 10.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.3% / 72.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 14.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 57.90 MiB / 58.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 30 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (13474.31 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.43 RPS (all instances) |
| **Achieved throughput** | 15.47 RPS (all instances) |
| **Attempted − achieved gap** | -0.04 RPS (-0.23%) |
| **Total attempted ops** | 14415 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 3.889 | 10706.943 | 23117.823 | 0.9646996917666839 | 0.00% | 0.025015634771732333 | 2 |
| 10 | 4.099 | 14344.191 | 42205.183 | 0.9657692036200838 | 0.00% | 0.025015634771732333 | 2 |
| 11 | 3.781 | 14204.927 | 41091.071 | 0.9698166038181165 | 0.00% | 0.025021894157387717 | 2 |
| 12 | 4.291 | 12279.807 | 35815.423 | 0.9657681707195775 | 0.00% | 0.025015634771732333 | 2 |
| 13 | 4.071 | 13393.919 | 38535.167 | 0.9722181936937954 | 0.00% | 0.025021894157387717 | 2 |
| 14 | 3.891 | 14008.319 | 40796.159 | 0.9689777391802834 | 0.00% | 0.025015634771732333 | 1 |
| 15 | 4.515 | 15114.239 | 41943.039 | 0.9767162068051031 | 0.00% | 0.025021894157387717 | 2 |
| 1 | 4.099 | 11403.263 | 24035.327 | 0.964698660010032 | 0.00% | 0.025021894157387717 | 2 |
| 2 | 4.219 | 12738.559 | 35586.047 | 0.9646996917666839 | 0.00% | 0.025015634771732333 | 2 |
| 3 | 4.295 | 16539.647 | 39452.671 | 0.964698660010032 | 0.00% | 0.02501876407305479 | 2 |
| 4 | 4.263 | 12812.287 | 39256.063 | 0.964698660010032 | 0.00% | 0.02501876407305479 | 2 |
| 5 | 4.463 | 11157.503 | 41091.071 | 0.964698660010032 | 0.00% | 0.02501876407305479 | 2 |
| 6 | 3.991 | 14581.759 | 40599.551 | 0.9646996917666839 | 0.00% | 0.025015634771732333 | 2 |
| 7 | 4.735 | 16179.199 | 40927.231 | 0.964698660010032 | 0.00% | 0.02501876407305479 | 2 |
| 8 | 3.997 | 13524.991 | 41287.679 | 0.9657692036200838 | 0.00% | 0.02501250625312656 | 1 |
| 9 | 3.793 | 12599.295 | 39845.887 | 0.9657692036200838 | 0.00% | 0.02501876407305479 | 2 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-14T23:59:05Z → 2026-07-15T00:14:05Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 50 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 43133 / 67207 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1394750617 | Cumulative since stats reset |
| Transactions rolled back | 890 | Non-zero → contention or application errors |
| Temp file bytes written | 20 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -20 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 2095 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 211371 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-14T23:59:05Z → 2026-07-15T00:14:05Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 1.0 | 2.0 | 2.9 | 3.1 | 2.9 | 3.9 | 31.4 | 35.2 | 11.6 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.0 | 2.0 | 2.0 | 4.3 | 2.9 | 12.7 | 33.3 | 35.2 | 11.5 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.0 | 1.9 | 2.9 | 2.9 | 2.9 | 3.9 | 5.9 | 34.2 | 11.6 | 11.7 |
| PostgreSQL | db | 657.1 | 868.8 | 1252.8 | 1289.7 | 1346.4 | 1150.9 | 1410.8 | 1597.8 | 1598.5 | 1598.6 | 133680.3 | 150403.0 |
| HAProxy | lb | 1.0 | 1.0 | 1.9 | 4.9 | 6.8 | 4.2 | 3.9 | 6.8 | 13.7 | 34.1 | 23.2 | 23.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T00:18:08Z*

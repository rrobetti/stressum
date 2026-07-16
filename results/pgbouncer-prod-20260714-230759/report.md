# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-14T22:19:57Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260714-230759` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.97 RPS (per instance) |
| **Total throughput** | 15.45 RPS (all instances) |
| **p50 latency** | 3.91 ms |
| **p95 latency** | 13584.44 ms |
| **p99 latency** | 36760.50 ms |
| **p999 latency** | 62382.19 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 14443 |
| **Failed requests** | 1 |
| **Total successful** | 14442 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 51.49 |
| observed_postgres_backends_median_numbackends | 49 |
| observed_client_backends_active_median | 43369 |
| observed_client_backends_active_max | 67514 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.9% / 2.9% / 3.9% |
| OJP proxy-tier host_cpu (avg / peak) | 12.3% / 73.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 5.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.80 MiB / 34.80 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 1.0% / 2.9% / 2.9% / 3.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.80 MiB / 34.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 2.9% / 3.9% / 4.9% |
| HAProxy RSS (avg / peak, summed) | 23.50 MiB / 23.70 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.8% / 1.9% / 4.9% / 5.9% / 7.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.2% / 78.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 10.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 58.30 MiB / 58.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 24 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (13584.44 ms) |
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
| **Attempted − achieved gap** | -0.03 RPS (-0.18%) |
| **Total attempted ops** | 14414 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 3.563 | 8863.743 | 22380.543 | 0.964698660010032 | 0.00% | 0.025015634771732333 | 2 |
| 10 | 3.525 | 14319.615 | 39092.223 | 0.9646996917666839 | 0.00% | 0.025015634771732333 | 1 |
| 11 | 4.073 | 14172.159 | 38436.863 | 0.9668366473869742 | 0.00% | 0.025021894157387717 | 1 |
| 12 | 3.379 | 13860.863 | 36306.943 | 0.9679661040542147 | 0.00% | 0.025015634771732333 | 1 |
| 13 | 3.551 | 12287.999 | 39944.191 | 0.9677723251372438 | 0.00% | 0.025020329115221254 | 2 |
| 14 | 4.339 | 14950.399 | 38928.383 | 0.9690857362157203 | 0.00% | 0.025015634771732333 | 1 |
| 15 | 3.613 | 14163.967 | 38764.543 | 0.9696030513600662 | 0.00% | 0.025021894157387717 | 2 |
| 1 | 4.243 | 14532.607 | 24854.527 | 0.964697628255587 | 0.00% | 0.025021894157387717 | 2 |
| 2 | 3.791 | 12705.791 | 38961.151 | 0.964698660010032 | 0.00% | 0.02501250625312656 | 2 |
| 3 | 4.455 | 12500.991 | 39780.351 | 0.964697628255587 | 0.00% | 0.025021894157387717 | 2 |
| 4 | 4.103 | 13836.287 | 38404.095 | 0.9646996917666839 | 0.00% | 0.025015634771732333 | 2 |
| 5 | 3.873 | 13680.639 | 35717.119 | 0.9625596385909411 | 0.11% | 0.025021894157387717 | 1 |
| 6 | 4.203 | 14123.007 | 40468.479 | 0.9657692036200838 | 0.00% | 0.025015634771732333 | 1 |
| 7 | 4.021 | 14032.895 | 40665.087 | 0.964698660010032 | 0.00% | 0.025021894157387717 | 2 |
| 8 | 4.111 | 15245.311 | 39354.367 | 0.9636291493004866 | 0.00% | 0.025015634771732333 | 1 |
| 9 | 3.655 | 14073.855 | 36110.335 | 0.964697628255587 | 0.00% | 0.025021894157387717 | 1 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 5 | SQLTransientConnectionException | 1 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=5, active=5, idle=0, waiting=2) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-14T22:19:57Z → 2026-07-14T22:34:57Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 49 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 43369 / 67514 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1393163092 | Cumulative since stats reset |
| Transactions rolled back | 790 | Non-zero → contention or application errors |
| Temp file bytes written | 16 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -16 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 2204 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 222368 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-14T22:19:57Z → 2026-07-14T22:34:57Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 1.0 | 2.0 | 2.0 | 3.6 | 2.9 | 4.9 | 33.2 | 35.2 | 11.6 | 11.6 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.0 | 1.9 | 2.0 | 4.1 | 2.9 | 5.9 | 33.3 | 36.2 | 11.6 | 11.6 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.0 | 1.9 | 1.9 | 5.0 | 2.9 | 17.6 | 35.2 | 38.0 | 11.6 | 11.6 |
| PostgreSQL | db | 644.4 | 798.5 | 1240.7 | 1262.4 | 1295.4 | 1131.2 | 1394.9 | 1597.8 | 1598.5 | 1598.9 | 136281.1 | 151225.0 |
| HAProxy | lb | 1.0 | 1.0 | 2.9 | 3.9 | 4.9 | 4.0 | 3.9 | 5.9 | 7.8 | 9.7 | 23.5 | 23.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-14T22:38:50Z*

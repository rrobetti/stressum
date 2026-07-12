# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T19:57:58Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260711-204607` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.85 RPS (per instance) |
| **Total throughput** | 15.40 RPS (all instances) |
| **p50 latency** | 7547.90 ms |
| **p95 latency** | 24702.97 ms |
| **p99 latency** | 32342.00 ms |
| **p999 latency** | 49397.75 ms |
| **Error rate** | 1.00% (0.01) |
| **Total requests** | 14482 |
| **Failed requests** | 210 |
| **Total successful** | 14272 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 22 |
| observed_postgres_backends_avg_numbackends | 18.35 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 21804 |
| observed_client_backends_active_max | 33003 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | pgbouncer-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 2.0% / 2.9% / 5.9% |
| OJP proxy-tier host_cpu (avg / peak) | 9.4% / 92.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 12.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 2.0% / 2.9% / 5.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 6.8% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 22.00 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.1% / 1.0% / 3.9% / 5.8% / 11.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 20.1% / 127.1% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 19.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.10 MiB / 56.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.11% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 30 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (24702.97 ms) |
| Error rate | < 0.1% | ❌ FAIL (1.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.54 RPS (all instances) |
| **Achieved throughput** | 15.40 RPS (all instances) |
| **Attempted − achieved gap** | 0.14 RPS (0.92%) |
| **Total attempted ops** | 14403 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 7716.863 | 22904.831 | 30343.167 | 3.85512637203152 | 0.77% | 0.10015022533800699 | 6 |
| 1 | 6590.463 | 25640.959 | 33030.143 | 3.862342163901956 | 0.91% | 0.15007503751875936 | 9 |
| 2 | 7159.807 | 20676.607 | 28606.463 | 3.900720374972475 | 0.75% | 0.10015022533800699 | 6 |
| 3 | 8724.479 | 29589.503 | 37388.287 | 3.780734663032037 | 3.37% | 0.10015022533800699 | 9 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 28 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=56) |
| 1 | SQLTransientConnectionException | 33 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=7, active=7, idle=0, waiting=73) |
| 2 | SQLTransientConnectionException | 27 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=66) |
| 3 | SQLTransientConnectionException | 122 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=56) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T19:57:58Z → 2026-07-11T20:12:58Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21804 / 33003 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 426619226 | Cumulative since stats reset |
| Transactions rolled back | 4504 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5582 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 418912 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T19:57:58Z → 2026-07-11T20:12:58Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 2.7 | 2.0 | 3.9 | 5.9 | 33.3 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 4.4 | 2.9 | 19.6 | 33.3 | 87.2 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 5.9 | 2.4 | 2.0 | 3.9 | 4.9 | 7.9 | 11.3 | 11.3 |
| PostgreSQL | db | 231.2 | 240.5 | 295.5 | 307.7 | 315.0 | 384.4 | 400.0 | 400.0 | 400.0 | 400.0 | 15129.6 | 17063.3 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 2.9 | 6.8 | 11.0 | 3.9 | 34.1 | 36.7 | 89.8 | 22.0 | 22.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T20:16:02Z*

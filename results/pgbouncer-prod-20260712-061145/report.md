# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T05:23:36Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260712-061145` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.89 RPS (per instance) |
| **Total throughput** | 15.54 RPS (all instances) |
| **p50 latency** | 29540.25 ms |
| **p95 latency** | 40353.75 ms |
| **p99 latency** | 48996.25 ms |
| **p999 latency** | 67837.75 ms |
| **Error rate** | 51.00% (0.51) |
| **Total requests** | 29799 |
| **Failed requests** | 15277 |
| **Total successful** | 14522 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.76 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 23277 |
| observed_client_backends_active_max | 34262 |
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
| OJP proxy-tier host_cpu (avg / peak) | 8.3% / 52.0% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 11.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.00 MiB / 34.00 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 2.0% / 2.9% / 5.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.00 MiB / 34.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 1.9% / 2.9% / 4.8% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 22.00 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.1% / 1.0% / 3.9% / 4.9% / 10.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 21.1% / 107.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 16.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.00 MiB / 56.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.13% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 38 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (40353.75 ms) |
| Error rate | < 0.1% | ❌ FAIL (51.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.83 RPS (all instances) |
| **Achieved throughput** | 15.54 RPS (all instances) |
| **Attempted − achieved gap** | 15.29 RPS (49.58%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29442.047 | 40206.335 | 47972.351 | 4.203177088513776 | 47.22% | 0.15007503751875936 | 10 |
| 1 | 29605.887 | 40370.175 | 50036.735 | 3.7549893524810325 | 52.89% | 0.1002004008016032 | 11 |
| 2 | 29540.351 | 40435.711 | 48037.887 | 3.699409080484653 | 53.66% | 0.10022551368400962 | 7 |
| 3 | 29573.119 | 40402.943 | 49938.431 | 3.8861989100234178 | 51.29% | 0.15 | 10 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 3516 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=240) |
| 1 | SQLTransientConnectionException | 3939 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=240) |
| 2 | SQLTransientConnectionException | 3998 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=239) |
| 3 | SQLTransientConnectionException | 3824 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=239) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T05:23:36Z → 2026-07-12T05:38:36Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 23277 / 34262 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 465475600 | Cumulative since stats reset |
| Transactions rolled back | 4891 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6417 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 501071 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T05:23:36Z → 2026-07-12T05:38:36Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 2.6 | 2.0 | 3.9 | 5.8 | 33.3 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.5 | 2.9 | 4.9 | 32.5 | 48.0 | 11.3 | 11.3 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 2.5 | 2.0 | 3.9 | 4.9 | 33.3 | 11.3 | 11.3 |
| PostgreSQL | db | 243.3 | 244.0 | 293.9 | 305.5 | 330.8 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 15407.2 | 17009.1 |
| HAProxy | lb | 0.5 | 0.0 | 1.9 | 2.9 | 4.8 | 13.2 | 4.8 | 35.9 | 61.5 | 100.5 | 22.0 | 22.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T05:41:43Z*

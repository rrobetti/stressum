# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-22T14:36:12Z |
| **Duration** | 1800 s |
| **Instances**| 4 |
| **Target RPS**| 5 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260522-152318` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.80 RPS (per instance) |
| **Total throughput** | 3.20 RPS (all instances) |
| **p50 latency** | 29040.75 ms |
| **p95 latency** | 60031.00 ms |
| **p99 latency** | 60031.00 ms |
| **p999 latency** | 65446.00 ms |
| **Error rate** | 80.00% (0.80) |
| **Total requests** | 36621 |
| **Failed requests** | 29414 |
| **Total successful** | 7207 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 25 |
| observed_postgres_backends_avg_numbackends | 21.86 |
| observed_postgres_backends_median_numbackends | 23 |
| observed_client_backends_active_median | 17235 |
| observed_client_backends_active_max | 26940 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.2% / 0.0% / 31.3% / 49.6% / 79.1% |
| OJP proxy-tier host_cpu (avg / peak) | 17.1% / 92.0% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 125.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 5 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.2% / 0.0% / 31.3% / 49.6% / 79.1% |
| PgBouncer tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.5% / 0.0% / 25.1% / 39.2% / 61.6% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 22.10 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 14.5% / 1.0% / 56.4% / 89.0% / 136.6% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 27.1% / 163.1% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 187.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.30 MiB / 56.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.13% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 14584 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 150 ms | ❌ FAIL (60031.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (80.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.97 RPS (all instances) |
| **Achieved throughput** | 3.20 RPS (all instances) |
| **Attempted − achieved gap** | 12.77 RPS (79.98%) |
| **Total attempted ops** | 42004 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.54 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 28852.223 | 60030.975 | 60030.975 | 0.8261593170416313 | 79.65% | 0.15007503751875936 | 3502 |
| 1 | 29130.751 | 60030.975 | 60030.975 | 0.7587536041904839 | 81.31% | 0.10080645161290322 | 3635 |
| 2 | 28934.143 | 60030.975 | 60030.975 | 0.844340655978189 | 79.20% | 0.15007503751875936 | 4181 |
| 3 | 29245.439 | 60030.975 | 60030.975 | 0.7667358162743113 | 81.11% | 0.10015022533800699 | 3266 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7294 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=150) |
| 1 | SQLTransientConnectionException | 7444 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=4, active=4, idle=0, waiting=150) |
| 2 | SQLTransientConnectionException | 7251 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=150) |
| 3 | SQLTransientConnectionException | 7425 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=3, active=3, idle=0, waiting=150) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-22T14:36:12Z → 2026-05-22T15:06:12Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 23 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 17235 / 26940 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 516135593 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6607 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 669749 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-22T14:36:12Z → 2026-05-22T15:06:12Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 2.4 | 0.0 | 14.7 | 23.5 | 42.0 | 5.5 | 2.0 | 21.6 | 33.8 | 63.4 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 2.9 | 0.0 | 15.6 | 19.6 | 33.1 | 6.2 | 2.9 | 21.6 | 33.2 | 53.9 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 3.0 | 0.0 | 17.6 | 29.2 | 50.6 | 5.8 | 2.9 | 22.9 | 35.5 | 56.2 | 11.4 | 11.4 |
| PostgreSQL | db | 298.2 | 306.7 | 333.6 | 341.1 | 347.3 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 111785.5 | 121840.0 |
| HAProxy | lb | 6.5 | 0.0 | 25.1 | 39.2 | 61.6 | 10.4 | 3.9 | 31.8 | 49.8 | 77.2 | 22.0 | 22.1 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-22T15:09:21Z*

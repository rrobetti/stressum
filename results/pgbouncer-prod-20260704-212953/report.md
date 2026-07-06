# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-04T20:41:44Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260704-212953` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.92 RPS (per instance) |
| **Total throughput** | 15.67 RPS (all instances) |
| **p50 latency** | 1494.79 ms |
| **p95 latency** | 17965.05 ms |
| **p99 latency** | 25567.25 ms |
| **p999 latency** | 39051.25 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 14443 |
| **Failed requests** | 29 |
| **Total successful** | 14414 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 17.29 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 20989 |
| observed_client_backends_active_max | 32293 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 2.9% / 3.9% |
| OJP proxy-tier host_cpu (avg / peak) | 11.2% / 71.7% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 8.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.00 MiB / 33.90 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 2.9% / 3.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.00 MiB / 33.90 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 2.9% |
| HAProxy RSS (avg / peak, summed) | 22.10 MiB / 22.10 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.2% / 1.0% / 3.9% / 4.9% / 5.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.3% / 103.9% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 11.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.10 MiB / 56.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.14% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 33 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (17965.05 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.66 RPS (all instances) |
| **Achieved throughput** | 15.67 RPS (all instances) |
| **Attempted − achieved gap** | -0.01 RPS (-0.07%) |
| **Total attempted ops** | 14404 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 1441.791 | 16875.519 | 25837.567 | 3.9091683027259934 | 0.22% | 0.1002757646372702 | 8 |
| 1 | 1126.399 | 20168.703 | 27000.831 | 3.9076611639015426 | 0.25% | 0.15007503751875936 | 9 |
| 2 | 1363.967 | 17924.095 | 25051.135 | 3.931559242217858 | 0.17% | 0.15015015015015015 | 9 |
| 3 | 2046.975 | 16891.903 | 24379.391 | 3.918288423831276 | 0.17% | 0.15 | 7 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 8 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=7, active=7, idle=0, waiting=50) |
| 1 | SQLTransientConnectionException | 9 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=7, active=7, idle=0, waiting=75) |
| 2 | SQLTransientConnectionException | 6 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=13, active=13, idle=0, waiting=49) |
| 3 | SQLTransientConnectionException | 6 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=8, active=8, idle=0, waiting=76) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-04T20:41:44Z → 2026-07-04T20:56:44Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 20989 / 32293 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 439004994 | Cumulative since stats reset |
| Transactions rolled back | 4304 | Non-zero → contention or application errors |
| Temp file bytes written | 2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5378 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 395995 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-04T20:41:44Z → 2026-07-04T20:56:44Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.4 | 2.0 | 3.9 | 33.2 | 34.3 | 11.3 | 11.3 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 4.4 | 2.9 | 19.6 | 33.5 | 37.9 | 11.4 | 11.3 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.6 | 2.9 | 4.9 | 33.3 | 63.4 | 11.3 | 11.3 |
| PostgreSQL | db | 219.6 | 248.7 | 322.0 | 337.6 | 343.6 | 352.0 | 400.0 | 400.0 | 400.0 | 400.0 | 14777.1 | 17217.3 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 2.9 | 2.9 | 4.3 | 3.9 | 5.8 | 34.0 | 35.0 | 22.1 | 22.1 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-04T20:59:37Z*

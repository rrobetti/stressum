# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-01T21:29:51Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260701-221800` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.49 RPS (per instance) |
| **Total throughput** | 13.97 RPS (all instances) |
| **p50 latency** | 23.97 ms |
| **p95 latency** | 15159.30 ms |
| **p99 latency** | 22929.40 ms |
| **p999 latency** | 35811.50 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 14476 |
| **Failed requests** | 22 |
| **Total successful** | 14454 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.95 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 21202 |
| observed_client_backends_active_max | 32765 |
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
| OJP proxy-tier host_cpu (avg / peak) | 11.9% / 89.8% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 9.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 2.9% / 3.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 3.9% |
| HAProxy RSS (avg / peak, summed) | 21.90 MiB / 21.90 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.2% / 1.0% / 2.9% / 4.9% / 7.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.7% / 95.6% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 13.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.00 MiB / 56.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.14% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 37 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (15159.30 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 13.92 RPS (all instances) |
| **Achieved throughput** | 13.97 RPS (all instances) |
| **Attempted − achieved gap** | -0.05 RPS (-0.35%) |
| **Total attempted ops** | 14404 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 21.311 | 18038.783 | 24035.327 | 3.4754972615977824 | 0.36% | 0.15015015015015015 | 10 |
| 1 | 19.327 | 12992.511 | 21430.271 | 3.495493162189143 | 0.08% | 0.1502253380070105 | 9 |
| 2 | 27.295 | 16203.775 | 23412.735 | 3.502669369122473 | 0.14% | 0.1002004008016032 | 10 |
| 3 | 27.951 | 13402.111 | 22839.295 | 3.498341670081254 | 0.03% | 0.1502253380070105 | 8 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 13 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=76) |
| 1 | SQLTransientConnectionException | 3 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=83) |
| 2 | SQLTransientConnectionException | 5 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=60) |
| 3 | SQLTransientConnectionException | 1 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=10, active=10, idle=0, waiting=53) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-01T21:29:51Z → 2026-07-01T21:44:51Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21202 / 32765 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 439825765 | Cumulative since stats reset |
| Transactions rolled back | 4387 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5440 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 400411 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-01T21:29:51Z → 2026-07-01T21:44:51Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 6.6 | 2.9 | 32.4 | 33.3 | 84.9 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.2 | 2.9 | 3.9 | 32.4 | 33.3 | 11.3 | 11.3 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 2.4 | 2.0 | 3.0 | 4.9 | 5.8 | 11.4 | 11.4 |
| PostgreSQL | db | 213.6 | 248.4 | 324.2 | 339.5 | 349.6 | 340.6 | 399.6 | 400.0 | 400.0 | 400.0 | 14672.3 | 16932.0 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 2.9 | 3.9 | 4.9 | 3.9 | 8.8 | 34.3 | 63.7 | 21.9 | 21.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-01T21:47:34Z*

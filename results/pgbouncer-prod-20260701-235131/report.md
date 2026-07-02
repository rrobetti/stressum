# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-01T23:03:22Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260701-235131` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.48 RPS (per instance) |
| **Total throughput** | 13.92 RPS (all instances) |
| **p50 latency** | 13.23 ms |
| **p95 latency** | 13606.92 ms |
| **p99 latency** | 19935.22 ms |
| **p999 latency** | 35819.50 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 14460 |
| **Failed requests** | 19 |
| **Total successful** | 14441 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 16.93 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 21528 |
| observed_client_backends_active_max | 32620 |
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
| OJP proxy-tier host_cpu (avg / peak) | 17.2% / 96.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 8.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 2.9% / 3.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 3.9% |
| HAProxy RSS (avg / peak, summed) | 21.80 MiB / 21.80 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.1% / 1.0% / 2.9% / 4.9% / 7.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 21.2% / 130.3% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 12.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.20 MiB / 56.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.13% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 34 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (13606.92 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 13.89 RPS (all instances) |
| **Achieved throughput** | 13.92 RPS (all instances) |
| **Attempted − achieved gap** | -0.04 RPS (-0.26%) |
| **Total attempted ops** | 14403 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 13.735 | 10870.783 | 16957.439 | 3.480305249364064 | 0.00% | 0.10025062656641603 | 6 |
| 1 | 13.023 | 12107.775 | 17727.487 | 3.4853423651901796 | 0.03% | 0.15015015015015015 | 10 |
| 2 | 12.351 | 11165.695 | 18268.159 | 3.4929031086451285 | 0.00% | 0.10025062656641603 | 9 |
| 3 | 13.799 | 20283.391 | 26787.839 | 3.4662045060658584 | 0.50% | 0.15007503751875936 | 9 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 1 | SQLTransientConnectionException | 1 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=37) |
| 3 | SQLTransientConnectionException | 18 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=97) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-01T23:03:22Z → 2026-07-01T23:18:22Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21528 / 32620 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 437924717 | Cumulative since stats reset |
| Transactions rolled back | 4251 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5214 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 377684 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-01T23:03:22Z → 2026-07-01T23:18:22Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 6.9 | 2.9 | 32.5 | 33.5 | 60.5 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 7.7 | 2.9 | 33.5 | 38.0 | 90.6 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 2.9 | 2.0 | 3.9 | 32.4 | 33.5 | 11.5 | 11.5 |
| PostgreSQL | db | 208.5 | 246.4 | 325.8 | 342.8 | 346.6 | 333.1 | 399.6 | 400.0 | 400.0 | 400.0 | 14624.3 | 16909.0 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 2.9 | 3.9 | 4.1 | 3.9 | 5.8 | 33.8 | 35.8 | 21.8 | 21.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-01T23:21:08Z*

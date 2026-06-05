# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-31T08:04:03Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260531-085132` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.92 RPS (per instance) |
| **Total throughput** | 1.84 RPS (all instances) |
| **p50 latency** | 29392.90 ms |
| **p95 latency** | 60031.00 ms |
| **p99 latency** | 60031.00 ms |
| **p999 latency** | 62488.50 ms |
| **Error rate** | 89.00% (0.89) |
| **Total requests** | 22339 |
| **Failed requests** | 19843 |
| **Total successful** | 2496 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 25 |
| observed_postgres_backends_avg_numbackends | 21.98 |
| observed_postgres_backends_median_numbackends | 23 |
| observed_client_backends_active_median | 14633 |
| observed_client_backends_active_max | 20433 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | pgbouncer-prod |
| Configured replicas | 2 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.1% / 0.0% / 1.0% / 2.0% / 2.9% |
| OJP proxy-tier host_cpu (avg / peak) | 13.4% / 67.1% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 6.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.40 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 5 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.1% / 0.0% / 1.0% / 2.0% / 2.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.40 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.1% / 0.0% / 1.0% / 1.9% / 3.9% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 22.00 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.9% / 2.9% / 4.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.9% / 70.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 10.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.40 MiB / 56.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.18% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 10 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (60031.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (89.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.94 RPS (all instances) |
| **Achieved throughput** | 1.84 RPS (all instances) |
| **Attempted − achieved gap** | 14.10 RPS (88.45%) |
| **Total attempted ops** | 28802 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.31 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29392.895 | 60030.975 | 60030.975 | 0.8649357128413434 | 89.51% | 0.20020020020020018 | 6 |
| 1 | 29392.895 | 60030.975 | 60030.975 | 0.9771087911747297 | 88.14% | 0.15007503751875936 | 4 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 10000 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=359) |
| 1 | SQLTransientConnectionException | 9843 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=360) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-31T08:04:03Z → 2026-05-31T08:19:03Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 23 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 14633 / 20433 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 429851352 | Cumulative since stats reset |
| Transactions rolled back | 890 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3554 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 362471 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-31T08:04:03Z → 2026-05-31T08:19:03Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.0 | 0.0 | 0.0 | 1.0 | 2.0 | 2.6 | 2.0 | 2.9 | 13.7 | 33.2 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.0 | 0.0 | 0.0 | 1.0 | 2.0 | 2.6 | 2.0 | 2.9 | 31.4 | 35.6 | 11.5 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.0 | 0.0 | 0.0 | 1.0 | 2.9 | 8.6 | 2.9 | 33.2 | 35.1 | 60.5 | 11.5 | 11.5 |
| PostgreSQL | db | 198.8 | 199.7 | 227.3 | 237.8 | 268.0 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 45158.0 | 50330.1 |
| HAProxy | lb | 0.1 | 0.0 | 1.0 | 1.9 | 3.9 | 3.6 | 2.9 | 4.8 | 26.2 | 34.8 | 22.0 | 22.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T08:22:00Z*

# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T03:49:30Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260712-043740` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.13 RPS (per instance) |
| **Total throughput** | 16.51 RPS (all instances) |
| **p50 latency** | 29474.75 ms |
| **p95 latency** | 39698.25 ms |
| **p99 latency** | 46416.00 ms |
| **p999 latency** | 66429.00 ms |
| **Error rate** | 48.00% (0.48) |
| **Total requests** | 29761 |
| **Failed requests** | 14341 |
| **Total successful** | 15420 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.57 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 23557 |
| observed_client_backends_active_max | 34801 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 2.0% / 3.9% / 4.9% |
| OJP proxy-tier host_cpu (avg / peak) | 9.4% / 67.7% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 11.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.10 MiB / 34.00 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.5% / 0.0% / 2.0% / 3.9% / 4.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.10 MiB / 34.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 3.9% / 7.8% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 22.00 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.1% / 1.0% / 3.9% / 6.8% / 12.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 27.6% / 131.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 19.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.10 MiB / 56.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.13% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 39 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (39698.25 ms) |
| Error rate | < 0.1% | ❌ FAIL (48.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.84 RPS (all instances) |
| **Achieved throughput** | 16.51 RPS (all instances) |
| **Attempted − achieved gap** | 14.33 RPS (46.47%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29573.119 | 39813.119 | 45219.839 | 4.142862345151416 | 48.09% | 0.15 | 10 |
| 1 | 29605.887 | 39911.423 | 46039.039 | 3.88680758533285 | 51.27% | 0.10010010010010009 | 7 |
| 2 | 29212.671 | 39288.831 | 47874.047 | 4.388202441265146 | 44.84% | 0.15 | 11 |
| 3 | 29507.583 | 39780.351 | 46530.559 | 4.0898045792121565 | 48.54% | 0.10010010010010009 | 11 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 3584 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=240) |
| 1 | SQLTransientConnectionException | 3814 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=15, active=15, idle=0, waiting=222) |
| 2 | SQLTransientConnectionException | 3336 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=240) |
| 3 | SQLTransientConnectionException | 3607 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=13, active=13, idle=0, waiting=240) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T03:49:30Z → 2026-07-12T04:04:30Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 23557 / 34801 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 491347397 | Cumulative since stats reset |
| Transactions rolled back | 4867 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6815 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 694807 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T03:49:30Z → 2026-07-12T04:04:30Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.0 | 2.0 | 3.9 | 32.4 | 34.1 | 11.3 | 11.3 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 3.4 | 2.0 | 4.9 | 32.4 | 34.5 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.2 | 2.9 | 4.8 | 32.4 | 34.1 | 11.4 | 11.3 |
| PostgreSQL | db | 247.2 | 247.8 | 294.9 | 310.1 | 322.9 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 15395.6 | 17213.2 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 3.9 | 7.8 | 18.8 | 7.8 | 52.2 | 84.9 | 102.0 | 22.0 | 22.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T04:07:40Z*

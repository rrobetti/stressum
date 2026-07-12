# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T08:32:41Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260712-092051` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.92 RPS (per instance) |
| **Total throughput** | 19.68 RPS (all instances) |
| **p50 latency** | 29298.75 ms |
| **p95 latency** | 37863.50 ms |
| **p99 latency** | 44277.75 ms |
| **p999 latency** | 60465.00 ms |
| **Error rate** | 38.00% (0.38) |
| **Total requests** | 29765 |
| **Failed requests** | 11394 |
| **Total successful** | 18371 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.87 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 27006 |
| observed_client_backends_active_max | 40237 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.9% / 3.9% / 5.9% |
| OJP proxy-tier host_cpu (avg / peak) | 8.2% / 42.1% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 11.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.50 MiB / 34.40 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.9% / 3.9% / 5.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.50 MiB / 34.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.7% / 0.0% / 2.9% / 3.9% / 5.8% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 22.00 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.3% / 1.0% / 3.9% / 6.8% / 11.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 19.3% / 105.9% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 17.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.50 MiB / 56.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.14% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 42 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (37863.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (38.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.86 RPS (all instances) |
| **Achieved throughput** | 19.68 RPS (all instances) |
| **Attempted − achieved gap** | 11.18 RPS (36.22%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29245.439 | 37879.807 | 45088.767 | 5.060919264861905 | 36.37% | 0.10025062656641603 | 11 |
| 1 | 29474.815 | 37978.111 | 43286.527 | 4.962308528934298 | 37.83% | 0.15 | 10 |
| 2 | 29310.975 | 38043.647 | 44957.695 | 4.760044732434761 | 40.27% | 0.15015015015015015 | 11 |
| 3 | 29163.519 | 37552.127 | 43778.047 | 4.897170165923858 | 38.64% | 0.15015015015015015 | 10 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2705 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=240) |
| 1 | SQLTransientConnectionException | 2818 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=240) |
| 2 | SQLTransientConnectionException | 2999 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=236) |
| 3 | SQLTransientConnectionException | 2872 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=231) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T08:32:41Z → 2026-07-12T08:47:41Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 27006 / 40237 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 551431623 | Cumulative since stats reset |
| Transactions rolled back | 5402 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7507 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 738140 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T08:32:41Z → 2026-07-12T08:47:41Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.1 | 2.9 | 4.9 | 32.4 | 33.5 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 2.6 | 2.0 | 3.9 | 5.9 | 32.5 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 4.9 | 2.7 | 2.9 | 3.9 | 5.9 | 34.1 | 11.5 | 11.4 |
| PostgreSQL | db | 300.3 | 303.4 | 359.6 | 364.1 | 370.4 | 399.9 | 400.0 | 400.0 | 400.0 | 400.0 | 14427.9 | 16336.7 |
| HAProxy | lb | 0.7 | 0.0 | 2.9 | 3.9 | 5.8 | 11.4 | 4.8 | 34.3 | 36.5 | 99.0 | 22.0 | 22.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T08:50:54Z*

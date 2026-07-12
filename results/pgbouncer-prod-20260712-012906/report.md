# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T00:40:55Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260712-012906` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.82 RPS (per instance) |
| **Total throughput** | 15.28 RPS (all instances) |
| **p50 latency** | 7011.32 ms |
| **p95 latency** | 24363.03 ms |
| **p99 latency** | 31576.00 ms |
| **p999 latency** | 47300.75 ms |
| **Error rate** | 2.00% (0.02) |
| **Total requests** | 14456 |
| **Failed requests** | 256 |
| **Total successful** | 14200 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 18.07 |
| observed_postgres_backends_median_numbackends | 19 |
| observed_client_backends_active_median | 21780 |
| observed_client_backends_active_max | 33041 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 2.9% / 4.9% |
| OJP proxy-tier host_cpu (avg / peak) | 8.9% / 72.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 8.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 2.9% / 4.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 6.8% |
| HAProxy RSS (avg / peak, summed) | 22.20 MiB / 22.20 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.1% / 1.0% / 3.9% / 4.9% / 11.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 27.6% / 130.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 15.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.30 MiB / 56.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.13% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 29 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (24363.03 ms) |
| Error rate | < 0.1% | ❌ FAIL (2.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.50 RPS (all instances) |
| **Achieved throughput** | 15.28 RPS (all instances) |
| **Attempted − achieved gap** | 0.22 RPS (1.41%) |
| **Total attempted ops** | 14404 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 7892.991 | 29917.183 | 37126.143 | 3.680499245369116 | 5.00% | 0.1002004008016032 | 10 |
| 1 | 5820.415 | 20103.167 | 27033.599 | 3.8808856689359006 | 0.25% | 0.15015015015015015 | 7 |
| 2 | 7385.087 | 24068.095 | 30375.935 | 3.857838490045678 | 0.89% | 0.1002004008016032 | 6 |
| 3 | 6946.815 | 23363.583 | 31768.575 | 3.8623330261309112 | 0.94% | 0.1500750375187594 | 6 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 181 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=84) |
| 1 | SQLTransientConnectionException | 9 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=63) |
| 2 | SQLTransientConnectionException | 32 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=76) |
| 3 | SQLTransientConnectionException | 34 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=99) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T00:40:55Z → 2026-07-12T00:55:55Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 19 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21780 / 33041 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 427451474 | Cumulative since stats reset |
| Transactions rolled back | 4468 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5440 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 406748 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T00:40:55Z → 2026-07-12T00:55:55Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.1 | 2.9 | 3.9 | 32.4 | 33.3 | 11.3 | 11.3 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.0 | 2.0 | 3.9 | 32.4 | 36.3 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.0 | 2.9 | 3.9 | 31.7 | 35.5 | 11.4 | 11.4 |
| PostgreSQL | db | 228.6 | 242.5 | 299.8 | 313.1 | 319.6 | 381.4 | 400.0 | 400.0 | 400.0 | 400.0 | 15060.3 | 17065.6 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 2.9 | 6.8 | 19.3 | 6.8 | 53.9 | 93.2 | 116.5 | 22.2 | 22.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T00:59:03Z*

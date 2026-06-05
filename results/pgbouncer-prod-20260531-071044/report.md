# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-31T06:23:24Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260531-071044` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.28 RPS (per instance) |
| **Total throughput** | 2.57 RPS (all instances) |
| **p50 latency** | 28573.70 ms |
| **p95 latency** | 60031.00 ms |
| **p99 latency** | 60031.00 ms |
| **p999 latency** | 61817.00 ms |
| **Error rate** | 77.00% (0.77) |
| **Total requests** | 14883 |
| **Failed requests** | 11403 |
| **Total successful** | 3480 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 25 |
| observed_postgres_backends_avg_numbackends | 21.72 |
| observed_postgres_backends_median_numbackends | 23 |
| observed_client_backends_active_median | 15348 |
| observed_client_backends_active_max | 21144 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 2.0% / 2.9% |
| OJP proxy-tier host_cpu (avg / peak) | 16.4% / 138.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 6.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 5 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 2.0% / 2.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 1.9% / 2.9% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 21.90 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.9% / 2.9% / 4.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 20.5% / 138.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 9.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.30 MiB / 56.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 12 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (60031.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (77.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 10.63 RPS (all instances) |
| **Achieved throughput** | 2.57 RPS (all instances) |
| **Attempted − achieved gap** | 8.06 RPS (75.84%) |
| **Total attempted ops** | 19202 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.20 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 28688.383 | 60030.975 | 60030.975 | 1.190395361812294 | 78.30% | 0.15022533800701052 | 6 |
| 1 | 28459.007 | 60030.975 | 60030.975 | 1.3778475762576272 | 74.94% | 0.14992503748125938 | 6 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 5820 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=240) |
| 1 | SQLTransientConnectionException | 5583 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=240) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-31T06:23:24Z → 2026-05-31T06:38:24Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 23 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 15348 / 21144 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 473161739 | Cumulative since stats reset |
| Transactions rolled back | 1079 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3742 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 382345 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-31T06:23:24Z → 2026-05-31T06:38:24Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.1 | 0.0 | 1.0 | 1.0 | 2.0 | 3.1 | 2.9 | 3.9 | 32.2 | 34.3 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.0 | 0.0 | 0.0 | 1.0 | 2.0 | 3.8 | 2.9 | 4.9 | 33.3 | 51.7 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.1 | 0.0 | 1.0 | 1.0 | 2.9 | 9.8 | 2.9 | 33.3 | 47.3 | 132.3 | 11.5 | 11.5 |
| PostgreSQL | db | 195.8 | 199.6 | 222.3 | 233.2 | 247.9 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 41537.5 | 48363.6 |
| HAProxy | lb | 0.2 | 0.0 | 1.0 | 1.9 | 2.9 | 4.3 | 2.9 | 5.8 | 33.3 | 35.8 | 22.0 | 21.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T06:41:25Z*

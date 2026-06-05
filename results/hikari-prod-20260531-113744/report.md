# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-31T10:49:59Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260531-113744` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.93 RPS (per instance) |
| **Total throughput** | 1.86 RPS (all instances) |
| **p50 latency** | 29712.40 ms |
| **p95 latency** | 60031.00 ms |
| **p99 latency** | 60031.00 ms |
| **p999 latency** | 60031.00 ms |
| **Error rate** | 89.00% (0.89) |
| **Total requests** | 22353 |
| **Failed requests** | 19838 |
| **Total successful** | 2515 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 75 |
| observed_postgres_backends_max_numbackends | 93 |
| observed_postgres_backends_avg_numbackends | 84.86 |
| observed_postgres_backends_median_numbackends | 84 |
| observed_client_backends_active_median | 13322 |
| observed_client_backends_active_max | 18307 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | hikari-prod |
| Configured replicas | 2 |
| Configured client pool size (per replica) | 38 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| OJP proxy-tier host_cpu (avg / peak) | N/A% / N/A% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 0% |
| OJP proxy-tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| PgBouncer tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | N/A% / N/A% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 0.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | N/A MiB / 0.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.18% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 24 ms | `GarbageCollectorMXBean.getCollectionTime()` |

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
| **Achieved throughput** | 1.86 RPS (all instances) |
| **Attempted − achieved gap** | 14.09 RPS (88.36%) |
| **Total attempted ops** | 28802 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.18 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 29736.959 | 60030.975 | 60030.975 | 0.9047897028142207 | 89.03% | 0.2004008016032064 | 12 |
| 1 | 29687.807 | 60030.975 | 60030.975 | 0.9512837903160934 | 88.46% | 0.15015015015015015 | 12 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 9953 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=38, active=38, idle=0, waiting=358) |
| 1 | SQLTransientConnectionException | 9885 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=38, active=38, idle=0, waiting=358) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-31T10:49:59Z → 2026-05-31T11:04:59Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 84 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 13322 / 18307 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 441410744 | Cumulative since stats reset |
| Transactions rolled back | 791 | Non-zero → contention or application errors |
| Temp file bytes written | -6 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 2801 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 296012 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-31T10:49:59Z → 2026-05-31T11:04:59Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 183.1 | 184.5 | 199.7 | 206.8 | 206.8 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 102092.3 | 114924.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-31T11:07:56Z*

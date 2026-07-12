# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T04:51:54Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260712-054017` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.34 RPS (per instance) |
| **Total throughput** | 13.37 RPS (all instances) |
| **p50 latency** | 28799.00 ms |
| **p95 latency** | 90980.50 ms |
| **p99 latency** | 205373.75 ms |
| **p999 latency** | 242548.75 ms |
| **Error rate** | 58.00% (0.58) |
| **Total requests** | 29744 |
| **Failed requests** | 17239 |
| **Total successful** | 12505 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 80 |
| observed_postgres_backends_max_numbackends | 90 |
| observed_postgres_backends_avg_numbackends | 87.53 |
| observed_postgres_backends_median_numbackends | 88 |
| observed_client_backends_active_median | 20347 |
| observed_client_backends_active_max | 28537 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | hikari-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 20 |
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
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 51 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (90980.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (58.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 30.81 RPS (all instances) |
| **Achieved throughput** | 13.37 RPS (all instances) |
| **Attempted − achieved gap** | 17.43 RPS (56.59%) |
| **Total attempted ops** | 28803 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 28688.383 | 92078.079 | 132972.543 | 3.546497512852845 | 55.38% | 0.15037593984962408 | 12 |
| 1 | 28934.143 | 96403.455 | 234487.807 | 3.059870140009647 | 61.48% | 0.15 | 14 |
| 2 | 28770.303 | 83230.719 | 232390.655 | 3.4170903716125887 | 57.08% | 0.15030060120240482 | 12 |
| 3 | 28803.071 | 92209.151 | 221642.751 | 3.3507806367017965 | 57.90% | 0.15 | 13 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 4115 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=20, active=20, idle=0, waiting=236) |
| 1 | SQLTransientConnectionException | 4567 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=20, active=20, idle=0, waiting=239) |
| 2 | SQLTransientConnectionException | 4249 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=20, active=20, idle=0, waiting=240) |
| 3 | SQLTransientConnectionException | 4308 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=20, active=20, idle=0, waiting=240) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T04:51:54Z → 2026-07-12T05:06:54Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 88 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 20347 / 28537 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 484734801 | Cumulative since stats reset |
| Transactions rolled back | 4307 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5848 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 481169 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T04:51:54Z → 2026-07-12T05:06:54Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 208.7 | 210.4 | 231.7 | 238.1 | 238.1 | 400.0 | 400.0 | 400.0 | 400.0 | 400.0 | 35709.0 | 39111.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T05:09:56Z*

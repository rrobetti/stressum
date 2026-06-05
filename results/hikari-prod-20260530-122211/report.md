# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T11:33:59Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260530-122211` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.67 RPS (per instance) |
| **Total throughput** | 1.34 RPS (all instances) |
| **p50 latency** | 5.69 ms |
| **p95 latency** | 11792.40 ms |
| **p99 latency** | 33382.40 ms |
| **p999 latency** | 48496.65 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 1809 |
| **Failed requests** | 0 |
| **Total successful** | 1809 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 75 |
| observed_postgres_backends_max_numbackends | 55 |
| observed_postgres_backends_avg_numbackends | 43.32 |
| observed_postgres_backends_median_numbackends | 41 |
| observed_client_backends_active_median | 16654 |
| observed_client_backends_active_max | 24071 |
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
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 37 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (11792.40 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 1.33 RPS (all instances) |
| **Achieved throughput** | 1.34 RPS (all instances) |
| **Attempted − achieved gap** | -0.01 RPS (-0.39%) |
| **Total attempted ops** | 2402 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.27 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5.587 | 11681.791 | 31899.647 | 0.6691869748381256 | 0.00% | 0.15022533800701052 | 18 |
| 1 | 5.791 | 11902.975 | 34865.151 | 0.670355970131012 | 0.00% | 0.1500750375187594 | 19 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T11:33:59Z → 2026-05-30T11:48:59Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 41 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 16654 / 24071 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 171649161 | Cumulative since stats reset |
| Transactions rolled back | 839 | Non-zero → contention or application errors |
| Temp file bytes written | 3 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1500 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 152339 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T11:33:59Z → 2026-05-30T11:48:59Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 46.4 | 1.3 | 178.2 | 205.2 | 209.4 | 375.2 | 373.4 | 400.0 | 400.0 | 400.0 | 6637.7 | 17927.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-30T11:51:41Z*

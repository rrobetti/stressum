# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T13:44:40Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260530-143241` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.67 RPS (per instance) |
| **Total throughput** | 1.34 RPS (all instances) |
| **p50 latency** | 4.29 ms |
| **p95 latency** | 7507.95 ms |
| **p99 latency** | 27934.75 ms |
| **p999 latency** | 41009.15 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 1807 |
| **Failed requests** | 0 |
| **Total successful** | 1807 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 17.96 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 16012 |
| observed_client_backends_active_max | 23022 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 1.0% / 2.0% |
| OJP proxy-tier host_cpu (avg / peak) | 19.4% / 156.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 3.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.50 MiB / 34.50 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 5 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 1.0% / 2.0% |
| PgBouncer tier RSS (avg / peak, summed) | 34.50 MiB / 34.50 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 1.0% / 1.9% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 22.00 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.0% / 1.9% / 2.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 22.9% / 159.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 4.90% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.50 MiB / 56.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.10% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 7 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (7507.95 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 1.34 RPS (all instances) |
| **Achieved throughput** | 1.34 RPS (all instances) |
| **Attempted − achieved gap** | -0.00 RPS (-0.28%) |
| **Total attempted ops** | 2402 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.28 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.283 | 8421.375 | 27574.271 | 0.6724644408391226 | 0.00% | 0.10015022533800699 | 3 |
| 1 | 4.291 | 6594.559 | 28295.167 | 0.6721665722556734 | 0.00% | 0.10005002501250625 | 4 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T13:44:40Z → 2026-05-30T13:59:40Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 16012 / 23022 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 170755103 | Cumulative since stats reset |
| Transactions rolled back | 839 | Non-zero → contention or application errors |
| Temp file bytes written | 5 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -5 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1370 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 139011 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T13:44:40Z → 2026-05-30T13:59:40Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.1 | 0.0 | 1.0 | 1.0 | 1.0 | 5.4 | 2.9 | 32.4 | 34.1 | 100.5 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.1 | 0.0 | 1.0 | 1.0 | 1.0 | 4.0 | 2.9 | 14.7 | 33.3 | 91.2 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.1 | 0.0 | 1.0 | 1.0 | 1.0 | 10.3 | 3.0 | 33.5 | 47.1 | 86.8 | 11.5 | 11.5 |
| PostgreSQL | db | 62.1 | 1.3 | 214.5 | 230.6 | 252.1 | 327.3 | 308.1 | 400.0 | 400.0 | 400.0 | 26334.5 | 36148.3 |
| HAProxy | lb | 0.2 | 0.0 | 1.0 | 1.0 | 1.9 | 3.6 | 2.9 | 3.9 | 27.4 | 34.0 | 22.0 | 22.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-30T14:02:27Z*

# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T12:11:14Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260711-125925` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.00 RPS (per instance) |
| **Total throughput** | 4.00 RPS (all instances) |
| **p50 latency** | 2.58 ms |
| **p95 latency** | 1001.60 ms |
| **p99 latency** | 6514.18 ms |
| **p999 latency** | 10229.75 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 3604 |
| **Failed requests** | 0 |
| **Total successful** | 3604 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 13.67 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 14143 |
| observed_client_backends_active_max | 21165 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.0% / 2.0% / 2.9% |
| OJP proxy-tier host_cpu (avg / peak) | 10.5% / 53.7% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 6.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.0% / 2.0% / 2.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.0% / 1.9% / 1.9% |
| HAProxy RSS (avg / peak, summed) | 21.80 MiB / 21.80 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 4.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.5% / 72.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 7.90% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 55.90 MiB / 55.90 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.09% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 14 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (1001.60 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 4.00 RPS (all instances) |
| **Achieved throughput** | 4.00 RPS (all instances) |
| **Attempted − achieved gap** | 0.00 RPS (0.00%) |
| **Total attempted ops** | 3604 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 2.567 | 1332.223 | 4028.415 | 1.0005119156416324 | 0.00% | 0.10010010010010009 | 3 |
| 1 | 2.651 | 1447.935 | 6193.151 | 1.0001909354504968 | 0.00% | 0.10005002501250625 | 3 |
| 2 | 2.495 | 569.343 | 7630.847 | 1.0001498559717605 | 0.00% | 0.0501002004008016 | 4 |
| 3 | 2.627 | 656.895 | 8204.287 | 1.0004252640134486 | 0.00% | 0.10010010010010009 | 4 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T12:11:14Z → 2026-07-11T12:26:14Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 14143 / 21165 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 89413687 | Cumulative since stats reset |
| Transactions rolled back | 1295 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1333 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 133509 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T12:11:14Z → 2026-07-11T12:26:14Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.1 | 0.0 | 1.0 | 1.0 | 2.0 | 5.2 | 2.9 | 31.4 | 34.5 | 44.9 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.1 | 0.0 | 1.0 | 1.0 | 2.0 | 3.0 | 2.0 | 3.9 | 32.2 | 47.8 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.1 | 0.0 | 1.0 | 1.0 | 2.0 | 2.6 | 2.0 | 3.9 | 4.9 | 32.5 | 11.3 | 11.3 |
| PostgreSQL | db | 31.6 | 0.7 | 182.7 | 263.7 | 291.9 | 163.9 | 123.6 | 398.7 | 400.0 | 400.0 | 10877.7 | 15465.8 |
| HAProxy | lb | 0.3 | 0.0 | 1.0 | 1.9 | 1.9 | 4.1 | 2.9 | 4.8 | 33.0 | 38.8 | 21.8 | 21.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T12:28:49Z*

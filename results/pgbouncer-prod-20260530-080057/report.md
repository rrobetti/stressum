# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T07:12:55Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260530-080057` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.67 RPS (per instance) |
| **Total throughput** | 1.34 RPS (all instances) |
| **p50 latency** | 4.12 ms |
| **p95 latency** | 6590.45 ms |
| **p99 latency** | 26558.45 ms |
| **p999 latency** | 42696.70 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 1806 |
| **Failed requests** | 0 |
| **Total successful** | 1806 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 17.84 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 15986 |
| observed_client_backends_active_max | 22986 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 2.0% / 2.0% |
| OJP proxy-tier host_cpu (avg / peak) | 15.8% / 94.7% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 3.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.40 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 5 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 2.0% / 2.0% |
| PgBouncer tier RSS (avg / peak, summed) | 34.40 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 1.0% / 1.9% |
| HAProxy RSS (avg / peak, summed) | 22.10 MiB / 22.10 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.0% / 2.0% / 2.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 21.2% / 100.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 4.90% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.50 MiB / 56.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.10% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 7 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (6590.45 ms) |
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
| **Attempted − achieved gap** | -0.00 RPS (-0.22%) |
| **Total attempted ops** | 2402 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.33 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.049 | 6471.679 | 26214.399 | 0.6711234815180916 | 0.00% | 0.10025062656641603 | 4 |
| 1 | 4.199 | 6709.247 | 26902.527 | 0.6716541137512811 | 0.00% | 0.10010010010010009 | 3 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T07:12:55Z → 2026-05-30T07:27:55Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 15986 / 22986 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 171417950 | Cumulative since stats reset |
| Transactions rolled back | 835 | Non-zero → contention or application errors |
| Temp file bytes written | 4 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -4 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1365 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 138159 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T07:12:55Z → 2026-05-30T07:27:55Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.1 | 0.0 | 1.0 | 1.0 | 1.0 | 5.0 | 2.9 | 32.4 | 34.3 | 59.5 | 11.5 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.1 | 0.0 | 1.0 | 1.0 | 1.0 | 2.8 | 2.0 | 2.9 | 32.2 | 33.3 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.1 | 0.0 | 1.0 | 1.0 | 1.0 | 8.4 | 2.9 | 32.4 | 33.5 | 54.9 | 11.4 | 11.4 |
| PostgreSQL | db | 60.1 | 1.2 | 213.3 | 225.2 | 237.8 | 325.8 | 310.3 | 400.0 | 400.0 | 400.0 | 27361.5 | 35767.2 |
| HAProxy | lb | 0.2 | 0.0 | 1.0 | 1.0 | 1.9 | 5.5 | 3.9 | 29.3 | 34.1 | 35.9 | 22.1 | 22.1 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-30T07:30:40Z*

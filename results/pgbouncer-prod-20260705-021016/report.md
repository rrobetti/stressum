# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T01:22:05Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260705-021016` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.98 RPS (per instance) |
| **Total throughput** | 15.90 RPS (all instances) |
| **p50 latency** | 6.47 ms |
| **p95 latency** | 9486.33 ms |
| **p99 latency** | 16148.50 ms |
| **p999 latency** | 26984.50 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 14430 |
| **Failed requests** | 0 |
| **Total successful** | 14430 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.40 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 21655 |
| observed_client_backends_active_max | 33433 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 2.9% / 3.9% |
| OJP proxy-tier host_cpu (avg / peak) | 9.2% / 103.9% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 9.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 2.9% / 3.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.10 MiB / 34.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 1.0% / 1.9% / 2.9% / 3.9% |
| HAProxy RSS (avg / peak, summed) | 22.10 MiB / 22.10 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.2% / 1.0% / 2.9% / 4.9% / 6.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 13.1% / 108.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 13.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.20 MiB / 56.20 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.14% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 30 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (9486.33 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.88 RPS (all instances) |
| **Achieved throughput** | 15.90 RPS (all instances) |
| **Attempted − achieved gap** | -0.03 RPS (-0.18%) |
| **Total attempted ops** | 14404 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.831 | 8151.039 | 13303.807 | 3.9846716183914044 | 0.00% | 0.1502253380070105 | 9 |
| 1 | 6.651 | 9117.695 | 16089.087 | 3.9662211629998176 | 0.00% | 0.15015015015015015 | 9 |
| 2 | 6.207 | 9928.703 | 16736.255 | 3.9672981127011835 | 0.00% | 0.10025062656641603 | 6 |
| 3 | 6.199 | 10747.903 | 18464.767 | 3.9860691794393452 | 0.00% | 0.15007503751875936 | 6 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T01:22:05Z → 2026-07-05T01:37:05Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21655 / 33433 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 442674311 | Cumulative since stats reset |
| Transactions rolled back | 4287 | Non-zero → contention or application errors |
| Temp file bytes written | -7 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 7 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5039 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 366346 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T01:22:05Z → 2026-07-05T01:37:05Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.1 | 2.0 | 3.9 | 32.4 | 40.2 | 11.3 | 11.3 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 2.5 | 2.0 | 3.9 | 3.9 | 13.7 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 3.8 | 2.9 | 5.9 | 33.2 | 96.1 | 11.4 | 11.4 |
| PostgreSQL | db | 198.9 | 230.7 | 325.9 | 334.6 | 337.6 | 323.9 | 399.5 | 400.0 | 400.0 | 400.0 | 14486.3 | 17023.7 |
| HAProxy | lb | 0.6 | 1.0 | 1.9 | 2.9 | 3.9 | 4.1 | 3.9 | 4.9 | 32.4 | 36.5 | 22.1 | 22.1 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T01:39:47Z*

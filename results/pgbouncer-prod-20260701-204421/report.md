# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-01T19:56:13Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260701-204421` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.48 RPS (per instance) |
| **Total throughput** | 13.92 RPS (all instances) |
| **p50 latency** | 25.45 ms |
| **p95 latency** | 13998.08 ms |
| **p99 latency** | 21598.20 ms |
| **p999 latency** | 34357.25 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 14449 |
| **Failed requests** | 13 |
| **Total successful** | 14436 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 21 |
| observed_postgres_backends_avg_numbackends | 16.88 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 21308 |
| observed_client_backends_active_max | 32457 |
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
| OJP proxy-tier host_cpu (avg / peak) | 11.3% / 68.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 8.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 4 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 2.0% / 2.9% / 4.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.30 MiB / 34.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.6% / 0.0% / 1.9% / 2.9% / 3.9% |
| HAProxy RSS (avg / peak, summed) | 21.90 MiB / 22.00 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.2% / 1.0% / 2.9% / 4.9% / 8.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.6% / 71.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 12.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.20 MiB / 56.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.15% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 34 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (13998.08 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 13.89 RPS (all instances) |
| **Achieved throughput** | 13.92 RPS (all instances) |
| **Attempted − achieved gap** | -0.03 RPS (-0.22%) |
| **Total attempted ops** | 14404 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 26.079 | 12566.527 | 19611.647 | 3.479658675804581 | 0.00% | 0.15015015015015015 | 10 |
| 1 | 23.007 | 16957.439 | 24887.295 | 3.474554677908781 | 0.19% | 0.15015015015015015 | 9 |
| 2 | 28.495 | 15392.767 | 23838.719 | 3.474551440709984 | 0.17% | 0.15007503751875936 | 7 |
| 3 | 24.223 | 11075.583 | 18055.167 | 3.4945064927660043 | 0.00% | 0.15015015015015015 | 8 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 1 | SQLTransientConnectionException | 7 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=11, active=11, idle=0, waiting=79) |
| 2 | SQLTransientConnectionException | 6 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=10, active=10, idle=0, waiting=61) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-01T19:56:13Z → 2026-07-01T20:11:13Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21308 / 32457 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 435670320 | Cumulative since stats reset |
| Transactions rolled back | 4286 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5300 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 387180 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-01T19:56:13Z → 2026-07-01T20:11:13Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.2 | 0.0 | 1.0 | 2.0 | 2.0 | 6.0 | 2.9 | 32.4 | 33.5 | 35.1 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.2 | 0.0 | 1.0 | 2.0 | 2.9 | 3.0 | 2.0 | 3.9 | 32.4 | 35.3 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.2 | 0.0 | 1.0 | 2.0 | 3.9 | 2.6 | 2.0 | 3.9 | 4.9 | 33.3 | 11.5 | 11.5 |
| PostgreSQL | db | 217.2 | 250.5 | 324.3 | 337.7 | 350.0 | 343.6 | 399.6 | 400.0 | 400.0 | 400.0 | 14662.5 | 16893.8 |
| HAProxy | lb | 0.6 | 0.0 | 1.9 | 2.9 | 3.9 | 5.5 | 3.9 | 23.4 | 35.3 | 60.2 | 21.9 | 22.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-01T20:14:03Z*

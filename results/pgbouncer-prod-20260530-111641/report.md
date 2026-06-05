# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T10:28:42Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260530-111641` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.67 RPS (per instance) |
| **Total throughput** | 1.34 RPS (all instances) |
| **p50 latency** | 4.14 ms |
| **p95 latency** | 7014.40 ms |
| **p99 latency** | 28549.10 ms |
| **p999 latency** | 42778.65 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 1806 |
| **Failed requests** | 0 |
| **Total successful** | 1806 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 17.96 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 16106 |
| observed_client_backends_active_max | 23085 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 1.0% / 2.9% |
| OJP proxy-tier host_cpu (avg / peak) | 15.1% / 92.9% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 5.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 5 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 1.0% / 2.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.40 MiB / 34.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.2% / 0.0% / 1.0% / 1.0% / 1.9% |
| HAProxy RSS (avg / peak, summed) | 22.00 MiB / 22.00 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.3% / 0.0% / 1.0% / 1.9% / 2.9% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.4% / 96.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 7.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 56.40 MiB / 56.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.13% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 6 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (7014.40 ms) |
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
| **Total scheduling delay** | 0.43 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.231 | 6549.503 | 27607.039 | 0.6709863424928294 | 0.00% | 0.15007503751875936 | 3 |
| 1 | 4.057 | 7479.295 | 29491.199 | 0.6716885864265348 | 0.00% | 0.10005002501250625 | 3 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T10:28:42Z → 2026-05-30T10:43:42Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 16106 / 23085 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 171090914 | Cumulative since stats reset |
| Transactions rolled back | 835 | Non-zero → contention or application errors |
| Temp file bytes written | 4 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -4 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1366 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 138177 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T10:28:42Z → 2026-05-30T10:43:42Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.1 | 0.0 | 1.0 | 1.0 | 2.0 | 4.7 | 2.9 | 31.4 | 33.3 | 63.0 | 11.4 | 11.4 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.1 | 0.0 | 1.0 | 1.0 | 2.0 | 2.3 | 2.0 | 2.9 | 3.9 | 4.8 | 11.5 | 11.5 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.1 | 0.0 | 1.0 | 1.0 | 1.9 | 8.4 | 2.9 | 32.5 | 44.9 | 52.9 | 11.5 | 11.5 |
| PostgreSQL | db | 60.5 | 1.2 | 208.6 | 219.9 | 228.7 | 323.3 | 304.4 | 400.0 | 400.0 | 400.0 | 24842.6 | 34920.5 |
| HAProxy | lb | 0.2 | 0.0 | 1.0 | 1.0 | 1.9 | 3.4 | 2.9 | 3.9 | 4.8 | 34.0 | 22.0 | 22.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-30T10:46:31Z*

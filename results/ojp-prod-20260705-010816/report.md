# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T00:20:09Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260705-010816` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.72 RPS (per instance) |
| **Total throughput** | 14.86 RPS (all instances) |
| **p50 latency** | 6.12 ms |
| **p95 latency** | 4367.35 ms |
| **p99 latency** | 9820.15 ms |
| **p999 latency** | 19103.75 ms |
| **Error rate** | 7.00% (0.07) |
| **Total requests** | 14459 |
| **Failed requests** | 970 |
| **Total successful** | 13489 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 15.88 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 22048 |
| observed_client_backends_active_max | 33004 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 12 |
| OJP servers | 3 |
| Real DB connections per OJP server | 4 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.0% / 3.9% / 11.8% / 21.6% / 30.4% |
| OJP proxy-tier host_cpu (avg / peak) | 15.8% / 73.1% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 73.40% |
| OJP proxy-tier RSS (avg / peak, summed) | 655.20 MiB / 657.30 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.0% / 3.9% / 11.8% / 21.6% / 30.4% |
| PgBouncer tier RSS (avg / peak, summed) | 655.20 MiB / 657.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.0% / 3.9% / 11.8% / 21.6% / 30.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.8% / 73.1% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 73.40% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 655.20 MiB / 657.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.38% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 676 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4367.35 ms) |
| Error rate | < 0.1% | ❌ FAIL (7.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.87 RPS (all instances) |
| **Achieved throughput** | 14.86 RPS (all instances) |
| **Attempted − achieved gap** | 1.01 RPS (6.35%) |
| **Total attempted ops** | 14404 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.147 | 3891.199 | 8683.519 | 3.722266899257648 | 6.92% | 0.3502627189470611 | 163 |
| 1 | 6.271 | 4296.703 | 9912.319 | 3.7102955476453428 | 6.69% | 0.40060090135202797 | 178 |
| 2 | 6.167 | 4669.439 | 10272.767 | 3.7137815597222907 | 6.53% | 0.35017508754377186 | 162 |
| 3 | 5.911 | 4612.095 | 10412.031 | 3.716329372774389 | 6.69% | 0.400200100050025 | 173 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 216 | Timeout waiting for fast operation slot for operation: e98e4f987f09ed4e |
| 0 | SQLException | 34 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 201 | Timeout waiting for fast operation slot for operation: e9cb50da3e8545 |
| 1 | SQLException | 41 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 185 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLException | 51 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 202 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLException | 40 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-05T00:20:09Z → 2026-07-05T00:35:09Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 25.4 | 40.0 | 0.330 | 84 | 0 |
| ojp-2 | 25.6 | 40.0 | 0.423 | 87 | 0 |
| ojp-3 | 24.8 | 40.0 | 0.377 | 77 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T00:20:09Z → 2026-07-05T00:35:09Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 22048 / 33004 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 419084973 | Cumulative since stats reset |
| Transactions rolled back | 3892 | Non-zero → contention or application errors |
| Temp file bytes written | -5 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 5 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4685 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 323535 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T00:20:09Z → 2026-07-05T00:35:09Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.7 | 1.0 | 4.9 | 10.8 | 24.5 | 4.7 | 3.9 | 7.9 | 20.8 | 37.4 | 219.3 | 220.0 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.8 | 1.0 | 4.9 | 12.7 | 26.4 | 5.0 | 3.9 | 9.7 | 34.5 | 36.3 | 220.3 | 220.9 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 4.9 | 11.8 | 22.5 | 6.4 | 3.9 | 31.2 | 35.5 | 57.1 | 215.6 | 216.4 |
| PostgreSQL | db | 150.9 | 150.7 | 301.9 | 330.1 | 335.9 | 314.5 | 390.9 | 400.0 | 400.0 | 400.0 | 6204.8 | 10537.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T00:37:50Z*

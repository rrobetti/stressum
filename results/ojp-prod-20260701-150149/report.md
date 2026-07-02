# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-01T14:14:01Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260701-150149` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.88 RPS (per instance) |
| **Total throughput** | 3.53 RPS (all instances) |
| **p50 latency** | 6.53 ms |
| **p95 latency** | 1890.56 ms |
| **p99 latency** | 7021.57 ms |
| **p999 latency** | 10912.77 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 3604 |
| **Failed requests** | 3 |
| **Total successful** | 3601 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 13.67 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 11031 |
| observed_client_backends_active_max | 16513 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.2% / 2.0% / 8.8% / 18.6% / 25.5% |
| OJP proxy-tier host_cpu (avg / peak) | 15.4% / 95.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 62.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 643.40 MiB / 648.80 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.2% / 2.0% / 8.8% / 18.6% / 25.5% |
| PgBouncer tier RSS (avg / peak, summed) | 643.40 MiB / 648.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.2% / 2.0% / 8.8% / 18.6% / 25.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.4% / 95.6% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 62.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 643.40 MiB / 648.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.20% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 185 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (1890.56 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 3.53 RPS (all instances) |
| **Achieved throughput** | 3.53 RPS (all instances) |
| **Attempted − achieved gap** | 0.00 RPS (0.08%) |
| **Total attempted ops** | 3601 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 7.155 | 1945.599 | 5578.751 | 0.880620568122711 | 0.22% | 0.20020020020020018 | 46 |
| 1 | 6.703 | 1938.431 | 6111.231 | 0.8815370872447461 | 0.11% | 0.20030045067601399 | 50 |
| 2 | 6.187 | 1903.615 | 8708.095 | 0.882496691861735 | 0.00% | 0.2001000500250125 | 45 |
| 3 | 6.087 | 1774.591 | 7688.191 | 0.8824292758889177 | 0.00% | 0.20020020020020018 | 44 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | StatusRuntimeException | 2 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | StatusRuntimeException | 1 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-01T14:14:01Z → 2026-07-01T14:29:01Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 27.0 | 45.0 | 0.037 | 16 | 0 |
| ojp-2 | 25.6 | 40.0 | 0.043 | 20 | 0 |
| ojp-3 | 26.6 | 45.0 | 0.051 | 20 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-01T14:14:01Z → 2026-07-01T14:29:01Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 11031 / 16513 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 90843190 | Cumulative since stats reset |
| Transactions rolled back | 1310 | Non-zero → contention or application errors |
| Temp file bytes written | -3 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 3 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1479 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 148294 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-01T14:14:01Z → 2026-07-01T14:29:01Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.1 | 1.0 | 3.9 | 12.8 | 20.6 | 7.0 | 3.9 | 33.3 | 35.5 | 89.8 | 213.4 | 215.3 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.1 | 1.0 | 3.9 | 8.8 | 24.5 | 3.9 | 3.9 | 5.9 | 12.7 | 28.3 | 215.9 | 217.6 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.1 | 1.0 | 3.9 | 7.8 | 17.6 | 4.7 | 3.9 | 8.8 | 34.1 | 74.9 | 214.1 | 215.9 |
| PostgreSQL | db | 33.2 | 1.3 | 204.9 | 243.3 | 283.8 | 132.3 | 87.5 | 399.5 | 400.0 | 400.0 | 3812.9 | 8656.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-01T14:31:32Z*

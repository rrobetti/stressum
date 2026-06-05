# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T14:17:23Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260530-150522` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.68 RPS (per instance) |
| **Total throughput** | 1.35 RPS (all instances) |
| **p50 latency** | 12.58 ms |
| **p95 latency** | 12333.05 ms |
| **p99 latency** | 27934.70 ms |
| **p999 latency** | 39436.30 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 1808 |
| **Failed requests** | 3 |
| **Total successful** | 1805 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 17.84 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 16445 |
| observed_client_backends_active_max | 23435 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 2 |
| Configured client pool size (per replica) | 15 |
| OJP servers | 3 |
| Real DB connections per OJP server | 5 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.7% / 2.0% / 7.8% / 17.6% / 31.3% |
| OJP proxy-tier host_cpu (avg / peak) | 21.4% / 128.1% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 64.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 643.80 MiB / 650.40 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.7% / 2.0% / 7.8% / 17.6% / 31.3% |
| PgBouncer tier RSS (avg / peak, summed) | 643.80 MiB / 650.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.7% / 2.0% / 7.8% / 17.6% / 31.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 21.4% / 128.1% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 64.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 643.80 MiB / 650.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.20% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 91 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (12333.05 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 1.35 RPS (all instances) |
| **Achieved throughput** | 1.35 RPS (all instances) |
| **Attempted − achieved gap** | -0.00 RPS (-0.17%) |
| **Total attempted ops** | 2402 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.29 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 14.015 | 12443.647 | 27131.903 | 0.6749456002825492 | 0.22% | 0.20030045067601399 | 46 |
| 1 | 11.151 | 12222.463 | 28737.535 | 0.6757843925985519 | 0.11% | 0.2001000500250125 | 45 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | StatusRuntimeException | 2 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: f891f847dfafb38c |
| 1 | StatusRuntimeException | 1 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e98e4f987f09ed4e |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-30T14:17:23Z → 2026-05-30T14:32:23Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 24.3 | 40.0 | 0.040 | 13 | 0 |
| ojp-2 | 25.5 | 45.0 | 0.026 | 10 | 0 |
| ojp-3 | 28.1 | 47.0 | 0.037 | 12 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T14:17:23Z → 2026-05-30T14:32:23Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 16445 / 23435 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 171198986 | Cumulative since stats reset |
| Transactions rolled back | 727 | Non-zero → contention or application errors |
| Temp file bytes written | 4 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -4 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1503 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 152189 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T14:17:23Z → 2026-05-30T14:32:23Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.0 | 1.0 | 2.9 | 9.8 | 27.4 | 6.1 | 3.9 | 31.4 | 35.5 | 52.7 | 206.6 | 209.6 |
| Proxy (OJP / pgBouncer) | ojp-2 | 0.8 | 0.0 | 2.9 | 7.8 | 17.6 | 4.8 | 3.0 | 14.7 | 34.3 | 37.1 | 217.1 | 219.0 |
| Proxy (OJP / pgBouncer) | ojp-3 | 0.9 | 0.0 | 2.9 | 12.7 | 19.6 | 10.9 | 3.9 | 34.5 | 47.8 | 103.5 | 220.1 | 221.8 |
| PostgreSQL | db | 57.5 | 1.4 | 207.3 | 222.9 | 236.2 | 329.2 | 313.1 | 400.0 | 400.0 | 400.0 | 6067.9 | 16800.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-30T14:35:08Z*

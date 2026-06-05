# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T09:23:32Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260530-101131` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.68 RPS (per instance) |
| **Total throughput** | 1.35 RPS (all instances) |
| **p50 latency** | 12.98 ms |
| **p95 latency** | 11030.55 ms |
| **p99 latency** | 29016.05 ms |
| **p999 latency** | 41304.05 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 1808 |
| **Failed requests** | 2 |
| **Total successful** | 1806 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 25 |
| observed_postgres_backends_avg_numbackends | 18.07 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 16461 |
| observed_client_backends_active_max | 23248 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.6% / 2.0% / 6.9% / 16.6% / 34.3% |
| OJP proxy-tier host_cpu (avg / peak) | 20.9% / 92.1% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 80.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 646.70 MiB / 652.80 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.6% / 2.0% / 6.9% / 16.6% / 34.3% |
| PgBouncer tier RSS (avg / peak, summed) | 646.70 MiB / 652.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.6% / 2.0% / 6.9% / 16.6% / 34.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 20.9% / 92.1% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 80.90% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 646.70 MiB / 652.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.20% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 91 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (11030.55 ms) |
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
| **Attempted − achieved gap** | -0.00 RPS (-0.22%) |
| **Total attempted ops** | 2402 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.27 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 13.271 | 11059.199 | 28213.247 | 0.6760267296327295 | 0.11% | 0.20030045067601399 | 47 |
| 1 | 12.687 | 11001.855 | 29818.879 | 0.6760236930208602 | 0.11% | 0.2001000500250125 | 44 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | StatusRuntimeException | 1 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e98e4f987f09ed4e |
| 1 | StatusRuntimeException | 1 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e98e4f987f09ed4e |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-30T09:23:32Z → 2026-05-30T09:38:32Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 24.4 | 43.0 | 0.027 | 11 | 0 |
| ojp-2 | 27.3 | 40.0 | 0.030 | 14 | 0 |
| ojp-3 | 22.6 | 40.0 | 0.032 | 14 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T09:23:32Z → 2026-05-30T09:38:32Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 16461 / 23248 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 171731244 | Cumulative since stats reset |
| Transactions rolled back | 731 | Non-zero → contention or application errors |
| Temp file bytes written | 4 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -4 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1500 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 152257 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T09:23:32Z → 2026-05-30T09:38:32Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 0.9 | 0.0 | 2.9 | 9.8 | 33.3 | 6.6 | 3.9 | 33.3 | 36.1 | 42.0 | 214.9 | 216.7 |
| Proxy (OJP / pgBouncer) | ojp-2 | 0.9 | 0.0 | 2.9 | 7.8 | 18.6 | 4.4 | 3.0 | 7.9 | 34.1 | 36.1 | 216.1 | 218.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.0 | 0.0 | 2.9 | 13.7 | 29.0 | 10.3 | 3.9 | 34.3 | 38.4 | 62.1 | 215.7 | 218.0 |
| PostgreSQL | db | 59.8 | 1.5 | 204.5 | 222.0 | 233.7 | 327.1 | 308.2 | 400.0 | 400.0 | 400.0 | 6226.5 | 17825.4 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-30T09:41:11Z*

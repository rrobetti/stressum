# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T11:01:41Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260530-114927` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.67 RPS (per instance) |
| **Total throughput** | 1.34 RPS (all instances) |
| **p50 latency** | 12.71 ms |
| **p95 latency** | 10563.60 ms |
| **p99 latency** | 28745.75 ms |
| **p999 latency** | 43597.80 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 1808 |
| **Failed requests** | 0 |
| **Total successful** | 1808 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 18.03 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 15938 |
| observed_client_backends_active_max | 22640 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.8% / 2.0% / 8.8% / 20.5% / 46.0% |
| OJP proxy-tier host_cpu (avg / peak) | 20.3% / 74.7% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 95.90% |
| OJP proxy-tier RSS (avg / peak, summed) | 664.00 MiB / 671.10 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.8% / 2.0% / 8.8% / 20.5% / 46.0% |
| PgBouncer tier RSS (avg / peak, summed) | 664.00 MiB / 671.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.8% / 2.0% / 8.8% / 20.5% / 46.0% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 20.3% / 74.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 95.90% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 664.00 MiB / 671.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.20% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 95 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (10563.60 ms) |
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
| **Attempted − achieved gap** | -0.00 RPS (-0.33%) |
| **Total attempted ops** | 2402 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.31 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 14.255 | 10575.871 | 28262.399 | 0.670985517401089 | 0.00% | 0.20020020020020018 | 46 |
| 1 | 11.159 | 10551.295 | 29229.055 | 0.6717044500419815 | 0.00% | 0.2 | 49 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-30T11:01:41Z → 2026-05-30T11:16:41Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 28.2 | 45.0 | 0.027 | 10 | 0 |
| ojp-2 | 26.8 | 45.0 | 0.032 | 11 | 0 |
| ojp-3 | 26.9 | 50.0 | 0.034 | 10 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T11:01:41Z → 2026-05-30T11:16:41Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 15938 / 22640 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 171558826 | Cumulative since stats reset |
| Transactions rolled back | 552 | Non-zero → contention or application errors |
| Temp file bytes written | 3 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -3 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1493 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 150927 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T11:01:41Z → 2026-05-30T11:16:41Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.0 | 0.0 | 2.9 | 10.8 | 34.3 | 7.2 | 3.9 | 33.5 | 42.0 | 56.6 | 217.0 | 220.2 |
| Proxy (OJP / pgBouncer) | ojp-2 | 0.8 | 0.0 | 2.9 | 8.8 | 17.6 | 3.6 | 3.0 | 5.9 | 11.8 | 19.7 | 219.6 | 221.5 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.0 | 0.0 | 2.9 | 13.7 | 44.0 | 10.0 | 3.9 | 34.1 | 39.2 | 54.6 | 227.4 | 229.4 |
| PostgreSQL | db | 58.9 | 1.5 | 207.2 | 221.5 | 238.5 | 326.2 | 311.3 | 400.0 | 400.0 | 400.0 | 6163.2 | 17013.4 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-30T11:19:32Z*

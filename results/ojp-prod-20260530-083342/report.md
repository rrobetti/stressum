# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-30T07:45:42Z |
| **Duration** | 900 s |
| **Instances**| 2 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260530-083342` |

---

## Aggregate Metrics (mean across 2 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.67 RPS (per instance) |
| **Total throughput** | 1.35 RPS (all instances) |
| **p50 latency** | 12.20 ms |
| **p95 latency** | 10334.25 ms |
| **p99 latency** | 28401.70 ms |
| **p999 latency** | 42123.30 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 1808 |
| **Failed requests** | 0 |
| **Total successful** | 1808 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 18.01 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 16450 |
| observed_client_backends_active_max | 23249 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.7% / 2.0% / 7.8% / 19.6% / 34.3% |
| OJP proxy-tier host_cpu (avg / peak) | 20.4% / 104.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 82.30% |
| OJP proxy-tier RSS (avg / peak, summed) | 655.00 MiB / 661.70 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.7% / 2.0% / 7.8% / 19.6% / 34.3% |
| PgBouncer tier RSS (avg / peak, summed) | 655.00 MiB / 661.70 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.7% / 2.0% / 7.8% / 19.6% / 34.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 20.4% / 104.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 82.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 655.00 MiB / 661.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.19% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 90 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (10334.25 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (2/2 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 1.34 RPS (all instances) |
| **Achieved throughput** | 1.35 RPS (all instances) |
| **Attempted − achieved gap** | -0.00 RPS (-0.33%) |
| **Total attempted ops** | 2402 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.27 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 12.279 | 10280.959 | 27574.271 | 0.6727622098154816 | 0.00% | 0.20020020020020018 | 46 |
| 1 | 12.127 | 10387.455 | 29229.055 | 0.6734959955298938 | 0.00% | 0.17511266900350525 | 44 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-30T07:45:42Z → 2026-05-30T08:00:42Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 24.7 | 45.0 | 0.027 | 10 | 0 |
| ojp-2 | 25.6 | 45.0 | 0.038 | 11 | 0 |
| ojp-3 | 27.6 | 43.0 | 0.026 | 12 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-30T07:45:42Z → 2026-05-30T08:00:42Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 16450 / 23249 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 171884869 | Cumulative since stats reset |
| Transactions rolled back | 586 | Non-zero → contention or application errors |
| Temp file bytes written | 5 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -4 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1478 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 149864 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-30T07:45:42Z → 2026-05-30T08:00:42Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.0 | 1.0 | 2.9 | 11.7 | 32.3 | 6.6 | 3.9 | 33.3 | 36.3 | 64.7 | 219.8 | 222.5 |
| Proxy (OJP / pgBouncer) | ojp-2 | 0.8 | 0.0 | 2.9 | 7.8 | 19.6 | 4.0 | 3.0 | 6.9 | 32.4 | 36.3 | 215.5 | 217.3 |
| Proxy (OJP / pgBouncer) | ojp-3 | 0.9 | 0.0 | 2.9 | 11.8 | 30.4 | 10.2 | 3.9 | 34.1 | 50.0 | 99.5 | 219.7 | 221.9 |
| PostgreSQL | db | 58.5 | 1.5 | 209.8 | 222.9 | 237.8 | 324.5 | 303.5 | 400.0 | 400.0 | 400.0 | 6363.3 | 19767.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-30T08:03:31Z*

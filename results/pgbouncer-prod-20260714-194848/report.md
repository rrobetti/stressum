# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-14T19:00:48Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260714-194848` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.97 RPS (per instance) |
| **Total throughput** | 15.46 RPS (all instances) |
| **p50 latency** | 3.62 ms |
| **p95 latency** | 12025.50 ms |
| **p99 latency** | 35847.12 ms |
| **p999 latency** | 62273.62 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 14445 |
| **Failed requests** | 0 |
| **Total successful** | 14445 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 51.46 |
| observed_postgres_backends_median_numbackends | 49 |
| observed_client_backends_active_median | 43316 |
| observed_client_backends_active_max | 67649 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | pgbouncer-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 2.9% / 3.9% / 4.9% |
| OJP proxy-tier host_cpu (avg / peak) | 11.4% / 72.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 6.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 34.70 MiB / 34.80 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 2.9% / 3.9% / 4.9% |
| PgBouncer tier RSS (avg / peak, summed) | 34.70 MiB / 34.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 2.9% / 3.9% / 4.9% |
| HAProxy RSS (avg / peak, summed) | 23.10 MiB / 23.30 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.9% / 1.9% / 3.9% / 6.8% / 8.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.5% / 78.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 11.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 57.80 MiB / 58.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 27 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (12025.50 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.43 RPS (all instances) |
| **Achieved throughput** | 15.46 RPS (all instances) |
| **Attempted − achieved gap** | -0.03 RPS (-0.20%) |
| **Total attempted ops** | 14415 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 3.447 | 8343.551 | 23134.207 | 0.964697628255587 | 0.00% | 0.025015634771732333 | 1 |
| 10 | 3.245 | 11722.751 | 37322.751 | 0.9646996917666839 | 0.00% | 0.025015634771732333 | 2 |
| 11 | 3.647 | 11223.039 | 38567.935 | 0.9763444154717685 | 0.00% | 0.025021894157387717 | 2 |
| 12 | 3.099 | 13516.799 | 37847.039 | 0.9668376814291231 | 0.00% | 0.025015634771732333 | 1 |
| 13 | 4.143 | 12976.127 | 35618.815 | 0.9657681707195775 | 0.00% | 0.025025025025025023 | 2 |
| 14 | 4.005 | 15294.463 | 42172.415 | 0.9717943403986181 | 0.00% | 0.025015634771732333 | 2 |
| 15 | 3.761 | 14893.055 | 36405.247 | 0.9708290021486967 | 0.00% | 0.025021894157387717 | 1 |
| 1 | 3.237 | 9199.615 | 25640.959 | 0.964698660010032 | 0.00% | 0.025025025025025023 | 1 |
| 2 | 3.809 | 10838.015 | 34832.383 | 0.964698660010032 | 0.00% | 0.025015634771732333 | 2 |
| 3 | 3.695 | 12541.951 | 36438.015 | 0.964698660010032 | 0.00% | 0.025021894157387717 | 2 |
| 4 | 3.749 | 11624.447 | 35127.295 | 0.964698660010032 | 0.00% | 0.02501250625312656 | 2 |
| 5 | 3.345 | 11624.447 | 38928.383 | 0.964697628255587 | 0.00% | 0.025021894157387717 | 1 |
| 6 | 3.645 | 11386.879 | 38043.647 | 0.9657692036200838 | 0.00% | 0.025015634771732333 | 2 |
| 7 | 3.737 | 12492.799 | 39616.511 | 0.964697628255587 | 0.00% | 0.025021894157387717 | 2 |
| 8 | 3.987 | 12083.199 | 37683.199 | 0.9646996917666839 | 0.00% | 0.02501250625312656 | 2 |
| 9 | 3.305 | 12648.447 | 36175.871 | 0.964698660010032 | 0.00% | 0.025025025025025023 | 2 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-14T19:00:48Z → 2026-07-14T19:15:48Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 49 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 43316 / 67649 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1407185441 | Cumulative since stats reset |
| Transactions rolled back | 895 | Non-zero → contention or application errors |
| Temp file bytes written | 18 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -18 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 2067 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 208880 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-14T19:00:48Z → 2026-07-14T19:15:48Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 1.0 | 2.0 | 2.0 | 3.7 | 2.9 | 4.9 | 33.2 | 35.2 | 11.6 | 11.6 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.0 | 1.9 | 2.9 | 4.7 | 2.9 | 24.4 | 34.2 | 41.1 | 11.6 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.4 | 0.0 | 1.0 | 1.9 | 1.9 | 3.2 | 2.9 | 4.9 | 5.8 | 33.1 | 11.5 | 11.5 |
| PostgreSQL | db | 630.2 | 736.1 | 1255.5 | 1291.7 | 1352.7 | 1120.0 | 1321.2 | 1597.8 | 1598.7 | 1598.8 | 137000.7 | 152303.0 |
| HAProxy | lb | 1.0 | 1.0 | 2.9 | 3.9 | 4.9 | 4.2 | 3.9 | 5.9 | 9.7 | 35.0 | 23.1 | 23.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-14T19:19:47Z*

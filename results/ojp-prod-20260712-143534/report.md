# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-12T13:47:29Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260712-143534` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 5.50 RPS (per instance) |
| **Total throughput** | 22.00 RPS (all instances) |
| **p50 latency** | 6.88 ms |
| **p95 latency** | 4213.75 ms |
| **p99 latency** | 22327.33 ms |
| **p999 latency** | 43622.25 ms |
| **Error rate** | 54.00% (0.54) |
| **Total requests** | 43339 |
| **Failed requests** | 23275 |
| **Total successful** | 20064 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.60 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 32282 |
| observed_client_backends_active_max | 46483 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.9% / 4.9% / 13.7% / 20.5% / 71.5% |
| OJP proxy-tier host_cpu (avg / peak) | 16.9% / 81.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 126.30% |
| OJP proxy-tier RSS (avg / peak, summed) | 704.50 MiB / 715.30 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.9% / 4.9% / 13.7% / 20.5% / 71.5% |
| PgBouncer tier RSS (avg / peak, summed) | 704.50 MiB / 715.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.9% / 4.9% / 13.7% / 20.5% / 71.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.9% / 81.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 126.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 704.50 MiB / 715.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.41% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1229 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4213.75 ms) |
| Error rate | < 0.1% | ❌ FAIL (54.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 47.37 RPS (all instances) |
| **Achieved throughput** | 22.00 RPS (all instances) |
| **Attempted − achieved gap** | 25.37 RPS (53.56%) |
| **Total attempted ops** | 43204 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.751 | 4028.415 | 17727.487 | 5.6957491413043835 | 51.96% | 0.4503377815033643 | 326 |
| 1 | 7.311 | 4155.391 | 23904.255 | 5.533454838596614 | 53.26% | 0.4010026070194551 | 298 |
| 2 | 6.535 | 4210.687 | 19890.175 | 5.553398528112911 | 53.52% | 0.4012036108324975 | 297 |
| 3 | 6.939 | 4460.543 | 27787.263 | 5.217252473027974 | 56.07% | 0.4008016032064128 | 308 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 5616 | Connection admission timeout for hash: _R1oo6-0VGP4VoeSd7fpBbwrG_FsZi1RdIyq5wGF_58 after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 5756 | Connection admission timeout for hash: _R1oo6-0VGP4VoeSd7fpBbwrG_FsZi1RdIyq5wGF_58 after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 5813 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLTransientConnectionException | 6090 | Client throttle limit reached; request rejected to avoid overloading the database |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-12T13:47:29Z → 2026-07-12T14:02:29Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 23.8 | 41.0 | 0.508 | 91 | 0 |
| ojp-2 | 28.4 | 47.0 | 0.231 | 101 | 0 |
| ojp-3 | 26.9 | 41.0 | 0.484 | 90 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-12T13:47:29Z → 2026-07-12T14:02:29Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 32282 / 46483 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 539715283 | Cumulative since stats reset |
| Transactions rolled back | 6452 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 11113 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 785693 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-12T13:47:29Z → 2026-07-12T14:02:29Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.8 | 1.0 | 5.9 | 9.8 | 23.5 | 5.9 | 4.9 | 10.9 | 35.3 | 38.4 | 219.8 | 220.1 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.3 | 2.0 | 5.9 | 10.8 | 39.1 | 5.3 | 4.9 | 8.8 | 33.5 | 47.3 | 246.8 | 250.2 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.9 | 1.0 | 5.9 | 10.8 | 63.7 | 6.0 | 4.0 | 15.6 | 36.1 | 66.7 | 237.9 | 245.0 |
| PostgreSQL | db | 201.7 | 201.9 | 344.8 | 359.6 | 361.6 | 359.6 | 399.5 | 400.0 | 400.0 | 400.0 | 6147.3 | 9102.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-12T14:05:22Z*

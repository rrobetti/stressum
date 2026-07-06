# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-05T15:55:25Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260705-164331` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.63 RPS (per instance) |
| **Total throughput** | 18.51 RPS (all instances) |
| **p50 latency** | 6.71 ms |
| **p95 latency** | 2564.60 ms |
| **p99 latency** | 22011.90 ms |
| **p999 latency** | 72138.75 ms |
| **Error rate** | 61.00% (0.61) |
| **Total requests** | 43559 |
| **Failed requests** | 26548 |
| **Total successful** | 17011 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 22 |
| observed_postgres_backends_avg_numbackends | 15.50 |
| observed_postgres_backends_median_numbackends | 15 |
| observed_client_backends_active_median | 27733 |
| observed_client_backends_active_max | 40201 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.7% / 4.9% / 13.7% / 21.5% / 73.1% |
| OJP proxy-tier host_cpu (avg / peak) | 25.7% / 139.7% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 105.30% |
| OJP proxy-tier RSS (avg / peak, summed) | 717.80 MiB / 722.70 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.7% / 4.9% / 13.7% / 21.5% / 73.1% |
| PgBouncer tier RSS (avg / peak, summed) | 717.80 MiB / 722.70 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.7% / 4.9% / 13.7% / 21.5% / 73.1% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 25.7% / 139.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 105.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 717.80 MiB / 722.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.48% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1436 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (2564.60 ms) |
| Error rate | < 0.1% | ❌ FAIL (61.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 47.01 RPS (all instances) |
| **Achieved throughput** | 18.51 RPS (all instances) |
| **Attempted − achieved gap** | 28.50 RPS (60.62%) |
| **Total attempted ops** | 43204 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 7.087 | 2545.663 | 22904.831 | 4.547063733594031 | 61.14% | 0.4511278195488722 | 303 |
| 1 | 7.019 | 2703.359 | 22691.839 | 4.447471752544274 | 62.00% | 0.4011030585490808 | 308 |
| 2 | 6.667 | 2658.303 | 18464.767 | 4.852790187862475 | 60.14% | 0.5513784461152882 | 403 |
| 3 | 6.071 | 2351.103 | 23986.175 | 4.6643187155250105 | 60.54% | 0.5012531328320802 | 422 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 6076 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | SQLException | 531 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 1 | SQLTransientConnectionException | 6193 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 1 | SQLException | 507 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 6088 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 2 | SQLException | 508 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 6132 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 3 | SQLException | 513 | Connection admission timeout for hash: VAsjw5zMeW6aVjCnBLOt_TTvuv1tOgI0mEDzFbxzBEE after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-05T15:55:25Z → 2026-07-05T16:10:25Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 25.6 | 40.0 | 0.199 | 56 | 0 |
| ojp-2 | 25.6 | 41.0 | 0.821 | 147 | 0 |
| ojp-3 | 25.0 | 41.0 | 0.468 | 90 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-05T15:55:25Z → 2026-07-05T16:10:25Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 15 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 27733 / 40201 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 399074559 | Cumulative since stats reset |
| Transactions rolled back | 6155 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 10006 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 759848 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-05T15:55:25Z → 2026-07-05T16:10:25Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.1 | 0.0 | 4.9 | 11.7 | 67.2 | 13.0 | 4.9 | 37.2 | 70.0 | 111.2 | 238.8 | 242.8 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.9 | 2.9 | 7.8 | 11.8 | 18.5 | 7.4 | 5.0 | 29.6 | 39.0 | 71.6 | 237.2 | 237.7 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.8 | 1.0 | 5.9 | 9.8 | 19.6 | 5.9 | 3.9 | 16.8 | 34.5 | 68.3 | 241.8 | 242.2 |
| PostgreSQL | db | 116.8 | 103.5 | 297.9 | 333.8 | 357.8 | 248.0 | 264.0 | 400.0 | 400.0 | 400.0 | 5017.3 | 9296.6 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-05T16:13:23Z*

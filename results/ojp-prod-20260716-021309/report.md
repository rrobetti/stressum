# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-16T01:25:35Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260716-021309` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.75 RPS (per instance) |
| **Total throughput** | 27.97 RPS (all instances) |
| **p50 latency** | 4.68 ms |
| **p95 latency** | 242.81 ms |
| **p99 latency** | 34446.25 ms |
| **p999 latency** | 43061.12 ms |
| **Error rate** | 55.00% (0.55) |
| **Total requests** | 57797 |
| **Failed requests** | 31736 |
| **Total successful** | 26061 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 52.51 |
| observed_postgres_backends_median_numbackends | 53 |
| observed_client_backends_active_median | 51044 |
| observed_client_backends_active_max | 72295 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 48 |
| OJP servers | 3 |
| Real DB connections per OJP server | 16 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.5% / 7.8% / 16.6% / 33.2% / 51.8% |
| OJP proxy-tier host_cpu (avg / peak) | 18.6% / 79.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 80.10% |
| OJP proxy-tier RSS (avg / peak, summed) | 1134.20 MiB / 1136.60 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.5% / 7.8% / 16.6% / 33.2% / 51.8% |
| PgBouncer tier RSS (avg / peak, summed) | 1134.20 MiB / 1136.60 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.5% / 7.8% / 16.6% / 33.2% / 51.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.6% / 79.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 80.10% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1134.20 MiB / 1136.60 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.06% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1163 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (242.81 ms) |
| Error rate | < 0.1% | ❌ FAIL (55.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 61.83 RPS (all instances) |
| **Achieved throughput** | 27.97 RPS (all instances) |
| **Attempted − achieved gap** | 33.86 RPS (54.77%) |
| **Total attempted ops** | 57614 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.567 | 1119.231 | 33505.279 | 1.8395387463543442 | 52.30% | 0.06257822277847308 | 67 |
| 10 | 4.263 | 38.847 | 35291.135 | 1.7165801955445967 | 55.59% | 0.06258213930261744 | 64 |
| 11 | 4.951 | 36.255 | 35323.903 | 1.7470150232541137 | 55.02% | 0.07508447002878238 | 81 |
| 12 | 4.411 | 34.335 | 34897.919 | 1.6783539826638445 | 57.01% | 0.06257039169065198 | 64 |
| 13 | 4.615 | 33.023 | 33849.343 | 1.7006857361945122 | 56.08% | 0.06262132907016288 | 75 |
| 14 | 4.359 | 49.631 | 35848.191 | 1.790582417275522 | 53.92% | 0.06258997333150808 | 74 |
| 15 | 4.455 | 31.167 | 33030.143 | 1.783742461564597 | 54.12% | 0.06258605582676179 | 78 |
| 1 | 5.631 | 53.727 | 32407.551 | 1.7728266209967607 | 54.27% | 0.06258605582676179 | 77 |
| 2 | 4.851 | 1148.927 | 34504.703 | 1.7305879817419751 | 55.32% | 0.050075112669003496 | 63 |
| 3 | 4.883 | 1077.247 | 35487.743 | 1.7550501809594703 | 54.51% | 0.0626017278076875 | 80 |
| 4 | 4.507 | 52.863 | 34439.167 | 1.7451576434043339 | 54.94% | 0.06257430723456253 | 60 |
| 5 | 5.007 | 55.135 | 34537.471 | 1.813772399012705 | 53.35% | 0.06259389083625437 | 85 |
| 6 | 4.299 | 46.303 | 35061.759 | 1.754004369474538 | 54.69% | 0.06257822277847308 | 69 |
| 7 | 4.727 | 33.311 | 34963.455 | 1.674125767217926 | 56.96% | 0.06259389083625437 | 73 |
| 8 | 4.615 | 34.463 | 33718.271 | 1.7199604355518503 | 55.56% | 0.06257822277847308 | 74 |
| 9 | 4.815 | 40.575 | 34275.327 | 1.7446421824510403 | 54.89% | 0.06261348719056094 | 79 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 1886 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
| 10 | SQLTransientConnectionException | 2008 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 11 | SQLTransientConnectionException | 1988 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 12 | SQLTransientConnectionException | 2062 | Client throttle limit reached; request rejected to avoid overloading the database |
| 13 | SQLTransientConnectionException | 2028 | Client throttle limit reached; request rejected to avoid overloading the database |
| 14 | SQLTransientConnectionException | 1951 | Client throttle limit reached; request rejected to avoid overloading the database |
| 15 | SQLTransientConnectionException | 1957 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLTransientConnectionException | 1957 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 2 | SQLTransientConnectionException | 1998 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLTransientConnectionException | 1966 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 4 | SQLTransientConnectionException | 1984 | Client throttle limit reached; request rejected to avoid overloading the database |
| 5 | SQLTransientConnectionException | 1927 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 6 | SQLTransientConnectionException | 1976 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 7 | SQLTransientConnectionException | 2058 | Timeout waiting for fast operation slot for operation: f891f847dfafb38c |
| 8 | SQLTransientConnectionException | 2007 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
| 9 | SQLTransientConnectionException | 1983 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-16T01:25:35Z → 2026-07-16T01:40:35Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 30.0 | 48.0 | 0.018 | 11 | 0 |
| ojp-2 | 33.5 | 58.0 | 0.402 | 156 | 0 |
| ojp-3 | 32.3 | 56.0 | 0.493 | 170 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-16T01:25:35Z → 2026-07-16T01:40:35Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 53 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 51044 / 72295 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1901061944 | Cumulative since stats reset |
| Transactions rolled back | 1652 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7360 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 523798 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-16T01:25:35Z → 2026-07-16T01:40:35Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 0.8 | 1.0 | 2.0 | 3.9 | 21.5 | 4.9 | 3.9 | 5.9 | 34.4 | 46.0 | 350.3 | 350.5 |
| Proxy (OJP / pgBouncer) | ojp-2 | 4.0 | 2.9 | 9.8 | 18.6 | 29.3 | 7.2 | 5.9 | 14.7 | 36.2 | 40.2 | 385.1 | 386.3 |
| Proxy (OJP / pgBouncer) | ojp-3 | 3.9 | 2.9 | 9.8 | 16.6 | 29.3 | 6.9 | 5.9 | 12.7 | 32.4 | 38.2 | 398.8 | 399.8 |
| PostgreSQL | db | 546.5 | 537.7 | 804.1 | 943.7 | 1030.6 | 1178.2 | 1209.7 | 1512.3 | 1572.9 | 1589.0 | 31988.5 | 42729.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-16T01:44:45Z*

# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-01T22:01:02Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260701-224915` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.30 RPS (per instance) |
| **Total throughput** | 13.19 RPS (all instances) |
| **p50 latency** | 6.15 ms |
| **p95 latency** | 4799.50 ms |
| **p99 latency** | 11878.42 ms |
| **p999 latency** | 25120.75 ms |
| **Error rate** | 6.00% (0.06) |
| **Total requests** | 14460 |
| **Failed requests** | 835 |
| **Total successful** | 13625 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.01 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 22176 |
| observed_client_backends_active_max | 33012 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.7% / 3.9% / 11.8% / 20.5% / 35.3% |
| OJP proxy-tier host_cpu (avg / peak) | 25.8% / 125.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 67.50% |
| OJP proxy-tier RSS (avg / peak, summed) | 663.30 MiB / 666.30 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.7% / 3.9% / 11.8% / 20.5% / 35.3% |
| PgBouncer tier RSS (avg / peak, summed) | 663.30 MiB / 666.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.7% / 3.9% / 11.8% / 20.5% / 35.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 25.8% / 125.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 67.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 663.30 MiB / 666.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.35% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 647 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4799.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (6.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 13.94 RPS (all instances) |
| **Achieved throughput** | 13.19 RPS (all instances) |
| **Attempted − achieved gap** | 0.75 RPS (5.41%) |
| **Total attempted ops** | 14402 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.199 | 4022.271 | 9863.167 | 3.3052576611772446 | 5.32% | 0.35035035035035034 | 177 |
| 1 | 6.223 | 4952.063 | 11460.607 | 3.290836776819497 | 5.98% | 0.35070140280561124 | 158 |
| 2 | 5.911 | 5365.759 | 13459.455 | 3.3025035200915993 | 5.58% | 0.35035035035035034 | 161 |
| 3 | 6.275 | 4857.855 | 12730.367 | 3.2903764489341913 | 6.22% | 0.35070140280561124 | 151 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 38 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 0 | SQLTransientException | 20 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 133 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 42 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 1 | SQLTransientException | 38 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 136 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e98e4f987f09ed4e |
| 2 | SQLException | 35 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 2 | SQLTransientException | 22 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 145 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 3 | SQLException | 43 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 3 | SQLTransientException | 41 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 141 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-01T22:01:02Z → 2026-07-01T22:16:02Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.0 | 40.0 | 0.331 | 78 | 0 |
| ojp-2 | 25.4 | 40.0 | 0.438 | 81 | 0 |
| ojp-3 | 27.6 | 45.0 | 0.173 | 75 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-01T22:01:02Z → 2026-07-01T22:16:02Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 22176 / 33012 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 423255848 | Cumulative since stats reset |
| Transactions rolled back | 3912 | Non-zero → contention or application errors |
| Temp file bytes written | -9 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 9 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4735 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 336183 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-01T22:01:02Z → 2026-07-01T22:16:02Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.5 | 1.0 | 4.9 | 10.8 | 24.4 | 8.7 | 3.9 | 34.1 | 40.4 | 96.6 | 220.4 | 221.1 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.7 | 1.0 | 5.9 | 13.7 | 19.6 | 12.5 | 4.9 | 36.3 | 53.2 | 106.3 | 219.9 | 220.7 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.5 | 1.0 | 3.9 | 9.8 | 23.5 | 5.1 | 3.9 | 10.7 | 34.3 | 48.8 | 223.0 | 224.5 |
| PostgreSQL | db | 163.7 | 163.9 | 312.7 | 338.5 | 349.6 | 327.7 | 398.5 | 400.0 | 400.0 | 400.0 | 6247.4 | 10105.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-01T22:18:48Z*

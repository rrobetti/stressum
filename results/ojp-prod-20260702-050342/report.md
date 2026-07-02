# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T04:15:32Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260702-050342` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.27 RPS (per instance) |
| **Total throughput** | 17.09 RPS (all instances) |
| **p50 latency** | 6.51 ms |
| **p95 latency** | 4255.23 ms |
| **p99 latency** | 18759.67 ms |
| **p999 latency** | 33746.75 ms |
| **Error rate** | 39.00% (0.39) |
| **Total requests** | 28823 |
| **Failed requests** | 11220 |
| **Total successful** | 17603 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.68 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 26491 |
| observed_client_backends_active_max | 39455 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.1% / 3.9% / 10.8% / 19.6% / 35.2% |
| OJP proxy-tier host_cpu (avg / peak) | 17.7% / 83.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 89.10% |
| OJP proxy-tier RSS (avg / peak, summed) | 680.30 MiB / 682.90 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.1% / 3.9% / 10.8% / 19.6% / 35.2% |
| PgBouncer tier RSS (avg / peak, summed) | 680.30 MiB / 682.90 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.1% / 3.9% / 10.8% / 19.6% / 35.2% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.7% / 83.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 89.10% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 680.30 MiB / 682.90 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.42% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1039 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4255.23 ms) |
| Error rate | < 0.1% | ❌ FAIL (39.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 27.97 RPS (all instances) |
| **Achieved throughput** | 17.09 RPS (all instances) |
| **Attempted − achieved gap** | 10.88 RPS (38.89%) |
| **Total attempted ops** | 28803 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.459 | 4012.031 | 19742.719 | 4.314875577107349 | 38.13% | 0.42592768383034313 | 287 |
| 1 | 6.783 | 4395.007 | 18268.159 | 4.263546388081424 | 38.86% | 0.40050065087621417 | 231 |
| 2 | 6.219 | 4259.839 | 20135.935 | 4.149596109229462 | 40.95% | 0.3510531594784353 | 230 |
| 3 | 6.563 | 4354.047 | 16891.903 | 4.364172904559509 | 37.77% | 0.5002501250625313 | 291 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 84 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 0 | SQLTransientException | 2597 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 66 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 92 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 1 | SQLTransientException | 2623 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 84 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLException | 91 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 2 | SQLTransientException | 2768 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 92 | RESOURCE_EXHAUSTED: Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 3 | SQLException | 81 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 3 | SQLTransientException | 2552 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 89 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: f891f847dfafb38c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-02T04:15:32Z → 2026-07-02T04:30:32Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 27.5 | 43.0 | 0.382 | 110 | 0 |
| ojp-2 | 30.0 | 45.0 | 0.306 | 88 | 0 |
| ojp-3 | 26.9 | 48.0 | 0.136 | 65 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T04:15:32Z → 2026-07-02T04:30:32Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 26491 / 39455 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 533893298 | Cumulative since stats reset |
| Transactions rolled back | 5640 | Non-zero → contention or application errors |
| Temp file bytes written | 5 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -5 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7567 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 718595 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T04:15:32Z → 2026-07-02T04:30:32Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.8 | 1.0 | 4.9 | 10.8 | 32.3 | 5.9 | 3.9 | 21.4 | 35.5 | 75.4 | 222.9 | 223.4 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.8 | 1.0 | 4.9 | 9.8 | 34.2 | 7.7 | 3.9 | 35.3 | 37.2 | 50.0 | 228.8 | 229.6 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 3.9 | 7.8 | 22.6 | 4.5 | 3.9 | 6.9 | 18.6 | 36.5 | 228.6 | 229.9 |
| PostgreSQL | db | 189.2 | 185.4 | 310.1 | 333.2 | 381.5 | 365.3 | 399.5 | 400.0 | 400.0 | 400.0 | 7128.3 | 10677.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T04:33:14Z*

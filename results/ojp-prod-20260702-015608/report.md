# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T01:07:59Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260702-015608` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.25 RPS (per instance) |
| **Total throughput** | 12.99 RPS (all instances) |
| **p50 latency** | 6.00 ms |
| **p95 latency** | 4781.05 ms |
| **p99 latency** | 11454.45 ms |
| **p999 latency** | 22630.40 ms |
| **Error rate** | 8.00% (0.08) |
| **Total requests** | 14441 |
| **Failed requests** | 1094 |
| **Total successful** | 13347 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.17 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 22564 |
| observed_client_backends_active_max | 33405 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.4% / 3.9% / 10.8% / 18.6% / 32.3% |
| OJP proxy-tier host_cpu (avg / peak) | 20.9% / 142.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 69.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 670.50 MiB / 674.70 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.4% / 3.9% / 10.8% / 18.6% / 32.3% |
| PgBouncer tier RSS (avg / peak, summed) | 670.50 MiB / 674.70 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.4% / 3.9% / 10.8% / 18.6% / 32.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 20.9% / 142.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 69.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 670.50 MiB / 674.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.35% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 641 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4781.05 ms) |
| Error rate | < 0.1% | ❌ FAIL (8.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 14.02 RPS (all instances) |
| **Achieved throughput** | 12.99 RPS (all instances) |
| **Attempted − achieved gap** | 1.03 RPS (7.34%) |
| **Total attempted ops** | 14402 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.187 | 4411.391 | 8986.623 | 3.282443418857159 | 6.92% | 0.3010536879076769 | 155 |
| 1 | 5.871 | 4714.495 | 10731.519 | 3.2511525043608276 | 7.45% | 0.40040040040040037 | 177 |
| 2 | 6.299 | 4927.487 | 12648.447 | 3.2337421112535587 | 7.81% | 0.3510531594784353 | 159 |
| 3 | 5.651 | 5070.847 | 13451.263 | 3.2226201125294653 | 8.11% | 0.35052578868302453 | 150 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 43 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 0 | SQLTransientException | 52 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 155 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e98e4f987f09ed4e |
| 1 | SQLException | 36 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 1 | SQLTransientException | 101 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 132 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLException | 46 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 2 | SQLTransientException | 88 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 148 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e98e4f987f09ed4e |
| 3 | SQLException | 49 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 3 | SQLTransientException | 91 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 153 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-02T01:07:59Z → 2026-07-02T01:22:59Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 27.3 | 43.0 | 0.164 | 75 | 0 |
| ojp-2 | 28.6 | 45.0 | 0.155 | 72 | 0 |
| ojp-3 | 27.4 | 45.0 | 0.140 | 63 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T01:07:59Z → 2026-07-02T01:22:59Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 22564 / 33405 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 422411654 | Cumulative since stats reset |
| Transactions rolled back | 3892 | Non-zero → contention or application errors |
| Temp file bytes written | -8 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 8 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4718 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 331070 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T01:07:59Z → 2026-07-02T01:22:59Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.3 | 1.0 | 3.9 | 7.8 | 30.4 | 7.5 | 3.9 | 33.5 | 36.1 | 68.0 | 221.9 | 223.0 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.5 | 1.0 | 3.9 | 9.8 | 19.6 | 7.9 | 3.9 | 34.5 | 37.2 | 45.6 | 224.1 | 225.6 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 4.9 | 12.7 | 19.6 | 6.0 | 3.9 | 21.6 | 36.3 | 83.7 | 224.5 | 226.1 |
| PostgreSQL | db | 159.3 | 161.0 | 303.9 | 337.3 | 352.9 | 330.2 | 398.3 | 400.0 | 400.0 | 400.0 | 6298.0 | 10373.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T01:25:38Z*

# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-01T20:27:35Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260701-211540` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.23 RPS (per instance) |
| **Total throughput** | 12.90 RPS (all instances) |
| **p50 latency** | 6.18 ms |
| **p95 latency** | 4958.23 ms |
| **p99 latency** | 13262.85 ms |
| **p999 latency** | 32870.50 ms |
| **Error rate** | 8.00% (0.08) |
| **Total requests** | 14443 |
| **Failed requests** | 1148 |
| **Total successful** | 13295 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.19 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 21498 |
| observed_client_backends_active_max | 32756 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.5% / 3.9% / 10.8% / 18.6% / 31.2% |
| OJP proxy-tier host_cpu (avg / peak) | 17.3% / 75.8% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 57.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 666.80 MiB / 670.60 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.5% / 3.9% / 10.8% / 18.6% / 31.2% |
| PgBouncer tier RSS (avg / peak, summed) | 666.80 MiB / 670.60 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.5% / 3.9% / 10.8% / 18.6% / 31.2% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.3% / 75.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 57.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 666.80 MiB / 670.60 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.38% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 677 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4958.23 ms) |
| Error rate | < 0.1% | ❌ FAIL (8.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 13.98 RPS (all instances) |
| **Achieved throughput** | 12.90 RPS (all instances) |
| **Attempted − achieved gap** | 1.08 RPS (7.70%) |
| **Total attempted ops** | 14403 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.231 | 4358.143 | 11206.655 | 3.270979275020699 | 7.09% | 0.400200100050025 | 175 |
| 1 | 6.079 | 5148.671 | 13582.335 | 3.173473840953073 | 9.53% | 0.35052578868302453 | 161 |
| 2 | 6.035 | 5054.463 | 14876.671 | 3.2410403005398516 | 7.06% | 0.40040040040040037 | 181 |
| 3 | 6.375 | 5271.551 | 13385.727 | 3.214717985959816 | 8.11% | 0.3508771929824561 | 160 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 51 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 0 | SQLTransientException | 5 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 200 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 67 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 1 | SQLTransientException | 12 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 265 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLException | 40 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 2 | SQLTransientException | 5 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 210 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLException | 59 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 3 | SQLTransientException | 7 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 227 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-01T20:27:35Z → 2026-07-01T20:42:35Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 27.7 | 45.0 | 0.126 | 63 | 0 |
| ojp-2 | 25.9 | 40.0 | 0.505 | 104 | 0 |
| ojp-3 | 28.0 | 45.0 | 0.126 | 59 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-01T20:27:35Z → 2026-07-01T20:42:35Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21498 / 32756 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 420914468 | Cumulative since stats reset |
| Transactions rolled back | 3890 | Non-zero → contention or application errors |
| Temp file bytes written | -3 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 3 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4858 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 341717 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-01T20:27:35Z → 2026-07-01T20:42:35Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.4 | 1.0 | 3.9 | 12.7 | 21.5 | 8.4 | 3.9 | 34.1 | 37.2 | 55.2 | 224.1 | 225.8 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.8 | 1.0 | 5.9 | 11.8 | 17.6 | 5.1 | 3.9 | 10.8 | 33.5 | 43.6 | 219.8 | 220.4 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.4 | 1.0 | 3.9 | 7.8 | 18.6 | 4.2 | 3.9 | 6.9 | 15.8 | 34.5 | 222.9 | 224.4 |
| PostgreSQL | db | 159.1 | 162.7 | 310.0 | 335.3 | 355.4 | 327.4 | 398.5 | 400.0 | 400.0 | 400.0 | 6261.5 | 10530.6 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-01T20:45:20Z*

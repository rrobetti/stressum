# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T15:13:04Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260702-160048` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.38 RPS (per instance) |
| **Total throughput** | 5.51 RPS (all instances) |
| **p50 latency** | 8.29 ms |
| **p95 latency** | 623.50 ms |
| **p99 latency** | 9948.17 ms |
| **p999 latency** | 45330.50 ms |
| **Error rate** | 87.00% (0.87) |
| **Total requests** | 43539 |
| **Failed requests** | 37760 |
| **Total successful** | 5779 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 13.52 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 22790 |
| observed_client_backends_active_max | 27418 |
| observed_client_backends_idle_median | 1 |
| observed_client_backends_idle_max | 1 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 12 |
| OJP servers | 3 |
| Real DB connections per OJP server | 4 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.9% / 2.0% / 7.8% / 15.7% / 59.7% |
| OJP proxy-tier host_cpu (avg / peak) | 18.3% / 104.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 100.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 727.90 MiB / 728.70 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.9% / 2.0% / 7.8% / 15.7% / 59.7% |
| PgBouncer tier RSS (avg / peak, summed) | 727.90 MiB / 728.70 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.9% / 2.0% / 7.8% / 15.7% / 59.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.3% / 104.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 100.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 727.90 MiB / 728.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.35% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 735 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (623.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (87.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 41.21 RPS (all instances) |
| **Achieved throughput** | 5.51 RPS (all instances) |
| **Attempted − achieved gap** | 35.70 RPS (86.62%) |
| **Total attempted ops** | 43203 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 8.359 | 992.255 | 11870.207 | 1.3068493777452417 | 87.38% | 0.35052578868302453 | 174 |
| 1 | 8.311 | 793.599 | 14868.479 | 1.3776682177765982 | 86.75% | 0.35052578868302453 | 181 |
| 2 | 8.359 | 614.399 | 5885.951 | 1.4942645067781366 | 85.59% | 0.35070140280561124 | 177 |
| 3 | 8.135 | 93.759 | 7167.999 | 1.3342813084343734 | 87.18% | 0.35052578868302453 | 203 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 1162 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 0 | SQLTransientException | 6733 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 1597 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 1 | SQLException | 1152 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 1 | SQLTransientException | 6715 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 1582 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLException | 1191 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 2 | SQLTransientException | 6795 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 1313 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 3 | SQLException | 1165 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 3 | SQLTransientException | 6786 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 1568 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-02T15:13:04Z → 2026-07-02T15:28:04Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 28.4 | 43.0 | 0.041 | 20 | 0 |
| ojp-2 | 28.6 | 45.0 | 0.010 | 4 | 0 |
| ojp-3 | 29.4 | 45.0 | 0.271 | 69 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T15:13:04Z → 2026-07-02T15:28:04Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 22790 / 27418 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 1 / 1 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 107006763 | Cumulative since stats reset |
| Transactions rolled back | 3686 | Non-zero → contention or application errors |
| Temp file bytes written | -7 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 7 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7689 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 728633 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T15:13:04Z → 2026-07-02T15:28:04Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 0.7 | 0.0 | 2.0 | 8.8 | 22.5 | 5.4 | 3.0 | 28.4 | 34.5 | 63.4 | 230.2 | 230.4 |
| Proxy (OJP / pgBouncer) | ojp-2 | 0.5 | 0.0 | 2.0 | 4.9 | 18.5 | 7.5 | 3.0 | 34.3 | 35.5 | 66.7 | 245.9 | 246.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.8 | 2.0 | 3.9 | 11.7 | 59.7 | 5.8 | 3.9 | 12.8 | 36.3 | 61.7 | 251.8 | 252.2 |
| PostgreSQL | db | 26.5 | 1.3 | 125.5 | 272.8 | 334.0 | 129.3 | 85.3 | 391.5 | 400.0 | 400.0 | 4815.0 | 9498.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T15:31:04Z*

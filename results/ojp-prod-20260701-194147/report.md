# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-01T18:53:41Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260701-194147` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.21 RPS (per instance) |
| **Total throughput** | 12.82 RPS (all instances) |
| **p50 latency** | 6.56 ms |
| **p95 latency** | 5218.82 ms |
| **p99 latency** | 15183.88 ms |
| **p999 latency** | 29778.00 ms |
| **Error rate** | 8.00% (0.08) |
| **Total requests** | 14436 |
| **Failed requests** | 1148 |
| **Total successful** | 13288 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 16.33 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 22300 |
| observed_client_backends_active_max | 33362 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.5% / 3.9% / 9.8% / 19.6% / 31.3% |
| OJP proxy-tier host_cpu (avg / peak) | 15.5% / 91.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 73.50% |
| OJP proxy-tier RSS (avg / peak, summed) | 676.60 MiB / 681.00 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.5% / 3.9% / 9.8% / 19.6% / 31.3% |
| PgBouncer tier RSS (avg / peak, summed) | 676.60 MiB / 681.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.5% / 3.9% / 9.8% / 19.6% / 31.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.5% / 91.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 73.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 676.60 MiB / 681.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.38% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 675 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (5218.82 ms) |
| Error rate | < 0.1% | ❌ FAIL (8.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 13.90 RPS (all instances) |
| **Achieved throughput** | 12.82 RPS (all instances) |
| **Attempted − achieved gap** | 1.08 RPS (7.75%) |
| **Total attempted ops** | 14403 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.291 | 4192.255 | 11665.407 | 3.1865067521295694 | 8.51% | 0.3508771929824561 | 150 |
| 1 | 6.451 | 5259.263 | 15818.751 | 3.2430626177638318 | 7.03% | 0.4008016032064128 | 181 |
| 2 | 6.555 | 5369.855 | 14409.727 | 3.2206709570352072 | 7.46% | 0.4008016032064128 | 181 |
| 3 | 6.959 | 6053.887 | 18841.599 | 3.173884128651702 | 8.81% | 0.35070140280561124 | 163 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 51 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 0 | SQLTransientException | 69 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 187 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 38 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 1 | SQLTransientException | 79 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 137 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLException | 36 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 2 | SQLTransientException | 110 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 123 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLException | 43 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 3 | SQLTransientException | 140 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 135 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-01T18:53:41Z → 2026-07-01T19:08:41Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 28.5 | 45.0 | 0.198 | 69 | 0 |
| ojp-2 | 29.2 | 45.0 | 0.149 | 69 | 0 |
| ojp-3 | 28.3 | 45.0 | 0.130 | 63 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-01T18:53:41Z → 2026-07-01T19:08:41Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 22300 / 33362 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 414526891 | Cumulative since stats reset |
| Transactions rolled back | 3871 | Non-zero → contention or application errors |
| Temp file bytes written | -7 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 7 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4643 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 323500 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-01T18:53:41Z → 2026-07-01T19:08:41Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.5 | 1.0 | 4.9 | 12.7 | 23.5 | 6.3 | 3.9 | 32.5 | 34.6 | 85.3 | 228.2 | 229.4 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.6 | 1.0 | 4.9 | 8.8 | 30.4 | 4.7 | 3.9 | 7.8 | 21.6 | 35.3 | 225.2 | 226.8 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.5 | 1.0 | 3.9 | 11.7 | 19.6 | 4.8 | 3.9 | 7.8 | 33.5 | 49.3 | 223.2 | 224.8 |
| PostgreSQL | db | 164.3 | 169.5 | 303.4 | 326.2 | 337.4 | 336.4 | 398.9 | 400.0 | 400.0 | 400.0 | 6425.1 | 10389.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-01T19:11:28Z*

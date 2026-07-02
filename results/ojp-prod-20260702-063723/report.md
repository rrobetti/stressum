# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T05:49:17Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260702-063723` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 4.18 RPS (per instance) |
| **Total throughput** | 16.71 RPS (all instances) |
| **p50 latency** | 6.41 ms |
| **p95 latency** | 4899.82 ms |
| **p99 latency** | 20094.97 ms |
| **p999 latency** | 33665.00 ms |
| **Error rate** | 40.00% (0.40) |
| **Total requests** | 28814 |
| **Failed requests** | 11633 |
| **Total successful** | 17181 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 17.08 |
| observed_postgres_backends_median_numbackends | 17 |
| observed_client_backends_active_median | 27000 |
| observed_client_backends_active_max | 39759 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.1% / 3.9% / 11.8% / 17.6% / 32.3% |
| OJP proxy-tier host_cpu (avg / peak) | 19.1% / 86.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 73.40% |
| OJP proxy-tier RSS (avg / peak, summed) | 683.80 MiB / 686.30 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.1% / 3.9% / 11.8% / 17.6% / 32.3% |
| PgBouncer tier RSS (avg / peak, summed) | 683.80 MiB / 686.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 5.1% / 3.9% / 11.8% / 17.6% / 32.3% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 19.1% / 86.3% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 73.40% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 683.80 MiB / 686.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.41% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 969 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (4899.82 ms) |
| Error rate | < 0.1% | ❌ FAIL (40.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 28.01 RPS (all instances) |
| **Achieved throughput** | 16.71 RPS (all instances) |
| **Attempted − achieved gap** | 11.30 RPS (40.35%) |
| **Total attempted ops** | 28804 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.127 | 4296.703 | 19660.799 | 4.337363454723117 | 38.08% | 0.4016064257028112 | 255 |
| 1 | 6.599 | 5091.327 | 20463.615 | 4.047086311320005 | 42.09% | 0.4008016032064128 | 242 |
| 2 | 6.051 | 5238.783 | 19726.335 | 4.203074988735682 | 40.05% | 0.4016064257028112 | 243 |
| 3 | 6.843 | 4972.543 | 20529.151 | 4.117754139900454 | 41.27% | 0.4506760140210316 | 229 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 79 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 0 | SQLTransientException | 2584 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 80 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: ac3451c82f425cef |
| 1 | SQLException | 75 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 1 | SQLTransientException | 2857 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 100 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLException | 76 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 2 | SQLTransientException | 2710 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 99 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLException | 116 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 3 | SQLTransientException | 2749 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 108 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 5719e1e7b8f36461 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-02T05:49:17Z → 2026-07-02T06:04:17Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 27.5 | 43.0 | 0.353 | 115 | 0 |
| ojp-2 | 24.8 | 40.0 | 0.535 | 96 | 0 |
| ojp-3 | 29.7 | 50.0 | 0.123 | 59 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T05:49:17Z → 2026-07-02T06:04:17Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 17 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 27000 / 39759 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 512345383 | Cumulative since stats reset |
| Transactions rolled back | 5513 | Non-zero → contention or application errors |
| Temp file bytes written | 2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7496 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 539784 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T05:49:17Z → 2026-07-02T06:04:17Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.7 | 1.0 | 4.9 | 8.8 | 32.3 | 7.1 | 3.9 | 33.3 | 35.5 | 68.9 | 225.9 | 226.7 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.9 | 1.0 | 5.9 | 9.8 | 21.5 | 8.2 | 4.9 | 35.3 | 41.0 | 80.4 | 222.0 | 222.3 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.6 | 1.0 | 4.9 | 8.8 | 19.6 | 4.2 | 3.9 | 6.9 | 11.8 | 24.5 | 235.9 | 237.3 |
| PostgreSQL | db | 186.6 | 187.2 | 307.5 | 327.8 | 347.2 | 361.4 | 399.5 | 400.0 | 400.0 | 400.0 | 6987.0 | 10523.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T06:07:00Z*

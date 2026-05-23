# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-22T20:42:29Z |
| **Duration** | 1800 s |
| **Instances**| 4 |
| **Target RPS**| 5 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-sqs-prod-20260522-213044` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.18 RPS (per instance) |
| **Total throughput** | 4.73 RPS (all instances) |
| **p50 latency** | 12.63 ms |
| **p95 latency** | 2482.83 ms |
| **p99 latency** | 17696.75 ms |
| **p999 latency** | 32039.00 ms |
| **Error rate** | 71.00% (0.71) |
| **Total requests** | 36013 |
| **Failed requests** | 25493 |
| **Total successful** | 10520 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 19.02 |
| observed_postgres_backends_median_numbackends | 20 |
| observed_client_backends_active_median | 23049 |
| observed_client_backends_active_max | 38454 |
| observed_client_backends_idle_median | 135 |
| observed_client_backends_idle_max | 139 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-sqs-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 15 |
| OJP servers | 3 |
| Real DB connections per OJP server | 5 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 35.4% / 3.9% / 173.7% / 304.9% / 490.8% |
| OJP proxy-tier host_cpu (avg / peak) | 45.8% / 509.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 573.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 2775.00 MiB / 3609.10 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 35.4% / 3.9% / 173.7% / 304.9% / 490.8% |
| PgBouncer tier RSS (avg / peak, summed) | 2775.00 MiB / 3609.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 35.4% / 3.9% / 173.7% / 304.9% / 490.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 45.8% / 509.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 573.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 2775.00 MiB / 3609.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.23% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 2940 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 150 ms | ❌ FAIL (2482.83 ms) |
| Error rate | < 0.1% | ❌ FAIL (71.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 16.20 RPS (all instances) |
| **Achieved throughput** | 4.73 RPS (all instances) |
| **Attempted − achieved gap** | 11.46 RPS (70.78%) |
| **Total attempted ops** | 42004 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 1.95 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 12.679 | 4161.535 | 16973.823 | 1.188225446755208 | 70.69% | 0.2506265664160401 | 663 |
| 1 | 12.695 | 2643.967 | 17563.647 | 1.1835627169209941 | 70.73% | 0.20502306509482315 | 718 |
| 2 | 12.447 | 3041.279 | 19709.951 | 1.1870196989494943 | 70.68% | 0.2506265664160401 | 762 |
| 3 | 12.719 | 84.543 | 16539.647 | 1.1736761590220894 | 71.05% | 0.20050125313283207 | 797 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 93 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 0 | SQLTransientException | 6187 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 85 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 784b8f8017db5c2a |
| 1 | SQLException | 85 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 1 | SQLTransientException | 6206 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 77 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 1895a7989b63b646 |
| 2 | SQLException | 88 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 2 | SQLTransientException | 6197 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 78 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 784b8f8017db5c2a |
| 3 | SQLException | 92 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 3 | SQLTransientException | 6206 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 99 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 784b8f8017db5c2a |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-22T20:42:29Z → 2026-05-22T21:12:29Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 518.1 | 787.0 | 17.492 | 810 | 3 |
| ojp-2 | 473.4 | 763.0 | 10.794 | 469 | 0 |
| ojp-3 | 462.7 | 624.0 | 16.270 | 899 | 3 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-22T20:42:29Z → 2026-05-22T21:12:29Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 20 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 23049 / 38454 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 135 / 139 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 446425036 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | -2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 3 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 13681 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 1377392 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-22T20:42:29Z → 2026-05-22T21:12:29Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 13.0 | 1.0 | 127.7 | 173.4 | 196.1 | 17.0 | 3.9 | 135.7 | 187.4 | 199.1 | 975.6 | 1203.3 |
| Proxy (OJP / pgBouncer) | ojp-2 | 9.5 | 1.0 | 79.5 | 163.7 | 181.3 | 12.7 | 3.0 | 85.6 | 174.4 | 192.3 | 953.5 | 1208.6 |
| Proxy (OJP / pgBouncer) | ojp-3 | 13.7 | 1.0 | 128.0 | 170.7 | 195.6 | 17.1 | 3.9 | 135.3 | 179.1 | 199.1 | 845.9 | 1197.2 |
| PostgreSQL | db | 210.2 | 231.5 | 318.1 | 333.3 | 360.2 | 345.7 | 396.5 | 400.0 | 400.0 | 400.0 | 16484.4 | 31958.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-22T21:15:02Z*

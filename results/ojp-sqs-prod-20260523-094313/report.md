# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-23T08:55:07Z |
| **Duration** | 1800 s |
| **Instances**| 4 |
| **Target RPS**| 5 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-sqs-prod-20260523-094313` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.24 RPS (per instance) |
| **Total throughput** | 4.97 RPS (all instances) |
| **p50 latency** | 12.25 ms |
| **p95 latency** | 1112.17 ms |
| **p99 latency** | 17141.78 ms |
| **p999 latency** | 31625.25 ms |
| **Error rate** | 69.00% (0.69) |
| **Total requests** | 36008 |
| **Failed requests** | 24911 |
| **Total successful** | 11097 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 23 |
| observed_postgres_backends_avg_numbackends | 18.85 |
| observed_postgres_backends_median_numbackends | 19 |
| observed_client_backends_active_median | 23565 |
| observed_client_backends_active_max | 39272 |
| observed_client_backends_idle_median | 91 |
| observed_client_backends_idle_max | 91 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-sqs-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 15 |
| OJP servers | 3 |
| Real DB connections per OJP server | 5 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 36.9% / 3.9% / 184.9% / 324.2% / 424.4% |
| OJP proxy-tier host_cpu (avg / peak) | 48.6% / 486.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 587.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 2704.80 MiB / 3595.40 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 36.9% / 3.9% / 184.9% / 324.2% / 424.4% |
| PgBouncer tier RSS (avg / peak, summed) | 2704.80 MiB / 3595.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 36.9% / 3.9% / 184.9% / 324.2% / 424.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 48.6% / 486.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 587.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 2704.80 MiB / 3595.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.24% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 3302 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 150 ms | ❌ FAIL (1112.17 ms) |
| Error rate | < 0.1% | ❌ FAIL (69.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 16.12 RPS (all instances) |
| **Achieved throughput** | 4.97 RPS (all instances) |
| **Attempted − achieved gap** | 11.15 RPS (69.18%) |
| **Total attempted ops** | 42004 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.58 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 12.255 | 1465.343 | 15679.487 | 1.3238113072793087 | 67.10% | 0.2503755633450175 | 878 |
| 1 | 11.743 | 96.319 | 17940.479 | 1.287795912616541 | 68.12% | 0.2502502502502503 | 769 |
| 2 | 12.263 | 2646.015 | 18350.079 | 1.2139001183474314 | 69.86% | 0.2503755633450175 | 784 |
| 3 | 12.743 | 241.023 | 16596.991 | 1.1438611589213998 | 71.65% | 0.20050125313283207 | 871 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 39 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 0 | SQLTransientException | 5941 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 60 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLException | 38 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 1 | SQLTransientException | 6040 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 54 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 784b8f8017db5c2a |
| 2 | SQLException | 50 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 2 | SQLTransientException | 6194 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 45 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 1895a7989b63b646 |
| 3 | SQLException | 62 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 3 | SQLTransientException | 6334 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 54 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 784b8f8017db5c2a |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-23T08:55:07Z → 2026-05-23T09:25:07Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 420.2 | 643.0 | 15.796 | 821 | 1 |
| ojp-2 | 448.5 | 682.0 | 13.875 | 732 | 1 |
| ojp-3 | 492.9 | 725.0 | 14.918 | 631 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-23T08:55:07Z → 2026-05-23T09:25:07Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 19 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 23565 / 39272 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 91 / 91 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 538035922 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | -2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 13591 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 1366773 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-23T08:55:07Z → 2026-05-23T09:25:07Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 13.7 | 1.0 | 126.5 | 169.9 | 195.1 | 17.3 | 3.9 | 134.0 | 177.0 | 200.0 | 901.0 | 1189.1 |
| Proxy (OJP / pgBouncer) | ojp-2 | 11.3 | 1.0 | 109.7 | 170.1 | 196.9 | 15.0 | 3.9 | 113.9 | 184.4 | 200.0 | 856.3 | 1199.0 |
| Proxy (OJP / pgBouncer) | ojp-3 | 12.7 | 1.0 | 114.0 | 168.0 | 195.8 | 17.4 | 3.9 | 125.2 | 177.1 | 200.0 | 947.5 | 1207.3 |
| PostgreSQL | db | 207.2 | 213.7 | 317.5 | 327.2 | 347.9 | 342.9 | 386.3 | 400.0 | 400.0 | 400.0 | 16233.6 | 28958.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-23T09:27:52Z*

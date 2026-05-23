# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-23T00:46:38Z |
| **Duration** | 1800 s |
| **Instances**| 4 |
| **Target RPS**| 5 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-sqs-prod-20260523-013451` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.27 RPS (per instance) |
| **Total throughput** | 5.09 RPS (all instances) |
| **p50 latency** | 11.87 ms |
| **p95 latency** | 1904.70 ms |
| **p99 latency** | 16013.33 ms |
| **p999 latency** | 35262.50 ms |
| **Error rate** | 69.00% (0.69) |
| **Total requests** | 36016 |
| **Failed requests** | 24694 |
| **Total successful** | 11322 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 18.88 |
| observed_postgres_backends_median_numbackends | 19 |
| observed_client_backends_active_median | 23778 |
| observed_client_backends_active_max | 39694 |
| observed_client_backends_idle_median | 104 |
| observed_client_backends_idle_max | 104 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-sqs-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 15 |
| OJP servers | 3 |
| Real DB connections per OJP server | 5 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 37.6% / 3.9% / 181.2% / 296.4% / 460.0% |
| OJP proxy-tier host_cpu (avg / peak) | 47.5% / 474.7% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 588.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 2799.90 MiB / 3638.30 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 37.6% / 3.9% / 181.2% / 296.4% / 460.0% |
| PgBouncer tier RSS (avg / peak, summed) | 2799.90 MiB / 3638.30 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 37.6% / 3.9% / 181.2% / 296.4% / 460.0% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 47.5% / 474.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 588.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 2799.90 MiB / 3638.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.24% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 3352 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 150 ms | ❌ FAIL (1904.70 ms) |
| Error rate | < 0.1% | ❌ FAIL (69.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 16.19 RPS (all instances) |
| **Achieved throughput** | 5.09 RPS (all instances) |
| **Attempted − achieved gap** | 11.10 RPS (68.55%) |
| **Total attempted ops** | 42004 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.66 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 12.055 | 2476.031 | 15581.183 | 1.344323674268754 | 66.81% | 0.3003003003003003 | 989 |
| 1 | 12.247 | 143.615 | 16539.647 | 1.2265019705378857 | 69.69% | 0.20714655618850336 | 662 |
| 2 | 11.367 | 2539.519 | 15613.951 | 1.2702949822450464 | 68.57% | 0.250501002004008 | 853 |
| 3 | 11.791 | 2459.647 | 16318.463 | 1.2499819822416973 | 69.18% | 0.20263429718927034 | 848 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 45 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 0 | SQLTransientException | 5904 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 67 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 784b8f8017db5c2a |
| 1 | SQLException | 48 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 1 | SQLTransientException | 6144 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 83 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 784b8f8017db5c2a |
| 2 | SQLException | 62 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 2 | SQLTransientException | 6056 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 56 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 1895a7989b63b646 |
| 3 | SQLException | 66 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 5000ms (phase=admission) |
| 3 | SQLTransientException | 6117 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 46 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 1895a7989b63b646 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-23T00:46:38Z → 2026-05-23T01:16:38Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 489.5 | 758.0 | 17.089 | 724 | 2 |
| ojp-2 | 482.8 | 735.0 | 14.637 | 652 | 0 |
| ojp-3 | 475.6 | 634.0 | 13.037 | 669 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-23T00:46:38Z → 2026-05-23T01:16:38Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 19 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 23778 / 39694 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 104 / 104 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 498975374 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 3 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 13773 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 1385684 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-23T00:46:38Z → 2026-05-23T01:16:38Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 13.9 | 1.0 | 130.7 | 171.6 | 196.3 | 17.2 | 3.9 | 137.0 | 179.7 | 200.0 | 973.9 | 1218.5 |
| Proxy (OJP / pgBouncer) | ojp-2 | 12.8 | 1.0 | 120.3 | 170.4 | 196.0 | 16.2 | 3.9 | 129.5 | 177.3 | 200.0 | 946.3 | 1208.5 |
| Proxy (OJP / pgBouncer) | ojp-3 | 11.7 | 1.0 | 107.8 | 168.1 | 195.7 | 15.2 | 3.9 | 115.9 | 178.5 | 200.0 | 879.7 | 1211.3 |
| PostgreSQL | db | 203.2 | 205.2 | 319.3 | 328.8 | 345.6 | 341.8 | 392.8 | 400.0 | 400.0 | 400.0 | 16273.4 | 31275.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-23T01:19:17Z*

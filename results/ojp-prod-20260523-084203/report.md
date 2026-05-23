# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-23T07:54:02Z |
| **Duration** | 1800 s |
| **Instances**| 4 |
| **Target RPS**| 5 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260523-084203` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.83 RPS (per instance) |
| **Total throughput** | 3.32 RPS (all instances) |
| **p50 latency** | 11.12 ms |
| **p95 latency** | 119.63 ms |
| **p99 latency** | 17641.47 ms |
| **p999 latency** | 40526.00 ms |
| **Error rate** | 79.00% (0.79) |
| **Total requests** | 36018 |
| **Failed requests** | 28529 |
| **Total successful** | 7489 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 23 |
| observed_postgres_backends_avg_numbackends | 17.67 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 21064 |
| observed_client_backends_active_max | 33242 |
| observed_client_backends_idle_median | 5 |
| observed_client_backends_idle_max | 14 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 15 |
| OJP servers | 3 |
| Real DB connections per OJP server | 5 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 22.0% / 2.9% / 159.7% / 198.2% / 314.4% |
| OJP proxy-tier host_cpu (avg / peak) | 32.7% / 333.8% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 588.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 2973.10 MiB / 3537.60 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 22.0% / 2.9% / 159.7% / 198.2% / 314.4% |
| PgBouncer tier RSS (avg / peak, summed) | 2973.10 MiB / 3537.60 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 22.0% / 2.9% / 159.7% / 198.2% / 314.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 32.7% / 333.8% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 588.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 2973.10 MiB / 3537.60 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.23% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1809 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 150 ms | ✅ PASS (119.63 ms) |
| Error rate | < 0.1% | ❌ FAIL (79.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.97 RPS (all instances) |
| **Achieved throughput** | 3.32 RPS (all instances) |
| **Attempted − achieved gap** | 12.65 RPS (79.20%) |
| **Total attempted ops** | 42004 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.63 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 10.567 | 164.863 | 17891.327 | 0.8487722071004186 | 78.74% | 0.250501002004008 | 558 |
| 1 | 10.991 | 66.047 | 16662.527 | 0.8367993025342113 | 79.04% | 0.2004008016032064 | 433 |
| 2 | 11.399 | 192.511 | 17940.479 | 0.8434443927577305 | 78.88% | 0.2502502502502503 | 552 |
| 3 | 11.511 | 55.103 | 18071.551 | 0.7920086065526518 | 80.17% | 0.20030045067601399 | 266 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 430 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 0 | SQLTransientException | 6450 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 209 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: 784b8f8017db5c2a |
| 1 | SQLException | 402 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 1 | SQLTransientException | 6530 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 185 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 2 | SQLException | 398 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 2 | SQLTransientException | 6460 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 245 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 3 | SQLException | 406 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 3 | SQLTransientException | 6520 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 294 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: 19ddf4bbc5b8c770 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-23T07:54:02Z → 2026-05-23T08:24:02Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 439.6 | 794.0 | 16.629 | 752 | 0 |
| ojp-2 | 683.2 | 980.0 | 10.910 | 122 | 15 |
| ojp-3 | 474.7 | 657.0 | 5.634 | 284 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-23T07:54:02Z → 2026-05-23T08:24:02Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 21064 / 33242 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 5 / 14 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 348957320 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -3 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 14363 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 1434207 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-23T07:54:02Z → 2026-05-23T08:24:02Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 14.6 | 1.0 | 137.8 | 171.2 | 196.2 | 17.9 | 3.9 | 145.2 | 178.6 | 200.0 | 946.2 | 1186.4 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.1 | 0.0 | 2.0 | 21.5 | 196.6 | 5.8 | 2.9 | 13.7 | 35.5 | 200.0 | 1177.9 | 1180.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 5.8 | 1.0 | 8.7 | 162.3 | 196.0 | 9.7 | 3.9 | 33.3 | 171.0 | 199.0 | 849.0 | 1171.1 |
| PostgreSQL | db | 112.0 | 99.6 | 305.5 | 323.3 | 331.4 | 233.9 | 204.1 | 400.0 | 400.0 | 400.0 | 13150.8 | 28408.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-23T08:27:08Z*

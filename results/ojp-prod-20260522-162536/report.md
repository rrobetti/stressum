# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-22T15:37:38Z |
| **Duration** | 1800 s |
| **Instances**| 4 |
| **Target RPS**| 5 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260522-162536` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.50 RPS (per instance) |
| **Total throughput** | 2.00 RPS (all instances) |
| **p50 latency** | 12.45 ms |
| **p95 latency** | 9730.05 ms |
| **p99 latency** | 45940.75 ms |
| **p999 latency** | 61726.75 ms |
| **Error rate** | 88.00% (0.88) |
| **Total requests** | 36016 |
| **Failed requests** | 31562 |
| **Total successful** | 4454 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 23 |
| observed_postgres_backends_avg_numbackends | 17.00 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 18057 |
| observed_client_backends_active_max | 25912 |
| observed_client_backends_idle_median | 114 |
| observed_client_backends_idle_max | 231 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 15 |
| OJP servers | 3 |
| Real DB connections per OJP server | 5 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 18.7% / 2.0% / 165.1% / 196.7% / 382.5% |
| OJP proxy-tier host_cpu (avg / peak) | 28.2% / 393.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 589.50% |
| OJP proxy-tier RSS (avg / peak, summed) | 2891.70 MiB / 3540.10 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 18.7% / 2.0% / 165.1% / 196.7% / 382.5% |
| PgBouncer tier RSS (avg / peak, summed) | 2891.70 MiB / 3540.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 18.7% / 2.0% / 165.1% / 196.7% / 382.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 28.2% / 393.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 589.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 2891.70 MiB / 3540.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.20% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1805 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 150 ms | ❌ FAIL (9730.05 ms) |
| Error rate | < 0.1% | ❌ FAIL (88.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 16.18 RPS (all instances) |
| **Achieved throughput** | 2.00 RPS (all instances) |
| **Attempted − achieved gap** | 14.18 RPS (87.63%) |
| **Total attempted ops** | 42004 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.62 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 11.999 | 10305.535 | 38567.935 | 0.5060774195170755 | 87.48% | 0.20060180541624875 | 478 |
| 1 | 12.071 | 8036.351 | 38273.023 | 0.4801588922061237 | 88.12% | 0.2001000500250125 | 508 |
| 2 | 13.263 | 12091.391 | 59736.063 | 0.47952202540027267 | 88.16% | 0.2007024586051179 | 410 |
| 3 | 12.455 | 8486.911 | 47185.919 | 0.5360928687495217 | 86.77% | 0.20020020020020018 | 409 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 933 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 0 | SQLTransientException | 5977 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 966 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: 19ddf4bbc5b8c770 |
| 1 | SQLException | 976 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 1 | SQLTransientException | 5807 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 1150 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: 1895a7989b63b646 |
| 2 | SQLException | 962 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 2 | SQLTransientException | 5848 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 1129 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: 1895a7989b63b646 |
| 3 | SQLException | 954 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 3 | SQLTransientException | 6125 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 735 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: 19ddf4bbc5b8c770 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-22T15:37:38Z → 2026-05-22T16:07:38Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 444.3 | 980.0 | 6.577 | 297 | 2 |
| ojp-2 | 577.1 | 937.0 | 5.809 | 357 | 2 |
| ojp-3 | 663.1 | 980.0 | 12.773 | 753 | 3 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-22T15:37:38Z → 2026-05-22T16:07:38Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 18057 / 25912 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 114 / 231 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 240043294 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6934 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 695119 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-22T15:37:38Z → 2026-05-22T16:07:38Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 5.0 | 0.0 | 4.9 | 182.0 | 197.2 | 8.3 | 3.0 | 18.7 | 194.4 | 200.0 | 965.6 | 1185.3 |
| Proxy (OJP / pgBouncer) | ojp-2 | 4.3 | 0.0 | 4.9 | 172.3 | 195.6 | 7.7 | 3.0 | 19.5 | 179.8 | 199.1 | 870.2 | 1173.3 |
| Proxy (OJP / pgBouncer) | ojp-3 | 9.7 | 1.0 | 76.8 | 193.5 | 196.7 | 12.7 | 3.0 | 82.0 | 197.2 | 200.0 | 1055.9 | 1181.5 |
| PostgreSQL | db | 72.3 | 0.7 | 305.6 | 327.6 | 339.6 | 177.7 | 99.0 | 400.0 | 400.0 | 400.0 | 12563.7 | 42024.4 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-22T16:10:17Z*

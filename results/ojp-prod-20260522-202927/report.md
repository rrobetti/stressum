# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-22T19:41:27Z |
| **Duration** | 1800 s |
| **Instances**| 4 |
| **Target RPS**| 5 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260522-202927` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.20 RPS (per instance) |
| **Total throughput** | 0.81 RPS (all instances) |
| **p50 latency** | 10.46 ms |
| **p95 latency** | 29585.50 ms |
| **p99 latency** | 59990.00 ms |
| **p999 latency** | 63086.50 ms |
| **Error rate** | 95.00% (0.95) |
| **Total requests** | 36035 |
| **Failed requests** | 34200 |
| **Total successful** | 1835 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 16.38 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 16348 |
| observed_client_backends_active_max | 22995 |
| observed_client_backends_idle_median | 135 |
| observed_client_backends_idle_max | 265 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 15 |
| OJP servers | 3 |
| Real DB connections per OJP server | 5 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 7.6% / 1.0% / 11.7% / 195.0% / 361.8% |
| OJP proxy-tier host_cpu (avg / peak) | 16.8% / 374.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 413.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 2983.40 MiB / 3541.60 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 7.6% / 1.0% / 11.7% / 195.0% / 361.8% |
| PgBouncer tier RSS (avg / peak, summed) | 2983.40 MiB / 3541.60 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 7.6% / 1.0% / 11.7% / 195.0% / 361.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.8% / 374.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 413.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 2983.40 MiB / 3541.60 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.18% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 676 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 150 ms | ❌ FAIL (29585.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (95.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.97 RPS (all instances) |
| **Achieved throughput** | 0.81 RPS (all instances) |
| **Attempted − achieved gap** | 15.15 RPS (94.90%) |
| **Total attempted ops** | 42004 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.64 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 10.303 | 29425.663 | 60030.975 | 0.2119712304486473 | 94.69% | 0.2004008016032064 | 196 |
| 1 | 9.927 | 29147.135 | 60030.975 | 0.23192678386286253 | 94.20% | 0.15022533800701052 | 201 |
| 2 | 11.399 | 29884.415 | 60030.975 | 0.1902419620553759 | 95.24% | 0.20030045067601399 | 111 |
| 3 | 10.223 | 29884.415 | 59867.135 | 0.17959897544327688 | 95.50% | 0.15015015015015015 | 168 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 1329 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 0 | SQLTransientException | 6298 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 901 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: 19ddf4bbc5b8c770 |
| 1 | SQLException | 1321 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 1 | SQLTransientException | 5907 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 1260 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: 7f357af8205cfa4e |
| 2 | SQLException | 1336 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 2 | SQLTransientException | 6288 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 956 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: 784b8f8017db5c2a |
| 3 | SQLException | 1375 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 3 | SQLTransientException | 6265 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 964 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-22T19:41:27Z → 2026-05-22T20:11:27Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 679.5 | 980.0 | 0.009 | 1 | 0 |
| ojp-2 | 433.2 | 551.0 | 5.191 | 285 | 2 |
| ojp-3 | 615.6 | 980.0 | 3.323 | 224 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-22T19:41:27Z → 2026-05-22T20:11:27Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 16348 / 22995 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 135 / 265 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 82071561 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | -2 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5871 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 588375 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-22T19:41:27Z → 2026-05-22T20:11:27Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 0.6 | 0.0 | 2.0 | 5.9 | 21.6 | 4.0 | 3.0 | 5.9 | 32.5 | 35.3 | 1172.8 | 1174.3 |
| Proxy (OJP / pgBouncer) | ojp-2 | 3.8 | 0.0 | 3.9 | 167.9 | 195.9 | 7.0 | 3.0 | 9.8 | 175.4 | 200.0 | 784.3 | 1183.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 3.3 | 0.0 | 3.9 | 146.6 | 196.1 | 6.2 | 3.0 | 6.8 | 155.6 | 200.0 | 1026.3 | 1184.2 |
| PostgreSQL | db | 24.7 | 0.6 | 246.9 | 304.5 | 335.1 | 128.1 | 96.7 | 395.6 | 400.0 | 400.0 | 9976.8 | 31930.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-22T20:14:30Z*

# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-05-22T23:46:04Z |
| **Duration** | 1800 s |
| **Instances**| 4 |
| **Target RPS**| 5 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260523-003408` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.51 RPS (per instance) |
| **Total throughput** | 2.05 RPS (all instances) |
| **p50 latency** | 12.42 ms |
| **p95 latency** | 8942.60 ms |
| **p99 latency** | 38289.50 ms |
| **p999 latency** | 61948.00 ms |
| **Error rate** | 87.00% (0.87) |
| **Total requests** | 36033 |
| **Failed requests** | 31451 |
| **Total successful** | 4582 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 15 |
| observed_postgres_backends_max_numbackends | 24 |
| observed_postgres_backends_avg_numbackends | 17.26 |
| observed_postgres_backends_median_numbackends | 16 |
| observed_client_backends_active_median | 17915 |
| observed_client_backends_active_max | 26614 |
| observed_client_backends_idle_median | 111 |
| observed_client_backends_idle_max | 214 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 15 |
| OJP servers | 3 |
| Real DB connections per OJP server | 5 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 13.8% / 2.0% / 125.7% / 195.7% / 232.4% |
| OJP proxy-tier host_cpu (avg / peak) | 28.6% / 249.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 587.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 2740.00 MiB / 3571.10 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 13.8% / 2.0% / 125.7% / 195.7% / 232.4% |
| PgBouncer tier RSS (avg / peak, summed) | 2740.00 MiB / 3571.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 13.8% / 2.0% / 125.7% / 195.7% / 232.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 28.6% / 249.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 587.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 2740.00 MiB / 3571.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.20% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1259 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 150 ms | ❌ FAIL (8942.60 ms) |
| Error rate | < 0.1% | ❌ FAIL (87.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 16.14 RPS (all instances) |
| **Achieved throughput** | 2.05 RPS (all instances) |
| **Attempted − achieved gap** | 14.09 RPS (87.27%) |
| **Total attempted ops** | 42004 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.52 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 12.255 | 7340.031 | 36143.103 | 0.5496174698362023 | 86.42% | 0.250501002004008 | 310 |
| 1 | 11.783 | 9551.871 | 39944.191 | 0.5667509688165808 | 85.98% | 0.20020020020020018 | 384 |
| 2 | 12.487 | 11599.871 | 38076.415 | 0.46257376040288156 | 88.51% | 0.20050125313283207 | 265 |
| 3 | 13.159 | 7278.591 | 38993.919 | 0.4758214534932739 | 88.22% | 0.15022533800701052 | 300 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 893 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 0 | SQLTransientException | 5849 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 1043 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: 7f357af8205cfa4e |
| 1 | SQLException | 883 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 1 | SQLTransientException | 5961 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 902 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: e7282124a6fbdd3c |
| 2 | SQLException | 966 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 2 | SQLTransientException | 6503 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 503 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: 1895a7989b63b646 |
| 3 | SQLException | 969 | Connection admission timeout for hash: Ld--4pNhqOb-WVk0RbA8aOPs_VIISdRyE87pgVYf_p8 after 30000ms (phase=admission) |
| 3 | SQLTransientException | 6431 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 548 | RESOURCE_EXHAUSTED: Timeout waiting for admission control slot for operation: 19ddf4bbc5b8c770 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-05-22T23:46:04Z → 2026-05-23T00:16:04Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 515.0 | 629.0 | 1.903 | 97 | 0 |
| ojp-2 | 411.8 | 646.0 | 7.408 | 552 | 3 |
| ojp-3 | 490.7 | 913.0 | 8.061 | 459 | 2 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-05-22T23:46:04Z → 2026-05-23T00:16:04Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 16 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 17915 / 26614 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 111 / 214 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 217043416 | Cumulative since stats reset |
| Transactions rolled back | 0 | Non-zero → contention or application errors |
| Temp file bytes written | 4 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 7 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6958 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 707087 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-05-22T23:46:04Z → 2026-05-23T00:16:04Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.5 | 0.0 | 3.9 | 58.6 | 195.7 | 5.9 | 3.0 | 10.8 | 61.9 | 200.0 | 711.4 | 1173.6 |
| Proxy (OJP / pgBouncer) | ojp-2 | 5.7 | 0.0 | 11.7 | 192.1 | 195.8 | 9.3 | 3.0 | 33.3 | 196.2 | 199.1 | 929.1 | 1186.5 |
| Proxy (OJP / pgBouncer) | ojp-3 | 5.9 | 1.0 | 10.7 | 164.7 | 196.3 | 14.0 | 3.9 | 36.3 | 181.6 | 200.0 | 1099.5 | 1211.0 |
| PostgreSQL | db | 78.0 | 0.7 | 306.4 | 321.4 | 337.9 | 185.3 | 100.0 | 400.0 | 400.0 | 400.0 | 12872.3 | 34846.4 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-05-23T00:18:51Z*

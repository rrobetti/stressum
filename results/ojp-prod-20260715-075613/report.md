# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T07:08:09Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 2 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260715-075613` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.80 RPS (per instance) |
| **Total throughput** | 28.74 RPS (all instances) |
| **p50 latency** | 5.13 ms |
| **p95 latency** | 296.65 ms |
| **p99 latency** | 34893.69 ms |
| **p999 latency** | 46221.25 ms |
| **Error rate** | 10.00% (0.10) |
| **Total requests** | 28833 |
| **Failed requests** | 2774 |
| **Total successful** | 26059 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 53.34 |
| observed_postgres_backends_median_numbackends | 53 |
| observed_client_backends_active_median | 45104 |
| observed_client_backends_active_max | 68085 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 48 |
| OJP servers | 3 |
| Real DB connections per OJP server | 16 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.1% / 7.8% / 14.7% / 18.6% / 22.5% |
| OJP proxy-tier host_cpu (avg / peak) | 21.1% / 79.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 47.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 1120.70 MiB / 1134.80 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.1% / 7.8% / 14.7% / 18.6% / 22.5% |
| PgBouncer tier RSS (avg / peak, summed) | 1120.70 MiB / 1134.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.1% / 7.8% / 14.7% / 18.6% / 22.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 21.1% / 79.3% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 47.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1120.70 MiB / 1134.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.06% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 953 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (296.65 ms) |
| Error rate | < 0.1% | ❌ FAIL (10.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 31.78 RPS (all instances) |
| **Achieved throughput** | 28.74 RPS (all instances) |
| **Attempted − achieved gap** | 3.04 RPS (9.56%) |
| **Total attempted ops** | 28810 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.939 | 1325.055 | 32555.007 | 1.8249061603002872 | 8.27% | 0.06256256256256257 | 51 |
| 10 | 4.659 | 56.543 | 36110.335 | 1.7693145625176003 | 10.04% | 0.06257039169065198 | 51 |
| 11 | 4.899 | 44.031 | 34209.791 | 1.7448712352684417 | 11.27% | 0.06256256256256257 | 63 |
| 12 | 4.887 | 55.615 | 34340.863 | 1.7962914916285309 | 9.71% | 0.0625782227784731 | 52 |
| 13 | 4.939 | 52.991 | 36667.391 | 1.739454963503092 | 11.54% | 0.06257039169065198 | 66 |
| 14 | 5.115 | 53.631 | 35454.975 | 1.821400681527758 | 8.88% | 0.06257822277847308 | 57 |
| 15 | 5.283 | 45.663 | 36405.247 | 1.770116847600895 | 11.10% | 0.06257039169065198 | 69 |
| 1 | 5.491 | 1390.591 | 33554.431 | 1.8188456231338632 | 8.49% | 0.06257039169065198 | 69 |
| 2 | 5.339 | 55.743 | 32948.223 | 1.8392038732639406 | 7.60% | 0.06256256256256257 | 56 |
| 3 | 5.083 | 1318.911 | 34340.863 | 1.8172638965452101 | 8.66% | 0.06257039169065198 | 62 |
| 4 | 5.151 | 57.087 | 35291.135 | 1.8036545635455454 | 9.77% | 0.0625782227784731 | 61 |
| 5 | 5.655 | 57.759 | 34570.239 | 1.7868968257472078 | 10.11% | 0.06255473539346929 | 59 |
| 6 | 6.083 | 55.583 | 33882.111 | 1.8136358795967626 | 9.27% | 0.06256647712660728 | 55 |
| 7 | 4.847 | 47.487 | 35586.047 | 1.7942550692677472 | 9.93% | 0.06256256256256257 | 61 |
| 8 | 4.487 | 74.495 | 35946.495 | 1.7929940906178772 | 9.82% | 0.06256256256256257 | 53 |
| 9 | 5.195 | 55.231 | 36438.015 | 1.8043377074518485 | 9.48% | 0.06257822277847308 | 68 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 149 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 10 | SQLTransientConnectionException | 181 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 11 | SQLTransientConnectionException | 203 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 12 | SQLTransientConnectionException | 175 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 13 | SQLTransientConnectionException | 208 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 14 | SQLTransientConnectionException | 160 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 15 | SQLTransientConnectionException | 200 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 1 | SQLTransientConnectionException | 153 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLTransientConnectionException | 137 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 3 | SQLTransientConnectionException | 156 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 4 | SQLTransientConnectionException | 176 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 5 | SQLTransientConnectionException | 182 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 6 | SQLTransientConnectionException | 167 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 7 | SQLTransientConnectionException | 179 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 8 | SQLTransientConnectionException | 177 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 9 | SQLTransientConnectionException | 171 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-15T07:08:09Z → 2026-07-15T07:23:09Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 29.6 | 50.0 | 0.294 | 142 | 0 |
| ojp-2 | 29.3 | 52.0 | 0.328 | 129 | 0 |
| ojp-3 | 30.6 | 52.0 | 0.341 | 125 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T07:08:09Z → 2026-07-15T07:23:09Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 53 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 45104 / 68085 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2238042515 | Cumulative since stats reset |
| Transactions rolled back | 1019 | Non-zero → contention or application errors |
| Temp file bytes written | -3 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 3 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3356 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 337024 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T07:08:09Z → 2026-07-15T07:23:09Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.6 | 2.0 | 6.8 | 9.8 | 15.7 | 9.1 | 4.9 | 35.3 | 40.2 | 59.7 | 353.5 | 359.2 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.9 | 2.0 | 7.8 | 10.8 | 13.7 | 6.5 | 4.9 | 11.8 | 35.3 | 45.0 | 376.1 | 380.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.8 | 2.0 | 6.8 | 11.7 | 17.6 | 6.0 | 4.9 | 10.7 | 34.3 | 37.2 | 391.1 | 395.5 |
| PostgreSQL | db | 746.6 | 763.9 | 989.5 | 1246.4 | 1314.1 | 1366.9 | 1460.2 | 1597.7 | 1598.8 | 1599.1 | 19407.0 | 31464.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T07:26:52Z*

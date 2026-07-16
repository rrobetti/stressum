# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T20:25:05Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260715-211258` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 2.75 RPS (per instance) |
| **Total throughput** | 44.08 RPS (all instances) |
| **p50 latency** | 4.58 ms |
| **p95 latency** | 179.30 ms |
| **p99 latency** | 36171.81 ms |
| **p999 latency** | 48136.19 ms |
| **Error rate** | 29.00% (0.29) |
| **Total requests** | 57724 |
| **Failed requests** | 16597 |
| **Total successful** | 41127 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 56 |
| observed_postgres_backends_avg_numbackends | 54.04 |
| observed_postgres_backends_median_numbackends | 56 |
| observed_client_backends_active_median | 59356 |
| observed_client_backends_active_max | 88409 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 10.4% / 9.8% / 17.6% / 23.5% / 39.1% |
| OJP proxy-tier host_cpu (avg / peak) | 34.6% / 116.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 69.50% |
| OJP proxy-tier RSS (avg / peak, summed) | 1162.90 MiB / 1168.40 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 10.4% / 9.8% / 17.6% / 23.5% / 39.1% |
| PgBouncer tier RSS (avg / peak, summed) | 1162.90 MiB / 1168.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 10.4% / 9.8% / 17.6% / 23.5% / 39.1% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 34.6% / 116.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 69.50% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1162.90 MiB / 1168.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.07% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1493 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (179.30 ms) |
| Error rate | < 0.1% | ❌ FAIL (29.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 61.75 RPS (all instances) |
| **Achieved throughput** | 44.08 RPS (all instances) |
| **Attempted − achieved gap** | 17.67 RPS (28.62%) |
| **Total attempted ops** | 57612 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 4.787 | 331.263 | 36962.303 | 2.5004812731278476 | 35.18% | 0.062625250501002 | 82 |
| 10 | 4.311 | 49.311 | 37388.287 | 2.888338387566801 | 25.59% | 0.075122073369225 | 90 |
| 11 | 4.935 | 44.191 | 34897.919 | 2.819199360279276 | 27.30% | 0.075122073369225 | 102 |
| 12 | 4.351 | 37.919 | 35028.991 | 2.6480511028908067 | 31.41% | 0.075122073369225 | 84 |
| 13 | 4.343 | 35.903 | 36110.335 | 2.772130251620017 | 28.10% | 0.07511266900350524 | 100 |
| 14 | 5.119 | 69.311 | 36438.015 | 2.6076121722822387 | 32.48% | 0.07511266900350524 | 86 |
| 15 | 4.339 | 47.871 | 35913.727 | 2.8104358853247904 | 27.25% | 0.07508447002878238 | 96 |
| 1 | 4.479 | 729.087 | 36143.103 | 2.7533924580616547 | 28.77% | 0.07507507507507508 | 99 |
| 2 | 4.571 | 55.103 | 35848.191 | 2.5490131004927807 | 34.03% | 0.07511737118636513 | 82 |
| 3 | 5.391 | 50.335 | 35651.583 | 2.6964361832672408 | 30.57% | 0.07511266900350526 | 100 |
| 4 | 4.463 | 758.783 | 36438.015 | 2.787106158157045 | 27.73% | 0.07511266900350526 | 87 |
| 5 | 4.459 | 167.423 | 36798.463 | 2.82839870683428 | 26.79% | 0.075122073369225 | 103 |
| 6 | 4.595 | 55.327 | 35520.511 | 2.766969118609957 | 28.46% | 0.07515030060120241 | 92 |
| 7 | 4.411 | 49.183 | 36241.407 | 2.822521516776182 | 26.95% | 0.07508447002878238 | 93 |
| 8 | 4.335 | 50.431 | 36044.799 | 2.977482786427641 | 22.84% | 0.075122073369225 | 92 |
| 9 | 4.315 | 337.407 | 37322.751 | 2.8495976342313294 | 26.59% | 0.07510326699211416 | 105 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 1269 | Client throttle limit reached; request rejected to avoid overloading the database |
| 10 | SQLTransientConnectionException | 923 | Client throttle limit reached; request rejected to avoid overloading the database |
| 11 | SQLTransientConnectionException | 985 | Client throttle limit reached; request rejected to avoid overloading the database |
| 12 | SQLTransientConnectionException | 1133 | Client throttle limit reached; request rejected to avoid overloading the database |
| 13 | SQLTransientConnectionException | 1013 | Client throttle limit reached; request rejected to avoid overloading the database |
| 14 | SQLTransientConnectionException | 1172 | Client throttle limit reached; request rejected to avoid overloading the database |
| 15 | SQLTransientConnectionException | 983 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLTransientConnectionException | 1038 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLTransientConnectionException | 1228 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLTransientConnectionException | 1103 | Client throttle limit reached; request rejected to avoid overloading the database |
| 4 | SQLTransientConnectionException | 1000 | Client throttle limit reached; request rejected to avoid overloading the database |
| 5 | SQLTransientConnectionException | 967 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 6 | SQLTransientConnectionException | 1027 | Client throttle limit reached; request rejected to avoid overloading the database |
| 7 | SQLTransientConnectionException | 973 | Client throttle limit reached; request rejected to avoid overloading the database |
| 8 | SQLTransientConnectionException | 824 | Client throttle limit reached; request rejected to avoid overloading the database |
| 9 | SQLTransientConnectionException | 959 | Client throttle limit reached; request rejected to avoid overloading the database |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-15T20:25:05Z → 2026-07-15T20:40:05Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 32.2 | 50.0 | 0.281 | 178 | 0 |
| ojp-2 | 31.4 | 56.0 | 0.436 | 171 | 0 |
| ojp-3 | 32.2 | 56.0 | 0.466 | 170 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T20:25:05Z → 2026-07-15T20:40:05Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 56 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 59356 / 88409 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2135026196 | Cumulative since stats reset |
| Transactions rolled back | 1888 | Non-zero → contention or application errors |
| Temp file bytes written | -1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7266 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 527979 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T20:25:05Z → 2026-07-15T20:40:05Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 3.0 | 2.9 | 7.8 | 12.7 | 28.4 | 5.4 | 4.9 | 9.8 | 15.7 | 37.4 | 383.2 | 386.0 |
| Proxy (OJP / pgBouncer) | ojp-2 | 3.9 | 2.9 | 7.8 | 10.8 | 24.5 | 14.2 | 6.9 | 39.2 | 54.0 | 89.2 | 382.2 | 383.5 |
| Proxy (OJP / pgBouncer) | ojp-3 | 3.7 | 2.9 | 9.8 | 11.7 | 16.6 | 15.7 | 7.8 | 38.2 | 51.9 | 77.3 | 397.5 | 398.9 |
| PostgreSQL | db | 765.4 | 764.5 | 997.8 | 1052.2 | 1156.8 | 1436.6 | 1508.3 | 1597.4 | 1598.3 | 1599.0 | 28266.2 | 39872.6 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T20:44:11Z*

# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T22:04:38Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260715-225230` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 3.12 RPS (per instance) |
| **Total throughput** | 50.00 RPS (all instances) |
| **p50 latency** | 4.28 ms |
| **p95 latency** | 28.92 ms |
| **p99 latency** | 34210.81 ms |
| **p999 latency** | 45228.12 ms |
| **Error rate** | 19.00% (0.19) |
| **Total requests** | 57717 |
| **Failed requests** | 11105 |
| **Total successful** | 46612 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 53.71 |
| observed_postgres_backends_median_numbackends | 53 |
| observed_client_backends_active_median | 65367 |
| observed_client_backends_active_max | 98033 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 11.8% / 10.8% / 19.6% / 26.4% / 42.0% |
| OJP proxy-tier host_cpu (avg / peak) | 20.6% / 58.7% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 84.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 1153.70 MiB / 1164.80 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 11.8% / 10.8% / 19.6% / 26.4% / 42.0% |
| PgBouncer tier RSS (avg / peak, summed) | 1153.70 MiB / 1164.80 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 11.8% / 10.8% / 19.6% / 26.4% / 42.0% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 20.6% / 58.7% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 84.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1153.70 MiB / 1164.80 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.08% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1649 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (28.92 ms) |
| Error rate | < 0.1% | ❌ FAIL (19.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 61.80 RPS (all instances) |
| **Achieved throughput** | 50.00 RPS (all instances) |
| **Attempted − achieved gap** | 11.80 RPS (19.10%) |
| **Total attempted ops** | 57611 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 3.905 | 34.399 | 36175.871 | 3.169612863613423 | 17.99% | 0.07508447002878238 | 97 |
| 10 | 4.081 | 26.623 | 35389.439 | 3.039516928569213 | 21.19% | 0.07508447002878238 | 95 |
| 11 | 4.243 | 27.375 | 34930.687 | 3.243674619962329 | 16.14% | 0.07510326699211416 | 113 |
| 12 | 4.045 | 27.503 | 34832.383 | 3.0158062087481943 | 21.93% | 0.0750938673341677 | 88 |
| 13 | 4.867 | 31.919 | 34111.487 | 3.0323042622445473 | 21.48% | 0.07508447002878238 | 111 |
| 14 | 5.803 | 31.775 | 31211.519 | 3.083951289715964 | 20.59% | 0.07508447002878237 | 88 |
| 15 | 4.295 | 26.783 | 34930.687 | 3.1780934874851834 | 17.94% | 0.07511737118636512 | 112 |
| 1 | 4.143 | 34.847 | 35717.119 | 3.2694347952565925 | 15.27% | 0.0875328248093035 | 119 |
| 2 | 4.045 | 29.967 | 33210.367 | 3.1513473190470824 | 18.63% | 0.07510326699211416 | 99 |
| 3 | 4.223 | 28.047 | 32309.247 | 3.267844262409288 | 15.49% | 0.08757662955085699 | 114 |
| 4 | 4.065 | 27.263 | 34373.631 | 3.1313138924201533 | 19.35% | 0.07510326699211416 | 93 |
| 5 | 4.275 | 25.103 | 33046.527 | 3.0123130575031154 | 22.17% | 0.0750938673341677 | 109 |
| 6 | 4.033 | 25.903 | 34308.095 | 3.2762936218842276 | 15.19% | 0.0751079679978097 | 98 |
| 7 | 4.355 | 29.663 | 35028.991 | 3.1108618594342534 | 19.88% | 0.08755472170106317 | 113 |
| 8 | 3.833 | 27.343 | 34897.919 | 2.982146696374039 | 22.71% | 0.06260564727474283 | 90 |
| 9 | 4.227 | 28.207 | 32899.071 | 3.0322829958568485 | 21.90% | 0.07509386733416772 | 110 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 649 | Client throttle limit reached; request rejected to avoid overloading the database |
| 10 | SQLTransientConnectionException | 764 | Client throttle limit reached; request rejected to avoid overloading the database |
| 11 | SQLTransientConnectionException | 582 | Client throttle limit reached; request rejected to avoid overloading the database |
| 12 | SQLTransientConnectionException | 791 | Client throttle limit reached; request rejected to avoid overloading the database |
| 13 | SQLTransientConnectionException | 775 | Client throttle limit reached; request rejected to avoid overloading the database |
| 14 | SQLTransientConnectionException | 743 | Client throttle limit reached; request rejected to avoid overloading the database |
| 15 | SQLTransientConnectionException | 647 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLTransientConnectionException | 551 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 2 | SQLTransientConnectionException | 672 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLTransientConnectionException | 559 | Client throttle limit reached; request rejected to avoid overloading the database |
| 4 | SQLTransientConnectionException | 698 | Client throttle limit reached; request rejected to avoid overloading the database |
| 5 | SQLTransientConnectionException | 800 | Client throttle limit reached; request rejected to avoid overloading the database |
| 6 | SQLTransientConnectionException | 548 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 7 | SQLTransientConnectionException | 717 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 8 | SQLTransientConnectionException | 819 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 9 | SQLTransientConnectionException | 790 | Client throttle limit reached; request rejected to avoid overloading the database |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-15T22:04:38Z → 2026-07-15T22:19:38Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 31.5 | 52.0 | 0.524 | 210 | 0 |
| ojp-2 | 31.4 | 54.0 | 0.519 | 207 | 0 |
| ojp-3 | 32.1 | 56.0 | 0.545 | 191 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T22:04:38Z → 2026-07-15T22:19:38Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 53 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 65367 / 98033 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1885754190 | Cumulative since stats reset |
| Transactions rolled back | 1677 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6130 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 615160 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T22:04:38Z → 2026-07-15T22:19:38Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 3.8 | 2.9 | 8.8 | 10.8 | 26.4 | 6.5 | 5.9 | 11.8 | 34.4 | 38.2 | 362.5 | 366.9 |
| Proxy (OJP / pgBouncer) | ojp-2 | 4.0 | 2.9 | 8.8 | 12.7 | 21.5 | 7.5 | 5.9 | 13.7 | 36.2 | 40.2 | 392.6 | 398.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 4.3 | 3.9 | 9.8 | 14.6 | 36.1 | 7.1 | 5.9 | 12.8 | 28.4 | 44.9 | 398.6 | 399.8 |
| PostgreSQL | db | 664.1 | 646.7 | 917.9 | 1077.8 | 1140.2 | 1334.6 | 1363.6 | 1592.1 | 1597.3 | 1598.6 | 28008.5 | 37307.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T22:23:35Z*

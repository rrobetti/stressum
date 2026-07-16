# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T23:44:10Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260716-003204` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.73 RPS (per instance) |
| **Total throughput** | 27.68 RPS (all instances) |
| **p50 latency** | 5.46 ms |
| **p95 latency** | 1315.09 ms |
| **p99 latency** | 34465.75 ms |
| **p999 latency** | 45414.38 ms |
| **Error rate** | 55.00% (0.55) |
| **Total requests** | 57710 |
| **Failed requests** | 31888 |
| **Total successful** | 25822 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 51.99 |
| observed_postgres_backends_median_numbackends | 53 |
| observed_client_backends_active_median | 52177 |
| observed_client_backends_active_max | 77922 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 9.2% / 6.8% / 23.5% / 33.2% / 52.7% |
| OJP proxy-tier host_cpu (avg / peak) | 18.8% / 78.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 77.30% |
| OJP proxy-tier RSS (avg / peak, summed) | 1117.10 MiB / 1126.40 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 9.2% / 6.8% / 23.5% / 33.2% / 52.7% |
| PgBouncer tier RSS (avg / peak, summed) | 1117.10 MiB / 1126.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 9.2% / 6.8% / 23.5% / 33.2% / 52.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.8% / 78.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 77.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1117.10 MiB / 1126.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.06% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 1115 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (1315.09 ms) |
| Error rate | < 0.1% | ❌ FAIL (55.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 61.75 RPS (all instances) |
| **Achieved throughput** | 27.68 RPS (all instances) |
| **Attempted − achieved gap** | 34.08 RPS (55.18%) |
| **Total attempted ops** | 57611 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5.327 | 1908.735 | 34799.615 | 1.7434961595962972 | 54.89% | 0.06257822277847308 | 64 |
| 10 | 4.723 | 1131.519 | 35848.191 | 1.9058395479887618 | 50.60% | 0.06257822277847308 | 65 |
| 11 | 5.347 | 74.879 | 34570.239 | 1.590333510155889 | 58.75% | 0.06259389083625437 | 72 |
| 12 | 5.999 | 108.031 | 33751.039 | 1.6962240299117235 | 56.04% | 0.06257039169065198 | 65 |
| 13 | 5.539 | 855.039 | 34144.255 | 1.6577238702611823 | 57.03% | 0.06258605582676179 | 71 |
| 14 | 4.599 | 66.431 | 34504.703 | 1.6726968600570897 | 56.63% | 0.06257822277847308 | 64 |
| 15 | 6.539 | 89.023 | 35618.815 | 1.6865967429538864 | 56.24% | 0.06258605582676179 | 73 |
| 1 | 5.831 | 1483.775 | 33292.287 | 1.705115019239562 | 56.49% | 0.06260956674179814 | 75 |
| 2 | 5.271 | 5382.143 | 34177.023 | 1.726678480782588 | 55.76% | 0.06256647712660728 | 63 |
| 3 | 5.487 | 1241.087 | 34111.487 | 1.74463109909612 | 54.96% | 0.0626017278076875 | 80 |
| 4 | 4.815 | 5332.991 | 35127.295 | 1.8930137099111566 | 50.94% | 0.06258605582676179 | 68 |
| 5 | 5.963 | 182.911 | 33488.895 | 1.762495676745872 | 54.38% | 0.06259389083625438 | 74 |
| 6 | 6.395 | 1174.527 | 33357.823 | 1.7933580442011903 | 53.58% | 0.06257822277847308 | 69 |
| 7 | 5.443 | 82.623 | 33751.039 | 1.60745912369414 | 58.32% | 0.06259389083625437 | 71 |
| 8 | 4.995 | 1244.159 | 35454.975 | 1.7101220186498485 | 55.64% | 0.050093926111458985 | 60 |
| 9 | 5.127 | 683.519 | 35454.975 | 1.7796448838418084 | 53.84% | 0.0626017278076875 | 81 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 1980 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | SQLException | 1 | Session d81c443e-92a3-43dc-b6fd-3c4213998bc1 is bound to server 172.236.16.74:1059 which is currently unavailable. Cannot continue with this session. |
| 10 | SQLTransientConnectionException | 1825 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 11 | SQLTransientConnectionException | 2118 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 12 | SQLTransientConnectionException | 2022 | Client throttle limit reached; request rejected to avoid overloading the database |
| 13 | SQLTransientConnectionException | 2057 | Client throttle limit reached; request rejected to avoid overloading the database |
| 14 | SQLTransientConnectionException | 2042 | Client throttle limit reached; request rejected to avoid overloading the database |
| 15 | SQLTransientConnectionException | 2027 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | SQLTransientConnectionException | 2038 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | SQLTransientConnectionException | 2012 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLTransientConnectionException | 1981 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | SQLException | 2 | Session 4f0f8163-1fc5-4343-95c7-49a0561836da is bound to server 172.236.16.74:1059 which is currently unavailable. Cannot continue with this session. |
| 4 | SQLTransientConnectionException | 1838 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 5 | SQLTransientConnectionException | 1961 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 5 | SQLException | 1 | Session 761be67e-beb0-4599-be5d-cc4a473deea5 is bound to server 172.236.16.74:1059 which is currently unavailable. Cannot continue with this session. |
| 6 | SQLTransientConnectionException | 1933 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 7 | SQLTransientConnectionException | 2103 | Client throttle limit reached; request rejected to avoid overloading the database |
| 8 | SQLTransientConnectionException | 2006 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 9 | SQLTransientConnectionException | 1941 | Client throttle limit reached; request rejected to avoid overloading the database |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-15T23:44:10Z → 2026-07-15T23:59:10Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 31.3 | 48.0 | 0.044 | 34 | 0 |
| ojp-2 | 32.2 | 54.0 | 0.442 | 168 | 0 |
| ojp-3 | 30.2 | 52.0 | 0.498 | 175 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T23:44:10Z → 2026-07-15T23:59:10Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 53 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 52177 / 77922 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1887400209 | Cumulative since stats reset |
| Transactions rolled back | 1781 | Non-zero → contention or application errors |
| Temp file bytes written | -5 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 5 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7656 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 539099 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T23:44:10Z → 2026-07-15T23:59:10Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.0 | 0.0 | 3.9 | 8.8 | 19.6 | 4.3 | 2.9 | 7.8 | 32.4 | 36.2 | 361.6 | 362.1 |
| Proxy (OJP / pgBouncer) | ojp-2 | 4.3 | 2.9 | 10.8 | 18.6 | 34.3 | 7.7 | 5.9 | 16.7 | 36.2 | 45.1 | 399.0 | 401.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 4.1 | 2.9 | 11.7 | 17.6 | 23.4 | 7.2 | 5.9 | 14.7 | 24.5 | 39.2 | 356.5 | 363.2 |
| PostgreSQL | db | 531.0 | 523.8 | 822.8 | 959.8 | 1001.9 | 1185.9 | 1192.5 | 1534.7 | 1587.1 | 1596.4 | 27152.5 | 38161.9 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-16T00:03:15Z*

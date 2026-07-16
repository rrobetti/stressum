# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T15:57:00Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 3 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260715-164515` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.29 RPS (per instance) |
| **Total throughput** | 20.58 RPS (all instances) |
| **p50 latency** | 21528.56 ms |
| **p95 latency** | 145407.50 ms |
| **p99 latency** | 388923.75 ms |
| **p999 latency** | 435388.75 ms |
| **Error rate** | 57.00% (0.57) |
| **Total requests** | 44548 |
| **Failed requests** | 25301 |
| **Total successful** | 19247 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 316 |
| observed_postgres_backends_avg_numbackends | 312.63 |
| observed_postgres_backends_median_numbackends | 312 |
| observed_client_backends_active_median | 34091 |
| observed_client_backends_active_max | 48885 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | hikari-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 19 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| OJP proxy-tier host_cpu (avg / peak) | N/A% / N/A% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 0% |
| OJP proxy-tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| PgBouncer tier RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | N/A% / N/A% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 0.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | N/A MiB / 0.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 0 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (145407.50 ms) |
| Error rate | < 0.1% | ❌ FAIL (57.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.31 RPS (all instances) |
| **Achieved throughput** | 20.58 RPS (all instances) |
| **Attempted − achieved gap** | 25.72 RPS (55.55%) |
| **Total attempted ops** | 43214 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 22839.295 | 134742.015 | 382730.239 | 1.4577446561840246 | 51.16% | 0.025021894157387717 | 0 |
| 10 | 21774.335 | 160956.415 | 388759.551 | 1.2577445944254964 | 57.85% | 0.025025025025025023 | 0 |
| 11 | 22085.631 | 148242.431 | 386400.255 | 1.188227669127257 | 60.19% | 0.025021894157387717 | 0 |
| 12 | 22495.231 | 146669.567 | 413401.087 | 1.189297180980657 | 59.84% | 0.02501876407305479 | 0 |
| 13 | 22233.087 | 152436.735 | 398458.879 | 1.188227669127257 | 60.18% | 0.025021894157387717 | 0 |
| 14 | 22364.159 | 154796.031 | 398458.879 | 1.2149654654622537 | 59.24% | 0.025021894157387717 | 0 |
| 15 | 21118.975 | 141688.831 | 379846.655 | 1.294107958550043 | 56.32% | 0.025025025025025023 | 0 |
| 1 | 20578.303 | 141033.471 | 396886.015 | 1.2769957871973152 | 57.23% | 0.025025025025025023 | 0 |
| 2 | 21053.439 | 144310.271 | 368312.319 | 1.3657651760895908 | 54.16% | 0.025021894157387717 | 0 |
| 3 | 20103.167 | 135004.159 | 379322.367 | 1.3679041975086819 | 54.14% | 0.025021894157387717 | 0 |
| 4 | 21364.735 | 141033.471 | 392953.855 | 1.3882249009900463 | 53.49% | 0.02501876407305479 | 0 |
| 5 | 20824.063 | 137232.383 | 398983.167 | 1.2363543802345867 | 58.51% | 0.025021894157387717 | 0 |
| 6 | 22085.631 | 152305.663 | 382205.951 | 1.2074775910768583 | 59.56% | 0.025021894157387717 | 0 |
| 7 | 19906.559 | 149946.367 | 414187.519 | 1.243840955201405 | 58.33% | 0.025021894157387717 | 0 |
| 8 | 21250.047 | 144834.559 | 377487.359 | 1.280205688519646 | 56.74% | 0.025021894157387717 | 0 |
| 9 | 22380.543 | 141295.615 | 364380.159 | 1.4277967972432293 | 51.74% | 0.025021894157387717 | 0 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 1428 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 10 | SQLTransientConnectionException | 1614 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 11 | SQLTransientConnectionException | 1680 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 12 | SQLTransientConnectionException | 1657 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=77) |
| 13 | SQLTransientConnectionException | 1679 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 14 | SQLTransientConnectionException | 1651 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 15 | SQLTransientConnectionException | 1560 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=72) |
| 1 | SQLTransientConnectionException | 1598 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 2 | SQLTransientConnectionException | 1509 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 3 | SQLTransientConnectionException | 1510 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 4 | SQLTransientConnectionException | 1493 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 5 | SQLTransientConnectionException | 1630 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 6 | SQLTransientConnectionException | 1663 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 7 | SQLTransientConnectionException | 1628 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=80) |
| 8 | SQLTransientConnectionException | 1570 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=66) |
| 9 | SQLTransientConnectionException | 1431 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=71) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T15:57:00Z → 2026-07-15T16:12:00Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 312 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 34091 / 48885 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2713682416 | Cumulative since stats reset |
| Transactions rolled back | 922 | Non-zero → contention or application errors |
| Temp file bytes written | 3 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 2 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 4977 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 340520 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T15:57:00Z → 2026-07-15T16:12:00Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 1085.8 | 1073.2 | 1173.0 | 1174.2 | 1174.2 | 1599.6 | 1599.6 | 1599.7 | 1599.9 | 1599.9 | 365791.8 | 406163.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T16:15:49Z*

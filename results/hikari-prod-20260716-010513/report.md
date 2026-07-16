# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | HIKARI_DISCIPLINED |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-16T00:17:07Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/hikari-prod-20260716-010513` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.38 RPS (per instance) |
| **Total throughput** | 22.04 RPS (all instances) |
| **p50 latency** | 24992.81 ms |
| **p95 latency** | 147471.88 ms |
| **p99 latency** | 391774.38 ms |
| **p999 latency** | 437992.50 ms |
| **Error rate** | 65.00% (0.65) |
| **Total requests** | 59347 |
| **Failed requests** | 38739 |
| **Total successful** | 20608 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 300 |
| observed_postgres_backends_max_numbackends | 316 |
| observed_postgres_backends_avg_numbackends | 312.50 |
| observed_postgres_backends_median_numbackends | 312 |
| observed_client_backends_active_median | 32319 |
| observed_client_backends_active_max | 49042 |
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
| p95 latency | < 1500 ms | ❌ FAIL (147471.88 ms) |
| Error rate | < 0.1% | ❌ FAIL (65.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 61.68 RPS (all instances) |
| **Achieved throughput** | 22.04 RPS (all instances) |
| **Attempted − achieved gap** | 39.64 RPS (64.27%) |
| **Total attempted ops** | 57609 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 25952.255 | 161611.775 | 384565.247 | 1.2588154514516485 | 68.38% | 0.02502815667626079 | 0 |
| 10 | 25296.895 | 151519.231 | 380108.799 | 1.287692271493445 | 67.35% | 0.02502815667626079 | 0 |
| 11 | 25264.127 | 148635.647 | 409468.927 | 1.3326117693362396 | 66.28% | 0.025025025025025023 | 0 |
| 12 | 25608.191 | 150732.799 | 392953.855 | 1.394643456833432 | 64.73% | 0.02502815667626079 | 0 |
| 13 | 24330.239 | 145883.135 | 369098.751 | 1.3721822403468638 | 65.28% | 0.025025025025025023 | 0 |
| 14 | 23560.191 | 141426.687 | 396361.727 | 1.453466608770425 | 63.53% | 0.025031289111389236 | 0 |
| 15 | 24854.527 | 139984.895 | 376700.927 | 1.4588126078200485 | 63.12% | 0.02502815667626079 | 0 |
| 1 | 24985.599 | 144703.487 | 393478.143 | 1.4352849072626273 | 63.94% | 0.02502815667626079 | 0 |
| 2 | 25772.031 | 157024.255 | 407633.919 | 1.2438422855040503 | 68.69% | 0.02502815667626079 | 0 |
| 3 | 25985.023 | 143785.983 | 383778.815 | 1.4149626687286834 | 64.46% | 0.02502815667626079 | 0 |
| 4 | 25214.975 | 151257.087 | 409206.783 | 1.2010618113680553 | 69.82% | 0.025025025025025023 | 0 |
| 5 | 25460.735 | 147587.071 | 408158.207 | 1.3240542584173167 | 66.48% | 0.02502815667626079 | 0 |
| 6 | 23674.879 | 140902.399 | 386400.255 | 1.486621476225821 | 62.66% | 0.02502815667626079 | 0 |
| 7 | 25509.887 | 148766.719 | 393215.999 | 1.4064065830523196 | 64.65% | 0.02502815667626079 | 0 |
| 8 | 24264.703 | 143654.911 | 390856.703 | 1.4898300117860206 | 62.54% | 0.02502815667626079 | 0 |
| 9 | 24150.015 | 142082.047 | 386400.255 | 1.4802044051054217 | 62.50% | 0.025025025025025023 | 0 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2545 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 10 | SQLTransientConnectionException | 2484 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=110) |
| 11 | SQLTransientConnectionException | 2449 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 12 | SQLTransientConnectionException | 2393 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 13 | SQLTransientConnectionException | 2412 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 14 | SQLTransientConnectionException | 2367 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 15 | SQLTransientConnectionException | 2334 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=99) |
| 1 | SQLTransientConnectionException | 2380 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 2 | SQLTransientConnectionException | 2551 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 3 | SQLTransientConnectionException | 2400 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 4 | SQLTransientConnectionException | 2598 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 5 | SQLTransientConnectionException | 2455 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=110) |
| 6 | SQLTransientConnectionException | 2333 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 7 | SQLTransientConnectionException | 2405 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 8 | SQLTransientConnectionException | 2326 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
| 9 | SQLTransientConnectionException | 2307 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=19, active=19, idle=0, waiting=112) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-16T00:17:07Z → 2026-07-16T00:32:07Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 312 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 32319 / 49042 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2928344396 | Cumulative since stats reset |
| Transactions rolled back | 920 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5714 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 405586 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-16T00:17:07Z → 2026-07-16T00:32:07Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| PostgreSQL | db | 1074.2 | 1068.3 | 1162.4 | 1166.3 | 1166.3 | 1599.5 | 1599.5 | 1599.7 | 1599.8 | 1599.8 | 361887.9 | 400445.0 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-16T00:35:58Z*

# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T21:31:14Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260715-221908` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.61 RPS (per instance) |
| **Total throughput** | 25.73 RPS (all instances) |
| **p50 latency** | 31460.38 ms |
| **p95 latency** | 49082.25 ms |
| **p99 latency** | 86294.38 ms |
| **p999 latency** | 105922.50 ms |
| **Error rate** | 60.00% (0.60) |
| **Total requests** | 59550 |
| **Failed requests** | 35488 |
| **Total successful** | 24062 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 59 |
| observed_postgres_backends_avg_numbackends | 55.96 |
| observed_postgres_backends_median_numbackends | 56 |
| observed_client_backends_active_median | 39948 |
| observed_client_backends_active_max | 60359 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | pgbouncer-prod |
| Configured replicas | 16 |
| Configured client pool size (per replica) | 20 |
| OJP servers | N/A |
| Real DB connections per OJP server | N/A |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 0.0% / 2.9% / 4.9% / 6.8% |
| OJP proxy-tier host_cpu (avg / peak) | 9.3% / 66.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 13.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 35.00 MiB / 35.00 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 0.0% / 2.9% / 4.9% / 6.8% |
| PgBouncer tier RSS (avg / peak, summed) | 35.00 MiB / 35.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 2.9% / 4.9% / 12.7% |
| HAProxy RSS (avg / peak, summed) | 22.90 MiB / 23.10 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.8% / 1.0% / 5.8% / 7.8% / 19.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 14.3% / 71.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 26.40% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 57.90 MiB / 58.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 28 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (49082.25 ms) |
| Error rate | < 0.1% | ❌ FAIL (60.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 61.62 RPS (all instances) |
| **Achieved throughput** | 25.73 RPS (all instances) |
| **Attempted − achieved gap** | 35.89 RPS (58.24%) |
| **Total attempted ops** | 57614 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 31883.263 | 52854.783 | 97452.031 | 1.5283308039405052 | 61.64% | 0.025021894157387717 | 2 |
| 10 | 30998.527 | 45613.055 | 72482.815 | 1.7550689514291888 | 55.88% | 0.025021894157387717 | 1 |
| 11 | 30507.007 | 47349.759 | 75431.935 | 1.6523940462477822 | 58.46% | 0.025031289111389236 | 2 |
| 12 | 31506.431 | 48234.495 | 75235.327 | 1.5946404679323258 | 59.95% | 0.025021894157387717 | 2 |
| 13 | 31522.815 | 50921.471 | 94175.231 | 1.7358158815923304 | 56.45% | 0.02502815667626079 | 2 |
| 14 | 31473.663 | 44826.623 | 73072.639 | 1.663089153343237 | 58.26% | 0.025021894157387717 | 3 |
| 15 | 31621.119 | 44695.551 | 91160.575 | 1.5721824244978106 | 60.55% | 0.02502815667626079 | 2 |
| 1 | 31391.743 | 50561.023 | 77135.871 | 1.6406294284427818 | 58.76% | 0.02502815667626079 | 2 |
| 2 | 31375.359 | 50790.399 | 96862.207 | 1.6481177660892017 | 58.66% | 0.025021894157387717 | 2 |
| 3 | 31277.055 | 49971.199 | 88014.847 | 1.58180633941778 | 60.25% | 0.02502815667626079 | 2 |
| 4 | 31277.055 | 48398.335 | 83886.079 | 1.6759250742775982 | 57.74% | 0.025021894157387717 | 1 |
| 5 | 31948.799 | 50495.487 | 73924.607 | 1.520842602416236 | 61.83% | 0.02502815667626079 | 2 |
| 6 | 31834.111 | 50003.967 | 95944.703 | 1.5101507370006182 | 62.08% | 0.02501876407305479 | 1 |
| 7 | 31080.447 | 50135.039 | 95223.807 | 1.5636263296706119 | 60.70% | 0.025031289111389236 | 1 |
| 8 | 31637.503 | 48398.335 | 93978.623 | 1.5347495096288153 | 61.44% | 0.025021894157387717 | 1 |
| 9 | 32030.719 | 52068.351 | 96731.135 | 1.5572075930982336 | 60.85% | 0.02502815667626079 | 2 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2296 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=120) |
| 10 | SQLTransientConnectionException | 2078 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=120) |
| 11 | SQLTransientConnectionException | 2174 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=4, active=4, idle=0, waiting=120) |
| 12 | SQLTransientConnectionException | 2232 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=120) |
| 13 | SQLTransientConnectionException | 2104 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=120) |
| 14 | SQLTransientConnectionException | 2170 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=5, active=5, idle=0, waiting=120) |
| 15 | SQLTransientConnectionException | 2256 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=120) |
| 1 | SQLTransientConnectionException | 2186 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=120) |
| 2 | SQLTransientConnectionException | 2187 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=119) |
| 3 | SQLTransientConnectionException | 2242 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=120) |
| 4 | SQLTransientConnectionException | 2141 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=120) |
| 5 | SQLTransientConnectionException | 2303 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=120) |
| 6 | SQLTransientConnectionException | 2312 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=120) |
| 7 | SQLTransientConnectionException | 2258 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=5, active=5, idle=0, waiting=120) |
| 8 | SQLTransientConnectionException | 2286 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=120) |
| 9 | SQLTransientConnectionException | 2263 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=118) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T21:31:14Z → 2026-07-15T21:46:14Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 56 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 39948 / 60359 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2729464148 | Cumulative since stats reset |
| Transactions rolled back | 1116 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6328 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 441276 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T21:31:14Z → 2026-07-15T21:46:14Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 2.0 | 2.9 | 3.9 | 2.7 | 2.9 | 3.9 | 5.9 | 34.2 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.0 | 2.9 | 5.9 | 3.1 | 2.9 | 4.9 | 17.6 | 39.2 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.9 | 2.9 | 3.9 | 3.8 | 2.9 | 5.8 | 33.2 | 36.1 | 11.6 | 11.6 |
| PostgreSQL | db | 1419.8 | 1424.8 | 1513.7 | 1525.0 | 1554.2 | 1599.3 | 1599.4 | 1599.8 | 1600.0 | 1600.0 | 147124.0 | 152388.0 |
| HAProxy | lb | 1.0 | 1.0 | 2.9 | 4.9 | 12.7 | 5.1 | 3.9 | 8.8 | 34.1 | 38.2 | 22.9 | 23.1 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T21:50:13Z*

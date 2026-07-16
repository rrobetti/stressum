# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T19:51:43Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 4 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260715-203940` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.63 RPS (per instance) |
| **Total throughput** | 26.10 RPS (all instances) |
| **p50 latency** | 31384.50 ms |
| **p95 latency** | 48091.00 ms |
| **p99 latency** | 80326.88 ms |
| **p999 latency** | 105643.75 ms |
| **Error rate** | 59.00% (0.59) |
| **Total requests** | 59432 |
| **Failed requests** | 35024 |
| **Total successful** | 24408 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 58 |
| observed_postgres_backends_avg_numbackends | 56.10 |
| observed_postgres_backends_median_numbackends | 56 |
| observed_client_backends_active_median | 40527 |
| observed_client_backends_active_max | 60358 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 1.0% / 2.9% / 3.9% / 9.8% |
| OJP proxy-tier host_cpu (avg / peak) | 26.8% / 108.7% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 19.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 35.10 MiB / 35.10 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.8% / 1.0% / 2.9% / 3.9% / 9.8% |
| PgBouncer tier RSS (avg / peak, summed) | 35.10 MiB / 35.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 2.9% / 4.9% / 11.6% |
| HAProxy RSS (avg / peak, summed) | 23.40 MiB / 23.50 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.8% / 1.0% / 5.8% / 8.8% / 21.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 31.6% / 114.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 31.20% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 58.50 MiB / 58.60 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 29 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (48091.00 ms) |
| Error rate | < 0.1% | ❌ FAIL (59.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 61.62 RPS (all instances) |
| **Achieved throughput** | 26.10 RPS (all instances) |
| **Attempted − achieved gap** | 35.52 RPS (57.64%) |
| **Total attempted ops** | 57613 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 30867.455 | 48496.639 | 69926.911 | 1.6759250742775982 | 57.92% | 0.025037556334501748 | 1 |
| 10 | 31686.655 | 47841.279 | 74252.287 | 1.6256562785091448 | 59.18% | 0.03753753753753754 | 2 |
| 11 | 31653.887 | 48693.247 | 76349.439 | 1.5775282965795978 | 60.37% | 0.025037556334501748 | 2 |
| 12 | 31457.279 | 43515.903 | 71958.527 | 1.6138933867804057 | 59.49% | 0.03753284123608157 | 1 |
| 13 | 30982.143 | 44007.423 | 73007.103 | 1.7347463708827848 | 56.40% | 0.03751875937968984 | 2 |
| 14 | 31539.199 | 46268.415 | 72482.815 | 1.6427702068222023 | 58.51% | 0.025034422330704718 | 2 |
| 15 | 32096.255 | 48136.191 | 77266.943 | 1.511220248854018 | 62.01% | 0.025025025025025023 | 2 |
| 1 | 32079.871 | 52920.319 | 93388.799 | 1.6235189934610046 | 58.95% | 0.025021894157387717 | 2 |
| 2 | 31358.975 | 52396.031 | 96403.455 | 1.5561397466968128 | 60.69% | 0.025034422330704718 | 2 |
| 3 | 31326.207 | 51773.439 | 92733.439 | 1.5219153673880168 | 61.61% | 0.02502815667626079 | 2 |
| 4 | 31358.975 | 48660.479 | 76808.191 | 1.5850148715464163 | 60.03% | 0.0375234521575985 | 1 |
| 5 | 30441.471 | 44171.263 | 69074.943 | 1.7433043210417902 | 56.17% | 0.025025025025025023 | 2 |
| 6 | 31129.599 | 50298.879 | 92864.511 | 1.6898269210818744 | 57.52% | 0.025043826696719257 | 2 |
| 7 | 31096.831 | 49119.231 | 79167.487 | 1.7860828849409685 | 55.06% | 0.02502815667626079 | 2 |
| 8 | 31703.039 | 46071.807 | 79822.847 | 1.5871555904454089 | 59.96% | 0.025031289111389236 | 2 |
| 9 | 31375.359 | 47087.615 | 89718.783 | 1.6299360645814038 | 59.05% | 0.025034422330704718 | 2 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 2157 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=119) |
| 10 | SQLTransientConnectionException | 2204 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=120) |
| 11 | SQLTransientConnectionException | 2247 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=6, active=6, idle=0, waiting=120) |
| 12 | SQLTransientConnectionException | 2216 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=120) |
| 13 | SQLTransientConnectionException | 2098 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=120) |
| 14 | SQLTransientConnectionException | 2166 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=112) |
| 15 | SQLTransientConnectionException | 2306 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=120) |
| 1 | SQLTransientConnectionException | 2180 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=106) |
| 2 | SQLTransientConnectionException | 2246 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=104) |
| 3 | SQLTransientConnectionException | 2284 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=101) |
| 4 | SQLTransientConnectionException | 2226 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=120) |
| 5 | SQLTransientConnectionException | 2089 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=120) |
| 6 | SQLTransientConnectionException | 2139 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=5, active=5, idle=0, waiting=120) |
| 7 | SQLTransientConnectionException | 2046 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=7, active=7, idle=0, waiting=120) |
| 8 | SQLTransientConnectionException | 2222 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=104) |
| 9 | SQLTransientConnectionException | 2198 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=120) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T19:51:43Z → 2026-07-15T20:06:43Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 56 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 40527 / 60358 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2784462853 | Cumulative since stats reset |
| Transactions rolled back | 1162 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6352 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 446803 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T19:51:43Z → 2026-07-15T20:06:43Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 2.0 | 2.9 | 5.9 | 4.8 | 2.9 | 24.5 | 34.3 | 36.1 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.0 | 2.9 | 5.9 | 10.7 | 3.9 | 34.2 | 58.5 | 66.4 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.9 | 2.9 | 7.8 | 12.0 | 3.9 | 34.2 | 44.9 | 63.5 | 11.7 | 11.7 |
| PostgreSQL | db | 1425.1 | 1430.4 | 1514.2 | 1545.6 | 1577.9 | 1599.4 | 1599.4 | 1600.0 | 1600.0 | 1600.0 | 147307.1 | 152797.0 |
| HAProxy | lb | 1.0 | 1.0 | 2.9 | 4.9 | 11.6 | 4.9 | 3.9 | 7.8 | 34.1 | 39.0 | 23.4 | 23.5 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T20:10:46Z*

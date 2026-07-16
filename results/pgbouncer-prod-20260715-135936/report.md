# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | PGBOUNCER |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T13:11:34Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 3 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/pgbouncer-prod-20260715-135936` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.63 RPS (per instance) |
| **Total throughput** | 26.06 RPS (all instances) |
| **p50 latency** | 30208.06 ms |
| **p95 latency** | 47075.38 ms |
| **p99 latency** | 79278.12 ms |
| **p999 latency** | 104125.00 ms |
| **Error rate** | 45.00% (0.45) |
| **Total requests** | 44542 |
| **Failed requests** | 20179 |
| **Total successful** | 24363 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 60 |
| observed_postgres_backends_avg_numbackends | 55.71 |
| observed_postgres_backends_median_numbackends | 56 |
| observed_client_backends_active_median | 40731 |
| observed_client_backends_active_max | 60813 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 0.0% / 2.9% / 4.9% / 8.8% |
| OJP proxy-tier host_cpu (avg / peak) | 11.1% / 69.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 20.50% |
| OJP proxy-tier RSS (avg / peak, summed) | 35.10 MiB / 35.10 MiB |
| PgBouncer nodes | 3 |
| PgBouncer server pool size per node | 16 |
| pgbouncer_reserve_pool_size | 0 |
| PgBouncer local HikariCP pool size per replica | 20 |
| HAProxy nodes | 1 |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 0.9% / 0.0% / 2.9% / 4.9% / 8.8% |
| PgBouncer tier RSS (avg / peak, summed) | 35.10 MiB / 35.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.0% / 1.0% / 2.9% / 4.9% / 7.8% |
| HAProxy RSS (avg / peak, summed) | 23.10 MiB / 23.20 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 1.8% / 1.0% / 5.8% / 9.8% / 15.6% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 16.2% / 73.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 28.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 58.20 MiB / 58.30 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.03% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 28 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (47075.38 ms) |
| Error rate | < 0.1% | ❌ FAIL (45.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.22 RPS (all instances) |
| **Achieved throughput** | 26.06 RPS (all instances) |
| **Attempted − achieved gap** | 20.16 RPS (43.62%) |
| **Total attempted ops** | 43215 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 30064.639 | 49250.303 | 76546.047 | 1.644909230529002 | 44.28% | 0.025025025025025023 | 1 |
| 10 | 30212.095 | 45842.431 | 74514.431 | 1.6128238749270059 | 45.81% | 0.025025025025025023 | 2 |
| 11 | 29736.959 | 44007.423 | 74383.359 | 1.8042626373250281 | 39.62% | 0.025021894157387717 | 2 |
| 12 | 30457.855 | 48365.567 | 83492.863 | 1.5326088467786874 | 48.32% | 0.025025025025025023 | 2 |
| 13 | 30146.559 | 47284.223 | 77856.767 | 1.69089643179142 | 43.39% | 0.025021894157387717 | 2 |
| 14 | 30556.159 | 46366.719 | 76546.047 | 1.5775282965795978 | 47.26% | 0.025025025025025023 | 1 |
| 15 | 30588.927 | 44662.783 | 78184.447 | 1.6427702068222023 | 44.83% | 0.025021894157387717 | 2 |
| 1 | 30556.159 | 49348.607 | 71041.023 | 1.5935692528833978 | 46.46% | 0.025021894157387717 | 2 |
| 2 | 30457.855 | 49414.143 | 75431.935 | 1.5582771038077792 | 47.67% | 0.025025025025025023 | 1 |
| 3 | 30539.775 | 48496.639 | 74252.287 | 1.4962470829064198 | 49.91% | 0.025021894157387717 | 3 |
| 4 | 30146.559 | 47710.207 | 90177.535 | 1.5828775430318094 | 46.93% | 0.02502815667626079 | 1 |
| 5 | 29966.335 | 45318.143 | 70451.199 | 1.7037305603059658 | 42.78% | 0.025021894157387717 | 2 |
| 6 | 29900.799 | 45449.215 | 69795.839 | 1.6395599177332363 | 44.90% | 0.025025025025025023 | 2 |
| 7 | 29868.031 | 48365.567 | 91881.471 | 1.6556025783764186 | 44.52% | 0.025021894157387717 | 1 |
| 8 | 30048.255 | 46006.271 | 92995.583 | 1.7090781138536932 | 42.62% | 0.025025025025025023 | 2 |
| 9 | 30081.023 | 47316.991 | 90898.431 | 1.6117526392850536 | 45.56% | 0.025021894157387717 | 2 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 1222 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=16, active=16, idle=0, waiting=55) |
| 10 | SQLTransientConnectionException | 1275 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=15, active=15, idle=0, waiting=84) |
| 11 | SQLTransientConnectionException | 1107 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=89) |
| 12 | SQLTransientConnectionException | 1340 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=67) |
| 13 | SQLTransientConnectionException | 1212 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=90) |
| 14 | SQLTransientConnectionException | 1322 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=9, active=9, idle=0, waiting=90) |
| 15 | SQLTransientConnectionException | 1248 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=8, active=8, idle=0, waiting=84) |
| 1 | SQLTransientConnectionException | 1293 | HikariPool-1 - Connection is not available, request timed out after 30001ms (total=9, active=9, idle=0, waiting=77) |
| 2 | SQLTransientConnectionException | 1327 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=70) |
| 3 | SQLTransientConnectionException | 1394 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=7, active=7, idle=0, waiting=90) |
| 4 | SQLTransientConnectionException | 1309 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=84) |
| 5 | SQLTransientConnectionException | 1191 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=10, active=10, idle=0, waiting=86) |
| 6 | SQLTransientConnectionException | 1249 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=8, active=8, idle=0, waiting=85) |
| 7 | SQLTransientConnectionException | 1242 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=87) |
| 8 | SQLTransientConnectionException | 1187 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=12, active=12, idle=0, waiting=78) |
| 9 | SQLTransientConnectionException | 1261 | HikariPool-1 - Connection is not available, request timed out after 30000ms (total=11, active=11, idle=0, waiting=68) |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T13:11:34Z → 2026-07-15T13:26:34Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 56 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 40731 / 60813 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2785076484 | Cumulative since stats reset |
| Transactions rolled back | 1217 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5965 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 412114 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T13:11:34Z → 2026-07-15T13:26:34Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | pgbouncer-1 | 0.3 | 0.0 | 1.0 | 2.9 | 4.9 | 4.2 | 2.9 | 5.9 | 33.3 | 36.2 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-2 | 0.3 | 0.0 | 1.9 | 2.9 | 7.8 | 4.0 | 2.9 | 6.8 | 33.2 | 39.1 | 11.7 | 11.7 |
| Proxy (OJP / pgBouncer) | pgbouncer-3 | 0.3 | 0.0 | 1.9 | 2.9 | 7.8 | 3.2 | 2.9 | 4.9 | 7.8 | 33.2 | 11.7 | 11.7 |
| PostgreSQL | db | 1425.8 | 1429.3 | 1509.6 | 1532.6 | 1563.5 | 1599.4 | 1599.5 | 1600.0 | 1600.0 | 1600.0 | 146412.8 | 152253.0 |
| HAProxy | lb | 1.0 | 1.0 | 2.9 | 4.9 | 7.8 | 5.2 | 3.9 | 10.7 | 34.1 | 38.0 | 23.1 | 23.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T13:30:38Z*

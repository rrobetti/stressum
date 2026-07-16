# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T08:47:05Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 2 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260715-093458` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.80 RPS (per instance) |
| **Total throughput** | 28.85 RPS (all instances) |
| **p50 latency** | 5.18 ms |
| **p95 latency** | 241.87 ms |
| **p99 latency** | 35020.81 ms |
| **p999 latency** | 44843.06 ms |
| **Error rate** | 9.00% (0.09) |
| **Total requests** | 28829 |
| **Failed requests** | 2684 |
| **Total successful** | 26145 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 53.53 |
| observed_postgres_backends_median_numbackends | 53 |
| observed_client_backends_active_median | 44031 |
| observed_client_backends_active_max | 66712 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.2% / 6.9% / 15.6% / 21.5% / 25.4% |
| OJP proxy-tier host_cpu (avg / peak) | 20.0% / 103.9% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 60.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 1103.80 MiB / 1115.50 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.2% / 6.9% / 15.6% / 21.5% / 25.4% |
| PgBouncer tier RSS (avg / peak, summed) | 1103.80 MiB / 1115.50 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.2% / 6.9% / 15.6% / 21.5% / 25.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 20.0% / 103.9% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 60.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1103.80 MiB / 1115.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.06% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 977 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (241.87 ms) |
| Error rate | < 0.1% | ❌ FAIL (9.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 31.80 RPS (all instances) |
| **Achieved throughput** | 28.85 RPS (all instances) |
| **Attempted − achieved gap** | 2.95 RPS (9.26%) |
| **Total attempted ops** | 28810 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5.439 | 1671.167 | 34275.327 | 1.8410661072729333 | 8.00% | 0.06256256256256257 | 55 |
| 10 | 5.003 | 39.999 | 34439.167 | 1.8079158593966234 | 9.38% | 0.06256256256256257 | 58 |
| 11 | 5.135 | 47.327 | 35225.599 | 1.7913359641732807 | 10.32% | 0.06257822277847308 | 66 |
| 12 | 5.147 | 36.671 | 35618.815 | 1.7859064251588734 | 10.65% | 0.06256256256256257 | 58 |
| 13 | 4.975 | 38.559 | 35553.279 | 1.817562570335483 | 8.49% | 0.06258605582676179 | 65 |
| 14 | 4.835 | 35.487 | 35192.831 | 1.8026535147887004 | 9.21% | 0.06256256256256257 | 55 |
| 15 | 5.007 | 35.487 | 36012.031 | 1.7942669476618838 | 9.71% | 0.06257039169065198 | 66 |
| 1 | 4.931 | 63.551 | 33685.503 | 1.8129992266459847 | 9.27% | 0.06257430723456253 | 63 |
| 2 | 4.995 | 55.135 | 34111.487 | 1.7698669755729917 | 10.21% | 0.06256256256256257 | 58 |
| 3 | 5.371 | 51.263 | 33751.039 | 1.8170678298260128 | 8.77% | 0.06259389083625437 | 67 |
| 4 | 4.955 | 57.279 | 34570.239 | 1.8277614069229366 | 8.27% | 0.06255473539346929 | 59 |
| 5 | 6.339 | 1516.543 | 34373.631 | 1.8053618810734253 | 8.32% | 0.06257822277847308 | 67 |
| 6 | 4.983 | 47.455 | 34766.847 | 1.7834266360142499 | 9.77% | 0.06255473539346929 | 56 |
| 7 | 5.571 | 54.911 | 35028.991 | 1.8243776660791802 | 8.44% | 0.06258213930261744 | 64 |
| 8 | 4.711 | 66.303 | 38076.415 | 1.7685416941114478 | 10.65% | 0.06255864897801593 | 56 |
| 9 | 5.527 | 52.799 | 35651.583 | 1.8022400849153613 | 9.49% | 0.06257822277847308 | 64 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 144 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 10 | SQLTransientConnectionException | 169 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 11 | SQLTransientConnectionException | 186 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 12 | SQLTransientConnectionException | 192 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 13 | SQLTransientConnectionException | 153 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 14 | SQLTransientConnectionException | 166 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 15 | SQLTransientConnectionException | 175 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 1 | SQLTransientConnectionException | 167 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 2 | SQLTransientConnectionException | 184 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 3 | SQLTransientConnectionException | 158 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 4 | SQLTransientConnectionException | 149 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 5 | SQLTransientConnectionException | 150 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 6 | SQLTransientConnectionException | 176 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 7 | SQLTransientConnectionException | 152 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 8 | SQLTransientConnectionException | 192 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 9 | SQLTransientConnectionException | 171 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-15T08:47:05Z → 2026-07-15T09:02:05Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 31.4 | 52.0 | 0.266 | 125 | 0 |
| ojp-2 | 32.0 | 54.0 | 0.286 | 118 | 0 |
| ojp-3 | 30.9 | 52.0 | 0.363 | 142 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T08:47:05Z → 2026-07-15T09:02:05Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 53 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 44031 / 66712 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2137992303 | Cumulative since stats reset |
| Transactions rolled back | 1013 | Non-zero → contention or application errors |
| Temp file bytes written | -5 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 5 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3373 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 338558 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T08:47:05Z → 2026-07-15T09:02:05Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.6 | 2.0 | 6.8 | 10.8 | 20.6 | 7.9 | 4.9 | 34.3 | 40.2 | 72.6 | 359.9 | 363.2 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.9 | 2.0 | 7.8 | 10.8 | 21.5 | 6.7 | 4.9 | 12.7 | 36.2 | 43.1 | 362.8 | 366.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.9 | 2.0 | 6.8 | 11.7 | 18.6 | 5.8 | 4.9 | 9.8 | 15.7 | 35.3 | 381.1 | 386.2 |
| PostgreSQL | db | 707.5 | 714.8 | 965.1 | 1065.7 | 1102.3 | 1376.4 | 1456.9 | 1595.8 | 1598.1 | 1598.4 | 19575.9 | 32740.7 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T09:05:46Z*

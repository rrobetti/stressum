# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T10:26:24Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 3 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260715-111421` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.51 RPS (per instance) |
| **Total throughput** | 24.22 RPS (all instances) |
| **p50 latency** | 5.17 ms |
| **p95 latency** | 875.95 ms |
| **p99 latency** | 36163.62 ms |
| **p999 latency** | 45369.38 ms |
| **Error rate** | 48.00% (0.48) |
| **Total requests** | 43324 |
| **Failed requests** | 20870 |
| **Total successful** | 22454 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 53.74 |
| observed_postgres_backends_median_numbackends | 53 |
| observed_client_backends_active_median | 43465 |
| observed_client_backends_active_max | 64120 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 7.5% / 6.8% / 13.7% / 19.6% / 27.4% |
| OJP proxy-tier host_cpu (avg / peak) | 17.1% / 73.6% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 58.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 1192.60 MiB / 1202.70 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 7.5% / 6.8% / 13.7% / 19.6% / 27.4% |
| PgBouncer tier RSS (avg / peak, summed) | 1192.60 MiB / 1202.70 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 7.5% / 6.8% / 13.7% / 19.6% / 27.4% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.1% / 73.6% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 58.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1192.60 MiB / 1202.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.06% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 979 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (875.95 ms) |
| Error rate | < 0.1% | ❌ FAIL (48.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 46.62 RPS (all instances) |
| **Achieved throughput** | 24.22 RPS (all instances) |
| **Attempted − achieved gap** | 22.40 RPS (48.04%) |
| **Total attempted ops** | 43211 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5.451 | 76.863 | 34668.543 | 1.6911961927618957 | 42.00% | 0.06257822277847308 | 60 |
| 10 | 4.663 | 38.111 | 35651.583 | 1.502205353842639 | 48.54% | 0.06257822277847308 | 60 |
| 11 | 5.103 | 1249.279 | 36798.463 | 1.5699381063468971 | 46.18% | 0.06257822277847308 | 69 |
| 12 | 5.019 | 53.375 | 36012.031 | 1.486924666440067 | 49.04% | 0.06257039169065198 | 57 |
| 13 | 5.179 | 1203.199 | 34766.847 | 1.4155193775613644 | 51.77% | 0.06257039169065198 | 69 |
| 14 | 4.831 | 1094.655 | 36110.335 | 1.5575613411971716 | 47.05% | 0.050075112669003496 | 56 |
| 15 | 5.267 | 4354.047 | 37715.967 | 1.4222525481572106 | 51.61% | 0.06257039169065198 | 71 |
| 1 | 5.003 | 1511.423 | 36077.567 | 1.6922970859312052 | 41.94% | 0.07505629221916436 | 68 |
| 2 | 6.567 | 55.487 | 36044.799 | 1.5348986631562667 | 47.62% | 0.050093926897120056 | 59 |
| 3 | 5.395 | 1535.999 | 37191.679 | 1.4771699357780228 | 49.24% | 0.056303189150909955 | 65 |
| 4 | 4.971 | 57.375 | 36700.159 | 1.5473692031533166 | 47.03% | 0.06256256256256257 | 54 |
| 5 | 5.427 | 64.479 | 35946.495 | 1.473209237711141 | 49.50% | 0.06255473539346929 | 64 |
| 6 | 4.907 | 40.031 | 36339.711 | 1.5143327713907595 | 48.10% | 0.06257039169065198 | 56 |
| 7 | 5.099 | 1180.671 | 35160.063 | 1.4695179980966244 | 49.54% | 0.06257039169065198 | 60 |
| 8 | 4.667 | 48.191 | 37322.751 | 1.4428473913901478 | 50.59% | 0.06256256256256257 | 50 |
| 9 | 5.123 | 1452.031 | 36110.335 | 1.4255703894193865 | 51.00% | 0.06257039169065198 | 61 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 1137 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 10 | SQLTransientConnectionException | 1315 | Client throttle limit reached; request rejected to avoid overloading the database |
| 11 | SQLTransientConnectionException | 1252 | Client throttle limit reached; request rejected to avoid overloading the database |
| 12 | SQLTransientConnectionException | 1326 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 13 | SQLTransientConnectionException | 1403 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 14 | SQLTransientConnectionException | 1274 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 15 | SQLTransientConnectionException | 1396 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLTransientConnectionException | 1135 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLTransientConnectionException | 1290 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLTransientConnectionException | 1334 | Client throttle limit reached; request rejected to avoid overloading the database |
| 4 | SQLTransientConnectionException | 1276 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 5 | SQLTransientConnectionException | 1341 | Client throttle limit reached; request rejected to avoid overloading the database |
| 6 | SQLTransientConnectionException | 1301 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
| 7 | SQLTransientConnectionException | 1340 | Timeout waiting for fast operation slot for operation: f891f847dfafb38c |
| 8 | SQLTransientConnectionException | 1370 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 9 | SQLTransientConnectionException | 1380 | Client throttle limit reached; request rejected to avoid overloading the database |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-15T10:26:24Z → 2026-07-15T10:41:24Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 33.2 | 52.0 | 0.017 | 10 | 0 |
| ojp-2 | 32.4 | 52.0 | 0.384 | 147 | 0 |
| ojp-3 | 30.7 | 56.0 | 0.425 | 150 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T10:26:24Z → 2026-07-15T10:41:24Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 53 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 43465 / 64120 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 2170229993 | Cumulative since stats reset |
| Transactions rolled back | 1296 | Non-zero → contention or application errors |
| Temp file bytes written | 1 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | -1 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 5913 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 403453 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T10:26:24Z → 2026-07-15T10:41:24Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 0.9 | 1.0 | 2.0 | 3.9 | 22.5 | 4.3 | 3.9 | 5.9 | 33.3 | 36.3 | 400.1 | 402.1 |
| Proxy (OJP / pgBouncer) | ojp-2 | 3.4 | 2.9 | 7.8 | 10.8 | 18.6 | 6.6 | 5.9 | 11.8 | 35.2 | 43.1 | 375.6 | 379.3 |
| Proxy (OJP / pgBouncer) | ojp-3 | 3.4 | 2.9 | 8.8 | 11.7 | 17.6 | 6.6 | 5.9 | 11.8 | 34.4 | 41.0 | 416.9 | 421.3 |
| PostgreSQL | db | 602.7 | 600.0 | 755.1 | 823.0 | 888.2 | 1267.8 | 1305.2 | 1484.6 | 1532.3 | 1547.9 | 28793.8 | 39505.6 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T10:45:40Z*

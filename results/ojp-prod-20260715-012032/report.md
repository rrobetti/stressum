# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T00:32:33Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260715-012032` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.96 RPS (per instance) |
| **Total throughput** | 15.37 RPS (all instances) |
| **p50 latency** | 6.47 ms |
| **p95 latency** | 7576.25 ms |
| **p99 latency** | 33077.25 ms |
| **p999 latency** | 53438.44 ms |
| **Error rate** | 1.00% (0.01) |
| **Total requests** | 14467 |
| **Failed requests** | 154 |
| **Total successful** | 14313 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 52.02 |
| observed_postgres_backends_median_numbackends | 52 |
| observed_client_backends_active_median | 30954 |
| observed_client_backends_active_max | 46727 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.4% / 4.9% / 16.6% / 27.3% / 56.7% |
| OJP proxy-tier host_cpu (avg / peak) | 17.0% / 92.0% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 101.60% |
| OJP proxy-tier RSS (avg / peak, summed) | 1143.80 MiB / 1174.70 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.4% / 4.9% / 16.6% / 27.3% / 56.7% |
| PgBouncer tier RSS (avg / peak, summed) | 1143.80 MiB / 1174.70 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.4% / 4.9% / 16.6% / 27.3% / 56.7% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.0% / 92.0% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 101.60% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1143.80 MiB / 1174.70 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.05% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 632 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (7576.25 ms) |
| Error rate | < 0.1% | ❌ FAIL (1.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.48 RPS (all instances) |
| **Achieved throughput** | 15.37 RPS (all instances) |
| **Attempted − achieved gap** | 0.11 RPS (0.71%) |
| **Total attempted ops** | 14409 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.647 | 5021.695 | 26935.295 | 0.9591585154286119 | 1.00% | 0.05004065823044251 | 36 |
| 10 | 5.995 | 9461.759 | 35717.119 | 0.9575285279309467 | 1.10% | 0.050031269543464665 | 35 |
| 11 | 6.823 | 5947.391 | 36372.479 | 0.949715352768987 | 1.77% | 0.050031269543464665 | 42 |
| 12 | 6.155 | 7286.783 | 32817.151 | 0.9550216972345147 | 1.66% | 0.04379615311403858 | 38 |
| 13 | 6.603 | 10461.183 | 35323.903 | 0.961650823192402 | 0.88% | 0.05002814102485889 | 41 |
| 14 | 6.011 | 5210.111 | 34504.703 | 0.9596138123667655 | 2.21% | 0.03754458434073752 | 33 |
| 15 | 5.979 | 1992.703 | 34045.951 | 0.9560023830160639 | 1.77% | 0.050031269543464665 | 40 |
| 1 | 6.907 | 6443.007 | 32014.335 | 0.9617283632585418 | 0.78% | 0.05002501250625312 | 43 |
| 2 | 6.451 | 8478.719 | 31932.415 | 0.9677197861146158 | 0.22% | 0.050031269543464665 | 37 |
| 3 | 6.491 | 8486.911 | 31391.743 | 0.9583287775197936 | 1.11% | 0.050031269543464665 | 51 |
| 4 | 6.471 | 8065.023 | 30801.919 | 0.9631962186745989 | 1.00% | 0.05003752814610958 | 35 |
| 5 | 7.175 | 9093.119 | 35094.527 | 0.961474703269014 | 0.44% | 0.050031269543464665 | 40 |
| 6 | 6.547 | 8335.359 | 32456.703 | 0.9621725057859646 | 1.22% | 0.05003752814610958 | 39 |
| 7 | 7.123 | 9256.959 | 30392.319 | 0.9629470056010341 | 1.11% | 0.050031269543464665 | 40 |
| 8 | 5.987 | 9076.735 | 33587.199 | 0.9623835424920703 | 0.55% | 0.03755398399890485 | 38 |
| 9 | 6.223 | 8601.599 | 35848.191 | 0.974915626072893 | 0.22% | 0.050031269543464665 | 44 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 9 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 10 | SQLTransientConnectionException | 10 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 11 | SQLTransientConnectionException | 16 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 12 | SQLTransientConnectionException | 15 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 13 | SQLTransientConnectionException | 8 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 14 | SQLTransientConnectionException | 20 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 15 | SQLTransientConnectionException | 16 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 1 | SQLTransientConnectionException | 7 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLTransientConnectionException | 2 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 10 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 4 | SQLTransientConnectionException | 9 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 5 | SQLTransientConnectionException | 4 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 6 | SQLTransientConnectionException | 11 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 7 | SQLTransientConnectionException | 10 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 8 | SQLTransientConnectionException | 5 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 9 | SQLTransientConnectionException | 2 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-15T00:32:33Z → 2026-07-15T00:47:33Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 28.8 | 48.0 | 0.160 | 76 | 0 |
| ojp-2 | 31.6 | 50.0 | 0.145 | 81 | 0 |
| ojp-3 | 31.2 | 52.0 | 0.168 | 89 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T00:32:33Z → 2026-07-15T00:47:33Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 52 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 30954 / 46727 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1345806178 | Cumulative since stats reset |
| Transactions rolled back | 746 | Non-zero → contention or application errors |
| Temp file bytes written | -9 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 9 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1983 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 199499 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T00:32:33Z → 2026-07-15T00:47:33Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.3 | 2.0 | 6.8 | 16.6 | 27.4 | 5.8 | 3.9 | 15.7 | 34.3 | 41.2 | 351.3 | 364.7 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.2 | 2.0 | 5.9 | 15.7 | 38.1 | 6.3 | 4.9 | 17.6 | 35.2 | 52.9 | 402.6 | 411.0 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.1 | 1.9 | 4.9 | 11.7 | 36.1 | 5.3 | 4.9 | 8.8 | 21.5 | 38.1 | 389.9 | 399.0 |
| PostgreSQL | db | 446.0 | 505.7 | 979.4 | 1184.0 | 1217.2 | 1146.7 | 1373.3 | 1596.3 | 1597.2 | 1597.5 | 20993.9 | 58640.6 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T00:51:33Z*

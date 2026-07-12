# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-11T12:42:19Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260711-133027` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.00 RPS (per instance) |
| **Total throughput** | 3.99 RPS (all instances) |
| **p50 latency** | 6.38 ms |
| **p95 latency** | 1839.62 ms |
| **p99 latency** | 7251.95 ms |
| **p999 latency** | 11880.42 ms |
| **Error rate** | 0.00% (0.00) |
| **Total requests** | 3604 |
| **Failed requests** | 9 |
| **Total successful** | 3595 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 13.69 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 12673 |
| observed_client_backends_active_max | 18808 |
| observed_client_backends_idle_median | 0 |
| observed_client_backends_idle_max | 0 |

## Topology-Specific Summary

| Field | Value |
|-------|-------|
| Scenario profile | ojp-prod |
| Configured replicas | 4 |
| Configured client pool size (per replica) | 12 |
| OJP servers | 3 |
| Real DB connections per OJP server | 4 |
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.4% / 2.0% / 9.8% / 24.4% / 39.2% |
| OJP proxy-tier host_cpu (avg / peak) | 13.5% / 80.3% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 85.80% |
| OJP proxy-tier RSS (avg / peak, summed) | 644.80 MiB / 660.10 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.4% / 2.0% / 9.8% / 24.4% / 39.2% |
| PgBouncer tier RSS (avg / peak, summed) | 644.80 MiB / 660.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 3.4% / 2.0% / 9.8% / 24.4% / 39.2% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 13.5% / 80.3% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 85.80% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 644.80 MiB / 660.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.16% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 184 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (1839.62 ms) |
| Error rate | < 0.1% | ✅ PASS (0.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 4.00 RPS (all instances) |
| **Achieved throughput** | 3.99 RPS (all instances) |
| **Attempted − achieved gap** | 0.01 RPS (0.25%) |
| **Total attempted ops** | 3604 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.451 | 1910.783 | 6148.095 | 0.9925481174892752 | 0.78% | 0.15030060120240482 | 48 |
| 1 | 7.047 | 1996.799 | 6508.543 | 0.9991041366241603 | 0.11% | 0.2001000500250125 | 45 |
| 2 | 5.767 | 1745.919 | 7970.815 | 1.0002375702997162 | 0.00% | 0.15022533800701052 | 46 |
| 3 | 6.255 | 1704.959 | 8380.415 | 0.9989743862967354 | 0.11% | 0.15022533800701052 | 45 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 7 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLTransientConnectionException | 1 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLTransientConnectionException | 1 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-11T12:42:19Z → 2026-07-11T12:57:19Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 27.2 | 48.0 | 0.053 | 16 | 0 |
| ojp-2 | 25.3 | 40.0 | 0.039 | 19 | 0 |
| ojp-3 | 25.1 | 40.0 | 0.058 | 28 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-11T12:42:19Z → 2026-07-11T12:57:19Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 12673 / 18808 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 92430761 | Cumulative since stats reset |
| Transactions rolled back | 1310 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1381 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 138347 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-11T12:42:19Z → 2026-07-11T12:57:19Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.2 | 1.0 | 3.9 | 13.7 | 36.2 | 4.6 | 3.9 | 7.8 | 33.3 | 43.1 | 222.2 | 226.7 |
| Proxy (OJP / pgBouncer) | ojp-2 | 1.0 | 1.0 | 3.9 | 9.8 | 16.7 | 5.1 | 3.9 | 12.8 | 34.5 | 73.4 | 212.1 | 213.8 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.2 | 1.0 | 3.9 | 11.8 | 32.9 | 4.1 | 3.9 | 6.9 | 16.7 | 35.3 | 210.5 | 219.6 |
| PostgreSQL | db | 29.8 | 1.3 | 181.9 | 239.4 | 291.9 | 166.1 | 128.7 | 399.0 | 400.0 | 400.0 | 3804.4 | 8576.4 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-11T13:00:00Z*

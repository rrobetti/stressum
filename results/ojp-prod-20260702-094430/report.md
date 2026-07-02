# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T08:56:18Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 8 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260702-094430` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 2.51 RPS (per instance) |
| **Total throughput** | 10.05 RPS (all instances) |
| **p50 latency** | 6.51 ms |
| **p95 latency** | 1352.58 ms |
| **p99 latency** | 4670.98 ms |
| **p999 latency** | 9078.77 ms |
| **Error rate** | 64.00% (0.64) |
| **Total requests** | 28861 |
| **Failed requests** | 18476 |
| **Total successful** | 10385 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 20 |
| observed_postgres_backends_avg_numbackends | 14.52 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 19880 |
| observed_client_backends_active_max | 28452 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.2% / 3.9% / 9.8% / 18.6% / 35.2% |
| OJP proxy-tier host_cpu (avg / peak) | 15.3% / 73.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 79.30% |
| OJP proxy-tier RSS (avg / peak, summed) | 689.60 MiB / 691.40 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.2% / 3.9% / 9.8% / 18.6% / 35.2% |
| PgBouncer tier RSS (avg / peak, summed) | 689.60 MiB / 691.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 4.2% / 3.9% / 9.8% / 18.6% / 35.2% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 15.3% / 73.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 79.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 689.60 MiB / 691.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.38% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 742 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (1352.58 ms) |
| Error rate | < 0.1% | ❌ FAIL (64.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 27.88 RPS (all instances) |
| **Achieved throughput** | 10.05 RPS (all instances) |
| **Attempted − achieved gap** | 17.83 RPS (63.95%) |
| **Total attempted ops** | 28803 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 6.215 | 1403.903 | 3868.671 | 2.524671826622383 | 63.94% | 0.35035035035035034 | 188 |
| 1 | 6.503 | 1524.735 | 4902.911 | 2.5546445044638495 | 63.44% | 0.40060090135202797 | 205 |
| 2 | 6.031 | 970.239 | 4898.815 | 2.515541280244609 | 63.86% | 0.35052578868302453 | 172 |
| 3 | 7.279 | 1511.423 | 5013.503 | 2.458023698565103 | 64.84% | 0.40040040040040037 | 177 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 355 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 0 | SQLTransientException | 3270 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 988 | RESOURCE_EXHAUSTED: Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 1 | SQLException | 339 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 1 | SQLTransientException | 3213 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 1025 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLException | 356 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 2 | SQLTransientException | 3263 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 989 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLException | 346 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 3 | SQLTransientException | 3363 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 969 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-02T08:56:18Z → 2026-07-02T09:11:18Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.8 | 45.0 | 0.005 | 3 | 0 |
| ojp-2 | 25.7 | 40.0 | 0.343 | 83 | 0 |
| ojp-3 | 27.5 | 45.0 | 0.279 | 75 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T08:56:18Z → 2026-07-02T09:11:18Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 19880 / 28452 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 272116675 | Cumulative since stats reset |
| Transactions rolled back | 4837 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 7068 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 539598 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T08:56:18Z → 2026-07-02T09:11:18Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 0.5 | 0.0 | 2.0 | 3.9 | 21.6 | 3.3 | 2.9 | 3.9 | 23.5 | 33.3 | 229.1 | 229.4 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.1 | 2.0 | 5.9 | 10.7 | 35.2 | 7.4 | 4.9 | 34.5 | 36.6 | 41.4 | 229.4 | 230.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 1.7 | 1.0 | 3.9 | 10.8 | 22.5 | 4.9 | 3.9 | 8.9 | 33.7 | 44.3 | 231.1 | 231.9 |
| PostgreSQL | db | 80.7 | 60.1 | 259.5 | 306.5 | 323.4 | 218.2 | 193.5 | 399.6 | 400.0 | 400.0 | 5146.7 | 9680.8 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T09:14:06Z*

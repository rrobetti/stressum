# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-02T12:03:52Z |
| **Duration** | 900 s |
| **Instances**| 4 |
| **Target RPS**| 12 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260702-125202` |

---

## Aggregate Metrics (mean across 4 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.09 RPS (per instance) |
| **Total throughput** | 4.36 RPS (all instances) |
| **p50 latency** | 8.21 ms |
| **p95 latency** | 139.95 ms |
| **p99 latency** | 1512.96 ms |
| **p999 latency** | 25104.50 ms |
| **Error rate** | 89.00% (0.89) |
| **Total requests** | 43259 |
| **Failed requests** | 38682 |
| **Total successful** | 4577 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 12 |
| observed_postgres_backends_max_numbackends | 16 |
| observed_postgres_backends_avg_numbackends | 13.02 |
| observed_postgres_backends_median_numbackends | 13 |
| observed_client_backends_active_median | 14817 |
| observed_client_backends_active_max | 18845 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.5% / 2.0% / 4.9% / 11.8% / 24.5% |
| OJP proxy-tier host_cpu (avg / peak) | 17.7% / 93.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 53.00% |
| OJP proxy-tier RSS (avg / peak, summed) | 717.10 MiB / 718.40 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.5% / 2.0% / 4.9% / 11.8% / 24.5% |
| PgBouncer tier RSS (avg / peak, summed) | 717.10 MiB / 718.40 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 2.5% / 2.0% / 4.9% / 11.8% / 24.5% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.7% / 93.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 53.00% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 717.10 MiB / 718.40 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.34% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 663 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (139.95 ms) |
| Error rate | < 0.1% | ❌ FAIL (89.00%) |

## Open-Loop Sanity (4/4 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 41.11 RPS (all instances) |
| **Achieved throughput** | 4.36 RPS (all instances) |
| **Attempted − achieved gap** | 36.75 RPS (89.41%) |
| **Total attempted ops** | 43204 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 8.163 | 28.095 | 1520.639 | 1.071072788400566 | 89.55% | 0.35070140280561124 | 161 |
| 1 | 8.043 | 204.799 | 1511.423 | 1.1734737685680756 | 88.63% | 0.35070140280561124 | 191 |
| 2 | 8.359 | 161.151 | 1517.567 | 1.0667673062845395 | 89.60% | 0.35070140280561124 | 160 |
| 3 | 8.263 | 165.759 | 1502.207 | 1.0439730632005233 | 89.90% | 0.3007518796992481 | 151 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLException | 1204 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 0 | SQLTransientException | 7278 | Client throttle limit reached; request rejected to avoid overloading the database |
| 0 | StatusRuntimeException | 1202 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 1 | SQLException | 1194 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 1 | SQLTransientException | 6938 | Client throttle limit reached; request rejected to avoid overloading the database |
| 1 | StatusRuntimeException | 1452 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLException | 1205 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 2 | SQLTransientException | 7284 | Client throttle limit reached; request rejected to avoid overloading the database |
| 2 | StatusRuntimeException | 1204 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLException | 1204 | Connection admission timeout for hash: gIy8lRvMLe58CtrX328JQiawIIjaU6iK6zTi5IpZ4QU after 30000ms (phase=admission) |
| 3 | SQLTransientException | 7379 | Client throttle limit reached; request rejected to avoid overloading the database |
| 3 | StatusRuntimeException | 1138 | RESOURCE_EXHAUSTED: Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-02T12:03:52Z → 2026-07-02T12:18:52Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 26.4 | 43.0 | 0.113 | 64 | 0 |
| ojp-2 | 27.1 | 45.0 | 0.010 | 4 | 0 |
| ojp-3 | 28.1 | 47.0 | 0.007 | 3 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-02T12:03:52Z → 2026-07-02T12:18:52Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 13 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 14817 / 18845 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 37151547 | Cumulative since stats reset |
| Transactions rolled back | 3397 | Non-zero → contention or application errors |
| Temp file bytes written | 0 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 0 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 6978 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 533147 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-02T12:03:52Z → 2026-07-02T12:18:52Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 1.4 | 1.0 | 2.9 | 6.8 | 11.8 | 6.7 | 3.9 | 33.5 | 36.3 | 88.2 | 227.7 | 228.5 |
| Proxy (OJP / pgBouncer) | ojp-2 | 0.6 | 0.0 | 2.0 | 2.0 | 19.6 | 7.5 | 3.9 | 34.3 | 35.5 | 86.0 | 246.5 | 246.7 |
| Proxy (OJP / pgBouncer) | ojp-3 | 0.5 | 0.0 | 2.0 | 3.9 | 21.6 | 3.9 | 3.0 | 4.9 | 33.3 | 35.1 | 242.9 | 243.2 |
| PostgreSQL | db | 6.0 | 0.7 | 47.5 | 95.2 | 99.2 | 85.4 | 80.7 | 160.4 | 198.0 | 263.8 | 6270.4 | 6490.4 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-02T12:22:00Z*

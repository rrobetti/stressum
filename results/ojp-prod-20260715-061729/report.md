# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-15T05:29:22Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 2 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260715-061729` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 1.74 RPS (per instance) |
| **Total throughput** | 27.78 RPS (all instances) |
| **p50 latency** | 5.91 ms |
| **p95 latency** | 46.79 ms |
| **p99 latency** | 36025.38 ms |
| **p999 latency** | 48543.69 ms |
| **Error rate** | 12.00% (0.12) |
| **Total requests** | 28831 |
| **Failed requests** | 3597 |
| **Total successful** | 25234 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 53.57 |
| observed_postgres_backends_median_numbackends | 54 |
| observed_client_backends_active_median | 43503 |
| observed_client_backends_active_max | 65472 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.0% / 6.8% / 15.6% / 21.5% / 35.2% |
| OJP proxy-tier host_cpu (avg / peak) | 18.6% / 62.5% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 60.70% |
| OJP proxy-tier RSS (avg / peak, summed) | 1191.40 MiB / 1203.50 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.0% / 6.8% / 15.6% / 21.5% / 35.2% |
| PgBouncer tier RSS (avg / peak, summed) | 1191.40 MiB / 1203.50 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 8.0% / 6.8% / 15.6% / 21.5% / 35.2% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.6% / 62.5% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 60.70% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1191.40 MiB / 1203.50 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.06% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 932 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ✅ PASS (46.79 ms) |
| Error rate | < 0.1% | ❌ FAIL (12.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 31.73 RPS (all instances) |
| **Achieved throughput** | 27.78 RPS (all instances) |
| **Attempted − achieved gap** | 3.94 RPS (12.43%) |
| **Total attempted ops** | 28809 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 5.811 | 57.151 | 34668.543 | 1.7661124978688618 | 10.27% | 0.06255082278805313 | 59 |
| 10 | 5.679 | 50.175 | 38633.471 | 1.721889492615828 | 13.32% | 0.06255473539346929 | 53 |
| 11 | 5.779 | 35.583 | 35225.599 | 1.689083447092042 | 14.65% | 0.06255082278805313 | 58 |
| 12 | 5.695 | 40.255 | 37715.967 | 1.7049305437696822 | 14.71% | 0.06255473539346929 | 53 |
| 13 | 5.807 | 37.823 | 37650.431 | 1.6949472159271792 | 15.21% | 0.06257822277847308 | 59 |
| 14 | 5.699 | 33.823 | 35422.207 | 1.6817676535977697 | 15.37% | 0.06255473539346929 | 53 |
| 15 | 6.103 | 37.823 | 37355.519 | 1.7836674032330468 | 9.16% | 0.075046904315197 | 72 |
| 1 | 6.023 | 69.567 | 32849.919 | 1.7661124978688618 | 10.32% | 0.06257822277847308 | 67 |
| 2 | 5.603 | 68.031 | 35880.959 | 1.7599862721070776 | 11.21% | 0.06255473539346929 | 50 |
| 3 | 6.207 | 51.071 | 36438.015 | 1.7359048486528588 | 12.43% | 0.06257822277847308 | 62 |
| 4 | 5.427 | 40.127 | 35454.975 | 1.72215906309325 | 12.15% | 0.06255473539346929 | 52 |
| 5 | 5.779 | 44.031 | 36110.335 | 1.7493008897363624 | 12.49% | 0.0625860558267618 | 65 |
| 6 | 5.875 | 38.399 | 35291.135 | 1.7903676450247585 | 10.21% | 0.06255473539346929 | 56 |
| 7 | 6.615 | 48.703 | 36077.567 | 1.7350636997370983 | 12.54% | 0.06256256256256257 | 63 |
| 8 | 6.603 | 52.575 | 36208.639 | 1.7435557030644984 | 12.54% | 0.06255473539346929 | 50 |
| 9 | 5.863 | 43.551 | 35422.207 | 1.7382063751242367 | 13.04% | 0.06257822277847308 | 60 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 185 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 10 | SQLTransientConnectionException | 240 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 11 | SQLTransientConnectionException | 264 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 12 | SQLTransientConnectionException | 265 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 13 | SQLTransientConnectionException | 274 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 14 | SQLTransientConnectionException | 277 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 15 | SQLTransientConnectionException | 165 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 1 | SQLTransientConnectionException | 186 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 2 | SQLTransientConnectionException | 202 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 3 | SQLTransientConnectionException | 224 | Timeout waiting for slow operation slot for operation: e98e4f987f09ed4e |
| 4 | SQLTransientConnectionException | 219 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 5 | SQLTransientConnectionException | 225 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 6 | SQLTransientConnectionException | 184 | Timeout waiting for slow operation slot for operation: ac3451c82f425cef |
| 7 | SQLTransientConnectionException | 226 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
| 8 | SQLTransientConnectionException | 226 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 9 | SQLTransientConnectionException | 235 | Timeout waiting for slow operation slot for operation: e9cb50da3e8545 |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-15T05:29:22Z → 2026-07-15T05:44:22Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 30.7 | 50.0 | 0.275 | 113 | 0 |
| ojp-2 | 30.6 | 52.0 | 0.295 | 126 | 0 |
| ojp-3 | 30.4 | 50.0 | 0.362 | 136 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-15T05:29:22Z → 2026-07-15T05:44:22Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 54 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 43503 / 65472 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1910889759 | Cumulative since stats reset |
| Transactions rolled back | 1007 | Non-zero → contention or application errors |
| Temp file bytes written | -4 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 4 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 3374 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 339514 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-15T05:29:22Z → 2026-07-15T05:44:22Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.5 | 2.0 | 6.8 | 10.8 | 18.6 | 5.4 | 4.9 | 9.8 | 21.6 | 40.1 | 382.1 | 386.0 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.8 | 2.0 | 7.8 | 10.8 | 27.4 | 6.8 | 4.9 | 14.7 | 36.3 | 40.1 | 439.2 | 444.1 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.8 | 2.0 | 7.8 | 9.8 | 14.7 | 6.9 | 4.9 | 12.7 | 37.2 | 45.9 | 370.1 | 373.4 |
| PostgreSQL | db | 656.4 | 663.3 | 867.4 | 960.1 | 983.2 | 1517.3 | 1565.5 | 1596.7 | 1598.1 | 1598.5 | 23191.9 | 33675.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-15T05:48:13Z*

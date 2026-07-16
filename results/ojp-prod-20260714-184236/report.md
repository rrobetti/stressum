# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-14T17:54:38Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260714-184236` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.96 RPS (per instance) |
| **Total throughput** | 15.29 RPS (all instances) |
| **p50 latency** | 6.72 ms |
| **p95 latency** | 6346.94 ms |
| **p99 latency** | 30748.62 ms |
| **p999 latency** | 61595.62 ms |
| **Error rate** | 2.00% (0.02) |
| **Total requests** | 14478 |
| **Failed requests** | 240 |
| **Total successful** | 14238 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 56 |
| observed_postgres_backends_avg_numbackends | 51.87 |
| observed_postgres_backends_median_numbackends | 50 |
| observed_client_backends_active_median | 31416 |
| observed_client_backends_active_max | 47949 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.6% / 4.9% / 14.7% / 28.3% / 77.2% |
| OJP proxy-tier host_cpu (avg / peak) | 18.9% / 89.2% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 115.30% |
| OJP proxy-tier RSS (avg / peak, summed) | 1102.70 MiB / 1126.10 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.6% / 4.9% / 14.7% / 28.3% / 77.2% |
| PgBouncer tier RSS (avg / peak, summed) | 1102.70 MiB / 1126.10 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.6% / 4.9% / 14.7% / 28.3% / 77.2% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 18.9% / 89.2% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 115.30% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1102.70 MiB / 1126.10 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.05% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 624 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (6346.94 ms) |
| Error rate | < 0.1% | ❌ FAIL (2.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.48 RPS (all instances) |
| **Achieved throughput** | 15.29 RPS (all instances) |
| **Attempted − achieved gap** | 0.19 RPS (1.23%) |
| **Total attempted ops** | 14407 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 8.823 | 4456.447 | 23117.823 | 0.9507828183170609 | 1.55% | 0.050050050050050046 | 34 |
| 10 | 7.051 | 7929.855 | 31834.111 | 0.9539923295594309 | 1.33% | 0.0375610366846125 | 40 |
| 11 | 5.763 | 8359.935 | 33341.439 | 0.9539913092675122 | 1.44% | 0.05003752814610958 | 39 |
| 12 | 5.919 | 7467.007 | 34111.487 | 0.9515567209613737 | 2.32% | 0.050050050050050046 | 37 |
| 13 | 7.103 | 3966.975 | 35422.207 | 0.9535676824126762 | 1.87% | 0.050043788314775434 | 44 |
| 14 | 5.503 | 2846.719 | 28426.239 | 0.963379652858225 | 1.88% | 0.03754693366708385 | 35 |
| 15 | 6.199 | 1296.383 | 32538.623 | 0.9537095642214672 | 2.32% | 0.050043788314775434 | 46 |
| 1 | 7.039 | 5943.295 | 30031.871 | 0.9619005605706846 | 1.11% | 0.050050050050050046 | 40 |
| 2 | 6.035 | 7606.271 | 25952.255 | 0.9611327805474474 | 1.33% | 0.03755163349605708 | 33 |
| 3 | 13.279 | 8368.127 | 30490.623 | 0.9566623399275975 | 1.22% | 0.050050050050050046 | 43 |
| 4 | 6.495 | 7147.519 | 30605.311 | 0.9518543513112595 | 1.55% | 0.050043788314775434 | 31 |
| 5 | 5.687 | 12828.671 | 31866.879 | 0.9547859858515141 | 1.88% | 0.05003752814610958 | 43 |
| 6 | 5.319 | 7536.639 | 29999.103 | 0.9595824310353915 | 1.33% | 0.050043788314775434 | 35 |
| 7 | 5.643 | 6168.575 | 31080.447 | 0.9586881788690492 | 1.55% | 0.050050050050050046 | 47 |
| 8 | 5.843 | 1915.903 | 30638.079 | 0.9443638164276524 | 2.32% | 0.05003752814610958 | 36 |
| 9 | 5.775 | 7712.767 | 32522.239 | 0.9643003471265038 | 1.55% | 0.050043788314775434 | 41 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 14 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 10 | SQLTransientConnectionException | 12 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 11 | SQLTransientConnectionException | 13 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 12 | SQLTransientConnectionException | 21 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 13 | SQLTransientConnectionException | 17 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 14 | SQLTransientConnectionException | 17 | Timeout waiting for fast operation slot for operation: e98e4f987f09ed4e |
| 15 | SQLTransientConnectionException | 21 | Timeout waiting for fast operation slot for operation: e98e4f987f09ed4e |
| 1 | SQLTransientConnectionException | 10 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 2 | SQLTransientConnectionException | 12 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 3 | SQLTransientConnectionException | 11 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
| 4 | SQLTransientConnectionException | 14 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
| 5 | SQLTransientConnectionException | 17 | Timeout waiting for fast operation slot for operation: 19ddf4bbc5b8c770 |
| 6 | SQLTransientConnectionException | 12 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
| 7 | SQLTransientConnectionException | 14 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
| 8 | SQLTransientConnectionException | 21 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
| 9 | SQLTransientConnectionException | 14 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-14T17:54:38Z → 2026-07-14T18:09:38Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 31.3 | 50.0 | 0.130 | 82 | 0 |
| ojp-2 | 30.0 | 50.0 | 0.151 | 77 | 0 |
| ojp-3 | 31.0 | 50.0 | 0.185 | 90 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-14T17:54:38Z → 2026-07-14T18:09:38Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 50 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 31416 / 47949 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1309204402 | Cumulative since stats reset |
| Transactions rolled back | 736 | Non-zero → contention or application errors |
| Temp file bytes written | -14 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 13 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1901 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 191500 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-14T17:54:38Z → 2026-07-14T18:09:38Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.5 | 2.0 | 6.8 | 19.6 | 47.9 | 7.5 | 4.9 | 33.3 | 37.2 | 52.9 | 346.5 | 357.6 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.2 | 1.9 | 5.9 | 16.6 | 32.3 | 5.8 | 4.9 | 10.8 | 35.2 | 37.2 | 362.4 | 368.7 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.1 | 1.9 | 4.9 | 11.7 | 35.1 | 6.0 | 4.9 | 10.8 | 35.2 | 49.9 | 393.8 | 399.8 |
| PostgreSQL | db | 422.6 | 463.5 | 995.1 | 1106.7 | 1221.1 | 1130.3 | 1333.2 | 1595.9 | 1597.1 | 1597.8 | 21491.4 | 60644.3 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-14T18:13:42Z*

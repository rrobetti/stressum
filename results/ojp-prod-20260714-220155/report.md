# Benchmark Report

| Field        | Value |
|-------------|-------|
| **SUT**      | OJP |
| **Workload** | W5_HTAP |
| **Run time** | 2026-07-14T21:14:01Z |
| **Duration** | 900 s |
| **Instances**| 16 |
| **Target RPS**| 1 (per instance) |
| **Results dir** | `/home/rogerio/Projects/stressar/ansible/playbooks/../../results/ojp-prod-20260714-220155` |

---

## Aggregate Metrics (mean across 16 instance(s))

| Metric | Value |
|--------|-------|
| **Achieved throughput** | 0.96 RPS (per instance) |
| **Total throughput** | 15.39 RPS (all instances) |
| **p50 latency** | 6.39 ms |
| **p95 latency** | 5752.37 ms |
| **p99 latency** | 31168.50 ms |
| **p999 latency** | 50452.56 ms |
| **Error rate** | 1.00% (0.01) |
| **Total requests** | 14466 |
| **Failed requests** | 120 |
| **Total successful** | 14346 |

## Connection Budget — Configured and Observed

| Field | Value |
|-------|-------|
| configured_db_connection_budget | 48 |
| observed_postgres_backends_max_numbackends | 57 |
| observed_postgres_backends_avg_numbackends | 51.88 |
| observed_postgres_backends_median_numbackends | 51 |
| observed_client_backends_active_median | 31807 |
| observed_client_backends_active_max | 48137 |
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
| OJP proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.7% / 5.9% / 15.6% / 23.5% / 51.8% |
| OJP proxy-tier host_cpu (avg / peak) | 17.6% / 75.4% |
| OJP proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 82.10% |
| OJP proxy-tier RSS (avg / peak, summed) | 1137.40 MiB / 1161.00 MiB |
| PgBouncer nodes | N/A |
| PgBouncer server pool size per node | N/A |
| pgbouncer_reserve_pool_size | N/A |
| PgBouncer local HikariCP pool size per replica | N/A |
| HAProxy nodes | N/A |
| PgBouncer tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.7% / 5.9% / 15.6% / 23.5% / 51.8% |
| PgBouncer tier RSS (avg / peak, summed) | 1137.40 MiB / 1161.00 MiB |
| HAProxy service_cpu (avg / p50 / p95 / p99 / aligned_peak) | N/A% / N/A% / N/A% / N/A% / N/A% |
| HAProxy RSS (avg / peak, summed) | N/A MiB / 0 MiB |
| Total PgBouncer proxy-tier service_cpu (avg / p50 / p95 / p99 / aligned_peak) | 6.7% / 5.9% / 15.6% / 23.5% / 51.8% |
| Total PgBouncer proxy-tier host_cpu (avg / peak) | 17.6% / 75.4% |
| Total PgBouncer proxy-tier service_cpu legacy_peak_sum (non-time-aligned) | 82.10% |
| Total PgBouncer proxy-tier RSS (avg / peak) | 1137.40 MiB / 1161.00 MiB |

## Bench JVM System Metrics (in-process, median across instances)

| Metric | Value | Source |
|--------|-------|--------|
| **bench_jvm_cpu (median)** | 0.05% | `OperatingSystemMXBean.getProcessCpuLoad()` (in-process) |
| **Bench JVM GC pause total** | 612 ms | `GarbageCollectorMXBean.getCollectionTime()` |

---

## SLO Evaluation

| SLO | Threshold | Result |
|-----|-----------|--------|
| p95 latency | < 1500 ms | ❌ FAIL (5752.37 ms) |
| Error rate | < 0.1% | ❌ FAIL (1.00%) |

## Open-Loop Sanity (16/16 instance(s))

> A large attempted-vs-achieved gap, non-zero missed opportunities, or high
> total scheduling delay indicate the open-loop dispatcher backlogged behind a
> too-small worker pool and the run effectively degraded to closed-loop. Tune
> via `workload.openLoopMaxConcurrency` if auto-sizing is insufficient.

| Metric | Value |
|--------|-------|
| **Attempted throughput** | 15.46 RPS (all instances) |
| **Achieved throughput** | 15.39 RPS (all instances) |
| **Attempted − achieved gap** | 0.08 RPS (0.49%) |
| **Total attempted ops** | 14410 |
| **Missed opportunities** | 0 |
| **Total scheduling delay** | 0.00 ms |

---

## Per-Instance Breakdown

| Instance | p50 (ms) | p95 (ms) | p99 (ms) | Throughput (RPS) | Error Rate | CPU (%) | GC pause (ms) |
|----------|----------|----------|----------|-----------------|------------|---------|---------------|
| 0 | 7.111 | 4878.335 | 25198.591 | 0.9576576229546787 | 0.89% | 0.050043788314775434 | 34 |
| 10 | 7.067 | 8200.191 | 31309.823 | 0.9639456510110195 | 0.44% | 0.03755633509033479 | 33 |
| 11 | 5.843 | 5996.543 | 32129.023 | 0.9589041095890412 | 0.99% | 0.050043788314775434 | 40 |
| 12 | 5.767 | 5599.231 | 37978.111 | 0.9577795779991075 | 1.10% | 0.03754693366708385 | 32 |
| 13 | 7.147 | 5734.399 | 36601.855 | 0.9608710183304625 | 0.88% | 0.050043788314775434 | 39 |
| 14 | 5.663 | 1645.567 | 36143.103 | 0.9601691275485654 | 1.44% | 0.050043788314775434 | 33 |
| 15 | 5.455 | 55.071 | 33505.279 | 0.9580152507416545 | 1.66% | 0.05003752814610958 | 43 |
| 1 | 6.531 | 5996.543 | 21282.815 | 0.9604102339077512 | 1.11% | 0.050043788314775434 | 41 |
| 2 | 5.435 | 6111.231 | 26755.071 | 0.965006933633988 | 0.77% | 0.05003752814610958 | 39 |
| 3 | 6.455 | 7544.831 | 30081.023 | 0.9649601525065912 | 0.44% | 0.050050050050050046 | 43 |
| 4 | 6.863 | 6701.055 | 29229.055 | 0.9647946641912915 | 0.66% | 0.050043788314775434 | 36 |
| 5 | 8.919 | 6569.983 | 29130.751 | 0.965041428003396 | 0.55% | 0.050043788314775434 | 44 |
| 6 | 5.183 | 6189.055 | 30081.023 | 0.9593408462092132 | 0.66% | 0.050043788314775434 | 34 |
| 7 | 6.511 | 7577.599 | 30654.463 | 0.9702649296557926 | 0.22% | 0.050043788314775434 | 40 |
| 8 | 5.683 | 5967.871 | 34144.255 | 0.959493524489573 | 0.88% | 0.05003439884478712 | 34 |
| 9 | 6.611 | 7270.399 | 34471.935 | 0.9631021531064597 | 0.55% | 0.05004065823044251 | 47 |

---

## Error Breakdown

| Instance | Error type | Count | First error message |
|----------|------------|-------|---------------------|
| 0 | SQLTransientConnectionException | 8 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 10 | SQLTransientConnectionException | 4 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 11 | SQLTransientConnectionException | 9 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 12 | SQLTransientConnectionException | 10 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 13 | SQLTransientConnectionException | 8 | Timeout waiting for slow operation slot for operation: 23a1c2cea61780ce |
| 14 | SQLTransientConnectionException | 13 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 15 | SQLTransientConnectionException | 15 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 1 | SQLTransientConnectionException | 10 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
| 2 | SQLTransientConnectionException | 7 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
| 3 | SQLTransientConnectionException | 4 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
| 4 | SQLTransientConnectionException | 6 | Connection admission timeout for hash: aHOSqngG4Q5gGB3v_yO2tnMrfevlSwgapbfCQ1r0rIA after 30000ms (phase=admission) |
| 5 | SQLTransientConnectionException | 5 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 6 | SQLTransientConnectionException | 6 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 7 | SQLTransientConnectionException | 2 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 8 | SQLTransientConnectionException | 8 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
| 9 | SQLTransientConnectionException | 5 | Timeout waiting for fast operation slot for operation: e7282124a6fbdd3c |
---
## OJP Proxy — JVM Heap and GC Metrics

> **Note:** Heap values are from `jstat -gc` (actual in-use JVM heap).
> OS RSS is **not** used here because the JVM does not return memory to the OS after GC.

> Stats are restricted to steady-state window: 2026-07-14T21:14:01Z → 2026-07-14T21:29:01Z.

| Proxy host | Heap used — median (MB) | Heap committed — median (MB) | Total GC time (s) | Young GC count | Full GC count |
|------------|------------------------|------------------------------|-------------------|----------------|---------------|
| ojp-1 | 30.8 | 50.0 | 0.137 | 81 | 0 |
| ojp-2 | 31.1 | 52.0 | 0.132 | 73 | 0 |
| ojp-3 | 30.2 | 50.0 | 0.174 | 91 | 0 |
---
## PostgreSQL — Database Statistics

> Stats are restricted to steady-state window: 2026-07-14T21:14:01Z → 2026-07-14T21:29:01Z.

| Metric | Value | Notes |
|--------|-------|-------|
| PostgreSQL backends (median, `numbackends`) | 51 | Total backend connections from `pg_stat_database` |
| Client backends in `state='active'` (median / max) | 31807 / 48137 | `pg_stat_activity` client backends only |
| Client backends in `state='idle'` (median / max) | 0 / 0 | `pg_stat_activity` client backends only |
| Buffer cache hit ratio (median) | N/A % | < 99 % on OLTP suggests insufficient `shared_buffers` |
| Transactions committed | 1370648805 | Cumulative since stats reset |
| Transactions rolled back | 603 | Non-zero → contention or application errors |
| Temp file bytes written | -16 | Non-zero → sort/hash spills; tune `work_mem` |
| Deadlocks | 16 | Should be 0 for OLTP workloads |
| Peak ungranted lock waits | 0 | Instantaneous max; > 0 indicates hot-row contention |
| Checkpoint buffers written | 1861 | High values → WAL/checkpoint I/O pressure |
| Checkpoint write time (ms) | 187604 | Cumulative; high → I/O-bound checkpoint |
---
## Process Resource Utilization

> `service_cpu` is service-process-tree CPU normalised to a single core (100% = 1 CPU fully busy).
> `host_cpu` is host-level busy in core-percent from `/proc/stat` (100% = 1 CPU; max ~= NCPU×100, cloud-comparable).
> Stats below are restricted to steady-state window: 2026-07-14T21:14:01Z → 2026-07-14T21:29:01Z.
> Memory values are Resident Set Size (RSS) — physical RAM in use.

| Component | Node | service_cpu avg (%) | service_cpu p50 (%) | service_cpu p95 (%) | service_cpu p99 (%) | service_cpu peak (%) | host_cpu avg (%) | host_cpu p50 (%) | host_cpu p95 (%) | host_cpu p99 (%) | host_cpu peak (%) | Avg RSS (MiB) | Peak RSS (MiB) |
|-----------|------|---------------------|---------------------|---------------------|---------------------|----------------------|------------------|------------------|------------------|------------------|-------------------|---------------|----------------|
| Proxy (OJP / pgBouncer) | ojp-1 | 2.4 | 1.9 | 5.9 | 15.7 | 30.3 | 5.5 | 4.9 | 9.8 | 22.5 | 35.2 | 360.0 | 369.7 |
| Proxy (OJP / pgBouncer) | ojp-2 | 2.3 | 1.9 | 6.8 | 15.6 | 33.3 | 6.9 | 4.9 | 25.5 | 36.2 | 65.6 | 394.0 | 401.7 |
| Proxy (OJP / pgBouncer) | ojp-3 | 2.2 | 1.9 | 5.8 | 10.7 | 18.5 | 5.7 | 4.9 | 8.8 | 19.5 | 37.2 | 383.4 | 389.6 |
| PostgreSQL | db | 430.0 | 453.9 | 959.6 | 1102.1 | 1111.9 | 1140.7 | 1302.3 | 1595.6 | 1596.9 | 1597.9 | 20093.5 | 60183.2 |

---

*Generated by `ansible/scripts/generate_report.sh` on 2026-07-14T21:33:00Z*

"""Static interpretation notes aligned with stressar-docs/METRICS.md."""

CAVEATS_MARKDOWN = """
## Measurement caveats (summary)

- **Aggregate throughput:** Reported system throughput is the **sum** of per-replica
  `achievedThroughputRps`, not the mean across replicas.
- **Latency percentiles across replicas:** Merging independent latency distributions
  requires **HDR histogram bucket merge**. Averaging or taking the median of
  per-replica percentiles is **not** equivalent to a global percentile over all
  requests. When HDR logs are absent from the bundle, treat cross-replica latency
  summaries as **indicative** only.
- **`stressum` (comparison mode):** When `.hlog` (or compatible) HDR logs are present,
  comparison merges them **across replicas within each run** before plotting;
  otherwise it falls back to the median of per-replica `summary.json` percentiles.
- **OJP / JVM memory:** Do not use `appRssMedian` from bench summaries as a proxy
  for live heap for OJP; prefer `heap_used_mb` from
  `node_metrics/proxy/*_jvm_metrics.csv` where available.
- **HDR clamp:** Histograms may clamp extreme tails at the configured maximum
  trackable value (see METRICS.md).
"""


def hdr_status_note(hdr_count: int) -> str:
    if hdr_count == 0:
        return (
            "No HDR histogram files (`.hlog` / `.hdr`) were found under this run; "
            "global tail latencies were not merged from raw histograms."
        )
    return (
        f"Found {hdr_count} HDR-related file(s) under the run directory; "
        "single-run figures here still use per-replica `summary.json` percentiles. "
        "Use `stressum` (comparison mode) to merge `.hlog` histograms across replicas for "
        "cross-scenario plots."
    )

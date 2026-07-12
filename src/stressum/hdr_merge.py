"""Merge HdrHistogram logs across replica files into run-level percentiles."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

from hdrh.histogram import HdrHistogram
from hdrh.log import HistogramLogReader

# Java bench typically records latency in nanoseconds.  Use 1 hour (3.6 T ns)
# as the upper bound so that production runs with timeout-induced outliers
# (> 60 s) are captured rather than causing an IndexError in HdrHistogram.add().
_MAX_TRACKABLE_NS = 3_600_000_000_000  # 1 hour in nanoseconds
_REF_HIST = HdrHistogram(1, _MAX_TRACKABLE_NS, 3)


def _looks_like_histogram_log(path: Path) -> bool:
    try:
        head = path.read_text(encoding="utf-8", errors="strict")[:4096]
    except (OSError, UnicodeDecodeError):
        return False
    if not head.strip():
        return False
    if head.lstrip().startswith("#"):
        return True
    if "StartTimestamp" in head and "Compressed_Histogram" in head:
        return True
    # Interval lines: float,float,float,base64...
    first = head.splitlines()[0]
    return first[:1].isdigit() or first.startswith('"StartTimestamp"')


def _load_histogram_log_merged(path: Path) -> HdrHistogram | None:
    if not _looks_like_histogram_log(path):
        return None
    merged = HdrHistogram(1, _MAX_TRACKABLE_NS, 3)
    reader = HistogramLogReader(str(path), _REF_HIST)
    try:
        while True:
            nxt = reader.add_next_interval_histogram(merged, 0.0, sys.maxsize, True)
            if nxt is None:
                break
    except (OSError, ValueError, TypeError, IndexError):
        return None
    finally:
        reader.close()
    if merged.get_total_count() == 0:
        return None
    return merged


def _infer_ns_to_ms_divisor(hist: HdrHistogram) -> float:
    """Infer raw histogram units and return the divisor to convert to milliseconds.

    Heuristic: raw p50 > 500_000 → nanoseconds (÷1e6), > 500 → microseconds (÷1e3),
    otherwise already milliseconds (÷1.0).  This correctly handles the common case
    where Java bench records latency in nanoseconds.  Edge case: if a future bench
    records in µs and p50 < 500 µs the heuristic will mis-classify — document and
    validate unit choice before adding sub-500-µs benchmarks.
    """
    raw_p50 = float(hist.get_value_at_percentile(50.0))
    if raw_p50 > 500_000:
        return 1e6
    if raw_p50 > 500:
        return 1e3
    return 1.0


@dataclass(frozen=True)
class MergedLatency:
    """Run-level latency after merging HDR logs (values reported in ms)."""

    p25_ms: float
    p50_ms: float
    p75_ms: float
    p90_ms: float
    p95_ms: float
    p99_ms: float
    p999_ms: float
    unit_divisor: float
    total_count: int
    hdr_paths_used: tuple[str, ...]


def merge_run_histogram(
    hdr_paths: list[Path],
) -> tuple[MergedLatency | None, list[str]]:
    """
    Merge all decodable histogram logs under one run into a single distribution.

    Returns (MergedLatency, warnings). On failure result is None and warnings explain why.
    """
    warnings: list[str] = []
    merged: HdrHistogram | None = None
    used: list[str] = []

    for p in sorted({x.resolve() for x in hdr_paths}):
        if not p.is_file():
            warnings.append(f"HDR path not a file: {p}")
            continue
        block = _load_histogram_log_merged(p)
        if block is None:
            warnings.append(
                f"Skipped HDR file (not a readable histogram log or empty): {p.name}"
            )
            continue
        if merged is None:
            merged = block
        else:
            try:
                merged.add(block)
            except (IndexError, ValueError) as e:
                warnings.append(f"Could not add histogram from {p.name}: {e}")
        used.append(p.as_posix())

    if merged is None or merged.get_total_count() == 0:
        return None, warnings

    div = _infer_ns_to_ms_divisor(merged)

    def q(pct: float) -> float:
        return float(merged.get_value_at_percentile(pct)) / div

    return (
        MergedLatency(
            p25_ms=q(25.0),
            p50_ms=q(50.0),
            p75_ms=q(75.0),
            p90_ms=q(90.0),
            p95_ms=q(95.0),
            p99_ms=q(99.0),
            p999_ms=q(99.9),
            unit_divisor=div,
            total_count=int(merged.get_total_count()),
            hdr_paths_used=tuple(used),
        ),
        warnings,
    )

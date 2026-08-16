"""Merge HdrHistogram logs across replica files into run-level percentiles."""

import re
from dataclasses import dataclass
from pathlib import Path

from hdrh.histogram import HdrHistogram

_INTERVAL_RE = re.compile(r'^(?:Tag=[^,]*,)?([-\d.]+),([-\d.]+),([-\d.]+),(.*)$')


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
    merged = HdrHistogram(1, 60_000_000_000, 5)
    try:
        with path.open("r", encoding="utf-8") as f:
            for raw_line in f:
                line = raw_line.strip()
                if not line or line.startswith("#") or line.startswith('"StartTimestamp"'):
                    continue
                match = _INTERVAL_RE.match(line)
                if not match:
                    continue
                merged.decode_and_add(match.group(4))
    except (OSError, ValueError, TypeError, IndexError):
        return None
    if merged.get_total_count() == 0:
        return None
    return merged


def _infer_ns_to_ms_divisor(hist: HdrHistogram) -> float:
    """Map raw histogram units to milliseconds using raw histogram magnitudes."""
    raw_p50 = float(hist.get_value_at_percentile(50.0))
    if raw_p50 > 500_000:
        return 1e6
    if raw_p50 > 500:
        return 1e3
    return 1.0


@dataclass(frozen=True)
class MergedLatency:
    """Run-level latency after merging HDR logs (values reported in ms)."""

    p50_ms: float
    p95_ms: float
    p99_ms: float
    p999_ms: float
    unit_divisor: float
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
            p50_ms=q(50.0),
            p95_ms=q(95.0),
            p99_ms=q(99.0),
            p999_ms=q(99.9),
            unit_divisor=div,
            hdr_paths_used=tuple(used),
        ),
        warnings,
    )

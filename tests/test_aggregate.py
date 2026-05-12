from __future__ import annotations

from pathlib import Path

from stressum.aggregate import aggregate_bundle
from stressum.load import load_run_bundle

FIXTURE = Path(__file__).resolve().parent / "fixtures" / "minimal-run"


def test_aggregate_sums_rps_and_requests() -> None:
    bundle = load_run_bundle(FIXTURE)
    agg = aggregate_bundle(bundle)
    assert agg.total_achieved_rps == 49.5 + 50.5
    assert agg.total_requests == 3000
    assert agg.total_failed == 30
    assert abs(agg.aggregate_error_rate - (30 / 3000)) < 1e-9
    assert agg.median_p50_ms == 1.25

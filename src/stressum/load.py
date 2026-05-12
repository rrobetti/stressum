from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import pandas as pd

_REPLICA_DIR = re.compile(r"^replica-(\d+)$", re.IGNORECASE)


@dataclass
class RunBundle:
    """Paths and parsed data for one exported Stressar run directory."""

    run_dir: Path
    metadata: dict[str, Any] | None
    summaries: list[dict[str, Any]] = field(default_factory=list)
    replica_ids: list[int] = field(default_factory=list)
    node_metrics_csvs: dict[str, Path] = field(default_factory=dict)
    report_md: Path | None = None
    hdr_paths: list[Path] = field(default_factory=list)


def _parse_replica_id(name: str) -> int | None:
    m = _REPLICA_DIR.match(name)
    return int(m.group(1)) if m else None


def discover_hdr_logs(run_dir: Path) -> list[Path]:
    out: list[Path] = []
    for pat in ("**/*.hlog", "**/*.hdr", "**/latency.hdr"):
        out.extend(run_dir.glob(pat))
    return sorted({p.resolve() for p in out})


def load_run_bundle(run_dir: Path) -> RunBundle:
    run_dir = run_dir.resolve()
    if not run_dir.is_dir():
        raise FileNotFoundError(f"Run directory not found: {run_dir}")

    meta_path = run_dir / "run_metadata.json"
    metadata: dict[str, Any] | None = None
    if meta_path.is_file():
        metadata = json.loads(meta_path.read_text(encoding="utf-8"))

    summaries: list[dict[str, Any]] = []
    replica_ids: list[int] = []

    for child in sorted(run_dir.iterdir(), key=lambda p: p.name):
        if not child.is_dir():
            continue
        rid = _parse_replica_id(child.name)
        if rid is None:
            continue
        sj = child / "summary.json"
        if not sj.is_file():
            continue
        data = json.loads(sj.read_text(encoding="utf-8"))
        summaries.append(data)
        replica_ids.append(rid)

    # Align summaries with sorted replica id order
    pairs = sorted(zip(replica_ids, summaries, strict=True), key=lambda x: x[0])
    replica_ids = [p[0] for p in pairs]
    summaries = [p[1] for p in pairs]

    node_root = run_dir / "node_metrics"
    node_csvs: dict[str, Path] = {}
    if node_root.is_dir():
        for p in sorted(node_root.rglob("*.csv")):
            rel = p.relative_to(run_dir).as_posix()
            node_csvs[rel] = p

    report = run_dir / "report.md"
    report_md = report if report.is_file() else None

    return RunBundle(
        run_dir=run_dir,
        metadata=metadata,
        summaries=summaries,
        replica_ids=replica_ids,
        node_metrics_csvs=node_csvs,
        report_md=report_md,
        hdr_paths=discover_hdr_logs(run_dir),
    )


def read_node_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, comment="#")

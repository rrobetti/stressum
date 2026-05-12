from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from stressum.caveats import CAVEATS_MARKDOWN, hdr_status_note

if TYPE_CHECKING:
    from stressum.aggregate import RunAggregates
    from stressum.load import RunBundle


def write_narrative(
    bundle: RunBundle,
    agg: RunAggregates,
    artifact_paths: dict[str, Path],
    out: Path,
) -> None:
    meta = bundle.metadata or {}
    ri = bundle.summaries[0].get("runInfo") if bundle.summaries else {}

    lines = [
        f"# Run narrative: `{bundle.run_dir.name}`",
        "",
        "## Identifiers",
        "",
        f"- **Run directory:** `{bundle.run_dir}`",
        f"- **Scenario (metadata):** {meta.get('scenario', '—')}",
        f"- **SUT:** {ri.get('sut', '—')}",
        f"- **Workload:** {ri.get('workload', '—')}",
        f"- **Load mode:** {ri.get('loadMode', '—')}",
        f"- **Target RPS (per replica):** {ri.get('targetRps', '—')}",
        f"- **Replicas (summaries loaded):** {len(agg.replica_ids)}",
        "",
        "## Aggregate client metrics",
        "",
        "Throughput is summed across replicas (see METRICS.md).",
        "",
        f"- **Sum of achieved throughput:** {agg.total_achieved_rps:.6g} RPS",
        f"- **Sum of attempted throughput:** {agg.total_attempted_rps:.6g} RPS",
        f"- **Total completed requests:** {agg.total_requests}",
        f"- **Total failed requests:** {agg.total_failed}",
        f"- **Aggregate error rate (failed / total):** {agg.aggregate_error_rate:.6g}",
        "",
        "## Latency (descriptive across replicas)",
        "",
        "Median of per-replica percentiles from `summary.json` (not a merged global histogram):",
        "",
        f"- **Median of replica p50:** {agg.median_p50_ms} ms",
        f"- **Median of replica p95:** {agg.median_p95_ms} ms",
        f"- **Median of replica p99:** {agg.median_p99_ms} ms",
        f"- **Median of replica p999:** {agg.median_p999_ms} ms",
        "",
        "## Generated artifacts",
        "",
    ]
    out_dir = out.parent
    for label, p in sorted(artifact_paths.items(), key=lambda x: x[0]):
        try:
            rel = p.relative_to(out_dir)
        except ValueError:
            rel = p
        lines.append(f"- **{label}:** `{rel}`")

    lines.extend(
        [
            "",
            "## HDR / histogram status",
            "",
            hdr_status_note(len(bundle.hdr_paths)),
            "",
            CAVEATS_MARKDOWN.strip(),
            "",
        ]
    )

    if bundle.report_md:
        lines.extend(
            [
                "## Harness report (reference)",
                "",
                f"Original `report.md` is at `{bundle.report_md.relative_to(bundle.run_dir)}`.",
                "",
            ]
        )

    out.write_text("\n".join(lines), encoding="utf-8")

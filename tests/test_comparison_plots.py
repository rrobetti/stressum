from __future__ import annotations

from stressum.comparison_plots import (
    _group_scenarios_by_technology,
    _short_bar_labels,
    _technology_from_label,
)


def test_technology_from_label_extracts_prefix_before_last_token() -> None:
    assert _technology_from_label("Hikari A") == "Hikari"
    assert _technology_from_label("pgBouncer T") == "pgBouncer"
    assert _technology_from_label("OJP Z") == "OJP"


def test_technology_from_label_uses_whole_label_without_space() -> None:
    assert _technology_from_label("cmp-a") == "cmp-a"
    assert _technology_from_label("B") == "B"


def test_short_bar_labels_strips_shared_technology_prefix() -> None:
    labels = ["OJP A", "OJP B", "OJP C"]
    assert _short_bar_labels(labels, "OJP") == ["A", "B", "C"]


def test_short_bar_labels_keeps_labels_when_prefix_does_not_match() -> None:
    assert _short_bar_labels(["cmp-a"], "cmp-a") == ["cmp-a"]
    assert _short_bar_labels(["B"], "B") == ["B"]


def test_group_scenarios_by_technology_preserves_first_seen_order() -> None:
    scenarios = [
        {"label": "Hikari A"},
        {"label": "OJP A"},
        {"label": "Hikari B"},
        {"label": "pgBouncer A"},
        {"label": "OJP B"},
    ]
    grouped = _group_scenarios_by_technology(scenarios)
    assert [technology for technology, _ in grouped] == ["Hikari", "OJP", "pgBouncer"]
    assert [s["label"] for s in grouped[0][1]] == ["Hikari A", "Hikari B"]
    assert [s["label"] for s in grouped[1][1]] == ["OJP A", "OJP B"]
    assert [s["label"] for s in grouped[2][1]] == ["pgBouncer A"]

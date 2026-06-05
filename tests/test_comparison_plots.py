from __future__ import annotations

from stressum.comparison_plots import (
    _cross_technology_plot_context,
    _group_scenarios_by_load_point,
    _group_scenarios_by_technology,
    _load_point_from_label,
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


def test_load_point_from_label_strips_technology_prefix() -> None:
    assert _load_point_from_label("Hikari A") == "A"
    assert _load_point_from_label("pgBouncer T") == "T"
    assert _load_point_from_label("cmp-a") == "cmp-a"


def test_group_scenarios_by_load_point_preserves_first_seen_order() -> None:
    scenarios = [
        {"label": "Hikari A"},
        {"label": "OJP A"},
        {"label": "Hikari B"},
        {"label": "pgBouncer A"},
    ]
    grouped = _group_scenarios_by_load_point(scenarios)
    assert [load_point for load_point, _ in grouped] == ["A", "B"]
    assert [s["label"] for s in grouped[0][1]] == ["Hikari A", "OJP A", "pgBouncer A"]
    assert [s["label"] for s in grouped[1][1]] == ["Hikari B"]


def test_cross_technology_plot_context_requires_shared_load_points() -> None:
    scenarios = [{"label": "Hikari A"}, {"label": "OJP A"}, {"label": "Hikari B"}]
    technologies, shared_load_points, lookup = _cross_technology_plot_context(scenarios)
    assert technologies == ["Hikari", "OJP"]
    assert shared_load_points == ["A"]
    assert lookup is not None
    assert lookup[("A", "Hikari")]["label"] == "Hikari A"
    assert lookup[("A", "OJP")]["label"] == "OJP A"
    assert ("B", "OJP") not in lookup

    single_tech = [{"label": "Hikari A"}, {"label": "Hikari B"}]
    _, _, missing = _cross_technology_plot_context(single_tech)
    assert missing is None

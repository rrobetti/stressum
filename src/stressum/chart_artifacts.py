from __future__ import annotations

from collections.abc import Iterable
from datetime import datetime
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import numpy as np


def companion_markdown_path(chart_path: Path) -> Path:
    return chart_path.with_suffix(".md")


def register_chart_artifacts(paths: dict[str, Path], out: Path, out_dir: Path) -> None:
    paths[out.relative_to(out_dir).as_posix()] = out
    md_out = companion_markdown_path(out)
    paths[md_out.relative_to(out_dir).as_posix()] = md_out


def save_chart_artifacts(fig: Any, out: Path) -> None:
    fig.tight_layout()
    fig.savefig(out, format="png")
    companion_markdown_path(out).write_text(_chart_markdown(fig, out), encoding="utf-8")
    plt.close(fig)


def _chart_markdown(fig: Any, out: Path) -> str:
    lines = [
        f"# {out.name}",
        "",
        "Numbers used in the chart.",
        "",
    ]
    for axis_index, ax in enumerate(fig.axes, start=1):
        lines.extend(_axis_markdown(ax, axis_index))
    return "\n".join(lines) + "\n"


def _axis_markdown(ax: Any, axis_index: int) -> list[str]:
    lines = [f"## Axis {axis_index}", ""]
    title = ax.get_title()
    if title:
        lines.extend([f"- title: {title}", ""])
    xlabel = ax.get_xlabel()
    if xlabel:
        lines.extend([f"- x_label: {xlabel}", ""])
    ylabel = ax.get_ylabel()
    if ylabel:
        lines.extend([f"- y_label: {ylabel}", ""])

    xticks = _tick_rows(ax.get_xticks(), ax.get_xticklabels())
    if xticks:
        lines.extend(["### X ticks", "", _markdown_table(xticks), ""])

    yticks = _tick_rows(ax.get_yticks(), ax.get_yticklabels())
    if yticks:
        lines.extend(["### Y ticks", "", _markdown_table(yticks), ""])

    for line_index, line in enumerate(ax.get_lines(), start=1):
        rows = [
            {"x": x_value, "y": y_value}
            for x_value, y_value in zip(line.get_xdata(), line.get_ydata(), strict=True)
        ]
        lines.extend(
            [
                f"### Line {line_index}: {_artist_label(line)}",
                "",
                _markdown_table(rows),
                "",
            ]
        )

    patch_rows = []
    for patch_index, patch in enumerate(ax.patches, start=1):
        patch_rows.append(
            {
                "patch": patch_index,
                "label": _artist_label(patch),
                "x": patch.get_x(),
                "y": patch.get_y(),
                "width": patch.get_width(),
                "height": patch.get_height(),
            }
        )
    if patch_rows:
        lines.extend(["### Patches", "", _markdown_table(patch_rows), ""])

    for collection_index, collection in enumerate(ax.collections, start=1):
        offsets = _finite_rows(
            [
                {"x": x_value, "y": y_value}
                for x_value, y_value in np.asarray(collection.get_offsets()).tolist()
            ]
        )
        if offsets:
            lines.extend(
                [
                    f"### Collection {collection_index} offsets: {_artist_label(collection)}",
                    "",
                    _markdown_table(offsets),
                    "",
                ]
            )
        path_rows = _collection_path_rows(collection)
        if path_rows:
            lines.extend(
                [
                    f"### Collection {collection_index} paths: {_artist_label(collection)}",
                    "",
                    _markdown_table(path_rows),
                    "",
                ]
            )

    image_rows = _image_rows(ax)
    if image_rows:
        lines.extend(["### Images", "", _markdown_table(image_rows), ""])

    text_rows = [
        {"text": text.get_text(), "x": text.get_position()[0], "y": text.get_position()[1]}
        for text in ax.texts
        if text.get_text()
    ]
    if text_rows:
        lines.extend(["### Text", "", _markdown_table(text_rows), ""])

    if len(lines) == 2:
        lines.extend(["_No plotted numeric data found._", ""])
    return lines


def _tick_rows(values: Iterable[Any], labels: Iterable[Any]) -> list[dict[str, Any]]:
    rows = []
    label_list = list(labels)
    value_list = list(values)
    for index, value in enumerate(value_list):
        label = label_list[index].get_text() if index < len(label_list) else ""
        if label or np.isfinite(value):
            rows.append({"value": value, "label": label})
    return rows


def _collection_path_rows(collection: Any) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for path_index, path in enumerate(collection.get_paths(), start=1):
        vertices = np.asarray(path.vertices)
        if vertices.size == 0:
            continue
        for vertex_index, (x_value, y_value) in enumerate(vertices.tolist(), start=1):
            row = {
                "path": path_index,
                "vertex": vertex_index,
                "x": x_value,
                "y": y_value,
            }
            if _row_has_finite_number(row):
                rows.append(row)
    return rows


def _image_rows(ax: Any) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for image_index, image in enumerate(ax.images, start=1):
        values = np.asarray(image.get_array())
        if values.ndim == 0:
            values = values.reshape(1, 1)
        for row_index, row_values in enumerate(values.tolist(), start=1):
            row: dict[str, Any] = {"image": image_index, "row": row_index}
            for column_index, value in enumerate(row_values, start=1):
                row[f"col_{column_index}"] = value
            if _row_has_finite_number(row):
                rows.append(row)
    return rows


def _markdown_table(rows: list[dict[str, Any]]) -> str:
    if not rows:
        return "_No data._"
    columns = list(rows[0].keys())
    header = "| " + " | ".join(columns) + " |"
    separator = "| " + " | ".join("---" for _ in columns) + " |"
    body = [
        "| " + " | ".join(_escape_markdown(_format_value(row.get(column, ""))) for column in columns) + " |"
        for row in rows
    ]
    return "\n".join([header, separator, *body])


def _finite_rows(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [row for row in rows if _row_has_finite_number(row)]


def _row_has_finite_number(row: dict[str, Any]) -> bool:
    for value in row.values():
        if isinstance(value, (int, np.integer)):
            return True
        if isinstance(value, (float, np.floating)) and np.isfinite(value):
            return True
    return False


def _artist_label(artist: Any) -> str:
    label = artist.get_label()
    if not label or label.startswith("_"):
        return "unlabeled"
    return label


def _format_value(value: Any) -> str:
    if isinstance(value, (np.floating, float)):
        if not np.isfinite(value):
            return ""
        return f"{float(value):.12g}"
    if isinstance(value, (np.integer, int)):
        return str(int(value))
    if isinstance(value, datetime):
        return value.isoformat()
    if hasattr(value, "isoformat"):
        try:
            return value.isoformat()
        except TypeError:
            pass
    if isinstance(value, str):
        return value
    return str(value)


def _escape_markdown(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>")

"""Animated statistics section."""

from components.utils import render_card_rows, section_header
from data.profile import STATS


def _stat_card(stat: dict, index: int) -> str:
    icon = stat.get("icon", "📊")
    label = stat["label"]
    delay = index * 0.08

    if stat.get("value") is not None:
        suffix = stat.get("suffix", "")
        value_html = f'<div class="stat-value">{stat["value"]}{suffix}</div>'
    else:
        text = stat.get("text", label)
        value_html = f'<div class="stat-value stat-value-text">{text}</div>'

    return (
        f'<div class="stat-card reveal-card" style="animation-delay:{delay}s">'
        f'<div class="stat-icon">{icon}</div>{value_html}'
        f'<div class="stat-label">{label}</div></div>'
    )


def render_stats() -> None:
    """Render statistics cards."""
    section_header(
        "Impact at a Glance",
        "Delivering measurable results across software, AI, and data science",
        badge="By the Numbers",
    )
    render_card_rows(STATS, _stat_card, columns=3)

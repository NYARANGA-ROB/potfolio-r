"""Shared utilities for portfolio components."""

import base64
import re
from pathlib import Path

import streamlit as st

ASSETS_DIR = Path(__file__).resolve().parent.parent / "assets"
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
STYLES_PATH = ASSETS_DIR / "styles.css"

PROFILE_IMAGE_CANDIDATES = [
    DATA_DIR / "profile.png",
    DATA_DIR / "profile.jpg",
    DATA_DIR / "profile.jpeg",
    DATA_DIR / "profile.webp",
    ASSETS_DIR / "images" / "profile.png",
    ASSETS_DIR / "images" / "profile.jpg",
    ASSETS_DIR / "images" / "profile_placeholder.svg",
]

MIME_TYPES = {
    ".png": "image/png",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".webp": "image/webp",
    ".svg": "image/svg+xml",
}


def init_session_state() -> None:
    """Initialize session state defaults."""
    defaults = {
        "theme": "dark",
        "page_loaded": False,
        "active_section": "home",
        "search_query": "",
        "project_filter": "All",
        "contact_submitted": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def load_css(theme: str = "dark") -> None:
    """Inject custom CSS with theme variables."""
    css = STYLES_PATH.read_text(encoding="utf-8")
    theme_class = "theme-dark" if theme == "dark" else "theme-light"
    st.markdown(
        f'<style>{css}</style>'
        f'<script>document.documentElement.className="{theme_class}";</script>',
        unsafe_allow_html=True,
    )


def get_profile_image_path() -> Path | None:
    """Return the first available profile image path."""
    for path in PROFILE_IMAGE_CANDIDATES:
        if path.exists():
            return path
    return None


def render_html(html: str) -> None:
    """Render HTML safely — single-line to avoid Streamlit markdown code-block escaping."""
    cleaned = re.sub(r">\s+<", "><", html.strip())
    cleaned = re.sub(r"\s+", " ", cleaned)
    st.markdown(cleaned, unsafe_allow_html=True)


def section_anchor(section_id: str) -> None:
    """Create an invisible anchor for navigation."""
    render_html(f'<div id="{section_id}" class="section-anchor"></div>')


def section_header(title: str, subtitle: str = "", badge: str = "", alt: bool = False) -> None:
    """Render a self-contained section header."""
    badge_html = f'<span class="section-badge">{badge}</span>' if badge else ""
    subtitle_html = f'<p class="section-subtitle">{subtitle}</p>' if subtitle else ""
    wrap_class = "section-header-wrap section-alt" if alt else "section-header-wrap"
    render_html(
        f'<div class="{wrap_class}"><div class="section-header">{badge_html}'
        f'<h2 class="section-title">{title}</h2>{subtitle_html}</div></div>'
    )


def render_card_rows(items: list, render_card, columns: int = 2) -> None:
    """Render items as HTML cards in a responsive column grid."""
    for row_start in range(0, len(items), columns):
        row_items = items[row_start: row_start + columns]
        cols = st.columns(columns)
        for col_idx, col in enumerate(cols):
            if col_idx >= len(row_items):
                break
            index = row_start + col_idx
            with col:
                render_html(render_card(row_items[col_idx], index))


def render_stars(rating: int) -> str:
    """Return star rating HTML."""
    return "★" * rating + "☆" * (5 - rating)

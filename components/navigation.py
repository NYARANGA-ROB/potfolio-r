"""Floating navigation and sticky CTA."""

import streamlit as st

from components.utils import render_html

NAV_ITEMS = [
    ("home", "Home"),
    ("solutions", "Solutions"),
    ("case-studies", "Cases"),
    ("services", "Services"),
    ("stack", "Stack"),
    ("about", "About"),
    ("contact", "Contact"),
]


def render_navigation() -> None:
    """Render floating navigation bar with HTML links."""
    links_html = "".join(
        f'<a href="#{anchor}" class="nav-link">{label}</a>'
        for anchor, label in NAV_ITEMS
    )
    render_html(
        f'<nav class="floating-nav" aria-label="Main navigation">'
        f'<a href="#home" class="nav-logo"><span class="nav-logo-full">Robert Nyaranga</span>'
        f'<span class="nav-logo-short">RN</span></a>'
        f'<div class="nav-links">{links_html}</div>'
        f'<a href="#contact" class="nav-cta">Hire Me</a>'
        f'</nav>'
    )

    theme_icon = "☀️" if st.session_state.theme == "dark" else "🌙"
    if st.button(theme_icon, key="theme_toggle_btn", help="Toggle light/dark mode"):
        st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"
        st.rerun()


def render_sticky_cta() -> None:
    """Render sticky consultation CTA button."""
    render_html('<div class="sticky-cta"><a href="#contact">Book a Consultation →</a></div>')

"""Interactive technology stack matrix."""

import plotly.graph_objects as go
import streamlit as st

from components.utils import render_html, section_anchor, section_header
from data.tech_stack import TECH_STACK


def _render_progress_bars() -> None:
    cols = st.columns(2)
    categories = list(TECH_STACK.keys())
    for i, category in enumerate(categories):
        with cols[i % 2]:
            items_html = "".join(
                f'<div class="tech-item"><span class="tech-icon">{tech["icon"]}</span>'
                f'<span class="tech-name">{tech["name"]}</span>'
                f'<div class="tech-bar-track"><div class="tech-bar-fill" style="width:{tech["level"]}%"></div></div>'
                f'<span class="tech-level">{tech["level"]}%</span></div>'
                for tech in TECH_STACK[category]
            )
            render_html(
                f'<div class="tech-category reveal-card">'
                f'<div class="tech-category-title">{category}</div>{items_html}</div>'
            )


def _render_radar_chart(theme: str) -> None:
    categories = list(TECH_STACK.keys())
    averages = [sum(t["level"] for t in TECH_STACK[cat]) / len(TECH_STACK[cat]) for cat in categories]
    text_color = "#fafafa" if theme == "dark" else "#09090b"
    grid_color = "rgba(255,255,255,0.1)" if theme == "dark" else "rgba(0,0,0,0.08)"

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=averages + [averages[0]],
        theta=categories + [categories[0]],
        fill="toself",
        fillcolor="rgba(99, 102, 241, 0.18)",
        line=dict(color="#6366f1", width=2),
        marker=dict(size=7, color="#8b5cf6"),
        name="Proficiency",
    ))
    fig.update_layout(
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(visible=True, range=[0, 100], gridcolor=grid_color, tickfont=dict(color="#a1a1aa", size=10)),
            angularaxis=dict(gridcolor=grid_color, tickfont=dict(color=text_color, size=11)),
        ),
        showlegend=False,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        margin=dict(l=50, r=50, t=30, b=30),
        height=420,
    )
    st.plotly_chart(fig, width="stretch", config={"displayModeBar": False})


def render_tech_stack() -> None:
    section_anchor("stack")
    section_header(
        "Technology Stack",
        "A comprehensive toolkit for building modern, intelligent applications",
        badge="Skills Matrix",
        alt=True,
    )
    tab_bars, tab_chart = st.tabs(["📊 Progress Matrix", "🎯 Skills Radar"])
    with tab_bars:
        _render_progress_bars()
    with tab_chart:
        _render_radar_chart(st.session_state.get("theme", "dark"))

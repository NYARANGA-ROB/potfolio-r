"""Featured solutions / projects section."""

import streamlit as st

from components.utils import render_card_rows, render_html, section_anchor, section_header
from data.projects import PROJECTS


def _filter_projects(query: str, category: str) -> list:
    filtered = PROJECTS
    if category and category != "All":
        filtered = [p for p in filtered if p["category"] == category]
    if query:
        q = query.lower()
        filtered = [
            p for p in filtered
            if q in p["name"].lower()
            or q in p["description"].lower()
            or any(q in f.lower() for f in p["features"])
            or any(q in t.lower() for t in p["tags"])
        ]
    return filtered


def _project_card(project: dict, index: int) -> str:
    features_html = "".join(f'<span class="feature-tag">{f}</span>' for f in project["features"][:5])
    tags_html = "".join(f'<span class="tech-tag">{t}</span>' for t in project["tags"])
    return (
        f'<div class="project-card reveal-card">'
        f'<div class="project-screenshot" style="background:{project["gradient"]}">'
        f'<span class="project-icon">{project["icon"]}</span>'
        f'<span class="project-mockup-label">Product Preview</span></div>'
        f'<div class="project-body"><div class="project-category">{project["category"]}</div>'
        f'<h3 class="project-name">{project["name"]}</h3>'
        f'<p class="project-description">{project["description"]}</p>'
        f'<div class="project-features">{features_html}</div>'
        f'<div class="project-impact"><strong>Impact:</strong> {project["impact"]}</div>'
        f'<div class="project-tags">{tags_html}</div></div></div>'
    )


def render_projects() -> None:
    section_anchor("solutions")
    section_header(
        "Featured Solutions",
        "Production-ready platforms built for schools, agriculture, enterprises, and NGOs",
        badge="Portfolio",
        alt=True,
    )

    categories = ["All"] + sorted({p["category"] for p in PROJECTS})
    col_search, col_filter = st.columns([3, 1])
    with col_search:
        query = st.text_input("Search", placeholder="🔍  Search by name, feature, or technology...", key="project_search", label_visibility="collapsed")
    with col_filter:
        category = st.selectbox("Category", categories, key="project_category_filter", label_visibility="collapsed")

    projects = _filter_projects(query, category)
    if not projects:
        render_html('<p class="empty-state">No projects match your search. Try different keywords or filters.</p>')
    else:
        render_card_rows(projects, _project_card, columns=2)

"""Case studies section with expandable cards."""

import streamlit as st

from components.utils import render_html, section_anchor, section_header
from data.projects import CASE_STUDIES


def render_case_studies() -> None:
    section_anchor("case-studies")
    section_header(
        "Case Studies",
        "Real problems solved with technology — measurable outcomes delivered",
        badge="Results",
        alt=True,
    )

    for case in CASE_STUDIES:
        results_html = "".join(f"<li>{r}</li>" for r in case["results"])
        tech_html = "".join(f'<span class="tech-tag">{t}</span>' for t in case["technologies"])

        with st.expander(f"**{case['title']}** — view problem, solution & results"):
            render_html(
                f'<div class="case-study-inner"><div class="case-columns">'
                f'<div class="case-col"><div class="case-preview" style="background:{case["gradient"]}">'
                f'<span>Case Study Preview</span></div>'
                f'<div class="case-section-label">Problem</div><p class="case-text">{case["problem"]}</p>'
                f'<div class="case-section-label">Solution</div><p class="case-text">{case["solution"]}</p></div>'
                f'<div class="case-col"><div class="case-section-label">Technologies Used</div>'
                f'<div class="case-tech-tags">{tech_html}</div>'
                f'<div class="case-section-label">Results</div><ul class="case-results">{results_html}</ul>'
                f'<div class="case-preview case-preview-sm" style="background:{case["gradient"]}">'
                f'<span>Screenshot Placeholder</span></div></div></div></div>'
            )

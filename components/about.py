"""About section with timeline."""

import streamlit as st

from components.utils import render_html, section_anchor, section_header
from data.profile import PROFILE, TIMELINE


def render_about() -> None:
    section_anchor("about")
    section_header(
        "About Me",
        "Engineering intelligent solutions at the intersection of software, AI, and data",
        badge="My Story",
    )

    col_story, col_timeline = st.columns(2, gap="large")

    with col_story:
        st.markdown(PROFILE["bio"])
        st.markdown(
            "With expertise spanning full-stack development, machine learning, and "
            "business intelligence, I partner with organizations to transform complex "
            "challenges into elegant, scalable solutions."
        )
        st.markdown(
            "My passion lies in solving real-world problems — whether it's automating "
            "school administration, empowering farmers with AI insights, or building "
            "data platforms that drive executive decisions."
        )
        render_html(
            '<div class="about-highlights">'
            '<div class="highlight-item"><div class="highlight-icon">💻</div><div class="highlight-label">Software Engineering</div></div>'
            '<div class="highlight-item"><div class="highlight-icon">📊</div><div class="highlight-label">Data Science</div></div>'
            '<div class="highlight-item"><div class="highlight-icon">🧠</div><div class="highlight-label">AI / ML Specialist</div></div>'
            '<div class="highlight-item"><div class="highlight-icon">🌍</div><div class="highlight-label">Real-World Impact</div></div>'
            '</div>'
        )

    with col_timeline:
        timeline_html = "".join(
            f'<div class="timeline-item" style="animation-delay:{i * 0.1}s">'
            f'<div class="timeline-dot"></div>'
            f'<div class="timeline-year">{item["year"]}</div>'
            f'<h4 class="timeline-title">{item["title"]}</h4>'
            f'<p class="timeline-desc">{item["description"]}</p></div>'
            for i, item in enumerate(TIMELINE)
        )
        render_html(f'<div class="timeline">{timeline_html}</div>')

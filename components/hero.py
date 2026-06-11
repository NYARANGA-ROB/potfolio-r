"""Hero section component."""

import streamlit as st

from components.utils import get_profile_image_path, render_html, section_anchor
from data.profile import PROFILE, SKILLS


def render_hero() -> None:
    """Render the hero landing section."""
    section_anchor("home")
    skills_html = "".join(f'<span class="skill-pill">{skill}</span>' for skill in SKILLS[:10])

    render_html(
        '<div class="hero-bg-layer">'
        '<div class="hero-orb hero-orb-1"></div>'
        '<div class="hero-orb hero-orb-2"></div>'
        '<div class="hero-orb hero-orb-3"></div>'
        '<div class="hero-grid"></div>'
        '</div>'
    )

    col_text, col_profile = st.columns([1.2, 1], gap="large")

    with col_text:
        render_html(
            f'<div class="hero-text">'
            f'<div class="hero-badge"><span class="hero-badge-dot"></span>Available for remote opportunities</div>'
            f'<h1 class="hero-headline">Building <span class="gradient-text">Intelligent Systems</span> That Solve Real Business Problems</h1>'
            f'<p class="hero-subtitle">{PROFILE["subtitle"]}</p>'
            f'<div class="hero-cta-buttons">'
            f'<a href="#solutions" class="cta-btn cta-primary">View My Work</a>'
            f'<a href="#contact" class="cta-btn cta-secondary">Book a Consultation</a>'
            f'<a href="mailto:{PROFILE["email"]}?subject=Resume%20Request" class="cta-btn cta-secondary">Download Resume</a>'
            f'<a href="{PROFILE["linkedin"]}" target="_blank" rel="noopener" class="cta-btn cta-ghost">LinkedIn →</a>'
            f'</div>'
            f'<div class="hero-skills">{skills_html}</div>'
            f'</div>'
        )

    with col_profile:
        profile_path = get_profile_image_path()
        if profile_path:
            st.image(str(profile_path), width=280)
        render_html(
            f'<div class="hero-profile">'
            f'<div class="profile-name-tag"><h3>{PROFILE["name"]}</h3><p>{PROFILE["title"]}</p></div>'
            f'<div class="profile-stats-mini">'
            f'<div><strong>5+</strong><span>Years</span></div>'
            f'<div><strong>20+</strong><span>Projects</span></div>'
            f'<div><strong>AI</strong><span>Specialist</span></div>'
            f'</div></div>'
        )

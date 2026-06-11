"""
Robert Nyaranga — Premium Portfolio
Software Engineer | AI Engineer | Data Scientist
"""

import streamlit as st

from components.about import render_about
from components.blog import render_blog
from components.case_studies import render_case_studies
from components.contact import render_contact
from components.footer import render_footer
from components.hero import render_hero
from components.navigation import render_navigation, render_sticky_cta
from components.projects import render_projects
from components.services import render_services
from components.stats import render_stats
from components.tech_stack import render_tech_stack
from components.testimonials import render_testimonials
from components.utils import init_session_state, load_css
from data.profile import PROFILE

st.set_page_config(
    page_title=f"{PROFILE['name']} | Software Engineer & AI Specialist",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed",
)

init_session_state()
load_css(st.session_state.theme)

st.markdown(
    """
    <meta name="description" content="Robert Nyaranga — Software Engineer, AI Engineer, and Data Scientist building intelligent systems, ML solutions, and data-driven platforms.">
    <meta name="keywords" content="Robert Nyaranga, Software Engineer, AI Engineer, Data Scientist, Machine Learning, Portfolio">
    <meta name="author" content="Robert Nyaranga">
    <meta property="og:title" content="Robert Nyaranga | Building Intelligent Systems">
    <meta property="og:description" content="Scalable software platforms, AI solutions, and data-driven applications.">
    <meta property="og:type" content="website">
    <meta name="twitter:card" content="summary_large_image">
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            document.querySelectorAll('a[href^="#"]').forEach(anchor => {
                anchor.addEventListener('click', function(e) {
                    const href = this.getAttribute('href');
                    if (!href || href === '#') return;
                    const target = document.querySelector(href);
                    if (target) {
                        e.preventDefault();
                        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    }
                });
            });

        });
    </script>
    """,
    unsafe_allow_html=True,
)

render_navigation()
render_sticky_cta()

render_hero()
render_stats()
render_projects()
render_case_studies()
render_services()
render_tech_stack()
render_testimonials()
render_blog()
render_about()
render_contact()
render_footer()

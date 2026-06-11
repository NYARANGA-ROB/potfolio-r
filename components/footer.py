"""Portfolio footer."""

from components.utils import render_html
from data.profile import PROFILE


def render_footer() -> None:
    render_html(
        f'<footer class="portfolio-footer">'
        f'<p class="footer-text">© 2025 {PROFILE["name"]} · {PROFILE["title"]}</p>'
        f'<div class="footer-links">'
        f'<a href="#home">Home</a><a href="#solutions">Solutions</a><a href="#contact">Contact</a>'
        f'<a href="{PROFILE["linkedin"]}" target="_blank" rel="noopener">LinkedIn</a>'
        f'<a href="mailto:{PROFILE["email"]}">Email</a>'
        f'</div>'
        f'<p class="footer-text footer-note">Built with Streamlit · Designed for impact</p>'
        f'</footer>'
    )

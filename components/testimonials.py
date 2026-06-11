"""Testimonials section."""

from components.utils import render_card_rows, render_stars, section_header
from data.testimonials import TESTIMONIALS


def _testimonial_card(testimonial: dict, index: int) -> str:
    initials = "".join(word[0] for word in testimonial["name"].split()[:2])
    stars = render_stars(testimonial["rating"])
    return f"""<div class="testimonial-card reveal-card" style="transition-delay: {index * 0.08}s"><div class="testimonial-stars">{stars}</div><p class="testimonial-quote">"{testimonial['quote']}"</p><div class="testimonial-author"><div class="testimonial-avatar">{initials}</div><div><div class="testimonial-name">{testimonial['name']}</div><div class="testimonial-role">{testimonial['role']}, {testimonial['organization']}</div></div></div></div>"""


def render_testimonials() -> None:
    """Render client testimonial cards."""
    section_header(
        "What Clients Say",
        "Trusted by school administrators, business leaders, and NGO directors",
        badge="Testimonials",
    )
    render_card_rows(TESTIMONIALS, _testimonial_card, columns=2)

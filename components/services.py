"""Services section."""

from components.utils import render_card_rows, section_anchor, section_header
from data.services import SERVICES


def _service_card(service: dict, index: int) -> str:
    items_html = "".join(f"<li>{item}</li>" for item in service["items"])
    return f"""<div class="service-card reveal-card" style="transition-delay: {index * 0.08}s"><div class="service-icon" style="background: {service['gradient']}">{service['icon']}</div><h3 class="service-category">{service['category']}</h3><ul class="service-items">{items_html}</ul></div>"""


def render_services() -> None:
    """Render service offering cards."""
    section_anchor("services")
    section_header(
        "Services",
        "End-to-end technology solutions tailored to your organization's needs",
        badge="What I Offer",
    )
    render_card_rows(SERVICES, _service_card, columns=2)

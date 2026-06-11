"""Contact section with form validation."""

import re

import streamlit as st

from components.utils import render_html, section_anchor, section_header
from data.profile import PROFILE


def _validate_email(email: str) -> bool:
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.match(pattern, email))


def render_contact() -> None:
    section_anchor("contact")
    section_header(
        "Let's Build Something Great",
        "Ready to transform your ideas into intelligent solutions? Get in touch.",
        badge="Contact",
    )

    col_info, col_form = st.columns([1, 1.15], gap="large")

    with col_info:
        st.markdown("### Get in Touch")
        st.markdown("Open to remote roles, consulting, and project collaborations worldwide.")
        st.markdown(f"**Email:** [{PROFILE['email']}](mailto:{PROFILE['email']})")
        st.markdown(f"**LinkedIn:** [Robert Nyaranga]({PROFILE['linkedin']})")
        st.markdown("**Availability:** Remote · Full-time & Contract")
        st.markdown("**Response Time:** Within 24 hours")
        st.link_button("Schedule Meeting", f"mailto:{PROFILE['email']}?subject=Meeting%20Request", width="stretch")
        st.link_button("Send Email", f"mailto:{PROFILE['email']}", width="stretch")
        st.link_button("Connect on LinkedIn", PROFILE["linkedin"], width="stretch")

    with col_form:
        st.markdown("### Send a Message")
        with st.form("contact_form", clear_on_submit=True):
            c1, c2 = st.columns(2)
            with c1:
                name = st.text_input("Full Name *", placeholder="Your name")
            with c2:
                email = st.text_input("Email Address *", placeholder="you@company.com")
            organization = st.text_input("Organization", placeholder="Company or institution")
            subject = st.selectbox(
                "How can I help?",
                ["Software Development Project", "AI / ML Solution", "Data Science & Analytics", "Consulting & Strategy", "Other"],
            )
            message = st.text_area("Message *", placeholder="Tell me about your project or challenge...", height=140)
            submitted = st.form_submit_button("Send Message →", type="primary", use_container_width=True)

            if submitted:
                errors = []
                if not name.strip():
                    errors.append("Name is required.")
                if not email.strip():
                    errors.append("Email is required.")
                elif not _validate_email(email):
                    errors.append("Please enter a valid email address.")
                if not message.strip():
                    errors.append("Message is required.")
                elif len(message.strip()) < 20:
                    errors.append("Message must be at least 20 characters.")
                if errors:
                    for error in errors:
                        st.error(error)
                else:
                    st.success(f"Thank you, {name}! Your message has been received. I'll get back to you at {email} within 24 hours.")
                    st.balloons()

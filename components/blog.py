"""Blog section with featured articles."""

from components.utils import render_card_rows, render_html, section_header
from data.blog import BLOG_POSTS


def _blog_card(post: dict, index: int) -> str:
    return f"""<div class="blog-card reveal-card" style="transition-delay: {index * 0.08}s"><div class="blog-thumbnail" style="background: {post['gradient']}">📝</div><div class="blog-body"><div class="blog-meta"><span class="blog-category">{post['category']}</span><span>{post['date']}</span><span>{post['read_time']}</span></div><h3 class="blog-title">{post['title']}</h3><p class="blog-excerpt">{post['excerpt']}</p><div class="blog-read-more">Read Article →</div></div></div>"""


def render_blog() -> None:
    """Render featured blog article cards."""
    section_header(
        "Insights & Articles",
        "Thoughts on AI, data science, and building impactful software",
        badge="Blog",
        alt=True,
    )
    render_card_rows(BLOG_POSTS, _blog_card, columns=2)
    render_html('<div class="section-end-spacer"></div>')

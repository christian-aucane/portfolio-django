from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def icon(font_awesome_icon, extra_classes=""):
    return mark_safe(f'<i class="{font_awesome_icon.css_classes} {extra_classes}" title="{font_awesome_icon.title}"></i>')


@register.simple_tag
def icon_li(font_awesome_icon, content="", extra_classes=""):
    return mark_safe(f"""
        <li>
            <i class="fa-li {font_awesome_icon.css_classes} {extra_classes}" title="{font_awesome_icon.title}"></i>
            {content}
        </li>
    """)

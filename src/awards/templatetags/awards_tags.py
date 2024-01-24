from django import template
from django.utils.translation import gettext as _

from common.templatetags.icon_tags import icon_li

register = template.Library()



@register.simple_tag
def render_award_li(award):
    font_awesome_icon = award.category.icon
    extra_classes = award.category.icon_color
    if award.file:
        content = f"""
            <a href="{award.get_file_url()}" target="_blank">
                {award.title}
            </a> - {award.text}
        """
    else:
        content = f"{award.title} - {award.text}"

    obtain_date = award.get_obtain_date()
    if obtain_date:
        content = f"{content} ({obtain_date})"
    else:
        content = f"{_('In progress')} : {content}"

    return icon_li(font_awesome_icon, content, extra_classes)
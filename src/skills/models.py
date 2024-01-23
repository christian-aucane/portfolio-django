from collections import defaultdict

from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import DisplayOrderBaseModel
from common.models import FontAwesomeIcon


class Skill(DisplayOrderBaseModel):
    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")
        unique_together = (
            ('name', 'category'),
        )

    CATEGORY_CHOICES = [
        ('language', _('Programming Languages & Tools')),
        ('framework', _('Frameworks & Libraries')),
        ('workflow', _('Workflow')),
    ]

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    category = models.CharField(
        max_length=255,
        choices=CATEGORY_CHOICES,
        verbose_name=_("Category")
    )
    icon = models.ForeignKey(FontAwesomeIcon, on_delete=models.CASCADE, verbose_name=_("Icon"))

    def __str__(self):
        return self.name

    @classmethod
    def get_skills_by_category(cls):
        skills_by_category = defaultdict(list)

        ordered_skills = cls.objects.order_by('category', 'display_order')

        for skill in ordered_skills:
            skills_by_category[skill.category].append(skill)

        return skills_by_category

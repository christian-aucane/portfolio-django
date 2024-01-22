from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import DisplayOrderBaseModel


class AwardCategory(DisplayOrderBaseModel):
    class Meta:
        verbose_name = _("Award Category")
        verbose_name_plural = _("Award Categories")

    title = models.CharField(max_length=255, unique=True, verbose_name=_("Title"))
    icon = models.CharField(max_length=255, verbose_name=_("Icon"))
    icon_color = models.CharField(max_length=255, verbose_name=_("Icon Color"))

    def __str__(self):
        return self.title


class Award(DisplayOrderBaseModel):
    class Meta:
        verbose_name = _("Award")
        verbose_name_plural = _("Awards")

    title = models.CharField(max_length=255, unique=True, verbose_name=_("Title"))
    text = models.TextField(verbose_name=_("Text"))
    file = models.FileField(upload_to="awards_files/", blank=True, null=True,
                            verbose_name=_("PDF File"))
    category = models.ForeignKey(AwardCategory, on_delete=models.CASCADE,
                                 related_name="awards", verbose_name=_("Category"))

    def __str__(self):
        return f"{self.title} ({self.category})"

    def get_file_url(self):
        return self.file.url
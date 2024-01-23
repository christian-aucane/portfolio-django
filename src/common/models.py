from django.db import models
from django.utils.translation import gettext as _

from base.models import UniqueEntryBaseModel


class SiteMetaData(UniqueEntryBaseModel):
    class Meta:
        verbose_name = _("Site Meta Data")
        verbose_name_plural = _("Site Meta Data")

    title = models.CharField(max_length=255, default=_("Default Site Title"), verbose_name=_("Site Title"))
    description = models.TextField(default=_("Default Site Description"), verbose_name=_("Site Description"))
    author = models.CharField(max_length=255, default=_("Default Author"), verbose_name=_("Author"))
    og_title = models.CharField(max_length=255, default=_("Default OG Title"), verbose_name=_("OG Title"))
    og_description = models.TextField(default=_("Default OG Description"), verbose_name=_("OG Description"))
    og_image = models.URLField(blank=True, null=True, verbose_name=_("OG Image URL"))

    def __str__(self):
        return _("Site Meta Data")


class FontAwesomeIcon(models.Model):
    class Meta:
        verbose_name = _("Font Awesome Icon")
        verbose_name_plural = _("Font Awesome Icons")

    title = models.CharField(max_length=255, unique=True, verbose_name=_("Name"))
    css_classes = models.CharField(max_length=255, verbose_name=_("Font Awesome Icon Classes"))

    def __str__(self):
        return self.title

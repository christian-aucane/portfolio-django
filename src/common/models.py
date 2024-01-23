from django.db import models
from django.utils.translation import gettext_lazy as _


class FontAwesomeIcon(models.Model):
    class Meta:
        verbose_name = _("Font Awesome Icon")
        verbose_name_plural = _("Font Awesome Icons")

    title = models.CharField(max_length=255, unique=True, verbose_name=_("Name"))
    css_classes = models.CharField(max_length=255, verbose_name=_("Font Awesome Icon Classes"))

    def __str__(self):
        return self.title

from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import DisplayOrderBaseModel


class Paragraph(DisplayOrderBaseModel):
    class Meta:
        verbose_name = _("Paragraph")
        verbose_name_plural = _("Paragraphs")

    title = models.CharField(max_length=255, unique=True)
    text = models.TextField()

    def __str__(self):
        return f"{self.title} - {_('Paragraph')} {self.display_order}"

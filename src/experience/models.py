from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import DurationBaseModel


class Experience(DurationBaseModel):
    class Meta:
        verbose_name = _("Experience")
        verbose_name_plural = _("Experiences")

    title = models.CharField(max_length=255, verbose_name=_("Title"))
    company = models.CharField(max_length=255, verbose_name=_("Company"))
    description = models.TextField(verbose_name=_("Description"))
    thumbnail = models.ImageField(upload_to='experience_thumbnails/', verbose_name=_("Thumbnail"))

    def __str__(self):
        return f"{self.title} at {self.company}"

    def get_thumbnail_url(self):
        return self.thumbnail.url

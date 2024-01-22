from django.db import models
from django.utils.translation import gettext_lazy as _


class Experience(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    company = models.CharField(max_length=255, verbose_name=_("Company"))
    description = models.TextField(verbose_name=_("Description"))
    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"), null=True, blank=True)
    thumbnail = models.ImageField(upload_to='experience_images/', verbose_name=_("Image"))

    def __str__(self):
        return f"{self.title} at {self.company}"

    def get_thumbnail_url(self):
        return self.thumbnail.url

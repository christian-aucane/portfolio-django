from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import DurationBaseModel


class Education(DurationBaseModel):
    class Meta:
        verbose_name = _("Education")
        verbose_name_plural = _("Educations")

    school_name = models.CharField(max_length=255, verbose_name=_("School Name"))
    program = models.CharField(max_length=255, verbose_name=_("Program"))
    role = models.CharField(max_length=255, verbose_name=_("Role"))
    description = models.TextField(verbose_name=_("Description"))
    thumbnail = models.ImageField(upload_to='education_images/', verbose_name=_("Thumbnail"))

    def __str__(self):
        return f"{self.school_name} - {self.program}"

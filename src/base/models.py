from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class DisplayOrderBaseModel(models.Model):
    display_order = models.PositiveIntegerField(default=1, verbose_name=_("Display Order"))

    class Meta:
        abstract = True
        ordering = ['display_order']

    def save(self, *args, **kwargs):
        # Ensures that there is only one entry in the table
        model_class = self.__class__
        if model_class.objects.exists() and not self.pk:
            self.display_order = model_class.objects.last().display_order + 1
        return super().save(*args, **kwargs)


class DurationBaseModel(models.Model):
    class Meta:
        abstract = True
        ordering = ['-start_date']

    start_date = models.DateField(verbose_name=_("Start Date"))
    end_date = models.DateField(verbose_name=_("End Date"), null=True, blank=True)

    def get_duration(self):
        start_date = self.start_date.strftime('%b %Y')
        end_date = self.end_date.strftime('%b %Y') if self.end_date else _('Present')
        return f"{start_date} - {end_date}"


class UniqueEntryBaseModel(models.Model):
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        # Ensures that there is only one entry in the table
        model_class = self.__class__
        if model_class.objects.exists() and not self.pk:
            raise ValidationError(_(f"There can only be one entry in the {model_class.__name__} table."))
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise ValidationError(_(f"Deleting the {self.__class__.__name__} object is prohibited."))

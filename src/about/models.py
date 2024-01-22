from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _


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
        super().save(*args, **kwargs)


class AboutInfo(models.Model):
    class Meta:
        verbose_name = _("About me")
        verbose_name_plural = _("About me")
        ordering = ['id']

    first_name = models.CharField(max_length=255, default=_("Your first name"), verbose_name=_("First Name"))
    last_name = models.CharField(max_length=255, default=_("Your last name"), verbose_name=_("Last Name"))
    description = models.TextField(default=_("Your description"), verbose_name=_("Description"))

    def __str__(self):
        return _("About me")

    def save(self, *args, **kwargs):
        # Ensures that there is only one entry in the table
        model_class = self.__class__
        if model_class.objects.exists() and not self.pk:
            raise ValidationError(_(f"There can only be one entry in the {model_class.__name__} table."))
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        raise ValidationError(_(f"Deleting the {self.__class__.__name__} object is prohibited."))


class AboutSkill(DisplayOrderBaseModel):
    about = models.ForeignKey(AboutInfo, on_delete=models.CASCADE, default=1, verbose_name=_("About me"))
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Name"))

    def __str__(self):
        return self.name


class SocialLink(DisplayOrderBaseModel):
    about = models.ForeignKey(AboutInfo, on_delete=models.CASCADE, default=1, verbose_name=_("About me"))
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Name"))
    url = models.URLField(verbose_name=_("URL"))
    icon_classes = models.CharField(max_length=255, verbose_name=_("Font Awesome Icon Classes"))

    def __str__(self):
        return self.name

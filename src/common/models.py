from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _

from base.models import UniqueEntryBaseModel, DisplayOrderBaseModel


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


class FooterCredits(DisplayOrderBaseModel):
    class Meta(DisplayOrderBaseModel.Meta):
        verbose_name = _("Footer Credit")
        verbose_name_plural = _("Footer Credits")

    site_meta_data = models.ForeignKey(SiteMetaData, on_delete=models.CASCADE, default=1,
                                       related_name='credits', verbose_name=_("Site Meta Data"))
    title = models.CharField(max_length=255, verbose_name=_("Name"), unique=True)
    html = models.TextField(verbose_name=_("HTML"), help_text=_("HTML for the credits"))

    def __str__(self):
        if self.id == 1:
            return _("Template Credits (Read Only)")
        return self.title

    def save(self, *args, **kwargs):
        if self.id == 1:
            original_instance = FooterCredits.objects.get(pk=self.pk)
            if original_instance.title != self.title:
                self.title = original_instance.title
            if original_instance.html != self.html:
                self.html = original_instance.html

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.id == 1:
            raise ValidationError(_("Template Credits cannot be deleted."))
        super().delete(*args, **kwargs)


class Favicon(UniqueEntryBaseModel):
    class Meta:
        verbose_name = _("Favicon")
        verbose_name_plural = _("Favicons")

    site_meta_data = models.OneToOneField(SiteMetaData, on_delete=models.CASCADE, default=1,
                                          related_name='favicon', verbose_name=_("Site Meta Data"))
    image = models.ImageField(upload_to='favicon/', blank=True, null=True, verbose_name=_("Image"))
    credits_html = models.TextField(blank=True, null=True,
                                    verbose_name=_("Credits HTML"),
                                    help_text=_("HTML for the credits"))

    def __str__(self):
        return _("Favicon")

    def get_url(self):
        return self.image.url if self.image else ""


class FontAwesomeIcon(models.Model):
    class Meta:
        verbose_name = _("Font Awesome Icon")
        verbose_name_plural = _("Font Awesome Icons")

    title = models.CharField(max_length=255, unique=True, verbose_name=_("Name"))
    css_classes = models.CharField(max_length=255, verbose_name=_("Font Awesome Icon Classes"))

    def __str__(self):
        return self.title

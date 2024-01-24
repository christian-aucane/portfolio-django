from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _

from base.models import DisplayOrderBaseModel, UniqueEntryBaseModel
from common.models import FontAwesomeIcon


class AboutInfo(UniqueEntryBaseModel):
    class Meta:
        verbose_name = _("About me")
        verbose_name_plural = _("About me")

    first_name = models.CharField(max_length=255, default=_("Your first name"), verbose_name=_("First Name"))
    last_name = models.CharField(max_length=255, default=_("Your last name"), verbose_name=_("Last Name"))
    description = models.TextField(default=_("Your description"), verbose_name=_("Description"))
    profile_thumbnail = models.ImageField(upload_to="profile_thumbnail/", null=True, blank=True,
                                          verbose_name=_("Thumbnail"))

    def __str__(self):
        return _("About me")

    def get_thumbnail_url(self):
        return self.profile_thumbnail.url if self.profile_thumbnail else ""

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"


class AboutSkill(DisplayOrderBaseModel):
    class Meta:
        verbose_name = _("Skill")
        verbose_name_plural = _("Skills")

    about = models.ForeignKey(AboutInfo, on_delete=models.CASCADE, default=1, related_name="skills", verbose_name=_("About me"))
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Name"))

    def __str__(self):
        return self.name


class SocialLink(DisplayOrderBaseModel):
    class Meta:
        verbose_name = _("Social Link")
        verbose_name_plural = _("Social Links")

    about = models.ForeignKey(AboutInfo, on_delete=models.CASCADE, default=1, related_name="social_links", verbose_name=_("About me"))
    name = models.CharField(max_length=255, unique=True, verbose_name=_("Name"))
    url = models.URLField(verbose_name=_("URL"))
    icon = models.ForeignKey(FontAwesomeIcon, on_delete=models.CASCADE, verbose_name=_("Font Awesome Icon"))

    def __str__(self):
        return self.name

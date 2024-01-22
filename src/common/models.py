from django.db import models
from django.utils.translation import gettext_lazy as _


class FontAwesomeIcon(models.Model):
    class Meta:
        verbose_name = _("Font Awesome Icon")
        verbose_name_plural = _("Font Awesome Icons")

    title = models.CharField(max_length=255, unique=True, verbose_name=_("Name"))
    classes = models.CharField(max_length=255, verbose_name=_("Font Awesome Icon Classes"))

    def __str__(self):
        return self.title

    def html(self):
        return f'<i class="{self.classes}" title={self.title}></i>'

    def li_html(self, content=""):
        return f'<li><i class="fa-li {self.classes}" title={self.title}></i>{content}</li>'

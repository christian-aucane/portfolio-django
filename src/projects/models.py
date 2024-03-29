from django.db import models
from django.utils.translation import gettext_lazy as _

from base.models import DisplayOrderBaseModel
from common.models import FontAwesomeIcon


class Technology(models.Model):
    class Meta:
        verbose_name = _("Technology")
        verbose_name_plural = _("Technologies")
        ordering = ['name']

    name = models.CharField(max_length=255, verbose_name=_("Name"), unique=True)
    icon = models.ForeignKey(FontAwesomeIcon, on_delete=models.CASCADE,
                             verbose_name=_("Icon"))

    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['name']

    name = models.CharField(max_length=255, verbose_name=_("Name"), unique=True)

    def __str__(self):
        return self.name


class Project(DisplayOrderBaseModel):
    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    name = models.CharField(max_length=255, verbose_name=_("Name"))
    description = models.TextField(verbose_name=_("Description"))
    thumbnail = models.ImageField(upload_to='projects_thumbnails/',
                                  null=True, blank=True, verbose_name=_("Image"))
    categories = models.ManyToManyField(Category, through='ProjectCategory', verbose_name=_("Categories"))

    def __str__(self):
        return self.name

    def get_thumbnail_url(self):
        return self.thumbnail.url

    def get_technologies_by_categories(self):
        technologies_by_category = defaultdict(list)
        categories = self.categories.objects.all().values_list('name', flat=True)
        for category in categories:

            technologies_by_category[category].append(category)
        ordered_technologies = self.categor.order_by('category', 'display_order')

        for technology in ordered_skills:
            skills_by_category[skill.category].append(skill)

        return skills_by_category


class ProjectLink(DisplayOrderBaseModel):
    class Meta:
        verbose_name = _("Project Link")
        verbose_name_plural = _("Project Links")

    project = models.ForeignKey('Project', on_delete=models.CASCADE,
                                related_name='links', verbose_name=_("Project"))
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    link = models.URLField(verbose_name=_("Link"))
    icon = models.ForeignKey(FontAwesomeIcon, on_delete=models.CASCADE,
                             verbose_name=_("Icon"))
    text = models.CharField(max_length=255, verbose_name=_("Text"), null=True, blank=True)

    def __str__(self):
        return f"{self.project} - {self.title}"


class ProjectTechnology(DisplayOrderBaseModel):
    class Meta:
        verbose_name = _("Project Technology")
        verbose_name_plural = _("Project Technologies")

    project_category = models.ForeignKey('ProjectCategory', on_delete=models.CASCADE,
                                         verbose_name=_("Project Category"))
    technology = models.ForeignKey(Technology, on_delete=models.CASCADE,
                                   verbose_name=_("Technology"))

    def __str__(self):
        return f"{self.project_category} - {self.technology}"


class ProjectCategory(DisplayOrderBaseModel):
    class Meta:
        verbose_name = _("Project Category")
        verbose_name_plural = _("Project Categories")

    project = models.ForeignKey('Project', on_delete=models.CASCADE,
                                related_name='categories_through',
                                verbose_name=_("Project"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name=_("Category"))
    technologies = models.ManyToManyField(Technology, through=ProjectTechnology, verbose_name=_("Technologies"))

    def __str__(self):
        return f"{self.project} - {self.category}"

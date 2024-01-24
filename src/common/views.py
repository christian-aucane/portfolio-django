from django.views.generic import TemplateView

from about.models import AboutInfo
from awards.models import AwardCategory
from common.models import SiteMetaData
from education.models import Education
from experience.models import Experience
from interests.models import Paragraph
from projects.models import Project
from skills.models import Skill


class IndexView(TemplateView):
    template_name = "common/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["site_meta_data"] = SiteMetaData.objects.first()
        context["about_info"] = AboutInfo.objects.first()
        context["experiences"] = Experience.objects.all()
        context["educations"] = Education.objects.all()
        context["skills"] = Skill.get_skills_by_category()
        context["projects"] = Project.objects.all()
        context["interests"] = Paragraph.objects.all()
        context["awards_categories"] = AwardCategory.objects.all()
        return context

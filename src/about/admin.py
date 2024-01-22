from django.contrib import admin
from .models import AboutInfo, AboutSkill, SocialLink


class AboutSkillInline(admin.TabularInline):
    model = AboutSkill
    extra = 0


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 0


@admin.register(AboutInfo)
class AboutInfoAdmin(admin.ModelAdmin):
    inlines = [AboutSkillInline, SocialLinkInline]

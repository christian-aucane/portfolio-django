from django.contrib import admin
from .models import FontAwesomeIcon, SiteMetaData, FooterCredits, Favicon


@admin.register(FontAwesomeIcon)
class FontAwesomeIconAdmin(admin.ModelAdmin):
    list_display = ('title', 'css_classes')
    list_editable = ('css_classes', )


class FaviconInline(admin.TabularInline):
    model = Favicon


class FooterCreditsInline(admin.TabularInline):
    model = FooterCredits
    extra = 0


@admin.register(SiteMetaData)
class SiteMetaDataAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    inlines = [
        FaviconInline,
        FooterCreditsInline
    ]

from django.contrib import admin
from .models import FontAwesomeIcon, SiteMetaData


@admin.register(FontAwesomeIcon)
class FontAwesomeIconAdmin(admin.ModelAdmin):
    list_display = ('title', 'css_classes')
    list_editable = ('css_classes', )


@admin.register(SiteMetaData)
class SiteMetaDataAdmin(admin.ModelAdmin):
    list_display = ('__str__', )

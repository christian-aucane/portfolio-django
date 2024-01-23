from django.contrib import admin
from .models import FontAwesomeIcon


@admin.register(FontAwesomeIcon)
class FontAwesomeIconAdmin(admin.ModelAdmin):
    list_display = ('title', 'css_classes')
    list_editable = ('css_classes', )



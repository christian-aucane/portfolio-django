from django.contrib import admin
from .models import FontAwesomeIcon


@admin.register(FontAwesomeIcon)
class FontAwesomeIconAdmin(admin.ModelAdmin):
    list_display = ('title', 'classes')
    list_editable = ('classes', )



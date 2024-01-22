from django.contrib import admin
from .models import FontAwesomeIcon


@admin.register(FontAwesomeIcon)
class FontAwesomeIconAdmin(admin.ModelAdmin):
    list_display = ('title', 'classes', 'rendered_html')
    list_editable = ('classes', )

    def rendered_html(self, obj):
        return obj.html()

    rendered_html.short_description = 'Rendered HTML'


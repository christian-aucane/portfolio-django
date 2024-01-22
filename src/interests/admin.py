from django.contrib import admin
from .models import Paragraph


@admin.register(Paragraph)
class ParagraphAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'display_order')
    list_editable = ('display_order',)

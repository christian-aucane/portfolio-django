from django.contrib import admin
from django import forms
from django.forms import inlineformset_factory
from .models import Project, Category, Technology, ProjectCategory, ProjectTechnology


class ProjectTechnologyInline(admin.TabularInline):
    model = ProjectTechnology
    extra = 1


class ProjectCategoryForm(forms.ModelForm):
    class Meta:
        model = ProjectCategory
        fields = '__all__'

    technologies = forms.ModelMultipleChoiceField(
        queryset=Technology.objects.all(),
        widget=admin.widgets.FilteredSelectMultiple("Technologies", is_stacked=False),
        required=False,
    )


class ProjectCategoryInline(admin.TabularInline):
    model = ProjectCategory
    form = ProjectCategoryForm
    inlines = [ProjectTechnologyInline]
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectCategoryInline]


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ['name']

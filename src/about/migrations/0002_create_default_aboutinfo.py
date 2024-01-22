from django.db import migrations
from django.utils.translation import gettext_lazy as _
from ..models import AboutInfo


def create_default_about_info(apps, schema_editor):
    AboutInfo.objects.get_or_create()


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_about_info, reverse_code=migrations.RunPython.noop),
    ]

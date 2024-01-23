from django.db import migrations

from about.models import AboutInfo
from common.models import SiteMetaData


def create_default_about_info(apps, schema_editor):
    AboutInfo.objects.get_or_create()

def create_default_site_meta_data(apps, schema_editor):
    SiteMetaData.objects.get_or_create()

class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_default_about_info, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(create_default_site_meta_data, reverse_code=migrations.RunPython.noop),
    ]

from django.db import migrations
from django.utils.translation import gettext_lazy as _

from common.models import Favicon, FooterCredits


def create_default_favicon(apps, schema_editor):
    Favicon.objects.get_or_create()


def create_template_credits(apps, schema_editor):
    html = f"""
    <div id="template-credit">
        <p>
            {_("This website was created with")}
            <a href="https://startbootstrap.com/theme/resume" title={_("Template used")} target="_blank">
                Resume Theme
            </a>
            {_("created by")}
            <a href="https://startbootstrap.com" title="Start Bootstrap" target="_blank">
                www.startbootstrap.com
            </a>.
        </p>
    </div>
    """.strip()
    FooterCredits.objects.get_or_create(title="Template credits", html=html)


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0008_favicon_footercredits'),
    ]

    operations = [
        migrations.RunPython(create_default_favicon, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(create_template_credits, reverse_code=migrations.RunPython.noop),
    ]

# Generated by Django 5.0.1 on 2024-01-23 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
        ('common', '0006_create_default_sitemetadata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awardcategory',
            name='icon',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.fontawesomeicon', verbose_name='Icon'),
        ),
    ]

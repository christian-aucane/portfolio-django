# Generated by Django 5.0.1 on 2024-01-22 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0002_alter_experience_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='experience',
            options={'ordering': ['-start_date'], 'verbose_name': 'Experience', 'verbose_name_plural': 'Experiences'},
        ),
    ]

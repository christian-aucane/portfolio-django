# Generated by Django 5.0.1 on 2024-01-23 15:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0004_alter_education_thumbnail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-start_date'], 'verbose_name': 'Education', 'verbose_name_plural': 'Educations'},
        ),
    ]

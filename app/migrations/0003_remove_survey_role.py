# Generated by Django 2.1.5 on 2019-01-27 06:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_survey_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='survey',
            name='role',
        ),
    ]

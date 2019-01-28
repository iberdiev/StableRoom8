# Generated by Django 2.1.5 on 2019-01-27 17:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_survey_scale1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='scale1',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]

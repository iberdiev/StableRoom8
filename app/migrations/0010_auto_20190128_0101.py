# Generated by Django 2.1.5 on 2019-01-27 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20190128_0032'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='extra1',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='survey',
            name='extra2',
            field=models.TextField(default='no data provided', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='extra3',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]

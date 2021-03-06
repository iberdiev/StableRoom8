# Generated by Django 2.1.5 on 2019-01-27 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20190127_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='survey',
            name='year',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Preparatory'), (1, 'Freshman'), (2, 'Sophomore'), (3, 'Junior'), (4, 'Senior')], default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='survey',
            name='scale1',
            field=models.IntegerField(),
        ),
    ]

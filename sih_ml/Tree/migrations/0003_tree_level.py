# Generated by Django 2.0.13 on 2020-07-07 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tree', '0002_auto_20200707_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='Level',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]

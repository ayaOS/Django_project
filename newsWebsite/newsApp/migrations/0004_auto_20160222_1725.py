# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 17:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0003_auto_20160222_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='upload_image',
            field=models.ImageField(upload_to='resources/%Y/%m/%d/'),
        ),
    ]

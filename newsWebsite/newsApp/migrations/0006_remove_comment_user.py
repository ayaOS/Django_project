# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 17:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0005_auto_20160228_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]

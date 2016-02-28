# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0007_auto_20160228_1743'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tagText', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(to='newsApp.Tag'),
        ),
    ]
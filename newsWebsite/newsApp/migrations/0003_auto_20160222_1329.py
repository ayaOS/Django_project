# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-22 13:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newsApp', '0002_post_humbnail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=50)),
                ('phone', models.IntegerField()),
                ('passwd', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='humbnail',
            new_name='upload_image',
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsApp.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsApp.User'),
        ),
    ]

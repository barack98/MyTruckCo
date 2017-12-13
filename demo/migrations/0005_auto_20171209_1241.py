# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0004_auto_20171209_1238'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('album_title', models.CharField(max_length=250)),
                ('album_logo', models.CharField(max_length=250)),
            ],
        ),
        migrations.DeleteModel(
            name='Photos',
        ),
    ]

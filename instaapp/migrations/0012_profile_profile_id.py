# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-01 15:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0011_auto_20190901_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_id',
            field=models.IntegerField(default=0),
        ),
    ]

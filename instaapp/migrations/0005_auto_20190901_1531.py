# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-01 15:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0004_auto_20190901_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='like',
            field=models.IntegerField(null=True),
        ),
    ]

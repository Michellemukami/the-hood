# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-01 16:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0015_auto_20190901_1556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

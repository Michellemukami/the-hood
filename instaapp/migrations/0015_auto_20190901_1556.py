# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-09-01 15:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instaapp', '0014_remove_image_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='editor',
            new_name='profile',
        ),
    ]

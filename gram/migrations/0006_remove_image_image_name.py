# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-12 07:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0005_image_image_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='image_name',
        ),
    ]
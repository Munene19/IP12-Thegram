# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-12 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0004_auto_20200212_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]

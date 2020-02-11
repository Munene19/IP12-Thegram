# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-10 12:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        ('gram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('image_caption', models.TextField(max_length=40)),
                ('likes', models.IntegerField(default=0, null=True)),
                ('comments', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('profile_photo', models.ImageField(upload_to='')),
                ('Bio', models.CharField(max_length=40)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='gram.Profile'),
        ),
    ]

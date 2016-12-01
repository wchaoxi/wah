# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-29 19:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wah', '0006_album_visibility'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='follow',
        ),
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='friends', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='pending_friends',
            field=models.ManyToManyField(blank=True, related_name='pending_friends', to=settings.AUTH_USER_MODEL),
        ),
    ]
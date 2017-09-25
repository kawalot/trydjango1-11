# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-25 18:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0004_auto_20170924_2005'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='restaurant',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-24 20:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_restaurant_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.CharField(max_length=120, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-14 14:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_profile_actication_key'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='actication_key',
            new_name='activation_key',
        ),
    ]

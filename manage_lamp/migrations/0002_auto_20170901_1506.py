# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 07:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manage_lamp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lamp',
            old_name='is_repeater',
            new_name='is_repeated',
        ),
    ]

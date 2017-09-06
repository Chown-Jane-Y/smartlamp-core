# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 05:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_lamp', '0004_auto_20170901_1508'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lamp',
            name='hub_id',
        ),
        migrations.AddField(
            model_name='lamp',
            name='hub_sn',
            field=models.CharField(default=1, max_length=16, verbose_name='所属集控'),
            preserve_default=False,
        ),
    ]
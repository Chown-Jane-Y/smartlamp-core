# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-01 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_hub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='deleted_time',
            field=models.DateTimeField(auto_now=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='hub',
            name='status',
            field=models.IntegerField(choices=[(1, '正常'), (2, '故障'), (3, '脱网')]),
        ),
    ]

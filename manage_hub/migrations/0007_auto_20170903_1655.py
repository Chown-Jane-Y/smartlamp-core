# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manage_hub', '0006_auto_20170901_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hub',
            name='registered_time',
            field=models.DateField(),
        ),
    ]

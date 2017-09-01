# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-28 10:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('manage_logs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='log_set', to=settings.AUTH_USER_MODEL, verbose_name='\u64cd\u4f5c\u7528\u6237\u7f16\u53f7'),
        ),
    ]
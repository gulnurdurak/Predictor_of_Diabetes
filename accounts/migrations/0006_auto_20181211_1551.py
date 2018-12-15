# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-12-11 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20181211_1516'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='staff',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-13 06:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_home_status', '0013_auto_20171013_1347'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='name',
            new_name='nama',
        ),
    ]
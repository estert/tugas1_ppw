# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 06:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_home_status', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 10, 13, 18, 4, 520428, tzinfo=utc)),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 05:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('app_home_status', '0002_auto_20171006_2111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 7, 5, 46, 21, 686305, tzinfo=utc)),
        ),
    ]
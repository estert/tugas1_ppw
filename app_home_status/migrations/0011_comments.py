# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_home_status', '0010_merge_20171012_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('comment', models.TextField()),
                ('comments_created_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

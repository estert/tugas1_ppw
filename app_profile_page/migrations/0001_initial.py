# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-10 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('birth_date', models.DateField()),
                ('expertise', models.TextField()),
                ('gender', models.CharField(max_length=8)),
                ('description', models.CharField(max_length=128)),
                ('picture_url', models.URLField()),
            ],
        ),
    ]

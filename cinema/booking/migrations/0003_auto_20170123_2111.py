# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-23 18:11
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_auto_20170123_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='seats',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(), max_length=10, size=None),
        ),
    ]

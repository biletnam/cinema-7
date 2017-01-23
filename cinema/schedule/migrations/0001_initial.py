# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-01-23 21:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('row_count', models.IntegerField(default=0)),
                ('seats_in_row', models.IntegerField(default=10)),
            ],
        ),
        migrations.CreateModel(
            name='Row',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('seat_count', models.IntegerField()),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Hall')),
            ],
        ),
        migrations.CreateModel(
            name='Seance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField(editable=False)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Hall')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Movie')),
            ],
        ),
        migrations.CreateModel(
            name='Seat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(default=0)),
                ('booked', models.BooleanField(default=False)),
                ('hall', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Hall')),
                ('row', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Row')),
                ('seance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schedule.Seance')),
            ],
        ),
    ]

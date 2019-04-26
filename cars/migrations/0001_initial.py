# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-16 10:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=30)),
                ('engine_type', models.CharField(max_length=30)),
                ('year_made', models.CharField(max_length=30)),
                ('gear_box', models.CharField(max_length=30)),
            ],
        ),
    ]
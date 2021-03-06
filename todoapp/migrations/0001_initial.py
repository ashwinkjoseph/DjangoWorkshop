# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-07 12:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userAuth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('description', models.TextField()),
                ('createdDate', models.DateTimeField(default=datetime.datetime(2017, 10, 7, 12, 56, 20, 446070, tzinfo=utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userAuth.User')),
            ],
        ),
    ]

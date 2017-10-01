# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=150)),
                ('dni', models.CharField(max_length=150)),
                ('codeme', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
    ]

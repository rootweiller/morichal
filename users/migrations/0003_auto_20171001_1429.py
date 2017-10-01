# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-01 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171001_1316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='document_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='document_type',
            field=models.CharField(blank=True, choices=[('CI', 'CEDULA DE IDENTIDAD'), ('PA', 'PASAPORTE'), ('DNI', 'DOCUMENTO DE IDENTIDAD')], max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-06 00:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0010_auto_20181101_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='bono',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='salario_comida',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='salario_transporte',
            field=models.FloatField(blank=True, default=1, null=True),
        ),
    ]

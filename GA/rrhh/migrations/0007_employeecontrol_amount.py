# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-10-28 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrhh', '0006_employeecontrol_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeecontrol',
            name='amount',
            field=models.IntegerField(default=1),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-12 11:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consortial_billing', '0014_auto_20170511_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='renewal',
            name='billing_complete',
            field=models.BooleanField(default=False),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-18 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consortial_billing', '0021_poll_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='processed',
            field=models.BooleanField(default=False),
        ),
    ]

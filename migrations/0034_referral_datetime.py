# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-28 14:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('consortial_billing', '0033_auto_20180227_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 08:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consortial_billing', '0030_auto_20171002_0845'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportlevel',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]

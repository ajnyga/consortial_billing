# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-06-22 08:53
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models
import plugins.consortial_billing.models


class Migration(migrations.Migration):

    dependencies = [
        ('consortial_billing', '0026_merge'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='institution',
            options={'ordering': ('sort_country', 'name')},
        ),
        migrations.AddField(
            model_name='banding',
            name='redirect_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='institution',
            name='sort_country',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='poll',
            name='file',
            field=models.FileField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/ajrbyers/Code/acta/src/media'), upload_to=plugins.consortial_billing.models.file_upload_path),
        ),
    ]

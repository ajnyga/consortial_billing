# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-10 13:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consortial_billing', '0011_auto_20170510_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='institution',
            name='billing_agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='consortial_billing.BillingAgent'),
        ),
    ]
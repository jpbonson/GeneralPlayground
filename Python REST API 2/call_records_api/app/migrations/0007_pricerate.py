# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2018-01-24 21:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20180124_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate_type', models.CharField(choices=[('std', 'standard'), ('rdc', 'reduced')], max_length=3)),
                ('start_datetime', models.TimeField()),
                ('end_datetime', models.TimeField()),
                ('standing_charge', models.DecimalField(decimal_places=2, max_digits=5)),
                ('charge_per_min', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]

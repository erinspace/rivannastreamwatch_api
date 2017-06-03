# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-03 18:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='lattitude',
            field=models.DecimalField(decimal_places=6, default=12.5, max_digits=9),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='longitude',
            field=models.DecimalField(decimal_places=6, default=12.5, max_digits=9),
            preserve_default=False,
        ),
    ]

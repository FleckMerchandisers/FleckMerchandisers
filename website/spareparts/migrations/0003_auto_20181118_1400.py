# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-11-18 14:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spareparts', '0002_item_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]

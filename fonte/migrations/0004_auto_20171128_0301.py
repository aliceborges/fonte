# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-11-28 05:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fonte', '0003_auto_20171128_0257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(unique=True),
        ),
        migrations.AlterField(
            model_name='font',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]

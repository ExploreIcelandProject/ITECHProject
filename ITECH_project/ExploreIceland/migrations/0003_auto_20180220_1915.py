# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 19:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExploreIceland', '0002_auto_20180220_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractionpage',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExploreIceland.attractionCategory'),
        ),
    ]

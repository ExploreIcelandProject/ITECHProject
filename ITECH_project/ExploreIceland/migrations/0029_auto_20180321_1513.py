# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-21 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExploreIceland', '0028_auto_20180320_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attractionpage',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='ExploreIceland.attractionCategory'),
        ),
    ]
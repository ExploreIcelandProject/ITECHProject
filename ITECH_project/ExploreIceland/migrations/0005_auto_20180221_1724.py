# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-21 17:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExploreIceland', '0004_auto_20180220_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='attractioncategory',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attractionpage',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExploreIceland.attractionCategory'),
        ),
    ]

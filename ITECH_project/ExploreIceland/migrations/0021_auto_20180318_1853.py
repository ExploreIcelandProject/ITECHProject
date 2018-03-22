# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-03-18 18:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ExploreIceland', '0020_auto_20180318_1848'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PageView',
        ),
        migrations.AddField(
            model_name='attractionpage',
            name='hits',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='attractionpage',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ExploreIceland.attractionCategory'),
        ),
    ]

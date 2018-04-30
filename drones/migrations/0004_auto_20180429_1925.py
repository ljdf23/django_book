# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-29 19:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drones', '0003_auto_20180429_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='drone',
            name='drones_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='drones', to='drones.DronesCategory'),
        ),
        migrations.AlterField(
            model_name='competition',
            name='pilot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='competitions', to='drones.Pilot'),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-20 13:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0007_auto_20170919_2023'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrequests',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=1, help_text='Add number required.', max_digits=6),
        ),
        migrations.AlterField(
            model_name='userrequests',
            name='description',
            field=models.TextField(help_text="Provide details of what's being requested, and where it can be purchased (preferably with a link)"),
        ),
    ]
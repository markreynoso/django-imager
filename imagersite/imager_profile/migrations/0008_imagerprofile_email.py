# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-26 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0007_auto_20171121_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagerprofile',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
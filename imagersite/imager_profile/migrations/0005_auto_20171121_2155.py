# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-21 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imager_profile', '0004_auto_20171121_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagerprofile',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='camera',
            field=models.CharField(blank=True, choices=[('CANON', 'Canon'), ('NIKON', 'Nikon'), ('SONY', 'Sony'), ('FUJIFILM', 'Fujifilm')], default='CANON', max_length=40),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='photo_styles',
            field=models.CharField(blank=True, choices=[('BW', 'Black and white'), ('COLOR', 'Color'), ('STILL', 'Still'), ('ACTION', 'Action')], default='COLOR', max_length=40),
        ),
        migrations.AlterField(
            model_name='imagerprofile',
            name='services',
            field=models.CharField(blank=True, choices=[('WEDDINGS', 'Weddings'), ('SCHOOL', 'School'), ('FAMILY', 'Family'), ('BABIES', 'Babies'), ('NATURE', 'Nature'), ('ABSTACT', 'Abstract'), ('OTHER', 'Other')], default='OTHER', max_length=70),
        ),
    ]

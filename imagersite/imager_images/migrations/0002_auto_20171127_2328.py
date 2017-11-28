# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 23:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imager_images', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='date_published',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='album',
            name='published',
            field=models.CharField(blank=True, choices=[('PRIVATE', 'Private'), ('SHARED', 'Shared'), ('PUBLIC', 'Public')], max_length=10),
        ),
        migrations.AlterField(
            model_name='album',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='album', to='imager_profile.ImagerProfile'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='date_published',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='photo',
            name='docfile',
            field=models.ImageField(upload_to='documents/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='photo',
            name='published',
            field=models.CharField(blank=True, choices=[('PRIVATE', 'Private'), ('SHARED', 'Shared'), ('PUBLIC', 'Public')], max_length=10),
        ),
        migrations.AlterField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photo', to='imager_profile.ImagerProfile'),
        ),
    ]

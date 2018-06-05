# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2018-03-01 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='follows',
            field=models.ManyToManyField(related_name='followed_by', to='profiles.Profile'),
        ),
    ]

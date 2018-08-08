# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-08 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_mp_user',
            field=models.IntegerField(choices=[(0, '否'), (1, '是')], default=0, verbose_name='是否是公众号用户'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-09 23:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='verifycode',
            name='mobile',
            field=models.CharField(help_text='手机号', max_length=11, verbose_name='手机号'),
        ),
    ]

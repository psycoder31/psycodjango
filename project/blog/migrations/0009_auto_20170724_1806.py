# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-24 09:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170724_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tag_set',
            field=models.ManyToManyField(blank=True, to='blog.Tag'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-17 13:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170717_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], default='d', max_length=1),
            preserve_default=False,
        ),
    ]
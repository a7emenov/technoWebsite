# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 20:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20161116_0858'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='correctFlag',
            new_name='correct',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2022-08-23 09:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='cont',
            new_name='Sub',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Address',
            new_name='messg',
        ),
    ]

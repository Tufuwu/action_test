# -*- coding: utf-8 -*-
# Generated by Django 1.11.25 on 2019-10-02 14:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projectroles', '0012_update_remotesite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appsetting',
            name='type',
            field=models.CharField(help_text='Type of the setting', max_length=64),
        ),
    ]

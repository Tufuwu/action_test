# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-12-04 16:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('a4reports', '0001_initial'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='report',
            index_together=set([('content_type', 'object_pk')]),
        ),
    ]

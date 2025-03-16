# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-14 14:55
from __future__ import unicode_literals

from django.db import migrations, models

from django_add_default_value import AddDefaultValue


class Migration(migrations.Migration):

    dependencies = [("app_add_not_null_column_followed_by_default", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="a", name="not_null_field", field=models.IntegerField(default=1)
        ),
        AddDefaultValue(model_name="a", name="not_null_field", value=1),
    ]

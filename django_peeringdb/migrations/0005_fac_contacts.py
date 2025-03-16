# Generated by Django 2.2.12 on 2020-04-03 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("django_peeringdb", "0004_rs_lg_fields"),
    ]

    operations = [
        migrations.AddField(
            model_name="facility",
            name="sales_email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="facility",
            name="sales_phone",
            field=models.CharField(blank=True, max_length=192),
        ),
        migrations.AddField(
            model_name="facility",
            name="tech_email",
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name="facility",
            name="tech_phone",
            field=models.CharField(blank=True, max_length=192),
        ),
    ]

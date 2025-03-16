# Generated by Django 2.2.5 on 2019-11-22 23:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0026_auto_20191115_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='integrated',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='partner',
            name='landing_page',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='partner_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='short_partner_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='partner',
            name='verified_by_instructor',
            field=models.BooleanField(default=False),
        ),
    ]

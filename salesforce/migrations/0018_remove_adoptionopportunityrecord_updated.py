# Generated by Django 2.0.13 on 2019-08-19 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0017_adoptionopportunityrecord_updated'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adoptionopportunityrecord',
            name='updated',
        ),
    ]

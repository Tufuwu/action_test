# Generated by Django 2.2.8 on 2020-10-30 14:36

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activity_calendar', '0003_auto_20200921_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityMoment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_description', models.TextField(blank=True, default=None, null=True)),
                ('local_location', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('local_max_participants', models.IntegerField(blank=True, default=None, help_text='-1 denotes unlimited participants', null=True, validators=[django.core.validators.MinValueValidator(-1)])),
                ('recurrence_id', models.DateTimeField(verbose_name='parent activity date/time')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('parent_activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='activity_calendar.Activity')),
            ],
            options={
                'unique_together': {('parent_activity', 'recurrence_id')},
            },
        ),
    ]

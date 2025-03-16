# Generated by Django 2.1.3 on 2018-11-29 21:44

import uuid

import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import swapper
from django.db import migrations, models

import openwisp_users.mixins


class Migration(migrations.Migration):

    dependencies = [
        swapper.dependency('openwisp_users', 'Group'),
        ('testapp', '0002_config_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'created',
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='created',
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                ('author', models.CharField(max_length=64, verbose_name='author')),
                (
                    'organization',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=swapper.get_model_name('openwisp_users', 'Organization'),
                        verbose_name='organization',
                    ),
                ),
            ],
            options={'abstract': False},
            bases=(openwisp_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Shelf',
            fields=[
                (
                    'id',
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    'created',
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='created',
                    ),
                ),
                (
                    'modified',
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name='modified',
                    ),
                ),
                ('name', models.CharField(max_length=64, verbose_name='name')),
                (
                    'organization',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=swapper.get_model_name('openwisp_users', 'Organization'),
                        verbose_name='organization',
                    ),
                ),
            ],
            options={'abstract': False},
            bases=(openwisp_users.mixins.ValidateOrgMixin, models.Model),
        ),
        migrations.AddField(
            model_name='book',
            name='shelf',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to='testapp.Shelf'
            ),
        ),
    ]

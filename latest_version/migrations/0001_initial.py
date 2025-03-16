# Generated by Django 2.2.3 on 2019-07-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=50, verbose_name='Latest Geany version')),
                ('release_date', models.DateTimeField()),
                ('github_link', models.CharField(max_length=255, verbose_name='Link to the Commits page on Github (everything after https://github.com/geany/geany/)')),
            ],
            options={
                'verbose_name_plural': 'Latest Version',
                'verbose_name': 'Latest Version',
            },
        ),
    ]

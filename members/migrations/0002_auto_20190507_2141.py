# Generated by Django 2.2 on 2019-05-07 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("members", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="floor",
            field=models.CharField(blank=True, max_length=10, verbose_name="Etage"),
        )
    ]

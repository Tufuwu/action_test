# Generated by Django 2.2.4 on 2019-09-03 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("enhydris", "0019_translatable_timestep")]

    operations = [
        migrations.AlterUniqueTogether(
            name="stationtypetranslation", unique_together=None
        ),
        migrations.RemoveField(model_name="stationtypetranslation", name="master"),
        migrations.RemoveField(model_name="station", name="stype"),
        migrations.DeleteModel(name="StationType"),
        migrations.DeleteModel(name="StationTypeTranslation"),
    ]

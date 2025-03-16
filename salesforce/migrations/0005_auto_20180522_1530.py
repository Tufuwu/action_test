# Generated by Django 2.0.2 on 2018-05-22 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salesforce', '0004_auto_20180522_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='achieving_the_dream_school',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='adoption_date',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='all_time_savings',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='all_time_students',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='current_year_savings',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='current_year_students',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='hbcu',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='key_institutional_partner',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='pell_grant_recipients',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='percent_students_pell_grant',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='texas_higher_ed',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='undergraduate_enrollment',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='school',
            name='website',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

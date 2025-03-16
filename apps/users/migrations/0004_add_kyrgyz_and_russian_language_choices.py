# Generated by Django 2.2.19 on 2021-03-04 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a4_candy_users', '0003_add_dutch_to_language_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('de', 'German'), ('nl', 'Dutch'), ('ky', 'Kyrgyz'), ('ru', 'Russian')], default='de', help_text='Specify your preferred language for the user interface and the notifications of the platform.', max_length=4, verbose_name='Your preferred language'),
        ),
    ]

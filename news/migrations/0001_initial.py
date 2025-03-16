# Generated by Django 2.2.3 on 2019-07-14 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import mezzanine.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(db_index=True, editable=False, max_length=255, verbose_name='Slug')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('content', mezzanine.core.fields.RichTextField(verbose_name='Content')),
                ('status', models.IntegerField(choices=[(1, 'Draft'), (2, 'Published')], db_index=True, default=2, help_text='With Draft chosen, will only be shown for admin users on the site.', verbose_name='Status')),
                ('entry_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Published')),
                ('publish_date', models.DateTimeField(blank=True, db_index=True, default=django.utils.timezone.now, verbose_name='Published on')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='newsposts', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
            ],
            options={
                'verbose_name_plural': 'News',
                'ordering': ('-publish_date',),
                'verbose_name': 'News',
            },
        ),
    ]

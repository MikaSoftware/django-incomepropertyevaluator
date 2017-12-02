# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-02 23:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import shared_foundation.models.profile
import shared_foundation.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('last_modified', models.DateTimeField(auto_now=True, db_index=True)),
                ('salt', models.CharField(blank=True, default=shared_foundation.utils.generate_hash, help_text='The unique salt value associated with this object.', max_length=127, null=True, unique=True, verbose_name='Salt')),
                ('pr_access_code', models.CharField(blank=True, default=shared_foundation.utils.generate_hash, help_text='The access code to enter the password reset page to be granted access to restart your password.', max_length=127, verbose_name='Password Reset Access Code')),
                ('pr_expiry_date', models.DateTimeField(blank=True, default=shared_foundation.models.profile.get_expiry_date, help_text='The date where the access code expires and no longer works.', verbose_name='Password Reset Access Code Expiry Date')),
                ('user', models.OneToOneField(blank=True, help_text='The user whom belongs to this profile.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
                'db_table': 'mika_shared_profiles',
            },
        ),
    ]

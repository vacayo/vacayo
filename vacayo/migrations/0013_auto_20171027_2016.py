# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 20:16
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacayo', '0012_auto_20171017_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('_address', models.CharField(blank=True, db_index=True, max_length=1024, null=True)),
                ('address1', models.CharField(blank=True, max_length=256, null=True)),
                ('address2', models.CharField(blank=True, max_length=256, null=True)),
                ('unit', models.CharField(blank=True, max_length=256, null=True)),
                ('city', models.CharField(blank=True, db_index=True, max_length=256, null=True)),
                ('state', models.CharField(blank=True, db_index=True, max_length=256, null=True)),
                ('zip_code', models.CharField(blank=True, db_index=True, max_length=256, null=True)),
                ('latitude', models.FloatField(blank=True, null=True)),
                ('longitude', models.FloatField(blank=True, null=True)),
                ('geo', django.contrib.gis.db.models.fields.PointField(blank=True, geography=True, null=True, srid=4326)),
                ('needs_review', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'location',
                'verbose_name': 'Location',
                'verbose_name_plural': 'Locations',
            },
        ),
        migrations.RenameField(
            model_name='host',
            old_name='manage_radius',
            new_name='radius',
        ),
        migrations.RemoveField(
            model_name='host',
            name='manage_address',
        ),
        migrations.AddField(
            model_name='property',
            name='location',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacayo.Location'),
        ),
        migrations.AddField(
            model_name='host',
            name='location',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vacayo.Location'),
        ),
    ]

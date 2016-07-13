# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('pin_code', models.CharField(max_length=100)),
                ('landmark', models.CharField(max_length=100)),
                ('phone_no', models.CharField(max_length=100)),
                ('user_email', models.CharField(max_length=100)),
                ('features', models.CharField(max_length=100)),
                ('tags', models.CharField(max_length=100)),
                ('cuisines', models.CharField(max_length=100)),
                ('timings', models.CharField(max_length=100)),
                ('details', models.CharField(max_length=100)),
                ('review', models.CharField(max_length=100)),
                ('opening_status', models.CharField(max_length=100)),
                ('restaurant_type', models.CharField(max_length=100)),
                ('restaurant_email', models.CharField(max_length=100)),
                ('restaurant_website', models.CharField(max_length=100)),
                ('social_media_sites', models.CharField(max_length=100)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'restaurant',
            },
        ),
    ]

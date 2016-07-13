# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'food_type',
            },
        ),
        migrations.CreateModel(
            name='Restaurant_type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('is_deleted', models.BooleanField(default=False)),
                ('food_type', models.ForeignKey(to='food_app.Food_type')),
            ],
            options={
                'db_table': 'restaurant_type',
            },
        ),
    ]

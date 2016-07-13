# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0006_auto_20160529_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu_category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('is_deleted', models.BooleanField(default=False)),
                ('restaurant', models.ForeignKey(to='food_app.Restaurant')),
            ],
            options={
                'db_table': 'menu_category',
            },
        ),
        migrations.CreateModel(
            name='Menu_category_details',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('description', models.CharField(max_length=300)),
                ('food', models.ForeignKey(to='food_app.Food')),
                ('menu_category', models.ForeignKey(to='food_app.Menu_category')),
            ],
            options={
                'db_table': 'menu_category_details',
            },
        ),
    ]

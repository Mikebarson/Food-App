# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0004_auto_20160523_1122'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('price', models.FloatField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('food_type', models.ForeignKey(to='food_app.Food_type')),
                ('restaurant', models.ForeignKey(to='food_app.Restaurant')),
            ],
            options={
                'db_table': 'food',
            },
        ),
    ]

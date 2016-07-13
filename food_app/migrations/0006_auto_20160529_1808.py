# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0005_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('description', models.CharField(max_length=300)),
            ],
            options={
                'db_table': 'food_details',
            },
        ),
        migrations.RemoveField(
            model_name='food',
            name='description',
        ),
        migrations.RemoveField(
            model_name='food',
            name='food_type',
        ),
        migrations.RemoveField(
            model_name='food',
            name='name',
        ),
        migrations.RemoveField(
            model_name='food',
            name='price',
        ),
        migrations.AddField(
            model_name='food_details',
            name='food',
            field=models.ForeignKey(to='food_app.Food'),
        ),
        migrations.AddField(
            model_name='food_details',
            name='food_type',
            field=models.ForeignKey(to='food_app.Food_type'),
        ),
    ]

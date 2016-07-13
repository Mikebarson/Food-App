# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0002_food_type_restaurant_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='restaurant_type',
        ),
        migrations.AddField(
        model_name='restaurant',
        name='restaurant_type',
        field=models.ForeignKey(to='food_app.Restaurant_type'),
        ),
    ]

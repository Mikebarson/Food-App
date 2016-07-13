# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0003_auto_20160523_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant_type',
            name='food_type',
        ),
        migrations.AddField(
            model_name='food_type',
            name='restaurant_type',
            field=models.ForeignKey(to='food_app.Restaurant_type', default=2),
            preserve_default=False,
        ),
    ]

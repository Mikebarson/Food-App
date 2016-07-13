# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0008_auto_20160710_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu_category_details',
            name='is_deleted',
            field=models.BooleanField(default=False),
        ),
    ]

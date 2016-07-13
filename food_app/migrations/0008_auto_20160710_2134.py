# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food_app', '0007_menu_category_menu_category_details'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu_category',
            name='name',
        ),
        migrations.RemoveField(
            model_name='menu_category_details',
            name='food',
        ),
        migrations.AddField(
            model_name='food_details',
            name='menu_category',
            field=models.ForeignKey(default=1, to='food_app.Menu_category'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu_category_details',
            name='name',
            field=models.CharField(max_length=100, default=1),
            preserve_default=False,
        ),
    ]

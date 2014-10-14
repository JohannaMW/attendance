# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendy_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='check_in_counter',
            field=models.IntegerField(default=0),
        ),
    ]

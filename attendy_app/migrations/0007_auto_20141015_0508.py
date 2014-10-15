# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('attendy_app', '0006_auto_20141015_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checked_in',
            name='date',
            field=models.DateField(default=datetime.date(2014, 10, 15)),
        ),
    ]

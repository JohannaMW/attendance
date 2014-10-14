# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendy_app', '0002_auto_20141014_2304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='check_in_date',
            field=models.DateField(null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendy_app', '0004_auto_20141014_2309'),
    ]

    operations = [
        migrations.RenameField(
            model_name='people',
            old_name='status',
            new_name='check_in',
        ),
    ]

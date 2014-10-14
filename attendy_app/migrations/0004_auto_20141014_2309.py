# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendy_app', '0003_auto_20141014_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='class_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='people',
            name='name',
            field=models.CharField(max_length=100, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='people',
            name='user_type',
            field=models.PositiveSmallIntegerField(default=0, choices=[(0, b'teacher'), (1, b'student')]),
        ),
    ]

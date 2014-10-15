# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('attendy_app', '0005_auto_20141015_0029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checked_in',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('user', models.ForeignKey(related_name=b'checked_in', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='people',
            name='check_in',
        ),
        migrations.RemoveField(
            model_name='people',
            name='check_in_date',
        ),
    ]

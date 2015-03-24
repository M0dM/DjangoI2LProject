# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sondages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reponse',
            name='score',
            field=models.PositiveIntegerField(default=0),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('date', '0003_auto_20141008_2032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='single',
            name='name',
        ),
    ]

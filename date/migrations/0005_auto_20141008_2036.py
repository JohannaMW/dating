# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('date', '0004_remove_single_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='single',
            name='image',
            field=models.ImageField(null=True, upload_to=b'', blank=True),
        ),
    ]

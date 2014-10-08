# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('date', '0005_auto_20141008_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='single',
            name='image',
            field=models.ImageField(null=True, upload_to=b'/static/img/', blank=True),
        ),
    ]

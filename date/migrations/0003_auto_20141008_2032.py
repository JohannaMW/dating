# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('date', '0002_auto_20141008_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='single',
            name='image',
            field=models.ImageField(null=True, upload_to=b'/static/img', blank=True),
        ),
    ]

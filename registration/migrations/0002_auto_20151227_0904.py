# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastexperiences',
            name='photo',
            field=models.ImageField(upload_to=b'pictures', blank=True),
        ),
    ]

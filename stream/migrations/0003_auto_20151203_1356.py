# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stream', '0002_droplink'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='droplink',
            options={'verbose_name': 'Link', 'verbose_name_plural': 'Links'},
        ),
    ]

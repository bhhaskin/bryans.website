# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20151203_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='slug',
            field=models.SlugField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogtag',
            name='slug',
            field=models.SlugField(null=True),
            preserve_default=True,
        ),
    ]

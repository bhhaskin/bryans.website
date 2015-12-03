# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151203_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcategory',
            name='slug',
            field=models.SlugField(unique=True, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='blogtag',
            name='slug',
            field=models.SlugField(unique=True, null=True),
            preserve_default=True,
        ),
    ]

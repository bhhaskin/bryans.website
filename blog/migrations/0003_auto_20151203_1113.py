# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151203_1037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogcategory',
            name='type',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='category',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='categories',
            field=models.ManyToManyField(to='blog.BlogCategory', null=True, blank=True),
            preserve_default=True,
        ),
    ]

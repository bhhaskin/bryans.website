# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(unique=True, max_length=70)),
                ('type', models.CharField(default=b'label-default', max_length=20, null=True, blank=True, choices=[(b'label-default', b'Default'), (b'label-primary', b'Primary'), (b'label-success', b'Success'), (b'label-info', b'Info'), (b'label-warning', b'Warning'), (b'label-danger', b'Danger')])),
                ('parent', models.ForeignKey(related_name='categoryParent', blank=True, to='blog.BlogCategory', null=True)),
            ],
            options={
                'abstract': False,
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='BlogTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(unique=True, max_length=70)),
            ],
            options={
                'ordering': ['tag'],
                'abstract': False,
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(blank=True, to='blog.BlogCategory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='tags',
            field=models.ManyToManyField(to='blog.BlogTag', null=True, blank=True),
            preserve_default=True,
        ),
    ]

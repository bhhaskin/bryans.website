# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'title')),
                ('content', models.TextField(verbose_name=b'content', blank=True)),
                ('excerpt', models.TextField(verbose_name=b'excerpt', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('edited', models.DateTimeField(auto_now=True)),
                ('published', models.DateTimeField(null=True, blank=True)),
                ('visibility', models.CharField(default=b'Public', max_length=18, choices=[(b'Public', b'Public'), (b'Password protected', b'Password protected'), (b'Private', b'Private')])),
                ('status', models.CharField(default=b'Draft', max_length=14, choices=[(b'Published', b'Published'), (b'Pending Review', b'Pending Review'), (b'Draft', b'Draft')])),
                ('slug', models.SlugField(unique_for_date=b'published')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-published'],
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]

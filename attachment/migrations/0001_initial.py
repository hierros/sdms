# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import attachment.models


class Migration(migrations.Migration):

    dependencies = [
        ('sample', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attachment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('path', models.FilePathField(null=True, blank=b'True')),
                ('filename', models.FileField(null=True, upload_to=attachment.models.get_upload_file_name, blank=b'True')),
                ('sdms', models.ManyToManyField(to='sample.Sample', null=True, blank=b'True')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

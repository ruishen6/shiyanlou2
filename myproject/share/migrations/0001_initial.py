# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('DownloadDocount', models.IntegerField(verbose_name='visit_times', default=0)),
                ('code', models.CharField(verbose_name='code', max_length=8)),
                ('Datetime', models.DateTimeField(verbose_name='add_time', default=datetime.datetime.now)),
                ('path', models.CharField(verbose_name='download_path', max_length=32)),
                ('name', models.CharField(verbose_name='file_name', default='', max_length=32)),
                ('Filesize', models.CharField(verbose_name='file_size', max_length=10)),
                ('PCIP', models.CharField(verbose_name='IP_address', default='', max_length=32)),
            ],
            options={
                'verbose_name': 'download',
                'db_table': 'download',
            },
        ),
    ]

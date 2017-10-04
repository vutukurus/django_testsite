# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('body', models.TextField()),
                ('amount', models.IntegerField()),
                ('status', models.CharField(default=b'unpaid', max_length=20, choices=[(b'paid', b'PAID'), (b'unpaid', b'UNPAID')])),
            ],
        ),
    ]

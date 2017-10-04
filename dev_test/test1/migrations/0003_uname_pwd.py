# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test1', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='uname_pwd',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=10)),
                ('pwd', models.CharField(max_length=10)),
            ],
        ),
    ]

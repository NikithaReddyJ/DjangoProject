# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-09-26 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_table1'),
    ]

    operations = [
        migrations.CreateModel(
            name='table2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('name', models.TextField()),
                ('salary', models.TextField()),
                ('country', models.TextField()),
            ],
        ),
    ]

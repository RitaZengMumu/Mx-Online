# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-05 21:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0006_auto_20171129_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='\u5168\u56fd\u77e5\u540d', max_length=10, verbose_name='\u673a\u6784\u6807\u7b7e'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-12-19 18:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0005_auto_20171218_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticia',
            name='destacado',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
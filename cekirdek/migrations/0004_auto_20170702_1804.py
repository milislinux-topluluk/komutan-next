# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cekirdek', '0003_auto_20170701_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tema',
            name='arkaplan',
            field=models.FilePathField(default='mavi.png', match='.*\\.png$', path='/opt/komutan2/static/img/artalanlar', recursive=True, verbose_name='Arayüz arkaplan resmi'),
        ),
    ]

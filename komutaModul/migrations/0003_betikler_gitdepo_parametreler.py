# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-24 04:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('komutaModul', '0002_auto_20170620_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Betikler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('betik', models.CharField(default='', max_length=50, verbose_name='Betiğin Dosya Adı')),
            ],
            options={
                'verbose_name_plural': 'Betikler',
                'db_table': 'Betikler',
                'verbose_name': 'Betik',
            },
        ),
        migrations.CreateModel(
            name='GitDepo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('depoAdresi', models.URLField(verbose_name='Git Depo Adresi')),
            ],
            options={
                'verbose_name_plural': 'Git Depo Ayarları',
                'db_table': 'BetikDepo',
                'verbose_name': 'Git Depo Ayarı',
            },
        ),
        migrations.CreateModel(
            name='Parametreler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parametre', models.CharField(default='', max_length=12, verbose_name='Betiğin aldığı parametre')),
                ('parametreBaslik', models.CharField(default='', editable=False, max_length=50)),
                ('deger', models.CharField(default='', max_length=50, verbose_name='Parametrenin aldığı varsayılan değer')),
                ('betik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='komutaModul.Betikler')),
            ],
            options={
                'verbose_name_plural': 'Parametreler',
                'verbose_name': 'Parametre',
                'db_table': 'BetikParametreler',
                'ordering': ('parametre',),
            },
        ),
    ]

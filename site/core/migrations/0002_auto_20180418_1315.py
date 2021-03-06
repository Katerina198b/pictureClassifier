# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2018-04-18 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Без категории', max_length=255, verbose_name='Категория')),
                ('file', models.FileField(blank=True, null=True, upload_to='uploads/%Y/%m/%d/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Картинка',
                'verbose_name_plural': 'Картинка',
                'ordering': ['created_at'],
            },
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]

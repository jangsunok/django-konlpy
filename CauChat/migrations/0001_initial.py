# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-02 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100)),
                ('priority', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bestKey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CauChat.Key')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CauChat.Chat')),
            ],
        ),
    ]
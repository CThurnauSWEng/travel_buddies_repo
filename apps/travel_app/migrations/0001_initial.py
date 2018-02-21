# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-02-21 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('dateFrom', models.DateField()),
                ('dateTo', models.DateField()),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('plannedBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planned_trips', to='user_app.User')),
                ('travelers', models.ManyToManyField(related_name='trips', to='user_app.User')),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 09:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('apellidos', models.CharField(blank=True, max_length=150)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('telefono', models.CharField(blank=True, max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('domicilio', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_caninos', models.IntegerField(blank=True, null=True)),
                ('razon', models.TextField(blank=True)),
                ('persona', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adopcion.Persona')),
            ],
            options={
                'verbose_name': 'Solicitud',
                'verbose_name_plural': 'Solicitudes',
            },
        ),
    ]

# Generated by Django 4.1.2 on 2022-11-14 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='hoteles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ubicacion', models.CharField(max_length=15)),
                ('cant_personas', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raza', models.CharField(max_length=19)),
                ('anios_mascota', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='vehiculos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_vehiculo', models.CharField(max_length=18)),
                ('marca', models.CharField(max_length=25)),
                ('color_vehiculo', models.CharField(max_length=30)),
            ],
        ),
    ]

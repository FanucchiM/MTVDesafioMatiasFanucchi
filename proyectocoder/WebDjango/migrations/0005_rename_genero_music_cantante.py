# Generated by Django 4.1.2 on 2022-11-16 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebDjango', '0004_rename_cant_personas_music_duracion_de_la_cancion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='music',
            old_name='genero',
            new_name='cantante',
        ),
    ]

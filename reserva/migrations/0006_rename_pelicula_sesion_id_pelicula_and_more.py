# Generated by Django 5.0.4 on 2024-05-28 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0005_rename_id_pelicula_sesion_pelicula_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sesion',
            old_name='pelicula',
            new_name='id_pelicula',
        ),
        migrations.RenameField(
            model_name='sesion',
            old_name='sala',
            new_name='id_sala',
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-28 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0004_remove_sesion_pelicula_remove_sesion_sala_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sesion',
            old_name='id_pelicula',
            new_name='pelicula',
        ),
        migrations.RenameField(
            model_name='sesion',
            old_name='id_sala',
            new_name='sala',
        ),
    ]

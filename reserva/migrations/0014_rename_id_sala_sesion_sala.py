# Generated by Django 5.0.4 on 2024-05-29 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0013_rename_sala_sesion_id_sala'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sesion',
            old_name='id_sala',
            new_name='sala',
        ),
    ]

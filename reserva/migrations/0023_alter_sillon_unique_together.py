# Generated by Django 5.0.4 on 2024-06-11 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0022_alter_sesion_sillones_ocupados'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='sillon',
            unique_together={('fila', 'columna')},
        ),
    ]

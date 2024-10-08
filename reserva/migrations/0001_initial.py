# Generated by Django 5.0.4 on 2024-04-23 09:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('autenticacion', '0001_initial'),
        ('cartelera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('aforo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sesion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.TimeField()),
                ('id_pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cartelera.pelicula')),
                ('id_sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserva.sala')),
            ],
        ),
        migrations.CreateModel(
            name='Entrada',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField()),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
                ('id_usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autenticacion.usuario')),
                ('id_sesion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reserva.sesion')),
            ],
        ),
    ]

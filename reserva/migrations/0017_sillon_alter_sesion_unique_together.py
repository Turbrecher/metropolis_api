# Generated by Django 5.0.4 on 2024-05-29 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0016_remove_entrada_descripcion_remove_entrada_nombre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sillon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fila', models.IntegerField()),
                ('columna', models.IntegerField()),
                ('estado', models.TextField()),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='sesion',
            unique_together={('sala', 'hora')},
        ),
    ]

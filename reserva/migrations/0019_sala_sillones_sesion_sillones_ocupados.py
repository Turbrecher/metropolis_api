# Generated by Django 5.0.4 on 2024-05-29 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0018_alter_sillon_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='sala',
            name='sillones',
            field=models.ManyToManyField(to='reserva.sillon'),
        ),
        migrations.AddField(
            model_name='sesion',
            name='sillones_ocupados',
            field=models.ManyToManyField(to='reserva.sillon'),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-28 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0008_remove_sesion_fecha'),
    ]

    operations = [
        migrations.AddField(
            model_name='entrada',
            name='fecha_compra',
            field=models.DateField(default='2004-07-25'),
            preserve_default=False,
        ),
    ]

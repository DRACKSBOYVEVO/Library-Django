# Generated by Django 2.2 on 2020-10-26 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0018_reserva_fecha_vencimiento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='fecha_creacion',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
    ]
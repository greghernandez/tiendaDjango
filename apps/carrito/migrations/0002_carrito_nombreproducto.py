# Generated by Django 2.0.5 on 2018-11-26 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carrito', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carrito',
            name='nombreProducto',
            field=models.CharField(default='Sin Nombre', max_length=30),
        ),
    ]

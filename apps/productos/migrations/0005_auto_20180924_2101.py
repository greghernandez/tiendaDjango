# Generated by Django 2.0.5 on 2018-09-25 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_auto_20180924_2058'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='descripcion',
            new_name='caracteristicas',
        ),
    ]
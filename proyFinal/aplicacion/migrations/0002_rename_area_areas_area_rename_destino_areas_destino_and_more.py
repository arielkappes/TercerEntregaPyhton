# Generated by Django 5.0.1 on 2024-02-12 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='areas',
            old_name='Area',
            new_name='area',
        ),
        migrations.RenameField(
            model_name='areas',
            old_name='Destino',
            new_name='destino',
        ),
        migrations.RenameField(
            model_name='areas',
            old_name='Responsable',
            new_name='responsable',
        ),
    ]
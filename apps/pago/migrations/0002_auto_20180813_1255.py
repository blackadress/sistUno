# Generated by Django 2.1 on 2018-08-13 17:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pago', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pago',
            old_name='usuario',
            new_name='cuenta_usuario',
        ),
        migrations.RenameField(
            model_name='pago',
            old_name='usuario_asignado',
            new_name='cuenta_usuario_asignado',
        ),
    ]

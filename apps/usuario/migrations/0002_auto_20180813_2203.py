# Generated by Django 2.1 on 2018-08-14 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entidad_bancaria',
            name='logo',
            field=models.ImageField(blank=True, upload_to='entidades_bancarias'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='foto_perfil',
            field=models.ImageField(blank=True, upload_to='usuario'),
        ),
    ]

# Generated by Django 2.1 on 2018-08-15 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0004_auto_20180815_1025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuenta_usuario',
            name='saldo',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]

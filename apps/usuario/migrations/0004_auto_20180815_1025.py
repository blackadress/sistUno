# Generated by Django 2.1 on 2018-08-15 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_auto_20180814_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='dni_referido',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='usuario.Usuario'),
        ),
    ]

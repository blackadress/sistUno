# Generated by Django 2.1 on 2018-08-14 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deposito', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('banner', models.ImageField(blank=True, upload_to='baner')),
            ],
        ),
    ]

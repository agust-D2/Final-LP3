# Generated by Django 3.0.8 on 2020-08-20 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0004_auto_20200820_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='estudiantes',
            fields=[
                ('idestudiante', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('dni', models.CharField(max_length=8)),
                ('direccion', models.CharField(max_length=100)),
                ('fecha_nacimiento', models.CharField(max_length=20)),
                ('estado', models.CharField(max_length=1)),
            ],
        ),
    ]
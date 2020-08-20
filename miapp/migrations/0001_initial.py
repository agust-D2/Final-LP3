# Generated by Django 3.0.8 on 2020-08-20 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cursos',
            fields=[
                ('idcurso', models.AutoField(primary_key=True, serialize=False)),
                ('codigo', models.CharField(max_length=10, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('horas', models.DateTimeField(auto_now_add=True)),
                ('creditos', models.IntegerField()),
                ('estados', models.CharField(max_length=1)),
            ],
        ),
    ]

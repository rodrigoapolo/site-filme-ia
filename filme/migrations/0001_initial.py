# Generated by Django 5.0.4 on 2024-04-04 23:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.AutoField(primary_key=True, serialize=False)),
                ('nomeCategoria', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(blank=True, max_length=150, null=True)),
                ('data_nascimento', models.DateField()),
                ('genero', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('idFilme', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=200)),
                ('classificacao', models.IntegerField()),
                ('lancamento', models.DateField()),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='filme.categoria')),
            ],
        ),
    ]

# Generated by Django 5.0.6 on 2024-05-21 17:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("filme", "0004_alter_filme_avaliacao"),
    ]

    operations = [
        migrations.AddField(
            model_name="filme",
            name="foto",
            field=models.ImageField(blank=True, null=True, upload_to="imagens/"),
        ),
    ]

# Generated by Django 4.0 on 2021-12-26 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0002_alter_avaliacoes_options'),
        ('core', '0005_alter_pontoturistico_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='avaliacoes',
            field=models.ManyToManyField(to='avaliacoes.Avaliacoes'),
        ),
    ]

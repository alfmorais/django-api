# Generated by Django 4.0 on 2021-12-26 19:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comentario',
            options={'verbose_name': 'Comentário', 'verbose_name_plural': 'Comentários'},
        ),
    ]
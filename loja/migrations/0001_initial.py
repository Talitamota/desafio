# Generated by Django 2.0.9 on 2018-10-21 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('atributos', models.TextField()),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='data de criação')),
            ],
        ),
    ]
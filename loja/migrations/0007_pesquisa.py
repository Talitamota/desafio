# Generated by Django 2.0.9 on 2018-11-07 12:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0006_foto_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pesquisa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loja.Loja')),
            ],
        ),
    ]

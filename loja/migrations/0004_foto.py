# Generated by Django 2.0.9 on 2018-10-22 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0003_produto_modificado_em'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='imagem/%Y/%m/%d')),
            ],
        ),
    ]
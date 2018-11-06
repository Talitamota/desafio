# Generated by Django 2.0.9 on 2018-11-06 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loja', '0004_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Loja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('logo', models.ImageField(upload_to='logo/')),
            ],
        ),
        migrations.AlterField(
            model_name='foto',
            name='imagem',
            field=models.ImageField(upload_to='imagem/'),
        ),
    ]

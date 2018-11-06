from django.db import models

class Produto(models.Model):
    atributos = models.TextField()
    criado_em = models.DateField('data de criação', auto_now_add=True)
    modificado_em = models.DateField('data de modificação', auto_now=True)

    def __str__(self):
        return self.atributos

class Foto(models.Model):
    imagem = models.ImageField(upload_to='imagem/')

class Loja(models.Model):
    nome = models.CharField(max_length=100)
    url = models.UrlField()
    logo =models.ImageField(upload_to='logo/')

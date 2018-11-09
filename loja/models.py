from django.db import models

class Produto(models.Model):
    atributos = models.TextField()
    criado_em = models.DateField('data de criação', auto_now_add=True)
    modificado_em = models.DateField('data de modificação', auto_now=True)

    def __str__(self):
        return self.atributos

class Foto(models.Model):
    imagem = models.ImageField(upload_to='imagem/')
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Loja(models.Model):
    nome = models.CharField(max_length=100)
    url = models.URLField()
    logo =models.ImageField(upload_to='logo/')

    def __str__(self):
        return self.nome

class Pesquisa(models.Model):
    loja = models.ForeignKey(Loja, on_delete=models.CASCADE)
    produto = models.ManyToManyField(Produto)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    criado_em = models.DateField('data de criação', auto_now_add=True)

    def __str__(self):
        return str(self.loja)

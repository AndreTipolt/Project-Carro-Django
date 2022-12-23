from django.db import models




class Categoria(models.Model):

    categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.categoria


class Carro(models.Model):

    nome = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    ano = models.CharField(max_length=4)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome



from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome


class Books(models.Model):
    nome = models.CharField(max_length=128)
    edicao = models.PositiveIntegerField()
    ano_de_publicacao = models.CharField(max_length=4)
    autores = models.ManyToManyField(Autor, related_name='books', blank=False)

    def __str__(self):
        return self.nome

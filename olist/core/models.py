from django.db import models


class Autor(models.Model):
    nome = models.CharField(max_length=120)

    def __str__(self):
        return self.nome

    def to_dict(self):
        return{
            "id": self.id,
            "nome": self.nome
        }


class Books(models.Model):
    nome = models.CharField(max_length=128)
    edicao = models.PositiveIntegerField()
    ano_de_publicacao = models.CharField(max_length=4)
    autores = models.ManyToManyField(Autor, related_name='books', blank=False)

    def __str__(self):
        return self.nome
    
    def to_dict(self):
        return {
            "nome": self.nome,
            "edicao": self.edicao,
            "ano_de_publicacao": self.ano_de_publicacao,
            "autores": self.autores,
        }

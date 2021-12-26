from django.db import models


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=256)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.nome}"

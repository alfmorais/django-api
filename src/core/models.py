from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario

class PontoTuristico(models.Model):
    nome = models.CharField(max_length=256)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracao = models.ManyToManyField(Atracao)
    comentario = models.ManyToManyField(Comentario)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Ponto Turistico"
        verbose_name_plural = "Pontos Turisticos"
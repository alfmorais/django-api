from atracoes.models import Atracao
from avaliacoes.models import Avaliacoes
from comentarios.models import Comentario
from django.db import models
from enderecos.models import Endereco


class PontoTuristico(models.Model):
    nome = models.CharField(max_length=256)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracao = models.ManyToManyField(Atracao)
    comentario = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacoes)
    endereco = models.ForeignKey(
        Endereco, on_delete=models.CASCADE, null=True, blank=True
    )
    foto = models.ImageField(upload_to="turismo/", null=True, blank=True)

    def __str__(self):
        return f"{self.nome}"

    class Meta:
        verbose_name = "Ponto Turistico"
        verbose_name_plural = "Pontos Turisticos"

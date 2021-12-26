from django.db import models


class Endereco(models.Model):
    linha1 = models.CharField(max_length=256)
    linha2 = models.CharField(max_length=256, null=True, blank=True)
    cidade = models.CharField(max_length=256)
    estado = models.CharField(max_length=256)
    pais = models.CharField(max_length=128)
    latitulde = models.IntegerField(null=True, blank=True)
    latitulde = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.linha1}"

    class Meta:
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"

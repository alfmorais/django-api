from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Avaliacoes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField(null=True, blank=True)
    nota = models.DecimalField(decimal_places=2, max_digits=3)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}"

    def clean(self):
        if self.nota < 0 or self.nota > 5:
            raise ValidationError(
                "Insira um valor entre 0 a 5"
            )

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    comentario = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    aprovado = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.usuario.username}"

    class Meta:
        verbose_name = "Comentário"
        verbose_name_plural = "Comentários"
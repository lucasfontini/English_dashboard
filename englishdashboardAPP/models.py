from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Expressao(models.Model):
    name = models.CharField(max_length=70)
    meaning = models.CharField(max_length=70)
    exemple = models.CharField(max_length=70)
    foto = models.ImageField(upload_to='')
    data = models.DateTimeField(default=datetime.now, blank=False)
    # associa a tabela com a tabela de usuarios
    usuario = models.ForeignKey(
        to=User,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name="user",
    )

    def __str__(self):
        return self.name




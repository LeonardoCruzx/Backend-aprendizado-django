from django.db import models

# Create your models here.
class PessoaModel(models.Model):
    nome = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    idade = models.PositiveIntegerField(
        null=False,
        blank=False
    )


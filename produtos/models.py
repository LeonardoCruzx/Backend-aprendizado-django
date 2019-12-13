from django.db import models

# Create your models here.
class CategoriaModel(models.Model):
    nome = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )

class ProdutoModel(models.Model):
    nome = models.CharField(
        max_length=30,
        null=False,
        blank=False
    )
    categoria = models.ForeignKey(
        "CategoriaModel",
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )
    preco = models.FloatField(
        null=False,
        blank=False
    )
    descricao = models.CharField(
        max_length=200,
        null=False,
        blank=False
    )
    imagem = models.ImageField(
        upload_to="imagens_de_doces",
        null=True,
        blank=True
    )




from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    preco = models.DecimalField(verbose_name='Preço', max_digits=7, decimal_places=2)
    qtd_estoque = models.IntegerField(verbose_name='Estoque')

    def __str__(self):
        return self.nome
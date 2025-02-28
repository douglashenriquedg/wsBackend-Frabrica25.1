from django.db import models


class catalogo(models.Model):
    titulo = models.CharField(max_length=100)
    sinopse = models.TextField(max_length=255)
    genero = models.CharField(max_length=255)
    duracao = models.CharField(max_length=255)
    diretor = models.CharField(max_length=255)
    ano = models.CharField(max_length=255)
# capa = models.ImageField(upload_to='') # quero coloca uma capa padrao caso a capa original nao seja carregada
    faixa_etaria_CHOICES = (
        ('L', 'Livre'),
        ('10', '10 anos'),
        ('12', '12 anos'),
        ('14', '14 anos'),
        ('16', '16 anos'),
        ('18', '18 anos'),
    )
    faixa_etaria = models.CharField(max_length=2, choices=faixa_etaria_CHOICES)

# Create your models here.

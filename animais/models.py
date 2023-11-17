from django.db import models

# Create your models here.

class Animais(models.Model):
    nome = models.CharField(max_length=100)
    raça = models.CharField(max_length=100)
    idade = models.IntegerField(decimal_places=0 max_digits=20)
    adotado = models.BooleanField(default=False)
     
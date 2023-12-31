from django.db import models

# Create your models here.

class Animais(models.Model):
    nome = models.CharField(max_length=100)
    raça = models.CharField(max_length=100)
    idade = models.IntegerField()
    descrição = models.CharField(max_length= 200, blank=True)
    tamanho = models.CharField( max_length= 100 )
    Cachorro = models.BooleanField( default= False, blank=True )
    Gato = models.BooleanField( default= False, blank=True )
    img = models.ImageField(upload_to ='img_pets', null=True, blank=True )
    
    def __str__(self) :
        return self.nome 
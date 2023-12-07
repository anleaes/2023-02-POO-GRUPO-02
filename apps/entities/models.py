from django.db import models

# Create your models here.
class Entity(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    email = models.EmailField()
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=50) 
    
    class Meta:
        verbose_name = 'Orgao'
        verbose_name_plural = 'Orgaos'
        ordering =['id']

    def __str__(self):
        return self.nome
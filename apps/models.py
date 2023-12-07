from django.db import models

# Create your models here.

class Supervisor(models.Model):
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    telefone = models.IntegerField()
    endereco = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'Supervisor'
        verbose_name_plural = 'Supervisores'
        ordering =['id']

    def __str__(self):
        return self.nome
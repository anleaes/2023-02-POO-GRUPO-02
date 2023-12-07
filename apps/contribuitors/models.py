from django.db import models

# Create your models here.

class Contribuitor(models.Model):
    nome = models.CharField('Nome', max_length=50)
    telefone = models.IntegerField('Telefone')
    email = models.EmailField('Email', max_length=20)
    endereco = models.CharField('Endereco', max_length=200)
    GENERO_ESCOLHAS = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENERO_ESCOLHAS)
    
    class Meta:
        verbose_name = 'Contribuinte'
        verbose_name_plural = 'Contribuintes'
        ordering =['id']

    def __str__(self):
        return self.nome
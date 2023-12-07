from django.db import models

# Create your models here.

class Material(models.Model):
    nome = models.CharField('Nome',max_length=50)
    tipo = models.CharField(max_length=50)
    description = models.TextField('Descricao', max_length=100)
    
    class Meta:
        verbose_name = 'Material'
        verbose_name_plural = 'Materiais'
        ordering =['id']

    def __str__(self):
        return self.nome
from django.db import models
from locations.models import Location
from contribuitors.models import Contribuitor

# Create your models here.

class Solicitation(models.Model):
    descricao = models.TextField('Descrição', max_length=100)
    data = models.DateField('Data', auto_now=False, auto_now_add=False) 
    local = models.ForeignKey(Location, on_delete=models.CASCADE)
    contribuinte = models.ForeignKey(Contribuitor, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Solicitacao'
        verbose_name_plural = 'Solicitacoes'
        ordering =['id']

    def __str__(self):
        return self.descricao
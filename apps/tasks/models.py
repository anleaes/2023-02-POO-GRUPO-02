from django.db import models
from entities.models import Entity
from solicitations.models import Solicitation
from supervisors.models import Supervisor

# Create your models here.

class Task(models.Model):
    descricao = models.TextField('Descrição', max_length=300,default=None)
    data = models.DateField('Data', auto_now=False, auto_now_add=False)
    STATUS_TASK = (
        ('E', 'Em Espera'),
        ('A', 'Em Andamento'),
        ('F', 'Finalizado'),
    )
    status = models.CharField('Status', max_length=1, choices=STATUS_TASK,default=None) 
    orgao = models.ForeignKey(Entity, on_delete=models.CASCADE)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE,default=None)
    solicitacao = models.ForeignKey(Solicitation, on_delete=models.CASCADE , default=None)

    class Meta:
        verbose_name = 'Servico'
        verbose_name_plural = 'Servicos'
        ordering =['id']

    def __str__(self):
        return self.descricao
    
    
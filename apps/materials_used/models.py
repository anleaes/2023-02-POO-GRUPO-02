from django.db import models
from materials.models import Material
from tasks.models import Task

# Create your models here.

class Material_Used(models.Model):
    material = models.ForeignKey(Material, on_delete=models.CASCADE,default=None)
    task = models.ForeignKey(Task,on_delete=models.CASCADE,default = None)
    qnt = models.CharField(max_length=100)
    MEDIDA_ESCOLHAS = (
        ('U', 'Unidade'),
        ('K', 'Kg'),
        ('L', 'Litros'),
        ('M', 'Metros'),
    )
    medida = models.CharField('', max_length=1, choices=MEDIDA_ESCOLHAS)
    
    class Meta:
        verbose_name = 'Materiais_utilizados'
        verbose_name_plural = 'Materials_utilizados'
        ordering =['id']

    def __str__(self):
        return self.material
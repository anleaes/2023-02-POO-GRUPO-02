from django.db import models
from solicitations.models import Solicitation
from contribuitors.models import Contribuitor

class Rating(models.Model):
    contribuinte = models.ForeignKey(Contribuitor, on_delete=models.CASCADE)
    solicitations = models.ForeignKey(Solicitation, on_delete=models.CASCADE,default=None)
    NOTA_ESCOLHAS = (
        ('0', '0 - Péssimo'),
        ('1', '1 - Ruim'),
        ('2', '2 - Dentro do esperado'),
        ('3', '3 - Bom'),
        ('4', '4 - Ótimo'),
        ('4', '5 - Perfeito!'),
    )
    nota = models.CharField('Nota', max_length=1, choices=NOTA_ESCOLHAS)
    comentarios = models.TextField('Comentários', max_length=400)

    class Meta:
        verbose_name = 'Avaliacao'
        verbose_name_plural = 'Avaliacoes'
        ordering =['id']

    def __str__(self):
        return self.descricao
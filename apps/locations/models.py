from django.db import models

class Location(models.Model):
    rua = models.CharField(max_length=50)
    bairro = models.CharField(max_length=50)
    cidade = models.CharField(max_length=50)
    cep = models.CharField(max_length=10)
    
    class Meta:
        verbose_name = 'Localizacao'
        verbose_name_plural = 'Localizacoes'
        ordering =['id']

    def __str__(self):
        return self.rua
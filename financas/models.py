from django.db import models

# Create your models here.

class RendaMensal(models.Model):
    nome = models.CharField(max_length=60,null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    



from django.db import models
# Create your models here.
class Automovil(models.Model):
   modelo=models.CharField(max_length=30)
   marca=models.CharField(max_length=30)

class Caracteristica_automovil(models.Model):
   motor=models.CharField(max_length=30)
   peso=models.CharField(max_length=30)
   color=models.CharField(max_length=30)


class Contrato(models.Model):
   cliente=models.CharField(max_length=30)
   automovil=models.CharField(max_length=30)
   
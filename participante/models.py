from django.db import models

# Create your models here.
class Informacion(models.Model):
   nombre=models.CharField(max_length=30)
   direccion=models.CharField(max_length=50)  
   telefono=models.CharField(max_length=7)
   email=models.EmailField()
   nombre=models.CharField(max_length=30)
   edad=models.IntegerField()
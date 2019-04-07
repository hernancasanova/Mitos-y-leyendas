from django.db import models

# Create your models here.

class carta(models.Model):
    nombre= models.CharField(max_length=30)
    habilidad=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images')

class card(models.Model):
    Nombre= models.CharField(max_length=30)
    Edicion=models.CharField(max_length=30)
    Habilidad=models.CharField(max_length=200)
    
    

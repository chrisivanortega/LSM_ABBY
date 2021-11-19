from django.db import models


# Create your models here.
class Pregunta(models.Model):
    pregunta = models.CharField(max_length=200)

class Senna(models.Model):
    id = models.AutoField(primary_key=True)    
    name = models.CharField(max_length=200)    
    img = models.TextField()
    desc = models.CharField(max_length=200,default='')

    
    
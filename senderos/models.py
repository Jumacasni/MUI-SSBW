from django.db import models

# Create your models here.
class Excursion(models.Model):
	nombre = models.CharField(max_length=100)
	descripcion = models.TextField(max_length=1000)
	likes = models.IntegerField(default=0)
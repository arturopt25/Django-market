from django.db import models

# Create your models here.
class Trabajadores(models.Model):
	nombre		= models.CharField(max_length=120)
	apellido	= models.CharField(max_length=120)
	cedula      = models.IntegerField(default=170)
	direccion	= models.CharField(max_length=120)
	edad	    = models.IntegerField(default=170)
	
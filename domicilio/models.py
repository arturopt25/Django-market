from django.db import models

# Create your models here.
class Domicilio(models.Model):
	direccion	= models.TextField(blank=False, null=False)
	ciudad      = models.CharField(max_length=50)
	estado      = models.CharField(max_length=50)
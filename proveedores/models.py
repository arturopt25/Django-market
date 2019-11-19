from django.db import models

# Create your models here.
class Proveedores(models.Model):
	empresa_proveedores		= models.CharField(max_length=70)
	telefono    			= models.IntegerField(default=170)
	direccion				= models.CharField(max_length=120)
from django.db import models

# Create your models here.
class Proveedores_Marca(models.Model):
	empresa_marca		= models.CharField(max_length=70)
	idproveedores  		= models.IntegerField(default=170)
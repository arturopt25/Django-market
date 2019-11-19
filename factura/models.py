from django.db import models

# Create your models here.
class Factura(models.Model):
	fecha 			= models.DateField(blank=True, null=True)
	idcliente		= models.IntegerField(default=170)
	idcompra		= models.IntegerField(default=170)
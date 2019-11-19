from django.db import models

# Create your models here.
class Factura_Producto(models.Model):
	idfactura		= models.IntegerField(default=170)
	idproducto		= models.IntegerField(default=170)
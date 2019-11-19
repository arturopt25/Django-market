from django.db import models

# Create your models here.
class Venta_Item(models.Model):
	idproducto  		= models.IntegerField(default=170)
	numero_de_items		= models.IntegerField(default=170)
	precio_total 		= models.FloatField(default=170)
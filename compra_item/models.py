from django.db import models

# Create your models here.
class Compra_Item(models.Model):
	idproducto		= models.IntegerField(default=170)
	numero_De_item	= models.IntegerField(default=170)
	precio_total 		= models.FloatField(default=170)
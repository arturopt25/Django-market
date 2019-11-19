from django.db import models

# Create your models here.
class Cupones(models.Model):
	idproducto		= models.IntegerField(default=170)
	valor_cupon		= models.IntegerField(default=170)
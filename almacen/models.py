from django.db import models

# Create your models here.
class Almacen(models.Model):
	idproducto_categoria	= models.IntegerField(default=170)
	idproducto				= models.IntegerField(default=170)
	posicion				= models.CharField(max_length=120)
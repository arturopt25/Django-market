from django.db import models

# Create your models here.
class Producto_Marca(models.Model):
	nombre		= models.CharField(max_length=120)
	idproducto	= models.IntegerField(default=170)
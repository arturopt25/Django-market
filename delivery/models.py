from django.db import models

# Create your models here.
class Delivery(models.Model):
	iddomicilio 		= models.IntegerField(default=170)
	idcliente 			= models.IntegerField(default=170)
	idfactura	 		= models.IntegerField(default=170)
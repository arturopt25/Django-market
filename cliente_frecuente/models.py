from django.db import models

# Create your models here.
class Cliente_Frecuente(models.Model):
	idcliente  		= models.IntegerField(default=170)
	idusuario  		= models.IntegerField(default=170)
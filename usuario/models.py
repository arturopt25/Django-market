from django.db import models

# Create your models here.
class Usuario(models.Model):
	nombre		= models.CharField(max_length=120)
	email 		= models.CharField(max_length=120)
	telefono    = models.IntegerField(default=170)
	contraseña	= models.CharField(max_length=50)




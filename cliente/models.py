from django.db import models

# Create your models here.
class Cliente(models.Model):
	idusuario     = models.IntegerField(max_length=50)

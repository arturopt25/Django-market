from django.db import models

# Create your models here.
class Venta(models.Model):
	cuenta_usuario_id  = models.IntegerField(max_length=50)
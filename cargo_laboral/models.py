from django.db import models

# Create your models here.
class Cargo_Laboral(models.Model):
	idtrabajadores 		= models.IntegerField(default=170)
	Cargo 				= models.CharField(max_length=70)
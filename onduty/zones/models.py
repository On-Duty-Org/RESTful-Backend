from django.db import models

# Create your models here.

class zones(models.Model):
	name = models.CharField(max_length=20)
	priority = models.CharField(max_length=5)

	def __str__(self):
		return self.name

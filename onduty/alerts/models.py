from django.db import models
from django.utils import timezone
import datetime

# Create your models here.

class alerts(models.Model):
	sent_by = models.CharField(max_length=10)
	sent_to = models.CharField(max_length=10)
	time = models.CharField(max_length=10)

	def __str__(self):
		return self.sent_by

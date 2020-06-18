from django.db import models
from django.utils import timezone
from django_mysql.models import ListCharField
import datetime

# Create your models here.

class allocations(models.Model):
    zone = models.CharField(max_length=20)
    priority = models.CharField(max_length=5)
    # police_allotted = models.CharField(max_length=50)
    police_allotted = ListCharField(
        base_field= models.CharField(max_length=20),
        size=7,
        max_length=(7 * 21)  # 6 * 10 character nominals, plus commas
    )
    date_posted = models.DateTimeField(default=timezone.now)
    time_slot = models.CharField(max_length=10)

    def __str__(self):
        return self.zone

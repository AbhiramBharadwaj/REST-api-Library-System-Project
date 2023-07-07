from statistics import quantiles
from django.db import models

# Create your models here.
class Tutorial(models.Model):
 title = models.CharField(max_length=70, blank=False, default='')
 author = models.CharField(max_length=200,blank=False, default='')
 availability = models.BooleanField(default=True)

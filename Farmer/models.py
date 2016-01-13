from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Farmer(models.Model):
    name=models.CharField(unique=True,max_length=200)
    contact_no=models.IntegerField()
    age=models.IntegerField()
    address=models.CharField(max_length=400);

from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.

class Operational_user(models.Model):
    user=models.OneToOneField(User)
    name=models.CharField(max_length=200)


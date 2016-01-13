from __future__ import unicode_literals
from Answer.models import *
from Question.models import *
from Response.models import *
from Operational_user.models import *
from Farmer.models import *

from django.db import models

# Create your models here.
class Feedback(models.Model):
    operational_user=models.ForeignKey(Operational_user)
    farmer=models.ForeignKey(Farmer)

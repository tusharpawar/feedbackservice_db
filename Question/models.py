from __future__ import unicode_literals

from django.db import models
from Answer.models import *

# Create your models here.
class Question(models.Model):
    question_text=models.TextField(unique=True)
    options=models.ManyToManyField(Answer)
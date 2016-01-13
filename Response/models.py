from __future__ import unicode_literals
from Question.models import *

from django.db import models

# Create your models here.
class Response(models.Model):
    question_id=models.ForeignKey(Question)
    answer_id=models.ForeignKey(Answer)

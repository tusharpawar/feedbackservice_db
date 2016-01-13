from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Answer(models.Model):
    answer_text=models.TextField(unique=True)



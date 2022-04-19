from django.db import models

# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

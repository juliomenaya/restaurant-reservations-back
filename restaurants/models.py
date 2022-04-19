from django.db import models
from owners.models import Owner

# Create your models here.

class Restaurant(models.Model):
    owner = models.ForeignKey(Owner, related_name='restaurants', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

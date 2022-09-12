from django.db import models

# Create your models here.
class Asgard_Data(models.Model):
    heading = models.CharField(max_length=50)
    text = models.CharField(max_length=100)
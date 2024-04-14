from django.db import models

# Create your models here.

class speechDetection(models.Model):
    # define all the fields that your model is supposed to have
    text = models.CharField(max_length=10000)

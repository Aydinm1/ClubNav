from django.db import models

# Create your models here.

class Club(models.Model):
    name = models.CharField()
    description = models.CharField()
    picture = models.ImageField()
    sponsor = models.CharField()
    sponsor_email = models.EmailField()
from django.db import models
from django.contrib import admin

# Create your models here...

class Days(models.Model):
    days = models.CharField(max_length=9)

class Categories(models.Model):
    categories = models.CharField(max_length=30)

class Club(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='./images')
    sponsor = models.CharField(max_length=30)
    sponsor_email = models.EmailField()
    category = models.ForeignKey(Categories)
    meeting_days = models.ManyToManyField(Days)

    def __str__(self):
        return self.name
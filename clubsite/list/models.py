from django.db import models

# DO NOT RUN INTEGRATE THIS INTO SQL YET. IT WILL LIKELY BREAK THE DATABASE. 
# Create your models here.

class Club(models.Model):
    name = models.CharField()
    description = models.CharField()
    picture = models.ImageField()
    sponsor = models.CharField()
    sponsor_email = models.EmailField()
    category_choices = [
        'STEM',
        'Reading/Writing',
        'Fun',
        'Fine Arts',
        'Politics',
        'Language',
        'Sports',
        'Activism/Volunteering',
        'Student Unions',
        'Competition',
        'Business',
        'Leadership'
    ]
    category = models.CharField(
        choices=category_choices,
    )

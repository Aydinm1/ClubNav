from django.db import models

# DO NOT RUN INTEGRATE THIS INTO SQL YET. IT WILL LIKELY BREAK THE DATABASE. 
# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    picture = models.ImageField()
    sponsor = models.CharField(max_length=30)
    sponsor_email = models.EmailField()
    category_choices = [
        ('STEM', 'STEM'),
        ('READWRITE', 'Reading/Writing'),
        ('FUN', 'Fun'),
        ('FINEART', 'Fine Arts'),
        ('POLITICS', 'Politics'),
        ('LANGUAGE', 'Language'),
        ('SPORTS', 'Sports'),
        ('ACTIVISMVOLUNTEER', 'Activism/Volunteering'),
        ('STUDUNION', 'Student Unions'),
        ('COMP', 'Competition'),
        ('BUSI', 'Business'),
        ('LEAD', 'Leadership'),
    ]
    category = models.CharField(
        max_length=17,
        choices=category_choices,
    )

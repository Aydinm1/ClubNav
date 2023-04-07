from django.db import models
from django.contrib import admin

# Create your models here.

class Club(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    picture = models.ImageField(upload_to='./images')
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
    meeting_days = models.CharField(
        max_length=2,
        choices=meeting_days_choices,
    )

    def __str__(self):
        return self.name


class Days(models.Model):
    days_choices = [
    ('SU', 'Sunday'),
    ('MO', 'Monday'),
    ('TU', 'Tuesday'),
    ('WE', 'Wednesday'),
    ('TH', 'Thursday'),
    ('FR', 'Friday'),
    ('SA', 'Saturday'),
    ]
    @admin.display
    def meeting_days(self):
        for day in days_choices:
            
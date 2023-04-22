from django.db import models
from django.core.validators import MinLengthValidator
from recurrence.fields import RecurrenceField

# Create your models here...

class Categories(models.Model):
    categories = models.CharField(max_length=30)

    def __str__(self):
        return self.categories
    
class SponsorName(models.Model):
    sponsor_name = models.CharField(max_length=30)
    sponsor_email = models.EmailField()

    def __str__(self):
        return self.sponsor_name
    
class MeetingRooms(models.Model):
    meeting_room_name = models.CharField(max_length=30, blank=True)
    meeting_room_number = models.CharField(max_length=5)

    def __str__(self):
        return self.meeting_room_number

class Club(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    picture = models.ImageField(upload_to='./images', blank=True)
    sponsor = models.ManyToManyField(SponsorName)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    recurrences = RecurrenceField()
    meeting_room = models.ManyToManyField(MeetingRooms, blank=True)
    google_classroom_code = models.CharField(max_length=7, validators=[MinLengthValidator(limit_value=6)], blank=True)

    def __str__(self):
        return self.name
from django.contrib import admin

# Register your models here.

from .models import Club, Categories, SponsorName
from django.db import models
from django.forms import CheckboxSelectMultiple

class ClubAdmin(admin.ModelAdmin):
    model = Club
    filter_horizontal = ('sponsor',)

admin.site.register(Club, ClubAdmin)
admin.site.register(Categories)
admin.site.register(SponsorName)
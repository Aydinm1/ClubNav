from django.contrib import admin

# Register your models here.

from .models import Club
from django.db import models
from django.forms import CheckboxSelectMultiple

class ClubAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple}
    }

admin.site.register(Club, ClubAdmin)
from django.contrib import admin

# Register your models here.

from .models import Club, Categories
from django.db import models
from django.forms import CheckboxSelectMultiple

class ClubAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple}
    }

admin.site.register(Club, ClubAdmin)
admin.site.register(Categories)
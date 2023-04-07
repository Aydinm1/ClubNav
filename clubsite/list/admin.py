from django.contrib import admin

# Register your models here.

from .models import Club
from .forms import ClubAdminForm

class ClubAdmin(admin.ModelAdmin):
    form = ClubAdminForm

admin.site.register(Club)
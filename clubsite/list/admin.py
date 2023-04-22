from django.contrib import admin

# Register your models here.

from .models import Club, Categories, SponsorName, MeetingRooms

class ClubAdmin(admin.ModelAdmin):
    model = Club
    filter_horizontal = ('sponsor', 'category', 'meeting_room',)

admin.site.register(Club, ClubAdmin)
admin.site.register(Categories)
admin.site.register(SponsorName)
admin.site.register(MeetingRooms)
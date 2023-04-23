from django.contrib import admin

# Register your models here.

from .models import Club, Categories, SponsorName, MeetingRooms, ClubPresidentName, OtherImage

class OtherImageAdmin(admin.StackedInline):
    model = OtherImage

class ClubAdmin(admin.ModelAdmin):
    model = Club
    filter_horizontal = ('sponsor', 'category', 'meeting_room','club_president',)
    inlines = [OtherImageAdmin]

admin.site.register(Club, ClubAdmin)
admin.site.register(Categories)
admin.site.register(SponsorName)
admin.site.register(MeetingRooms)
admin.site.register(ClubPresidentName)
admin.site.register(OtherImage)
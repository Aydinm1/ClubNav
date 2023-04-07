from django import forms
from .models import Club

class ClubAdminForm(forms.ModelForm):
    days = forms.MultipleChoiceField(choices = Club.meeting_days_choices, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Club
        fields = ('meeting_days',)
from django import forms
from .models import Club

class ClubAdminForm(forms.ModelForm):
    meeting_days = forms.MultipleChoiceField(choices = Club.meeting_days_choices, widget=forms.CheckboxSelectMultiple())

    class Meta:
        model = Club
        fields = '__all__'
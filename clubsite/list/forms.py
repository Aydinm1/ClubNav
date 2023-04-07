from django import forms
from models import Club

class ClubAdminForm(forms.ModelForm):
    days = forms.MultipleChoiceField(choices = meeting_days_choices)
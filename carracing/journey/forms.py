from django import forms
from django.forms import NumberInput

from .models import Journey


class UserJourneyForm(forms.ModelForm):
    """Journey Form"""

    class Meta:
        model = Journey
        fields = ('car', 'distance',)
        widgets = {
            'distance': NumberInput(attrs={'min': 0, 'step': "0.1"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['distance'].initial = 0.1

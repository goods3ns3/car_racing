import datetime

from django import forms
from django.forms import NumberInput

from .models import Car, Journey


class UserJourneyForm(forms.Form):
    """Journey Form"""
    car = forms.ModelChoiceField(
        queryset=Car.objects.all(),
        label='Your car',
        empty_label='Select car'
    )
    distance = forms.FloatField(
        label='Distance (km)',
        min_value=0,
        initial=0.1,
        widget=NumberInput(attrs={'step': "0.1"})
    )

    def save_journey(self, request):
        """Build and send the email message."""
        cd = self.cleaned_data.copy()
        now = datetime.datetime.now()
        speed = Car.objects.filter(id=cd['car'].id).first().speed * (5/18)  # m/s
        time_in_trip = cd['distance']*1000 / speed
        journey, created = Journey.objects.get_or_create(
            session=request.session,
        )
        if created:
            journey.user_name = f'User-{Journey.objects.last().id}'
            journey.car = cd['car']
            journey.time_start = now
            journey.time_finish = now + datetime.timedelta(seconds=time_in_trip)
            journey.save(
                update_fields=['user_name', 'car', 'time_start', 'time_finish']
            )
        return time_in_trip  # seconds

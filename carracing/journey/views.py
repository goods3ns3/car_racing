from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, ListView

from .forms import UserJourneyForm
from .models import Journey, Car


class JourneyView(FormView):
    model = Journey
    template_name = 'journey/journey_form.html'
    form_class = UserJourneyForm

    def form_valid(self, form):
        self.time_in_trip = form.save_journey(self.request)
        return super().form_valid(form)

    def get_success_url(self):
        success_url = reverse_lazy(
            'journey_success',
            kwargs={'time_in_trip': self.time_in_trip}
        )
        return success_url


class JourneySuccessView(TemplateView):
    template_name = 'journey/journey_success.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        time_in_trip = kwargs.get('time_in_trip')
        ctx['time_in_trip'] = time_in_trip
        return ctx


class VehicleStatsView(ListView):
    template_name = 'journey/vehicle_stats.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.all()


class PassengerStatsView(ListView):
    template_name = 'journey/passengers_stats.html'
    context_object_name = 'passengers'

    def get_queryset(self):
        return Journey.objects.all()

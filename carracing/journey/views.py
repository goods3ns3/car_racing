from django.views.generic import FormView, TemplateView


class JourneyView(TemplateView):
    template_name = 'journey/journey_form.html'


class VehicleStatsView(TemplateView):
    template_name = 'journey/vehicle_stats.html'


class PassengerStatsView(TemplateView):
    template_name = 'journey/passengers_stats.html'

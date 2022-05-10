from django.db.models import Sum, F
from django.urls import reverse_lazy
from django.views.generic import FormView, TemplateView, ListView

from .forms import UserJourneyForm
from .models import Journey, Car, User


class JourneyView(FormView):
    model = Journey
    template_name = 'journey/journey_form.html'
    form_class = UserJourneyForm

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        if not self.request.session or not self.request.session.session_key:
            self.request.session.save()
        user, created = User.objects.get_or_create(
            session=self.request.session.session_key
        )
        if created:
            user.user_name = f"User-{user.id}"
            user.save(update_fields=["user_name"])
        self.obj.user = user
        self.obj.travel_time = self.obj.distance / self.obj.car.speed
        self.obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        success_url = reverse_lazy(
            'journey_success',
            kwargs={'travel_time': self.obj.travel_time}
        )
        return success_url


class JourneySuccessView(TemplateView):
    template_name = 'journey/journey_success.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['travel_time'] = kwargs.get('travel_time')
        return ctx


class VehicleStatsView(ListView):
    template_name = 'journey/vehicle_stats.html'
    context_object_name = 'cars'

    def get_queryset(self):
        return Car.objects.all().annotate(distance=Sum('journey__distance'))


class PassengerStatsView(ListView):
    template_name = 'journey/passengers_stats.html'
    context_object_name = 'passengers'

    def get_queryset(self):
        return User.objects.all()

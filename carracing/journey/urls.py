from django.urls import path, re_path

from .views import JourneyView, VehicleStatsView, PassengerStatsView, JourneySuccessView

urlpatterns = [
    path('', JourneyView.as_view(), name='journey'),
    re_path(
        r'journey-success/(?P<travel_time>\d+\.\d*)/$',
        JourneySuccessView.as_view(),
        name='journey_success'
    ),
    path(
        'stats/vehicle/',
        VehicleStatsView.as_view(),
        name='vehicle_stats'
    ),
    path(
        'stats/passenger/',
        PassengerStatsView.as_view(),
        name='passenger_stats'
    ),
]

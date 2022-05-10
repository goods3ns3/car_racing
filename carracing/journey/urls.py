from django.urls import path, re_path

from .views import JourneyView, VehicleStatsView, PassengerStatsView

urlpatterns = [
    path('', JourneyView.as_view(), name='journey'),
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

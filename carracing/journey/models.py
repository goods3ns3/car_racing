from django.conf import settings
from django.db import models


User = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Car(models.Model):
    """Car model"""
    name = models.CharField(
        verbose_name='Name', max_length=254, db_index=True
    )
    car_number = models.SlugField(
        verbose_name='Registration number', max_length=254,
        db_index=True, unique=True
    )
    speed = models.IntegerField(verbose_name='Speed (km/h)')

    class Meta:
        app_label = 'journey'
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return f"{self.name} ({self.speed} km/h)"


class Journey(models.Model):
    """User profile"""

    user_name = models.CharField(
        verbose_name="Username", blank=True, max_length=254
    )
    session = models.CharField(
        verbose_name="Session", blank=True, max_length=100
    )
    car = models.ForeignKey(
        Car, verbose_name="Car",
        on_delete=models.CASCADE,
        related_name='journey',
        blank=True, null=True
    )
    time_start = models.DateTimeField(
        verbose_name="Time start", blank=True, null=True
    )
    time_finish = models.DateTimeField(
        verbose_name="Time finish", blank=True, null=True
    )

    class Meta:
        app_label = 'journey'
        verbose_name = "Journey"
        verbose_name_plural = "Journeys"

    def __str__(self):
        return f"{self.user_name} {self.car} ({self.time_start}-{self.time_finish})"

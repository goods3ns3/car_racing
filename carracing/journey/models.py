from django.conf import settings
from django.db import models


User = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class Car(models.Model):
    """Car model"""
    name = models.CharField(
        verbose_name='Name', max_length=254, db_index=True
    )
    car_number = models.SlugField(
        verbose_name='Slug', max_length=254, db_index=True, unique=True
    )

    class Meta:
        app_label = 'journey'
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.name


class Journey(models.Model):
    """User profile"""

    user = models.OneToOneField(
        User,
        related_name='journey',
        verbose_name="User",
        null=True, blank=True,
        on_delete=models.CASCADE
    )
    car = models.ForeignKey(
        Car, verbose_name="Car",
        on_delete=models.CASCADE,
        related_name='journey'
    )
    time_start = models.DateTimeField(
        verbose_name="Time start", auto_now_add=True
    )
    time_finish = models.DateTimeField(verbose_name="Time finish")

    class Meta:
        app_label = 'journey'
        verbose_name = "Journey"
        verbose_name_plural = "Journeys"

    def __str__(self):
        return f"{self.user} {self.car} ({self.time_start}-{self.time_finish})"

from django.db import models


class User(models.Model):
    """User model"""
    user_name = models.CharField(
        verbose_name="Username", blank=True, max_length=254
    )
    session = models.CharField(
        verbose_name="Session", blank=True, max_length=100
    )

    class Meta:
        app_label = 'journey'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.user_name


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
    """Journey model"""

    user = models.ForeignKey(
        User, verbose_name="User",
        on_delete=models.CASCADE,
        related_name='journey',
        blank=True, null=True
    )
    car = models.ForeignKey(
        Car, verbose_name="Car",
        on_delete=models.CASCADE,
        related_name='journey',
        blank=True, null=True
    )
    distance = models.FloatField(
        verbose_name="Distance (km)", blank=True, null=True
    )
    travel_time = models.FloatField(
        verbose_name="Travel time (h)", blank=True, null=True
    )

    class Meta:
        app_label = 'journey'
        verbose_name = "Journey"
        verbose_name_plural = "Journeys"

    def __str__(self):
        return f"{self.user} - {self.car} - {self.distance} - {self.travel_time}"

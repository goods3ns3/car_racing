from django.contrib import admin

from .models import Car, Journey, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'session']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car_number', 'speed']
    prepopulated_fields = {'car_number': ('name',)}


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'car', 'distance', 'travel_time']

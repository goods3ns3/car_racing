from django.contrib import admin

from .models import Car, Journey


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'car_number', 'speed']
    prepopulated_fields = {'car_number': ('name',)}


@admin.register(Journey)
class JourneyAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'car', 'time_start', 'time_finish']

from django.contrib import admin
from main.models import Weather


@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'temperature', 'weather_description',)
    list_display_links = ('date',)
    ordering = ('-date',)

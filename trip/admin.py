from django.contrib import admin
from .models import Location, Trip


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = (
                'location',
                'status',
                'date_created',
                'author'
                )
    list_filter = (
                'status',
                )

@admin.register(Trip)
class TripAdmin(admin.ModelAdmin):
    list_display = (
                    'bus',
                    'driver1',
                    'driver2',
                    'cityFrom',
                    'cityTo',
                    'start_time',
                    'end_time',
                    'company',
                    'create_at',
                     'author'
                )
    list_filter = (
                'company',
                'author'
                )

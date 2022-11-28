from django.contrib import admin

from .models import AirLine,Flight , FlightSchedule

admin.site.register(Flight)
admin.site.register(FlightSchedule)


@admin.register(AirLine)
class AirLineAdmin(admin.ModelAdmin):

    list_display = ( 'id',
                'name',
                'logo',)